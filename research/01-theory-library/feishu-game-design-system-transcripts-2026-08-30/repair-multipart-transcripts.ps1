param(
    [ValidateSet("Inventory", "Repair", "Finalize", "All", "Summary")]
    [string]$Action = "All",

    [int]$PollSeconds = 5,
    [int]$MaxAttempts = 2,
    [ValidateRange(1, 16)]
    [int]$Concurrency = 1,
    [ValidateRange(10, 600)]
    [int]$ProviderBackoffSeconds = 60,
    [string]$OnlyKey = "",
    [switch]$RefreshInventory
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$packageRoot = $PSScriptRoot
$manifestPath = Join-Path $packageRoot "manifest.json"
$inventoryPath = Join-Path $packageRoot "multipart-inventory.json"
$statePath = Join-Path $packageRoot "multipart-repair-state.json"
$transcriptsRoot = Join-Path $packageRoot "transcripts"
$wrapperPath = "C:\Users\Administrator\.codex\skills\bilisum-transcribe\scripts\bilisum-transcribe.ps1"
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

function Assert-File([string]$Path, [string]$Label) {
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "$Label was not found: $Path"
    }
}

function Write-Utf8NoBom([string]$Path, [string]$Content) {
    $normalized = $Content.Replace("`r`n", "`n").Replace("`r", "`n")
    $normalized = $normalized.TrimEnd([char]10) + "`n"
    [System.IO.File]::WriteAllText($Path, $normalized, $utf8NoBom)
}

function Write-Json([string]$Path, [object]$Value, [int]$Depth = 20) {
    $json = $Value | ConvertTo-Json -Depth $Depth
    Write-Utf8NoBom -Path $Path -Content ($json + "`n")
}

function Read-Json([string]$Path) {
    return [System.IO.File]::ReadAllText($Path, [System.Text.Encoding]::UTF8) | ConvertFrom-Json
}

function Get-Bvid([string]$Url) {
    $match = [regex]::Match($Url, "BV[0-9A-Za-z]+")
    if (-not $match.Success) {
        throw "No BV id found in URL: $Url"
    }
    return $match.Value
}

function Get-RelativePath([string]$Path) {
    $rootUri = [Uri](($packageRoot.TrimEnd("\") + "\"))
    $pathUri = [Uri]$Path
    return [Uri]::UnescapeDataString($rootUri.MakeRelativeUri($pathUri).ToString())
}

function Get-Sha256([string]$Path) {
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
}

function Get-TextCharacterCount([string]$Path) {
    return ([System.IO.File]::ReadAllText($Path, [System.Text.Encoding]::UTF8)).Length
}

function ConvertFrom-JsonOutput([object[]]$Output, [string]$Operation) {
    $text = ($Output | ForEach-Object { $_.ToString() }) -join "`n"
    $start = $text.IndexOf("{")
    if ($start -lt 0) {
        throw "$Operation returned no JSON response: $text"
    }
    try {
        return $text.Substring($start) | ConvertFrom-Json
    } catch {
        throw "$Operation returned invalid JSON: $text"
    }
}

function Invoke-BiliSumJson([string[]]$Arguments, [string]$Operation) {
    $command = @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", $wrapperPath
    ) + $Arguments

    $output = & powershell @command 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "$Operation failed: $($output -join ' ')"
    }
    return ConvertFrom-JsonOutput -Output $output -Operation $Operation
}

function Get-BiliSumStatus([string]$TranscriptionId) {
    return Invoke-BiliSumJson -Arguments @(
        "-Action", "status",
        "-TranscriptionId", $TranscriptionId
    ) -Operation "BiliSum status"
}

function Start-BiliSumTranscription([string]$Url, [string]$Title) {
    return Invoke-BiliSumJson -Arguments @(
        "-Action", "transcribe",
        "-Source", $Url,
        "-Language", "zh",
        "-Title", $Title,
        "-NoWait"
    ) -Operation "BiliSum transcription submission"
}

function Export-BiliSumTranscript([string]$TranscriptionId, [string]$OutputPath) {
    $temporaryPath = "$OutputPath.partial"
    if (Test-Path -LiteralPath $temporaryPath) {
        [System.IO.File]::Delete($temporaryPath)
    }

    $command = @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", $wrapperPath,
        "-Action", "artifact",
        "-TranscriptionId", $TranscriptionId,
        "-Format", "txt",
        "-OutputPath", $temporaryPath
    )
    $output = & powershell @command 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "BiliSum TXT export failed: $($output -join ' ')"
    }
    if (-not (Test-Path -LiteralPath $temporaryPath -PathType Leaf)) {
        throw "BiliSum reported a successful export but no file was created: $temporaryPath"
    }
    if ((Get-Item -LiteralPath $temporaryPath).Length -eq 0) {
        throw "BiliSum exported an empty TXT file: $temporaryPath"
    }

    if (Test-Path -LiteralPath $OutputPath) {
        [System.IO.File]::Delete($OutputPath)
    }
    [System.IO.File]::Move($temporaryPath, $OutputPath)
}

