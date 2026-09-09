# 研究与证据文件契约

版本：v1.0。状态：`Reference Ready / Operational Contract`。更新日期：2026-09-09。

本页规定玩法探索区如何把研究问题、外部来源、观察、推断、假设和结论保存为可追踪文件。它是共享方法，不是任何项目的玩法决定；两个探索项目必须先按项目注册表路由，再将文件写入各自项目根目录 `P/`。

## 1. 用途与边界

研究文件回答“我们知道什么、依据是什么、还不知道什么、下一步如何验证”。它服务于外部媒体或产品分析、规则与数值研究、模拟运行与原型试玩观察，以及将研究转化为候选设计假设。

研究文件不承担 GDD 正文、代码实现说明、构建日志或玩法采纳记录。研究结果必须经过目标项目的 `idea-inbox → 资格确认 → idea-materials → Proposal/Evaluation` 流程，才可影响正式设计；模拟或试玩完成不自动把假设升级为 `Confirmed` 或 `Accepted`。

## 2. 文件类型与保存位置

路径中的 `P` 指当前 Project ID 对应的项目根：`exploration/game-002-optimization/` 或 `exploration/new-roguelike/`。

| 文件类型 | 目的 | 保存位置 | 最低状态 |
| --- | --- | --- | --- |
| `Question` | 可验证的研究问题与范围 | `P/questions/YYYY-MM-DD-<short-name>.md` | `Open / Answered / Parked` |
| `Source Card` | 一个外部来源或项目内输入的身份、版本和许可边界 | 项目 `insights/` 报告内嵌，或 `P/insights/sources/SRC-<id>.md` | `Registered / Retrieved / Failed / Superseded` |
| `Evidence Card` | 来源中的可定位事实、玩家解释或观察片段 | `P/insights/evidence/E-<id>.md` | `Observed / Reported / Inferred / Disputed` |
| `Research Insight` | 围绕一个问题组织证据、分析和限制的报告 | `P/insights/YYYY-MM-DD-<topic>-analysis.md` | `Research / Reviewed / Superseded` |
| `Design Hypothesis` | 可进入资格确认的候选设计假设 | `P/idea-inbox/YYYY-MM-DD-<short-name>.md` | `Raw Idea / Unqualified` |
| `Research Conclusion` | 对问题的暂时结论及下一步 | 通常作为 Insight 的末节；必要时独立放 `P/insights/conclusions/` | `Provisional / Supported / Rejected / Unknown` |

如果项目没有建立 `sources/` 或 `evidence/` 子目录，可先把卡片放在报告同一文件中，但必须使用下方字段，不得省略来源 ID 和定位信息。共享目录只放本契约，不放项目研究结果。

### `Question` 最小模板

```markdown
# Q-YYYY-MM-DD-short-name

- Project ID：
- 状态：Open / Answered / Parked
- 提出日期与负责人：
- 问题：一句可被证据或实验回答的问题
- 相关候选/章节：路径、版本或 `Unknown`
- 当前已知：引用 `[SRC-...]` / `[E-...]`
- 未知与影响：
- 方法与最小验证：网络搜索 / 媒体分析 / 模拟 / 原型 / 人工评议
- 成功信号、失败信号、停止条件：
- 下一步与更新时间：
```

问题状态表示研究工作进度，不表示玩法状态；`Answered` 也可能得到 `Unknown` 或 `Insufficient Evidence`。

## 3. 通用文件头

所有研究文件至少包含以下元数据；未知值写 `Unknown`，不可留空：

```yaml
---
id: E-YYYYMMDD-001
type: Evidence Card
project_id: game-002-optimization
status: Observed
created: 2026-09-09
updated: 2026-09-09
question_ids: [Q-20260909-001]
source_ids: [SRC-EXAMPLE-001]
method: media-analysis
author: agent | user | external
version: v1
---
```

`project_id`、`status`、`question_ids` 和 `source_ids` 是必填；`method` 必须与实际方法一致。文件更新时保留旧版本链接或在变更记录中说明替代关系。

可用的 `method` 值包括 `media-analysis`、`web-research`、`simulation`、`prototype` 和 `desk-review`。不同文件类型可复用同一头部，但 `id` 前缀应与类型匹配，例如 `Q-`、`SRC-`、`E-`、`I-` 或 `H-`。

## 4. 来源登记契约

来源先登记再引用。外部网页、视频、文章、论文、游戏版本、用户提供文件和项目背景包都必须有唯一 `Source ID`。仅供一个项目使用的来源可登记在该项目 `insights/`；会被两个探索项目复用、或需要作为共享框架依据的来源，必须同时登记到[探索区来源注册表](../../registry/source-registry.md)。来源卡至少写：

```markdown
# SRC-<id> <标题>

- 类型：网页 / 视频 / 论文 / 游戏版本 / 用户文件 / 项目背景
- 位置：URL 或仓库相对路径
- 所属项目：Project ID 或 `Shared`
- 发布/版本日期：Unknown 也要注明
- 获取时间：YYYY-MM-DD HH:mm TZ
- 固定版本：URL、提交、文件 mtime 或内容哈希（至少一种）
- 许可与保存边界：可引用范围、是否允许本地副本
- 状态：Registered / Retrieved / Failed / Superseded

## 摘要

只写来源实际表达；不要混入本项目推断。

## 可引用定位

- 章节、页码、时间戳、段落或文件行号：
```

