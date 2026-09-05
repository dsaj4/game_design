# Phase 0 转写覆盖与失败报告

> 用途：记录飞书“游戏设计系统课”资料包在正式分析前的完整性状态。本文只报告来源覆盖、分集状态和可复现错误，不把未完成分集推断为已转写。

## 1. 快照结论

核验时间：2026-09-05（`manifest.json` 在本次 Finalize 后生成）

| 指标 | 结果 |
| --- | ---: |
| 飞书课程记录 | 237 |
| 去重后 B 站视频 | 235 |
| B 站接口成功读取 | 235/235 |
| 多分集视频 | 15 |
| 多分集总数 | 533 P |
| 全部资料分集总数 | 753 P |
| 已完成分集 | 749 P |
| 分集覆盖率 | 99.47%（749/753） |
| 完整视频 | 233/235 |
| 不完整视频 | 2 |
| 仍失败分集 | 4 P |
| 转写来源 | 224 份 `bilibili-subtitle`；525 份 `dashscope_funasr` |

结论：资料包可以进入“有证据边界的正式内容生产”。除下表 4 个分集外，已有分集逐字稿可以作为研究输入；两个课程的合并稿仍应标记为 `partial`，涉及缺失分集的具体观点不得从邻近分集或标题推断。

## 2. 受影响课程

| 课程 | B 站视频 | 分集完成度 | 合并稿 | 可用范围 |
| --- | --- | ---: | --- | --- |
| SJ-004 专业GDD写作全攻略 | [BV1pgNZ6JERH](https://www.bilibili.com/video/BV1pgNZ6JERH) | 44/45 | `transcripts/BV1pgNZ6JERH.txt`（48,503 字符） | 可分析其余 44 集；不得替代 P005 |
| SJ-009 你的游戏为什么不好玩？(下) 构建游戏设计体系 | [BV1cagy6xEmp](https://www.bilibili.com/video/BV1cagy6xEmp) | 74/77 | `transcripts/BV1cagy6xEmp.txt`（161,129 字符） | 可分析其余 74 集；不得替代 P007、P033、P040 |

## 3. 失败分集明细

以下记录同时存在于 `multipart-repair-state.json`、Finalize 后的 `manifest.json` 和 `failed-items.md`。对应逐字稿文件及 `.partial` 文件均已核验不存在；repair state 中的 `transcriptChars` 为 `0`、`sha256` 为 `null`，因此没有可供引用的伪稿或残留稿。

| Key | 分集标题 | CID | 预期时长 | BiliSum 任务 ID | 累计尝试次数 | 状态 |
| --- | --- | ---: | ---: | --- | ---: | --- |
| `BV1pgNZ6JERH:5` | 1-5 记住3S和3C | 40048069359 | 242 秒 | `d857f540771c4b4eb156336f67c67e25` | 8 | `failed` |
| `BV1cagy6xEmp:7` | 2-1 章节概览 | 40202406059 | 484 秒 | `bc5270a292c04a41814c89e0c457e3dd` | 8 | `failed` |
| `BV1cagy6xEmp:33` | 3-4 原型制作 | 40202470011 | 164 秒 | `e356cce293094235b315f7e0e4b26894` | 9 | `failed` |
| `BV1cagy6xEmp:40` | 4-2 游戏测试基础 | 40202470954 | 241 秒 | `dfacfdd904c0454884ed940f0757c327` | 8 | `failed` |

分集链接：

- [SJ-004 P005](https://www.bilibili.com/video/BV1pgNZ6JERH?p=5)
- [SJ-009 P007](https://www.bilibili.com/video/BV1cagy6xEmp?p=7)
- [SJ-009 P033](https://www.bilibili.com/video/BV1cagy6xEmp?p=33)
- [SJ-009 P040](https://www.bilibili.com/video/BV1cagy6xEmp?p=40)

## 4. 错误与修复证据

- 四个任务都完成了视频下载和音频提取，但在 DashScope FunASR 请求阶段失败。
- repair state 当前记录的累计尝试为 8/8/9/8 次；早期尝试历史未逐次保留，因此这里只报告可复核的累计值。四项最终错误均为：`DashScope FunASR request failed: id:1 / event:error / data:{}`。
- 修复状态中的最终失败任务时间为 2026-09-04 10:38:50–10:48:22；每个条目均为 `transcriptChars: 0`、`sha256: null`。
- B 站公开接口读取成功（`multipart-inventory.json`：235/235），所以当前证据不支持“分集不存在”或“CID 无效”作为原因。
- 官方 B 站字幕接口对四个 CID 均无可用字幕，未形成字幕回退稿。
- Finalize 已运行：`manifest.json` 显示 `completedPartCount: 749`、`completedVideoCount: 233`、`incompleteVideoCount: 2`；`failed-items.md` 仍列出同 4 个分集。
- 离线 `-Action Verify` 已通过：逐分集 Key/页码/CID、状态、任务 ID、provider、字符数、SHA-256、课程/视频/分集统计和合并稿失败占位相互一致。

当前最稳妥的技术判断是：输入可获取，但 FunASR 对这四段音频的请求在服务端返回通用错误；仅凭现有错误体无法进一步区分音频编码、内容或服务端瞬态原因。尚未切换其他 ASR 提供商，也未使用私有登录或绕过平台风控。

## 5. 正式分析使用规则

1. 课程级引用必须写明 `SJ-004 (44/45)` 或 `SJ-009 (74/77)`，不能把课程标成完整。
2. 分集级观点只允许引用 `status: completed` 且存在非空逐字稿、字符数与 SHA-256 的条目。
3. P005、P007、P033、P040 只能作为“缺失分集/待修复项”记录；不得根据标题、课程顺序或相邻分集补写结论。
4. 若后续取得替代转写，必须新建任务并在 `multipart-repair-state.json`、`manifest.json`、`failed-items.md` 同步记录任务 ID、提供商、时长、字符数和哈希，再重新运行 Finalize。
5. 任何由视频画面、外部资料或人工听写补足的内容，必须标注独立来源，不得伪装成 BiliSum 逐字稿。

## 6. 证据文件

- [manifest.json](manifest.json)：课程级汇总和逐分集状态。
- [multipart-inventory.json](multipart-inventory.json)：B 站公开接口展开的分集、CID 和预期时长。
- [multipart-repair-state.json](multipart-repair-state.json)：可断点续跑的逐分集任务状态。
- [failed-items.md](failed-items.md)：面向人工阅读的失败清单。
- [README.md](README.md)：资料包来源、处理边界和使用说明。