function Get-BilibiliView([string]$Bvid) {
    $uri = "https://api.bilibili.com/x/web-interface/view?bvid=$Bvid"
    $response = Invoke-RestMethod -Uri $uri -Method Get -TimeoutSec 30
    if ([int]$response.code -ne 0) {
        throw "Bilibili view API failed for $Bvid with code $($response.code): $($response.message)"
    }
    return $response.data
}

function New-Inventory {
    Assert-File -Path $manifestPath -Label "Manifest"
    $manifest = Read-Json -Path $manifestPath
    $groups = $manifest.records | Group-Object bilibiliUrl | Sort-Object Name
    $videos = [System.Collections.Generic.List[object]]::new()
    $failures = [System.Collections.Generic.List[object]]::new()
    $position = 0

    foreach ($group in $groups) {
        $position++
        $bvid = Get-Bvid -Url $group.Name
        try {
            $view = Get-BilibiliView -Bvid $bvid
            $parts = @($view.pages | ForEach-Object {
                [pscustomobject]@{
                    page = [int]$_.page
                    cid = [long]$_.cid
                    title = [string]$_.part
                    durationSeconds = [int]$_.duration
                    url = "https://www.bilibili.com/video/${bvid}?p=$([int]$_.page)"
                }
            })
            $videos.Add([pscustomobject]@{
                bvid = $bvid
                url = $group.Name
                title = [string]$view.title
                recordCodes = @($group.Group.code)
                pageCount = [int]$view.videos
                totalDurationSeconds = [int]$view.duration
                parts = $parts
            })
        } catch {
            $failures.Add([pscustomobject]@{
                bvid = $bvid
                url = $group.Name
                recordCodes = @($group.Group.code)
                message = $_.Exception.Message
            })
        }

        if (($position % 25) -eq 0 -or $position -eq $groups.Count) {
            Write-Host "[inventory] inspected $position/$($groups.Count) videos"
        }
    }

    $multipartVideos = @($videos | Where-Object pageCount -gt 1)
    $multipartPartCount = 0
    foreach ($video in $multipartVideos) {
        $multipartPartCount += [int]$video.pageCount
    }
    $inventory = [ordered]@{
        generatedAt = [DateTime]::UtcNow.ToString("o")
        source = "https://api.bilibili.com/x/web-interface/view"
        uniqueVideoCount = $groups.Count
        apiSuccessCount = $videos.Count
        apiFailureCount = $failures.Count
        multipartVideoCount = $multipartVideos.Count
        multipartPartCount = $multipartPartCount
        videos = @($videos)
        failures = @($failures)
    }
    Write-Json -Path $inventoryPath -Value $inventory -Depth 20
    Write-Host "[inventory] multipart videos: $($inventory.multipartVideoCount); parts: $($inventory.multipartPartCount)"
    return $inventory
}

function Get-Inventory {
    if ($RefreshInventory -or -not (Test-Path -LiteralPath $inventoryPath -PathType Leaf)) {
        return New-Inventory
    }
    return Read-Json -Path $inventoryPath
}