网络搜索是外部产品研究的必做步骤。记录搜索日期、查询词、筛选理由和最终采用的来源；搜索摘要只能作为线索，不能替代原文证据。完整体验视频可选调用 `bilisum-transcribe`，若调用则记录工具版本、转写文件路径/哈希和人工抽查范围；未调用不构成缺陷。

## 5. 证据与推理分层

一条证据只表达一个可定位事实或明确观点，并标注证据层级：

| 层级 | 写法 | 含义 |
| --- | --- | --- |
| `Direct Observation` | `Observed` | 从视频画面、实际试玩、日志或数据直接看到/测得 |
| `Source Claim` | `Reported` | 来源作者、开发者或玩家明确说出的观点 |
| `Agent Inference` | `Inferred` | 基于一条或多条证据的分析推断 |
| `Player Interpretation` | `Interpreted` | 玩家能否理解、喜欢或形成策略的解释 |
| `Unknown` | `Unknown` | 当前材料无法判断，保留待验证问题 |

不得把 `Reported` 改写成项目事实，不得把 `Inferred` 写成已验证体验。`Observed`、`Reported`、`Inferred` 和 `Interpreted` 是证据层级；`Disputed` 表示证据之间存在冲突，`Unknown` 表示尚无足够证据。每条引用使用 `[E-<id>]`，并在报告中给出来源定位。

## 6. 研究报告最小结构

```markdown
# <主题>研究

- Project ID：
- 状态：Research / Reviewed
- 研究问题：Q-...
- 日期与材料覆盖：
- 方法：web-research / media-analysis / simulation / prototype
- 来源：SRC-...

## 主要结论
按“观察 / 来源观点 / 推断”区分，直接回答问题。

## 证据
| ID | 层级 | 事实或观点 | 定位 | 限制 |
| --- | --- | --- | --- | --- |
| E-... | Observed |  |  |  |

## 机制与行为
`玩家处境 → 可见信息 → 行动 → 规则变化 → 反馈 → 下一次选择`

## 可转化假设
说明目标项目中的设计对象、玩家影响、预期价值和最小验证方式。新候选只登记到 `P/idea-inbox/`，状态为 `Raw Idea / Unqualified`。

## 未知、冲突与限制

## 下一步
问题、实验/原型、成功信号、失败信号、停止条件。
```

报告可以按材料增减章节，但不能删除问题、来源、证据层级、限制和下一步。一个报告只围绕一个主要研究问题；多个问题要分别建立 `Question ID` 或在报告中明确子问题。

## 7. 状态边界与晋级

- `Research`：材料已整理，结论仍受证据范围限制。
- `Reviewed`：完成来源定位、证据层级和自检；不代表设计采纳。
- `Provisional / Supported`：研究问题在限定范围内得到支持，仍需项目资格确认或实验复核。
- `Rejected`：该假设在当前证据和范围内不支持；保留失败原因，不删除来源。
- `Unknown`：关键证据缺失或冲突，禁止用语言复杂度代替验证。
- `Raw Idea / Unqualified`：研究触发的候选想法，必须走 `grill-with-docs` 才能进入正式素材库。

只有目标项目明确建立 `Qualified GDD Material`、Proposal 或 Evaluation 后，研究结果才可作为其来源之一。跨项目引用需在目标项目重新登记来源、说明适用范围并独立确认，不能继承原项目的资格或结论。

## 8. 与其他契约的关系

- `media-analysis` 负责外部游戏拆解；其报告按本页登记来源与证据。
- `simulation-contracts` 负责可复现实验输入和结果；原始结果不等于玩家体验证据。
- `prototype-contracts` 负责原型范围、试玩任务和验收；观察写入 `P/insights/`。
- `evaluation-frameworks` 负责候选设计的评判维度；评估引用研究证据 ID，不反向修改来源。
- `gdd-standards` 负责将合格素材组织成 GDD；研究报告本身不构成 GDD 章节。

## 9. 禁止内容

- 不把搜索结果、视频转写或 agent 猜测直接写成 `Confirmed`。
- 不在共享目录保存项目专属结论、实验结果或隐式背景。
- 不把代码路径、类名、构建命令和实现完成度写成设计证据；需要时只引用项目原型索引。
- 不删除失败来源、冲突证据或过期结论；用 `Failed`、`Disputed` 或 `Superseded` 保留历史。
- 不因模拟通过、一次试玩成功或外部产品流行而跳过素材资格、Proposal/Evaluation 或 Draft Change。

## 10. 交付自检

提交研究文件前确认：

1. 能从问题反查来源、证据、方法和版本/哈希。
2. 每个关键判断都标明观察、来源观点、推断或 Unknown。
3. 报告写出材料覆盖、冲突、限制、最小验证和停止条件。
4. 研究触发的新想法已隔离到项目 `idea-inbox/`，没有偷偷进入 GDD 或核心构思。
5. 文件路径、Project ID 和状态符合项目 README 与探索区 AGENTS 规则。
