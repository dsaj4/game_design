param(
    [ValidateSet("Inventory", "Repair", "Finalize", "Verify", "All", "Summary")]
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
$jsonFormatterPath = Join-Path $packageRoot "format-json.js"
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

function Assert-File([string]$Path, [string]$Label) {
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "$Label was not found: $Path"
    }
}

function ConvertTo-CanonicalText([string]$Content) {
    $normalized = $Content.Replace("`r`n", "`n").Replace("`r", "`n")
    return $normalized.TrimEnd([char]10) + "`n"
}

function Write-Utf8NoBom([string]$Path, [string]$Content) {
    $normalized = ConvertTo-CanonicalText -Content $Content
    [System.IO.File]::WriteAllText($Path, $normalized, $utf8NoBom)
}

function Write-Json([string]$Path, [object]$Value, [int]$Depth = 20) {
    $json = $Value | ConvertTo-Json -Depth $Depth -Compress
    $transactionId = [Guid]::NewGuid().ToString("N")
    $temporaryPath = "$Path.$transactionId.tmp"
    $backupPath = "$Path.$transactionId.bak"
    try {
        Write-Utf8NoBom -Path $temporaryPath -Content ($json + "`n")

        # BiliSum already requires Node; use a script file to avoid PowerShell 5.1 mangling node -e quotes.
        Assert-File -Path $jsonFormatterPath -Label "JSON formatter"
        $nodeArguments = @($jsonFormatterPath, $temporaryPath)
        $previousErrorActionPreference = $ErrorActionPreference
        try {
            $ErrorActionPreference = "Continue"
            $formatOutput = & node @nodeArguments 2>&1
            $formatExitCode = $LASTEXITCODE
        } finally {
            $ErrorActionPreference = $previousErrorActionPreference
        }
        if ($formatExitCode -ne 0) {
            throw "JSON formatting failed for ${Path}: $($formatOutput -join ' ')"
        }

        if (Test-Path -LiteralPath $Path -PathType Leaf) {
            [System.IO.File]::Replace($temporaryPath, $Path, $backupPath)
            [System.IO.File]::Delete($backupPath)
        } else {
            [System.IO.File]::Move($temporaryPath, $Path)
        }
    } finally {
        if (Test-Path -LiteralPath $temporaryPath) {
            [System.IO.File]::Delete($temporaryPath)
        }
        if (Test-Path -LiteralPath $backupPath) {
            [System.IO.File]::Delete($backupPath)
        }
    }
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

function Get-TextSha256([string]$Content) {
    $algorithm = [System.Security.Cryptography.SHA256]::Create()
    try {
        $hash = $algorithm.ComputeHash($utf8NoBom.GetBytes($Content))
        return ([System.BitConverter]::ToString($hash) -replace "-", "").ToLowerInvariant()
    } finally {
        $algorithm.Dispose()
    }
}

function Get-TextCharacterCount([string]$Path) {
    return ([System.IO.File]::ReadAllText($Path, [System.Text.Encoding]::UTF8)).Length
}

function Get-EntryTranscriptIntegrity([object]$Entry) {
    if ([string]::IsNullOrWhiteSpace([string]$Entry.transcriptionId)) {
        return [pscustomobject]@{ valid = $false; message = "BiliSum transcription ID is missing for $($Entry.key)"; actualChars = 0; actualSha256 = $null }
    }
    if ([string]::IsNullOrWhiteSpace([string]$Entry.provider)) {
        return [pscustomobject]@{ valid = $false; message = "Transcript provider is missing for $($Entry.key)"; actualChars = 0; actualSha256 = $null }
    }
    $outputPath = Join-Path $packageRoot ($Entry.transcriptFile -replace "/", "\")
    if (-not (Test-Path -LiteralPath $outputPath -PathType Leaf)) {
        return [pscustomobject]@{ valid = $false; message = "Transcript file is missing: $($Entry.transcriptFile)"; actualChars = 0; actualSha256 = $null }
    }
    if ((Get-Item -LiteralPath $outputPath).Length -le 0) {
        return [pscustomobject]@{ valid = $false; message = "Transcript file is empty: $($Entry.transcriptFile)"; actualChars = 0; actualSha256 = $null }
    }

    $actualChars = Get-TextCharacterCount -Path $outputPath
    $actualSha256 = Get-Sha256 -Path $outputPath
    if ([int64]$Entry.transcriptChars -le 0 -or [string]::IsNullOrWhiteSpace([string]$Entry.sha256)) {
        return [pscustomobject]@{ valid = $false; message = "Recorded transcript length or SHA-256 is missing for $($Entry.key)"; actualChars = $actualChars; actualSha256 = $actualSha256 }
    }
    if ($actualChars -ne [int64]$Entry.transcriptChars) {
        return [pscustomobject]@{ valid = $false; message = "Transcript character count mismatch for $($Entry.key): expected $($Entry.transcriptChars), found $actualChars"; actualChars = $actualChars; actualSha256 = $actualSha256 }
    }
    if ($actualSha256 -ne ([string]$Entry.sha256).ToLowerInvariant()) {
        return [pscustomobject]@{ valid = $false; message = "Transcript SHA-256 mismatch for $($Entry.key): expected $($Entry.sha256), found $actualSha256"; actualChars = $actualChars; actualSha256 = $actualSha256 }
    }
    return [pscustomobject]@{ valid = $true; message = $null; actualChars = $actualChars; actualSha256 = $actualSha256 }
}

function Set-EntryIntegrityFailure([object]$Entry, [object]$Integrity, [string]$Status = "failed") {
    $Entry.status = $Status
    $Entry.error = [pscustomobject]@{
        code = "LOCAL_TRANSCRIPT_INTEGRITY_MISMATCH"
        message = $Integrity.message
        actualChars = $Integrity.actualChars
        actualSha256 = $Integrity.actualSha256
    }
    $Entry.updatedAt = [DateTime]::UtcNow.ToString("o")
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
            $existingPart = $null
            if ($null -ne $record -and ($record.PSObject.Properties.Name -contains "parts")) {
                $existingPart = @($record.parts | Where-Object { [int]$_.page -eq [int]$part.page } | Select-Object -First 1)
                if ($existingPart.Count -gt 0) { $existingPart = $existingPart[0] } else { $existingPart = $null }
            }
            $existingP1 = $null -eq $existingPart -and $part.page -eq 1 -and $null -ne $record -and $record.status -eq "completed"
            $knownTaskId = if ($knownTasks.ContainsKey($key)) {
                $knownTasks[$key]
            } elseif ($null -ne $existingPart) {
                $existingPart.transcriptionId
            } elseif ($existingP1) {
                $record.transcriptionId
            } else {
                $null
            }
            $partDirectory = Join-Path $transcriptsRoot $video.bvid
            $fileName = "p{0:D3}.txt" -f [int]$part.page
            $outputPath = Join-Path $partDirectory $fileName

            $entryStatus = if ($null -ne $existingPart) { [string]$existingPart.status } elseif ($existingP1) { "seeded" } elseif ($knownTaskId) { "submitted" } else { "pending" }
            $entryAttempts = if ($null -ne $existingPart) { [int]$existingPart.attempts } elseif ($knownTaskId) { 1 } else { 0 }
            $entryProvider = if ($null -ne $existingPart) { $existingPart.provider } elseif ($existingP1) { $record.provider } else { $null }
            $entryDuration = if ($null -ne $existingPart) { $existingPart.durationSeconds } elseif ($existingP1) { $record.durationSeconds } else { $null }
            $entryChars = if ($null -ne $existingPart) { [int64]$existingPart.transcriptChars } elseif ($existingP1) { [int64]$record.transcriptChars } else { 0 }
            $entrySha256 = if ($null -ne $existingPart) { $existingPart.sha256 } elseif ($existingP1) { $record.sha256 } else { $null }
            $entryError = if ($null -ne $existingPart) { $existingPart.error } else { $null }

            $entries.Add([pscustomobject]@{
                key = $key
                bvid = [string]$video.bvid
                page = [int]$part.page
                cid = [long]$part.cid
                title = [string]$part.title
                url = [string]$part.url
                expectedDurationSeconds = [int]$part.durationSeconds
                transcriptFile = Get-RelativePath -Path $outputPath
                status = $entryStatus
                attempts = $entryAttempts
                transcriptionId = $knownTaskId
                provider = $entryProvider
                durationSeconds = $entryDuration
                transcriptChars = $entryChars
                sha256 = $entrySha256
                error = $entryError
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

function Assert-RepairStateMatchesInventory([object]$State, [object]$Inventory) {
    $expectedByKey = @{}
    foreach ($video in @($Inventory.videos | Where-Object pageCount -gt 1)) {
        foreach ($part in $video.parts) {
            $key = "$($video.bvid):$($part.page)"
            if ($expectedByKey.ContainsKey($key)) {
                throw "Inventory contains a duplicate multipart key: $key"
            }
            $expectedByKey[$key] = [pscustomobject]@{ bvid = [string]$video.bvid; page = [int]$part.page; cid = [long]$part.cid; url = [string]$part.url }
        }
    }
    if (@($State.entries).Count -ne $expectedByKey.Count) {
        throw "Repair state has $(@($State.entries).Count) entries, but the current inventory has $($expectedByKey.Count). Review multipart-repair-state.json before continuing."
    }

    $seen = @{}
    foreach ($entry in $State.entries) {
        if ($seen.ContainsKey([string]$entry.key)) {
            throw "Repair state contains a duplicate key: $($entry.key)"
        }
        $seen[[string]$entry.key] = $true
        if (-not $expectedByKey.ContainsKey([string]$entry.key)) {
            throw "Repair state key is absent from the current inventory: $($entry.key)"
        }
        $expected = $expectedByKey[[string]$entry.key]
        if ([string]$entry.bvid -ne $expected.bvid -or [int]$entry.page -ne $expected.page -or [long]$entry.cid -ne $expected.cid -or [string]$entry.url -ne $expected.url) {
            throw "Repair state metadata no longer matches the inventory for $($entry.key). Review page/CID changes before continuing."
        }
    }
}

function Get-RepairState([object]$Inventory) {
    if (-not (Test-Path -LiteralPath $statePath -PathType Leaf)) {
        return New-RepairState -Inventory $Inventory
    }
    $state = Read-Json -Path $statePath
    if (@($state.entries).Count -eq 0 -and [int]$Inventory.multipartPartCount -gt 0) {
        return New-RepairState -Inventory $Inventory
    }
    Assert-RepairStateMatchesInventory -State $state -Inventory $Inventory
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
    if ((Get-Item -LiteralPath $sourcePath).Length -le 0) {
        throw "Existing P1 transcript is empty: $sourcePath"
    }
    $sourceChars = Get-TextCharacterCount -Path $sourcePath
    $sourceSha256 = Get-Sha256 -Path $sourcePath
    if ([int64]$Entry.transcriptChars -gt 0 -and $sourceChars -ne [int64]$Entry.transcriptChars) {
        throw "Existing P1 character count mismatch for $($Entry.key): expected $($Entry.transcriptChars), found $sourceChars"
    }
    if (-not [string]::IsNullOrWhiteSpace([string]$Entry.sha256) -and $sourceSha256 -ne ([string]$Entry.sha256).ToLowerInvariant()) {
        throw "Existing P1 SHA-256 mismatch for $($Entry.key): expected $($Entry.sha256), found $sourceSha256"
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
    # Keep the filtered result an array even when OnlyKey selects one entry.
    $entriesToProcess = @(if ($OnlyKey) {
        $state.entries | Where-Object { $_.key -eq $OnlyKey }
    } else {
        $state.entries
    })
    if ($OnlyKey -and $entriesToProcess.Count -eq 0) {
        throw "No repair entry found for key: $OnlyKey"
    }
    $total = $entriesToProcess.Count
    $stateChanged = $false
    foreach ($entry in $entriesToProcess) {
        $outputPath = Join-Path $packageRoot ($entry.transcriptFile -replace "/", "\")
        [System.IO.Directory]::CreateDirectory((Split-Path -Parent $outputPath)) | Out-Null
        if ($entry.status -eq "completed") {
            $integrity = Get-EntryTranscriptIntegrity -Entry $entry
            if ($integrity.valid) {
                continue
            }
            $recoveryStatus = if ([string]::IsNullOrWhiteSpace([string]$entry.transcriptionId)) { "failed" } else { "submitted" }
            Set-EntryIntegrityFailure -Entry $entry -Integrity $integrity -Status $recoveryStatus
            $stateChanged = $true
            Write-Warning "[repair] invalidated $($entry.key): $($integrity.message)"
        }
        if ($entry.status -eq "failed" -and $entry.error -and [string]$entry.error.code -eq "LOCAL_TRANSCRIPT_INTEGRITY_MISMATCH" -and -not [string]::IsNullOrWhiteSpace([string]$entry.transcriptionId)) {
            $entry.status = "submitted"
            $stateChanged = $true
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
    if ($stateChanged) {
        Save-RepairState -State $state
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

function Get-CombinedTranscriptContent([object]$Video, [object[]]$Entries) {
    $orderedEntries = @($Entries | Sort-Object page)
    $completed = @($orderedEntries | Where-Object status -eq "completed")
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
    return ConvertTo-CanonicalText -Content $builder.ToString()
}

function New-CombinedTranscript([object]$Video, [object[]]$Entries) {
    $combinedPath = Join-Path $transcriptsRoot "$($Video.bvid).txt"
    $content = Get-CombinedTranscriptContent -Video $Video -Entries $Entries
    Write-Utf8NoBom -Path $combinedPath -Content $content
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
                    $taskId = if ([string]::IsNullOrWhiteSpace([string]$part.transcriptionId)) { "Unknown" } else { [string]$part.transcriptionId }
                    [void]$builder.AppendLine(("  - P{0:D3} [{1}]({2})；Key {3}；BiliSum 任务 ID {4}；CID {5}；时长 {6} 秒；累计尝试 {7} 次；错误：{8}" -f [int]$part.page, $partTitle, $part.url, $part.key, $taskId, $part.cid, $part.expectedDurationSeconds, $part.attempts, $partError))
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
- 完整 B 站视频：$($Manifest.completedVideoCount) 个
- 不完整或失败 B 站视频：$($Manifest.incompleteVideoCount) 个
- 成功逐字稿分集：$($Manifest.completedPartCount) P
- 转写来源：$partProviders
- 逐字稿总字符数：$($Manifest.totalTranscriptChars)

## 文件结构

- [course-catalog.md](course-catalog.md)：$($Manifest.courseRecordCount) 条飞书记录、课程链接、时长、关键词和逐字稿状态。
- [manifest.json](manifest.json)：课程记录、分集、BiliSum 任务 ID、转写来源、文件路径、哈希和错误信息；多分集视频以 ``parts[*].transcriptionId`` 为权威任务 ID，顶层只保留 ``initialTranscriptionId`` 追踪最初的基础 URL 任务。
- [multipart-inventory.json](multipart-inventory.json)：从 B 站公开接口读取的分集结构与 CID。
- [multipart-repair-state.json](multipart-repair-state.json)：逐分集修复任务的断点状态。
- [failed-items.md](failed-items.md)：仍无法完成或不完整的课程。
- ``transcripts/<BV>.txt``：课程合并逐字稿。
- ``transcripts/<BV>/pNNN.txt``：多分集课程的单集逐字稿。
- [repair-multipart-transcripts.ps1](repair-multipart-transcripts.ps1)：可重复执行、可断点续跑的修复脚本。
- ``format-json.js``：供修复脚本调用的稳定 JSON 格式化器，避免 PowerShell 5.1 产生全文件缩进噪声。
- ``.gitattributes``：把逐字稿和清单固定为 LF，避免 Windows checkout 改写字节后造成字符数或 SHA-256 误报。
- 离线核验：运行 ``repair-multipart-transcripts.ps1 -Action Verify``，复核状态、分集映射、文件字符数、SHA-256、汇总统计和失败占位。

## 多分集处理

BiliSum 1.19.1 的单 URL 转写接口不会自动遍历 B 站分 P。修复脚本先读取 ``data.pages``，再把每个 ``https://www.bilibili.com/video/<BV>?p=<N>`` 作为独立任务提交。已有第 1 P 会复用，避免重复转写。

使用 ``-RefreshInventory`` 时，脚本会逐项核对现有 repair state 的 Key、页码、CID 和 URL。若 B 站分集结构发生变化，脚本会停止，保留已有尝试记录并要求人工核对，不会静默改配旧任务。

## 使用边界

逐字稿只是研究输入，可能包含字幕断句、专名和语音识别错误。引用具体观点前应回看原视频并核对上下文。

本资料包不等同于 ``research/02-theory-digests/`` 的理论摘要，也不会直接改变 GDD、Proposal 或 ``core-concept.md``。下一步应按当前设计问题选择少量相关课程，整理摘要，并回答“它如何改变本项目设计判断”。
"@
    Write-Utf8NoBom -Path (Join-Path $packageRoot "README.md") -Content $content
}

function Invoke-Finalize([object]$Inventory) {
    $manifest = Read-Json -Path $manifestPath
    $state = Get-RepairState -Inventory $Inventory
    $integrityFailures = [System.Collections.Generic.List[string]]::new()
    if ([int]$Inventory.apiFailureCount -ne 0 -or [int]$Inventory.apiSuccessCount -ne [int]$Inventory.uniqueVideoCount) {
        $integrityFailures.Add("Bilibili inventory is incomplete: $($Inventory.apiSuccessCount)/$($Inventory.uniqueVideoCount) videos read, $($Inventory.apiFailureCount) failures")
    }
    foreach ($entry in $state.entries) {
        $entryPath = Join-Path $packageRoot ($entry.transcriptFile -replace "/", "\")
        if ($entry.status -eq "completed") {
            $integrity = Get-EntryTranscriptIntegrity -Entry $entry
            if (-not $integrity.valid) {
                $integrityFailures.Add("$($entry.key): $($integrity.message)")
            }
        } elseif ($entry.status -eq "failed") {
            if ((Test-Path -LiteralPath $entryPath) -or (Test-Path -LiteralPath "$entryPath.partial")) {
                $integrityFailures.Add("$($entry.key): failed part retains a transcript artifact")
            }
            if ([int64]$entry.transcriptChars -ne 0 -or -not [string]::IsNullOrWhiteSpace([string]$entry.sha256)) {
                $integrityFailures.Add("$($entry.key): failed part retains completed metadata")
            }
            if (-not $entry.error -or [string]::IsNullOrWhiteSpace([string]$entry.error.message)) {
                $integrityFailures.Add("$($entry.key): failed part has no error evidence")
            }
        } else {
            $integrityFailures.Add("$($entry.key): repair state is not terminal ($($entry.status))")
        }
    }
    $inventoryByBvid = @{}
    foreach ($video in $Inventory.videos) { $inventoryByBvid[$video.bvid] = $video }
    foreach ($record in @($manifest.records | Group-Object bilibiliUrl | ForEach-Object { $_.Group | Select-Object -First 1 })) {
        $recordBvid = Get-Bvid -Url $record.bilibiliUrl
        if (-not $inventoryByBvid.ContainsKey($recordBvid)) {
            $integrityFailures.Add("$($record.code): Bilibili video is absent from the current inventory")
        }
    }
    $singleRecords = @($manifest.records | Where-Object {
        $singleBvid = Get-Bvid -Url $_.bilibiliUrl
        $inventoryByBvid.ContainsKey($singleBvid) -and [int]$inventoryByBvid[$singleBvid].pageCount -le 1 -and $_.status -eq "completed"
    })
    foreach ($record in $singleRecords) {
        if ([string]::IsNullOrWhiteSpace([string]$record.transcriptionId) -or [string]::IsNullOrWhiteSpace([string]$record.provider)) {
            $integrityFailures.Add("$($record.code): completed single-part task metadata is incomplete")
            continue
        }
        $integrity = Get-RecordedFileIntegrity -RelativePath ([string]$record.transcriptFile) -ExpectedChars ([int64]$record.transcriptChars) -ExpectedSha256 ([string]$record.sha256)
        if (-not $integrity.valid) {
            $integrityFailures.Add("$($record.code): $($integrity.message)")
        }
    }
    if ($integrityFailures.Count -gt 0) {
        throw "Finalize stopped because completed transcript integrity validation failed:`n- $($integrityFailures -join "`n- "). Run Repair for a multipart artifact or restore/retranscribe a single-part artifact before retrying."
    }
    $stateByBvid = @{}
    foreach ($entry in $state.entries) {
        if (-not $stateByBvid.ContainsKey($entry.bvid)) {
            $stateByBvid[$entry.bvid] = [System.Collections.Generic.List[object]]::new()
        }
        $stateByBvid[$entry.bvid].Add($entry)
    }
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
        if (-not ($record.PSObject.Properties.Name -contains "initialTranscriptionId")) {
            $record | Add-Member -NotePropertyName initialTranscriptionId -NotePropertyValue $record.transcriptionId
        }
        $record.transcriptionId = $null
        $record | Add-Member -Force -NotePropertyName transcriptionIdAuthority -NotePropertyValue "parts[].transcriptionId"
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
    $partialVideos = @($uniqueRecords | Where-Object status -eq "partial").Count
    $failedVideos = @($uniqueRecords | Where-Object status -eq "failed").Count
    $completedRecords = @($manifest.records | Where-Object status -eq "completed").Count
    $partialRecords = @($manifest.records | Where-Object status -eq "partial").Count
    $failedRecords = @($manifest.records | Where-Object status -eq "failed").Count
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
    $providerVideos = @($uniqueRecords | Where-Object { [int]$_.partCompletion.completed -gt 0 } | Group-Object provider | ForEach-Object { [pscustomobject]@{ provider = $_.Name; count = $_.Count } })

    $manifest.generatedAt = [DateTime]::UtcNow.ToString("o")
    if (($manifest.PSObject.Properties.Name -contains "providerCounts") -and -not ($manifest.PSObject.Properties.Name -contains "initialCompletedVideoProviderCounts")) {
        $manifest | Add-Member -NotePropertyName initialCompletedVideoProviderCounts -NotePropertyValue $manifest.providerCounts
    }
    $manifest.PSObject.Properties.Remove("providerCounts")
    $manifest.PSObject.Properties.Remove("completedTranscriptCount")
    $manifest.PSObject.Properties.Remove("failedTranscriptCount")
    $manifest.totalTranscriptChars = $totalTranscriptChars
    $manifest | Add-Member -Force -NotePropertyName completedRecordCount -NotePropertyValue $completedRecords
    $manifest | Add-Member -Force -NotePropertyName partialRecordCount -NotePropertyValue $partialRecords
    $manifest | Add-Member -Force -NotePropertyName failedRecordCount -NotePropertyValue $failedRecords
    $manifest | Add-Member -Force -NotePropertyName totalPartCount -NotePropertyValue $totalParts
    $manifest | Add-Member -Force -NotePropertyName completedPartCount -NotePropertyValue $completedParts
    $manifest | Add-Member -Force -NotePropertyName completedVideoCount -NotePropertyValue $completedVideos
    $manifest | Add-Member -Force -NotePropertyName partialVideoCount -NotePropertyValue $partialVideos
    $manifest | Add-Member -Force -NotePropertyName failedVideoCount -NotePropertyValue $failedVideos
    $manifest | Add-Member -Force -NotePropertyName incompleteVideoCount -NotePropertyValue ($partialVideos + $failedVideos)
    $manifest | Add-Member -Force -NotePropertyName videoProviderCounts -NotePropertyValue $providerVideos
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

function Add-VerificationIssue([System.Collections.Generic.List[string]]$Issues, [string]$Message) {
    $Issues.Add($Message) | Out-Null
}

function Get-RecordedFileIntegrity([string]$RelativePath, [int64]$ExpectedChars, [string]$ExpectedSha256) {
    if ([string]::IsNullOrWhiteSpace($RelativePath)) {
        return [pscustomobject]@{ valid = $false; message = "Transcript path is missing" }
    }
    $fullPath = Join-Path $packageRoot ($RelativePath -replace "/", "\")
    if (-not (Test-Path -LiteralPath $fullPath -PathType Leaf)) {
        return [pscustomobject]@{ valid = $false; message = "Transcript file is missing: $RelativePath" }
    }
    if ((Get-Item -LiteralPath $fullPath).Length -le 0) {
        return [pscustomobject]@{ valid = $false; message = "Transcript file is empty: $RelativePath" }
    }
    $actualChars = Get-TextCharacterCount -Path $fullPath
    $actualSha256 = Get-Sha256 -Path $fullPath
    if ($actualChars -ne $ExpectedChars) {
        return [pscustomobject]@{ valid = $false; message = "Character count mismatch for ${RelativePath}: expected $ExpectedChars, found $actualChars" }
    }
    if ([string]::IsNullOrWhiteSpace($ExpectedSha256) -or $actualSha256 -ne $ExpectedSha256.ToLowerInvariant()) {
        return [pscustomobject]@{ valid = $false; message = "SHA-256 mismatch for ${RelativePath}: expected $ExpectedSha256, found $actualSha256" }
    }
    return [pscustomobject]@{ valid = $true; message = $null }
}

function Invoke-Verify([object]$Inventory) {
    $manifest = Read-Json -Path $manifestPath
    $state = Get-RepairState -Inventory $Inventory
    $issues = [System.Collections.Generic.List[string]]::new()
    $manifestUniqueRecords = @($manifest.records | Group-Object bilibiliUrl | ForEach-Object { $_.Group | Select-Object -First 1 })
    $inventoryByBvid = @{}
    foreach ($video in $Inventory.videos) {
        if ($inventoryByBvid.ContainsKey([string]$video.bvid)) {
            Add-VerificationIssue -Issues $issues -Message "Bilibili inventory contains duplicate video $($video.bvid)."
        } else {
            $inventoryByBvid[[string]$video.bvid] = $video
        }
    }

    if ([int]$Inventory.apiFailureCount -ne 0 -or [int]$Inventory.apiSuccessCount -ne [int]$Inventory.uniqueVideoCount) {
        Add-VerificationIssue -Issues $issues -Message "Bilibili inventory is incomplete."
    }
    if (@($manifest.records).Count -ne [int]$manifest.courseRecordCount) {
        Add-VerificationIssue -Issues $issues -Message "courseRecordCount does not match records[]."
    }
    if ($manifestUniqueRecords.Count -ne [int]$manifest.uniqueVideoCount) {
        Add-VerificationIssue -Issues $issues -Message "uniqueVideoCount does not match unique Bilibili URLs."
    }

    foreach ($record in $manifest.records) {
        $recordBvid = Get-Bvid -Url $record.bilibiliUrl
        if (-not $inventoryByBvid.ContainsKey($recordBvid)) {
            Add-VerificationIssue -Issues $issues -Message "$($record.code) is absent from the Bilibili inventory."
            continue
        }

        $video = $inventoryByBvid[$recordBvid]
        $recordParts = if ($record.PSObject.Properties.Name -contains "parts") { @($record.parts) } else { @() }
        if (-not ($record.PSObject.Properties.Name -contains "bilibiliPageCount") -or [int]$record.bilibiliPageCount -ne [int]$video.pageCount) {
            Add-VerificationIssue -Issues $issues -Message "$($record.code) bilibiliPageCount does not match the inventory."
        }
        if (-not ($record.PSObject.Properties.Name -contains "partCompletion") -or [int]$record.partCompletion.total -ne [int]$video.pageCount) {
            Add-VerificationIssue -Issues $issues -Message "$($record.code) partCompletion.total does not match the inventory."
        }

        if ([int]$video.pageCount -le 1) {
            if ($recordParts.Count -ne 0) {
                Add-VerificationIssue -Issues $issues -Message "$($record.code) is single-part in the inventory but has manifest parts."
            }
            continue
        }
        if ($recordParts.Count -ne [int]$video.pageCount) {
            Add-VerificationIssue -Issues $issues -Message "$($record.code) has $($recordParts.Count) manifest parts; expected $($video.pageCount) from the inventory."
        }

        $inventoryPartsByPage = @{}
        foreach ($inventoryPart in $video.parts) {
            $inventoryPage = [int]$inventoryPart.page
            if ($inventoryPartsByPage.ContainsKey($inventoryPage)) {
                Add-VerificationIssue -Issues $issues -Message "Bilibili inventory contains duplicate page $inventoryPage for $recordBvid."
            } else {
                $inventoryPartsByPage[$inventoryPage] = $inventoryPart
            }
        }
        $seenPages = @{}
        foreach ($part in $recordParts) {
            $page = [int]$part.page
            $expectedKey = "${recordBvid}:$page"
            if ($seenPages.ContainsKey($page)) {
                Add-VerificationIssue -Issues $issues -Message "$($record.code) contains duplicate manifest page $page."
            } else {
                $seenPages[$page] = $true
            }
            if ([string]$part.bvid -ne $recordBvid -or [string]$part.key -ne $expectedKey) {
                Add-VerificationIssue -Issues $issues -Message "$($record.code) part $($part.key) is attached to the wrong parent video or key."
            }
            if (-not $inventoryPartsByPage.ContainsKey($page)) {
                Add-VerificationIssue -Issues $issues -Message "$($record.code) manifest page $page is absent from the inventory."
                continue
            }
            $inventoryPart = $inventoryPartsByPage[$page]
            if ([long]$part.cid -ne [long]$inventoryPart.cid -or [string]$part.url -ne [string]$inventoryPart.url) {
                Add-VerificationIssue -Issues $issues -Message "$($record.code) manifest page $page CID or URL differs from the inventory."
            }
        }
    }

    $manifestPartsByKey = @{}
    foreach ($record in $manifestUniqueRecords) {
        $recordBvid = Get-Bvid -Url $record.bilibiliUrl
        if (-not $inventoryByBvid.ContainsKey($recordBvid) -or [int]$inventoryByBvid[$recordBvid].pageCount -le 1) {
            continue
        }
        $video = $inventoryByBvid[$recordBvid]
        if ($null -ne $record.transcriptionId -or [string]::IsNullOrWhiteSpace([string]$record.initialTranscriptionId) -or [string]$record.transcriptionIdAuthority -ne "parts[].transcriptionId") {
            Add-VerificationIssue -Issues $issues -Message "Multipart task authority fields are invalid for $($record.code)."
        }
        foreach ($part in $record.parts) {
            if ($manifestPartsByKey.ContainsKey([string]$part.key)) {
                Add-VerificationIssue -Issues $issues -Message "Manifest contains duplicate multipart key $($part.key)."
            } else {
                $manifestPartsByKey[[string]$part.key] = $part
            }
        }

        $combinedIntegrity = Get-RecordedFileIntegrity -RelativePath ([string]$record.transcriptFile) -ExpectedChars ([int64]$record.transcriptChars) -ExpectedSha256 ([string]$record.sha256)
        $combinedText = $null
        if (-not $combinedIntegrity.valid) {
            Add-VerificationIssue -Issues $issues -Message "$($record.code): $($combinedIntegrity.message)"
        } else {
            $combinedPath = Join-Path $packageRoot ($record.transcriptFile -replace "/", "\")
            $combinedText = [System.IO.File]::ReadAllText($combinedPath, [System.Text.Encoding]::UTF8)
            $placeholderCount = [regex]::Matches($combinedText, [regex]::Escape("[本分集转写失败：")).Count
            $expectedPlaceholders = @($record.parts | Where-Object status -ne "completed").Count
            if ($placeholderCount -ne $expectedPlaceholders) {
                Add-VerificationIssue -Issues $issues -Message "$($record.code) has $placeholderCount failure placeholders; expected $expectedPlaceholders."
            }
        }
        try {
            $expectedCombinedText = Get-CombinedTranscriptContent -Video $video -Entries @($record.parts)
            $expectedCombinedSha256 = Get-TextSha256 -Content $expectedCombinedText
            if ($expectedCombinedText.Length -ne [int64]$record.transcriptChars -or $expectedCombinedSha256 -ne ([string]$record.sha256).ToLowerInvariant()) {
                Add-VerificationIssue -Issues $issues -Message "$($record.code) combined transcript metadata does not match content rebuilt from its parts."
            }
            if ($null -ne $combinedText -and -not [string]::Equals($combinedText, $expectedCombinedText, [System.StringComparison]::Ordinal)) {
                Add-VerificationIssue -Issues $issues -Message "$($record.code) combined transcript content differs from content rebuilt from its parts."
            }
        } catch {
            Add-VerificationIssue -Issues $issues -Message "$($record.code) combined transcript could not be rebuilt from its parts: $($_.Exception.Message)"
        }
    }

    if ($manifestPartsByKey.Count -ne @($state.entries).Count) {
        Add-VerificationIssue -Issues $issues -Message "Manifest multipart part count does not match repair state."
    }
    foreach ($entry in $state.entries) {
        if (-not $manifestPartsByKey.ContainsKey([string]$entry.key)) {
            Add-VerificationIssue -Issues $issues -Message "Repair state entry is absent from manifest: $($entry.key)."
            continue
        }
        $manifestPart = $manifestPartsByKey[[string]$entry.key]
        $manifestErrorCode = if ($manifestPart.error) { [string]$manifestPart.error.code } else { "" }
        $manifestErrorMessage = if ($manifestPart.error) { [string]$manifestPart.error.message } else { "" }
        $entryErrorCode = if ($entry.error) { [string]$entry.error.code } else { "" }
        $entryErrorMessage = if ($entry.error) { [string]$entry.error.message } else { "" }
        if ([string]$manifestPart.bvid -ne [string]$entry.bvid -or [int]$manifestPart.page -ne [int]$entry.page -or [long]$manifestPart.cid -ne [long]$entry.cid -or [string]$manifestPart.title -ne [string]$entry.title -or [string]$manifestPart.url -ne [string]$entry.url -or [int]$manifestPart.expectedDurationSeconds -ne [int]$entry.expectedDurationSeconds -or [string]$manifestPart.transcriptFile -ne [string]$entry.transcriptFile -or [string]$manifestPart.status -ne [string]$entry.status -or [int]$manifestPart.attempts -ne [int]$entry.attempts -or [string]$manifestPart.transcriptionId -ne [string]$entry.transcriptionId -or [string]$manifestPart.provider -ne [string]$entry.provider -or [string]$manifestPart.durationSeconds -ne [string]$entry.durationSeconds -or [int64]$manifestPart.transcriptChars -ne [int64]$entry.transcriptChars -or [string]$manifestPart.sha256 -ne [string]$entry.sha256 -or $manifestErrorCode -ne $entryErrorCode -or $manifestErrorMessage -ne $entryErrorMessage -or [string]$manifestPart.updatedAt -ne [string]$entry.updatedAt) {
            Add-VerificationIssue -Issues $issues -Message "Manifest part metadata differs from repair state for $($entry.key)."
        }

        $partPath = Join-Path $packageRoot ($entry.transcriptFile -replace "/", "\")
        if ($entry.status -eq "completed") {
            $integrity = Get-EntryTranscriptIntegrity -Entry $entry
            if (-not $integrity.valid) {
                Add-VerificationIssue -Issues $issues -Message $integrity.message
            }
        } elseif ($entry.status -eq "failed") {
            if ((Test-Path -LiteralPath $partPath) -or (Test-Path -LiteralPath "$partPath.partial")) {
                Add-VerificationIssue -Issues $issues -Message "Failed part retains a transcript artifact: $($entry.key)."
            }
            if ([int64]$entry.transcriptChars -ne 0 -or -not [string]::IsNullOrWhiteSpace([string]$entry.sha256)) {
                Add-VerificationIssue -Issues $issues -Message "Failed part retains completed metadata: $($entry.key)."
            }
            if (-not $entry.error -or [string]::IsNullOrWhiteSpace([string]$entry.error.message)) {
                Add-VerificationIssue -Issues $issues -Message "Failed part has no error evidence: $($entry.key)."
            }
        } else {
            Add-VerificationIssue -Issues $issues -Message "Repair state is not terminal for $($entry.key): $($entry.status)."
        }
    }

    foreach ($record in $manifest.records) {
        $recordBvid = Get-Bvid -Url $record.bilibiliUrl
        if (-not $inventoryByBvid.ContainsKey($recordBvid) -or [int]$inventoryByBvid[$recordBvid].pageCount -gt 1) {
            continue
        }
        if ($record.status -eq "completed") {
            if ([string]::IsNullOrWhiteSpace([string]$record.transcriptionId) -or [string]::IsNullOrWhiteSpace([string]$record.provider)) {
                Add-VerificationIssue -Issues $issues -Message "Single-part task metadata is incomplete for $($record.code)."
            }
            $integrity = Get-RecordedFileIntegrity -RelativePath ([string]$record.transcriptFile) -ExpectedChars ([int64]$record.transcriptChars) -ExpectedSha256 ([string]$record.sha256)
            if (-not $integrity.valid) {
                Add-VerificationIssue -Issues $issues -Message "$($record.code): $($integrity.message)"
            }
        }
    }

    $computedTotalParts = 0
    $computedCompletedParts = 0
    $computedTotalTranscriptChars = 0L
    foreach ($record in $manifestUniqueRecords) {
        $recordBvid = Get-Bvid -Url $record.bilibiliUrl
        $actualTotal = if (@($record.parts).Count -gt 0) { @($record.parts).Count } else { 1 }
        $actualCompleted = if (@($record.parts).Count -gt 0) { @($record.parts | Where-Object status -eq "completed").Count } elseif ($record.status -eq "completed") { 1 } else { 0 }
        if ([int]$record.partCompletion.total -ne $actualTotal -or [int]$record.partCompletion.completed -ne $actualCompleted) {
            Add-VerificationIssue -Issues $issues -Message "$($record.code) partCompletion does not match its actual part states."
        }
        if ([int]$record.bilibiliPageCount -ne $actualTotal) {
            Add-VerificationIssue -Issues $issues -Message "$($record.code) bilibiliPageCount does not match its actual parts."
        }
        if ($Inventory.videos.bvid -notcontains $recordBvid) {
            Add-VerificationIssue -Issues $issues -Message "$($record.code) is absent from the Bilibili inventory."
        }
        $expectedStatus = if ($actualCompleted -eq $actualTotal) { "completed" } elseif ($actualCompleted -gt 0) { "partial" } else { "failed" }
        if ([string]$record.status -ne $expectedStatus) {
            Add-VerificationIssue -Issues $issues -Message "$($record.code) status is $($record.status); expected $expectedStatus from part states."
        }
        $computedTotalParts += $actualTotal
        $computedCompletedParts += $actualCompleted
        if (-not [string]::IsNullOrWhiteSpace([string]$record.transcriptFile)) {
            $computedTotalTranscriptChars += [int64]$record.transcriptChars
        }
    }
    $computedCompletedVideos = @($manifestUniqueRecords | Where-Object status -eq "completed").Count
    $computedPartialVideos = @($manifestUniqueRecords | Where-Object status -eq "partial").Count
    $computedFailedVideos = @($manifestUniqueRecords | Where-Object status -eq "failed").Count
    $computedCompletedRecords = @($manifest.records | Where-Object status -eq "completed").Count
    $computedPartialRecords = @($manifest.records | Where-Object status -eq "partial").Count
    $computedFailedRecords = @($manifest.records | Where-Object status -eq "failed").Count
    if ([int]$manifest.totalPartCount -ne $computedTotalParts -or [int]$manifest.completedPartCount -ne $computedCompletedParts) {
        Add-VerificationIssue -Issues $issues -Message "Manifest part totals do not match record data."
    }
    if ([int]$manifest.completedVideoCount -ne $computedCompletedVideos -or [int]$manifest.partialVideoCount -ne $computedPartialVideos -or [int]$manifest.failedVideoCount -ne $computedFailedVideos -or [int]$manifest.incompleteVideoCount -ne ($computedPartialVideos + $computedFailedVideos)) {
        Add-VerificationIssue -Issues $issues -Message "Manifest video status totals do not match unique records."
    }
    if ([int]$manifest.completedRecordCount -ne $computedCompletedRecords -or [int]$manifest.partialRecordCount -ne $computedPartialRecords -or [int]$manifest.failedRecordCount -ne $computedFailedRecords) {
        Add-VerificationIssue -Issues $issues -Message "Manifest course-record status totals do not match records[]."
    }
    if ([int64]$manifest.totalTranscriptChars -ne $computedTotalTranscriptChars) {
        Add-VerificationIssue -Issues $issues -Message "totalTranscriptChars does not match unique record metadata."
    }

    $expectedPartProviders = @{}
    foreach ($record in @($manifestUniqueRecords | Where-Object { [int]$_.partCompletion.total -eq 1 -and $_.status -eq "completed" })) {
        $provider = [string]$record.provider
        if (-not $expectedPartProviders.ContainsKey($provider)) { $expectedPartProviders[$provider] = 0 }
        $expectedPartProviders[$provider]++
    }
    foreach ($entry in @($state.entries | Where-Object status -eq "completed")) {
        $provider = [string]$entry.provider
        if (-not $expectedPartProviders.ContainsKey($provider)) { $expectedPartProviders[$provider] = 0 }
        $expectedPartProviders[$provider]++
    }
    $reportedPartProviders = @{}
    foreach ($providerCount in $manifest.partProviderCounts) { $reportedPartProviders[[string]$providerCount.provider] = [int]$providerCount.count }
    foreach ($provider in @(@($expectedPartProviders.Keys) + @($reportedPartProviders.Keys) | Sort-Object -Unique)) {
        $expectedCount = if ($expectedPartProviders.ContainsKey($provider)) { [int]$expectedPartProviders[$provider] } else { 0 }
        $reportedCount = if ($reportedPartProviders.ContainsKey($provider)) { [int]$reportedPartProviders[$provider] } else { 0 }
        if ($expectedCount -ne $reportedCount) {
            Add-VerificationIssue -Issues $issues -Message "partProviderCounts mismatch for ${provider}: expected $expectedCount, found $reportedCount."
        }
    }

    $expectedVideoProviders = @{}
    foreach ($record in @($manifestUniqueRecords | Where-Object { [int]$_.partCompletion.completed -gt 0 })) {
        $provider = [string]$record.provider
        if (-not $expectedVideoProviders.ContainsKey($provider)) { $expectedVideoProviders[$provider] = 0 }
        $expectedVideoProviders[$provider]++
    }
    $reportedVideoProviders = @{}
    foreach ($providerCount in $manifest.videoProviderCounts) { $reportedVideoProviders[[string]$providerCount.provider] = [int]$providerCount.count }
    foreach ($provider in @(@($expectedVideoProviders.Keys) + @($reportedVideoProviders.Keys) | Sort-Object -Unique)) {
        $expectedCount = if ($expectedVideoProviders.ContainsKey($provider)) { [int]$expectedVideoProviders[$provider] } else { 0 }
        $reportedCount = if ($reportedVideoProviders.ContainsKey($provider)) { [int]$reportedVideoProviders[$provider] } else { 0 }
        if ($expectedCount -ne $reportedCount) {
            Add-VerificationIssue -Issues $issues -Message "videoProviderCounts mismatch for ${provider}: expected $expectedCount, found $reportedCount."
        }
    }

    if ($issues.Count -gt 0) {
        throw "Transcript package verification failed with $($issues.Count) issue(s):`n- $($issues -join "`n- ")"
    }
    Write-Host "[verify] records: $($manifest.courseRecordCount); videos: $($manifest.uniqueVideoCount); parts: $computedCompletedParts/$computedTotalParts; failed parts: $(@($state.entries | Where-Object status -eq 'failed').Count)"
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
    "Verify" { Invoke-Verify -Inventory $inventory }
    "Summary" { Show-Summary -Inventory $inventory }
    "All" {
        Invoke-Repair -Inventory $inventory | Out-Null
        Invoke-Finalize -Inventory $inventory | Out-Null
        Invoke-Verify -Inventory $inventory
        Show-Summary -Inventory $inventory
    }
}