function New-RepairState([object]$Inventory) {
    $manifest = Read-Json -Path $manifestPath
    $entries = [System.Collections.Generic.List[object]]::new()
    $knownTasks = @{
        "BV1uiNc6KEqq:2" = "a8699454489b4dac99369719fe3a847f"
    }

    foreach ($video in @($Inventory.videos | Where-Object pageCount -gt 1)) {
        $record = $manifest.records | Where-Object bilibiliUrl -eq $video.url | Select-Object -First 1
        foreach ($part in $video.parts) {
            $key = "$($video.bvid):$($part.page)"
            $existingP1 = $part.page -eq 1 -and $null -ne $record -and $record.status -eq "completed"
            $knownTaskId = if ($knownTasks.ContainsKey($key)) { $knownTasks[$key] } elseif ($existingP1) { $record.transcriptionId } else { $null }
            $partDirectory = Join-Path $transcriptsRoot $video.bvid
            $fileName = "p{0:D3}.txt" -f [int]$part.page
            $outputPath = Join-Path $partDirectory $fileName

            $entries.Add([pscustomobject]@{
                key = $key
                bvid = [string]$video.bvid
                page = [int]$part.page
                cid = [long]$part.cid
                title = [string]$part.title
                url = [string]$part.url
                expectedDurationSeconds = [int]$part.durationSeconds
                transcriptFile = Get-RelativePath -Path $outputPath
                status = if ($existingP1) { "seeded" } elseif ($knownTaskId) { "submitted" } else { "pending" }
                attempts = if ($knownTaskId) { 1 } else { 0 }
                transcriptionId = $knownTaskId
                provider = if ($existingP1) { $record.provider } else { $null }
                durationSeconds = if ($existingP1) { $record.durationSeconds } else { $null }
                transcriptChars = if ($existingP1) { $record.transcriptChars } else { 0 }
                sha256 = if ($existingP1) { $record.sha256 } else { $null }
                error = $null
                updatedAt = [DateTime]::UtcNow.ToString("o")
            })
        }
    }

    $state = [ordered]@{
        schemaVersion = 1
        createdAt = [DateTime]::UtcNow.ToString("o")
        updatedAt = [DateTime]::UtcNow.ToString("o")
        entries = @($entries)
    }
    Write-Json -Path $statePath -Value $state -Depth 12
    return Read-Json -Path $statePath
}

function Get-RepairState([object]$Inventory) {
    if (-not (Test-Path -LiteralPath $statePath -PathType Leaf)) {
        return New-RepairState -Inventory $Inventory
    }
    $state = Read-Json -Path $statePath
    if (@($state.entries).Count -eq 0 -and [int]$Inventory.multipartPartCount -gt 0) {
        return New-RepairState -Inventory $Inventory
    }
    return $state
}

function Save-RepairState([object]$State) {
    $State.updatedAt = [DateTime]::UtcNow.ToString("o")
    Write-Json -Path $statePath -Value $State -Depth 12
}

function Complete-EntryFromResult([object]$Entry, [object]$Status, [string]$OutputPath) {
    Export-BiliSumTranscript -TranscriptionId $Entry.transcriptionId -OutputPath $OutputPath
    $Entry.status = "completed"
    $Entry.provider = $Status.result.provider
    $Entry.durationSeconds = [double]$Status.result.duration_seconds
    $Entry.transcriptChars = Get-TextCharacterCount -Path $OutputPath
    $Entry.sha256 = Get-Sha256 -Path $OutputPath
    $Entry.error = $null
    $Entry.updatedAt = [DateTime]::UtcNow.ToString("o")
}

function Seed-ExistingP1([object]$Entry) {
    $sourcePath = Join-Path $transcriptsRoot "$($Entry.bvid).txt"
    $outputPath = Join-Path $packageRoot ($Entry.transcriptFile -replace "/", "\")
    if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) {
        throw "Existing P1 transcript is missing: $sourcePath"
    }
    [System.IO.Directory]::CreateDirectory((Split-Path -Parent $outputPath)) | Out-Null
    [System.IO.File]::Copy($sourcePath, $outputPath, $true)
    $Entry.status = "completed"
    $Entry.transcriptChars = Get-TextCharacterCount -Path $outputPath
    $Entry.sha256 = Get-Sha256 -Path $outputPath
    $Entry.error = $null
    $Entry.updatedAt = [DateTime]::UtcNow.ToString("o")
}

function Invoke-Repair([object]$Inventory) {
    Assert-File -Path $wrapperPath -Label "BiliSum skill wrapper"
    $state = Get-RepairState -Inventory $Inventory
    $entriesToProcess = if ($OnlyKey) {
        @($state.entries | Where-Object { $_.key -eq $OnlyKey })
    } else {
        @($state.entries)
    }
    if ($OnlyKey -and $entriesToProcess.Count -eq 0) {
        throw "No repair entry found for key: $OnlyKey"
    }
    $total = $entriesToProcess.Count
    foreach ($entry in $entriesToProcess) {
        $outputPath = Join-Path $packageRoot ($entry.transcriptFile -replace "/", "\")
        [System.IO.Directory]::CreateDirectory((Split-Path -Parent $outputPath)) | Out-Null
        if ($entry.status -eq "completed" -and (Test-Path -LiteralPath $outputPath -PathType Leaf) -and (Get-Item -LiteralPath $outputPath).Length -gt 0) {
            continue
        }
        if ($entry.status -eq "seeded") {
            Seed-ExistingP1 -Entry $entry
            Save-RepairState -State $state
            Write-Host "[repair] copied $($entry.key) from the existing P1 transcript"
            continue
        }
        if ($entry.status -eq "completed") {
            $entry.status = "submitted"
        }
    }

    while ($true) {
        $providerBackoffNeeded = $false
        $active = @($entriesToProcess | Where-Object { $_.status -in @("submitted", "queued", "running") })
        foreach ($entry in $active) {
            $status = Get-BiliSumStatus -TranscriptionId $entry.transcriptionId
            if ($status.status -eq "completed") {
                $outputPath = Join-Path $packageRoot ($entry.transcriptFile -replace "/", "\")
                Complete-EntryFromResult -Entry $entry -Status $status -OutputPath $outputPath
                Save-RepairState -State $state
                $completedCount = @($entriesToProcess | Where-Object status -eq "completed").Count
                Write-Host "[repair] $completedCount/$total completed $($entry.key) via $($entry.provider)"
            } elseif ($status.status -in @("queued", "running")) {
                $entry.status = [string]$status.status
                $entry.updatedAt = [DateTime]::UtcNow.ToString("o")
            } else {
                $entry.status = "failed"
                $entry.error = if ($status.error) { $status.error } else { [pscustomobject]@{ message = "Task ended with status $($status.status)" } }
                $entry.updatedAt = [DateTime]::UtcNow.ToString("o")
                Save-RepairState -State $state
                Write-Warning "[repair] failed $($entry.key): $($entry.error.message)"
                if ($entry.error.message -like "*Access to model denied*") {
                    $providerBackoffNeeded = $true
                }
            }
        }
        Save-RepairState -State $state

        if ($providerBackoffNeeded) {
            Write-Warning "[repair] provider access was temporarily denied; cooling down for $ProviderBackoffSeconds seconds"
            Start-Sleep -Seconds $ProviderBackoffSeconds
            continue
        }

        $active = @($entriesToProcess | Where-Object { $_.status -in @("submitted", "queued", "running") })
        $availableSlots = [Math]::Max(0, $Concurrency - $active.Count)
        if ($availableSlots -gt 0) {
            $candidates = @($entriesToProcess | Where-Object {
                ($_.status -eq "pending" -or $_.status -eq "failed") -and [int]$_.attempts -lt $MaxAttempts
            } | Select-Object -First $availableSlots)

            foreach ($entry in $candidates) {
                $entry.attempts = [int]$entry.attempts + 1
                $submissionTitle = "$($entry.bvid) P$($entry.page) $($entry.title)"
                $submission = Start-BiliSumTranscription -Url $entry.url -Title $submissionTitle
                $entry.transcriptionId = $submission.transcription_id
                $entry.status = "submitted"
                $entry.error = $null
                $entry.updatedAt = [DateTime]::UtcNow.ToString("o")
                Save-RepairState -State $state
                Write-Host "[repair] submitted $($entry.key) as $($entry.transcriptionId)"
            }
        }

        $remaining = @($entriesToProcess | Where-Object {
            $_.status -ne "completed" -and -not ($_.status -eq "failed" -and [int]$_.attempts -ge $MaxAttempts)
        })
        if ($remaining.Count -eq 0) {
            break
        }
        Start-Sleep -Seconds $PollSeconds
    }

    return $state
}

function Escape-Markdown([string]$Text) {
    if ($null -eq $Text) { return "" }
    return ($Text -replace "\|", "\|" -replace "`r?`n", " ")
}

function New-CombinedTranscript([object]$Video, [object[]]$Entries) {
    $orderedEntries = @($Entries | Sort-Object page)
    $completed = @($orderedEntries | Where-Object status -eq "completed")
    $combinedPath = Join-Path $transcriptsRoot "$($Video.bvid).txt"
    $builder = [System.Text.StringBuilder]::new()
    [void]$builder.AppendLine("课程：$($Video.title)")
    [void]$builder.AppendLine("B站视频：$($Video.url)")
    [void]$builder.AppendLine("分集完成度：$($completed.Count)/$($Video.pageCount)")
    [void]$builder.AppendLine()

    foreach ($entry in $orderedEntries) {
        [void]$builder.AppendLine(("=" * 72))
        [void]$builder.AppendLine(("P{0:D3} - {1}" -f [int]$entry.page, $entry.title))
        [void]$builder.AppendLine("来源：$($entry.url)")
        [void]$builder.AppendLine(("=" * 72))
        [void]$builder.AppendLine()
        if ($entry.status -eq "completed") {
            $partPath = Join-Path $packageRoot ($entry.transcriptFile -replace "/", "\")
            [void]$builder.AppendLine([System.IO.File]::ReadAllText($partPath, [System.Text.Encoding]::UTF8).TrimEnd())
        } else {
            $errorMessage = if ($entry.error) { ([string]$entry.error.message -replace "`r?`n", " ") } else { "Unknown error" }
            [void]$builder.AppendLine("[本分集转写失败：$errorMessage]")
        }
        [void]$builder.AppendLine()
        [void]$builder.AppendLine()
    }
    Write-Utf8NoBom -Path $combinedPath -Content $builder.ToString()
    return $combinedPath
}

function New-FailedItems([object]$Manifest) {
    $failedRecords = @($Manifest.records | Where-Object status -ne "completed")
    $builder = [System.Text.StringBuilder]::new()
    [void]$builder.AppendLine("# 转写失败或不完整项目")
    [void]$builder.AppendLine()
    if ($failedRecords.Count -eq 0) {
        [void]$builder.AppendLine("全部课程和分集均已转写完成。")
    } else {
        [void]$builder.AppendLine("以下课程仍有无法由 BiliSum 完成的分集。未尝试绕过平台风控或使用私有登录数据。")
        [void]$builder.AppendLine()
        foreach ($record in $failedRecords) {
            [void]$builder.AppendLine("## $($record.code)")
            [void]$builder.AppendLine()
            [void]$builder.AppendLine("- 课程：$($record.title)")
            [void]$builder.AppendLine("- 视频：[$(Get-Bvid -Url $record.bilibiliUrl)]($($record.bilibiliUrl))")
            [void]$builder.AppendLine(('- 状态：`{0}`' -f $record.status))
            if ($record.PSObject.Properties.Name -contains "partCompletion") {
                [void]$builder.AppendLine("- 分集完成度：$($record.partCompletion.completed)/$($record.partCompletion.total)")
            }
            if ($record.error) {
                [void]$builder.AppendLine("- 原因：$($record.error.message)")
            }
            $failedParts = @($record.parts | Where-Object status -ne "completed" | Sort-Object page)
            if ($failedParts.Count -gt 0) {
                [void]$builder.AppendLine("- 未完成分集：")
                foreach ($part in $failedParts) {
                    $partTitle = Escape-Markdown -Text $part.title
                    $partError = if ($part.error) { ([string]$part.error.message -replace "`r?`n", " ") } else { "Unknown error" }
                    [void]$builder.AppendLine(("  - P{0:D3} [{1}]({2})；任务 {3}；CID {4}；时长 {5} 秒；尝试 {6} 次；错误：{7}" -f [int]$part.page, $partTitle, $part.url, $part.key, $part.cid, $part.expectedDurationSeconds, $part.attempts, $partError))
                }
            }
            [void]$builder.AppendLine()
        }
    }
    Write-Utf8NoBom -Path (Join-Path $packageRoot "failed-items.md") -Content $builder.ToString()
}

function New-CourseCatalog([object]$Manifest) {
    $builder = [System.Text.StringBuilder]::new()
    [void]$builder.AppendLine("# 飞书游戏设计系统课程逐字稿目录")
    [void]$builder.AppendLine()
    [void]$builder.AppendLine("| # | 编号 | 课程 | 时长 | 关键词 | 状态 |")
    [void]$builder.AppendLine("| ---: | --- | --- | --- | --- | --- |")
    foreach ($record in $Manifest.records) {
        $title = Escape-Markdown -Text $record.title
        $duration = Escape-Markdown -Text $record.durationLabel
        $keywords = Escape-Markdown -Text (($record.keywords) -join "、")
        $status = if ($record.status -eq "completed") {
            if ($record.partCompletion.total -gt 1) {
                "[已转写 $($record.partCompletion.completed)/$($record.partCompletion.total) P]($($record.transcriptFile))"
            } else {
                "[已转写]($($record.transcriptFile))"
            }
        } elseif ($record.partCompletion.completed -gt 0) {
            "[部分转写 $($record.partCompletion.completed)/$($record.partCompletion.total) P]($($record.transcriptFile))"
        } else {
            "[失败](failed-items.md#$($record.code.ToLowerInvariant()))"
        }
        [void]$builder.AppendLine("| $($record.index) | $($record.code) | [$title]($($record.bilibiliUrl)) | $duration | $keywords | $status |")
    }
    Write-Utf8NoBom -Path (Join-Path $packageRoot "course-catalog.md") -Content $builder.ToString()
}

function New-PackageReadme([object]$Manifest) {
    $partProviders = @($Manifest.partProviderCounts | ForEach-Object { "$($_.count) 份 $($_.provider)" }) -join "，"
    $content = @"
# 飞书游戏设计系统课程逐字稿资料包

状态：``Research Input / Transcript Archive``

本资料包来自飞书多维表格“游戏设计系统课程”的“游戏设计系统课”视图。课程链接统一交给 BiliSum 转写；多分集视频先通过 B 站公开页面接口展开，再以 ``?p=N`` 逐集提交。这里保留原始逐字稿和来源追踪，不把课程内容直接写成项目设计结论。

## 来源与范围

- 飞书来源：[“哈基米游戏”在线课程表]($($Manifest.source.url))
- 表：``$($Manifest.source.table)``
- 视图：``$($Manifest.source.view)``
- 飞书课程记录：$($Manifest.courseRecordCount) 条
- 去重后 B 站视频：$($Manifest.uniqueVideoCount) 个
- B 站分集总数：$($Manifest.totalPartCount) P
- 完整课程：$($Manifest.completedVideoCount) 个
- 不完整或失败课程：$($Manifest.incompleteVideoCount) 个
- 成功逐字稿分集：$($Manifest.completedPartCount) P
- 转写来源：$partProviders
- 逐字稿总字符数：$($Manifest.totalTranscriptChars)

## 文件结构

- [course-catalog.md](course-catalog.md)：$($Manifest.courseRecordCount) 条飞书记录、课程链接、时长、关键词和逐字稿状态。
- [manifest.json](manifest.json)：课程记录、分集、BiliSum 任务 ID、转写来源、文件路径、哈希和错误信息。
- [multipart-inventory.json](multipart-inventory.json)：从 B 站公开接口读取的分集结构与 CID。
- [multipart-repair-state.json](multipart-repair-state.json)：逐分集修复任务的断点状态。
- [failed-items.md](failed-items.md)：仍无法完成或不完整的课程。
- ``transcripts/<BV>.txt``：课程合并逐字稿。
- ``transcripts/<BV>/pNNN.txt``：多分集课程的单集逐字稿。
- [repair-multipart-transcripts.ps1](repair-multipart-transcripts.ps1)：可重复执行、可断点续跑的修复脚本。

## 多分集处理

BiliSum 1.19.1 的单 URL 转写接口不会自动遍历 B 站分 P。修复脚本先读取 ``data.pages``，再把每个 ``https://www.bilibili.com/video/<BV>?p=<N>`` 作为独立任务提交。已有第 1 P 会复用，避免重复转写。

## 使用边界

逐字稿只是研究输入，可能包含字幕断句、专名和语音识别错误。引用具体观点前应回看原视频并核对上下文。

本资料包不等同于 ``research/02-theory-digests/`` 的理论摘要，也不会直接改变 GDD、Proposal 或 ``core-concept.md``。下一步应按当前设计问题选择少量相关课程，整理摘要，并回答“它如何改变本项目设计判断”。
"@
    Write-Utf8NoBom -Path (Join-Path $packageRoot "README.md") -Content $content
}

function Invoke-Finalize([object]$Inventory) {
    $manifest = Read-Json -Path $manifestPath
    $state = Get-RepairState -Inventory $Inventory
    $stateByBvid = @{}
    foreach ($entry in $state.entries) {
        if (-not $stateByBvid.ContainsKey($entry.bvid)) {
            $stateByBvid[$entry.bvid] = [System.Collections.Generic.List[object]]::new()
        }
        $stateByBvid[$entry.bvid].Add($entry)
    }
    $inventoryByBvid = @{}
    foreach ($video in $Inventory.videos) { $inventoryByBvid[$video.bvid] = $video }

    foreach ($record in $manifest.records) {
        $bvid = Get-Bvid -Url $record.bilibiliUrl
        if (-not $inventoryByBvid.ContainsKey($bvid)) {
            if (-not ($record.PSObject.Properties.Name -contains "partCompletion")) {
                $record | Add-Member -NotePropertyName partCompletion -NotePropertyValue ([pscustomobject]@{ completed = 0; total = 1 })
            }
            continue
        }
        $video = $inventoryByBvid[$bvid]
        if ([int]$video.pageCount -le 1) {
            $completed = if ($record.status -eq "completed") { 1 } else { 0 }
            $record | Add-Member -Force -NotePropertyName bilibiliPageCount -NotePropertyValue 1
            $record | Add-Member -Force -NotePropertyName bilibiliTotalDurationSeconds -NotePropertyValue ([int]$video.totalDurationSeconds)
            $record | Add-Member -Force -NotePropertyName partCompletion -NotePropertyValue ([pscustomobject]@{ completed = $completed; total = 1 })
            $record | Add-Member -Force -NotePropertyName parts -NotePropertyValue @()
            continue
        }

        $entries = @($stateByBvid[$bvid] | Sort-Object page)
        $completedEntries = @($entries | Where-Object status -eq "completed")
        if ($completedEntries.Count -gt 0) {
            $combinedPath = New-CombinedTranscript -Video $video -Entries $entries
            $record.transcriptFile = Get-RelativePath -Path $combinedPath
            $record.transcriptChars = Get-TextCharacterCount -Path $combinedPath
            $record.sha256 = Get-Sha256 -Path $combinedPath
            $completedDuration = 0.0
            foreach ($completedEntry in $completedEntries) {
                $completedDuration += [double]$completedEntry.durationSeconds
            }
            $record.durationSeconds = $completedDuration
            $providers = @($completedEntries.provider | Sort-Object -Unique)
            $record.provider = if ($providers.Count -eq 1) { $providers[0] } else { "mixed" }
        }
        $record.status = if ($completedEntries.Count -eq [int]$video.pageCount) { "completed" } elseif ($completedEntries.Count -gt 0) { "partial" } else { "failed" }
        $record.error = if ($record.status -eq "completed") { $null } else { [pscustomobject]@{ code = "MULTIPART_INCOMPLETE"; message = "$($completedEntries.Count)/$($video.pageCount) parts completed" } }
        $record | Add-Member -Force -NotePropertyName bilibiliPageCount -NotePropertyValue ([int]$video.pageCount)
        $record | Add-Member -Force -NotePropertyName bilibiliTotalDurationSeconds -NotePropertyValue ([int]$video.totalDurationSeconds)
        $record | Add-Member -Force -NotePropertyName partCompletion -NotePropertyValue ([pscustomobject]@{ completed = $completedEntries.Count; total = [int]$video.pageCount })
        $record | Add-Member -Force -NotePropertyName parts -NotePropertyValue $entries
    }

    $uniqueRecords = $manifest.records | Group-Object bilibiliUrl | ForEach-Object { $_.Group | Select-Object -First 1 }
    $completedParts = 0
    $totalParts = 0
    $totalTranscriptChars = 0L
    foreach ($uniqueRecord in $uniqueRecords) {
        $completedParts += [int]$uniqueRecord.partCompletion.completed
        $totalParts += [int]$uniqueRecord.partCompletion.total
        if ($uniqueRecord.transcriptFile) {
            $totalTranscriptChars += [long]$uniqueRecord.transcriptChars
        }
    }
    $completedVideos = @($uniqueRecords | Where-Object status -eq "completed").Count
    $completedPartProviders = @(
        foreach ($uniqueRecord in $uniqueRecords) {
            if ([int]$uniqueRecord.partCompletion.total -eq 1 -and $uniqueRecord.status -eq "completed") {
                [string]$uniqueRecord.provider
            }
        }
        foreach ($entry in $state.entries) {
            if ($entry.status -eq "completed") {
                [string]$entry.provider
            }
        }
    )
    $providerParts = @($completedPartProviders | Group-Object | ForEach-Object { [pscustomobject]@{ provider = $_.Name; count = $_.Count } })

    $manifest.generatedAt = [DateTime]::UtcNow.ToString("o")
    $manifest.completedTranscriptCount = $completedVideos
    $manifest.failedTranscriptCount = @($uniqueRecords | Where-Object status -ne "completed").Count
    $manifest.totalTranscriptChars = $totalTranscriptChars
    $manifest | Add-Member -Force -NotePropertyName totalPartCount -NotePropertyValue $totalParts
    $manifest | Add-Member -Force -NotePropertyName completedPartCount -NotePropertyValue $completedParts
    $manifest | Add-Member -Force -NotePropertyName completedVideoCount -NotePropertyValue $completedVideos
    $manifest | Add-Member -Force -NotePropertyName incompleteVideoCount -NotePropertyValue @($uniqueRecords | Where-Object status -ne "completed").Count
    $manifest | Add-Member -Force -NotePropertyName partProviderCounts -NotePropertyValue $providerParts

    Write-Json -Path $manifestPath -Value $manifest -Depth 20
    New-CourseCatalog -Manifest $manifest
    New-FailedItems -Manifest $manifest
    New-PackageReadme -Manifest $manifest
    Write-Host "[finalize] videos completed: $completedVideos/$($manifest.uniqueVideoCount); parts completed: $completedParts/$totalParts"
    return $manifest
}

function Show-Summary([object]$Inventory) {
    $state = Get-RepairState -Inventory $Inventory
    $groups = $state.entries | Group-Object status | Sort-Object Name
    Write-Host "Multipart videos: $($Inventory.multipartVideoCount)"
    Write-Host "Multipart parts: $($Inventory.multipartPartCount)"
    foreach ($group in $groups) {
        Write-Host "$($group.Name): $($group.Count)"
    }
}

Assert-File -Path $manifestPath -Label "Manifest"
Assert-File -Path $wrapperPath -Label "BiliSum skill wrapper"
$inventory = Get-Inventory

switch ($Action) {
    "Inventory" { Show-Summary -Inventory $inventory }
    "Repair" {
        Invoke-Repair -Inventory $inventory | Out-Null
        Show-Summary -Inventory $inventory
    }
    "Finalize" { Invoke-Finalize -Inventory $inventory | Out-Null }
    "Summary" { Show-Summary -Inventory $inventory }
    "All" {
        Invoke-Repair -Inventory $inventory | Out-Null
        Invoke-Finalize -Inventory $inventory | Out-Null
        Show-Summary -Inventory $inventory
    }
}
