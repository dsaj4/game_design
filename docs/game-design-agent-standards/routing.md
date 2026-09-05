# 输入路由规范

文档 ID：`AGS-ROUTE-001`

状态：`Proposed / Phase 4 draft`

版本：`0.1.0`

更新时间：`2026-09-04`

复审日期：`2026-10-04`

## 1. 目的与边界

路由的任务是识别用户当前要推进的工作，并把内容放到职责正确的目录。路由不判断想法是否优秀，也不替用户确认尚未说清的规则。一个请求可以同时包含多个意图；模糊部分先隔离为 `Raw Idea / Unqualified`，不能因为同一句话还有明确部分就跳过资格闸门。

## 2. 意图到目录的映射

| 用户信号 | 意图状态 | 标准去向 | 不能做的事 |
| --- | --- | --- | --- |
| “我想到一个玩法/卡牌效果” | `Raw Idea / Unqualified` | `game-design-workflow/idea-inbox/` | 直接写 GDD、Proposal 或核心构思 |
| “把这个想法写成 GDD” | `GDD` | `game-design-workflow/gdd/` | 跳过素材审查，直接采纳 inbox 内容 |
| “这个机制能不能做/值不值得做” | `Proposal / Evaluation` | `idea-proposals/` 或 `evaluations/` | 在素材不合格时生成正式 Proposal |
| “这个像某款游戏” | `Market Reference / Research` | `market-reference.md` 或 `research/03-product-case-studies/` | 直接复制产品系统或把案例当行业规则 |
| “我看到文章/课程/视频” | `Research Material` | `research/01-theory-library/`、`02-theory-digests/` | 把讲者观点写成项目决策 |
| “这个结论确认了，写进正式文档” | `Draft Change` | `game-design-workflow/draft-changes/`，确认后核心文档 | 未经确认直接改 `core-concept.md` |
| “实现/修 Bug/代码进度” | `Development Progress` | `docs/code-development-index.md` 与对应代码仓库 | 把类、函数、API、构建或 Bug 写进 GDD |
| “下一步验证什么/试玩发现了什么” | `Prototype Insight` | `research/06-prototype-insights/`、当前问题清单 | 用一次试玩把假设自动标为 Accepted |

## 3. 规则条目

### ADRULE-ROUTE-001：先分类，再写入

Strength：`SHOULD`

Status：`Proposed`

Trigger：收到任何会产生文件、设计判断或开发记录的用户输入。

Preconditions：已阅读与请求相关的核心上下文；不确定时至少确认 `README.md`、`AGENTS.md` 和对应目录说明。

Input：用户原始请求、相关仓库上下文、当前状态轴和候选目标目录。

MUST：

1. 用一句话写明用户意图、内容状态、目标阶段和候选去向。
2. 将同一输入拆成可独立路由的部分；无法判断的部分标 `Unknown`。
3. 在回复中说明当前状态和下一步，不把路由判断写成设计结论。

MUST NOT：

- 仅凭关键词“系统”“设计”“完成”就选择目录；
- 将材料、设计、代码进度和决策状态合并成一个“已完成”；
- 因目录方便而越过 `idea-inbox`、研究或代码进度边界。

Procedure：`识别意图 -> 标记状态轴 -> 查表 -> 检查前置闸门 -> 创建/更新目标文件 -> 建立来源链接`。

Output：目标文件路径、状态轴、来源/决策链接、下一步问题或阶段门结果。

Pass criteria：读者能从输出中看出为什么写到该目录，以及哪些内容被明确排除。

Failure handling：意图仍有两个以上不可合并的解释时，分别保留候选并一次询问一个会改变路由的问题；不得自行选定高风险路径。

Evidence：`AGENTS.md` 用户意图识别与工作区分流；知识系统 Spec 第 4、9 节。

Owner/version/review date：知识系统维护者 / `0.1.0` / `2026-10-04`。

Review trigger：目录职责、GDD 模板或核心流程发生变化。

### ADRULE-ROUTE-002：原始想法资格闸门

Strength：`HARD`（继承自 `AGENTS.md`，本目录不新增政策）

Status：`Inherited`

Trigger：输入是尚未完整说明的机制、题材、卡牌、世界观或玩家体验。

Preconditions：至少能保留用户原话或等价原意。

Input：用户原始表达、触发来源、相关核心构思与资格模板字段。

MUST：

1. 使用 `game-design-workflow/templates/idea-template.md` 的结构在 `idea-inbox/` 建档。
2. 默认标为 `Raw Idea / Unqualified`，未知字段写 `Unknown`。
3. 使用 `grill-with-docs` 一次确认一个关键资格问题。
4. 只有七项资格字段全部清楚时，才在 `idea-materials/` 创建 `M-YYYY-MM-DD-short-name.md` 并双向链接。

资格字段：来源可追溯、设计对象/GDD 章节、玩家处境、玩家行为或可见影响、预期反馈/价值、与当前构思关系、最大未知与验证方式。

MUST NOT：把模糊聊天、自行补全的猜测或未确认 inbox 内容当作 GDD、Proposal、Evaluation 或核心构思来源。

Procedure：`保存原始表达 -> 标记 Raw Idea / Unqualified -> 对照仓库文档补齐可回答项 -> 一次确认一个关键问题 -> 通过七项门槛后晋级并双向链接`。

Output：原始想法文件；通过后才有合格素材文件和资格记录。

Pass criteria：每项资格字段均有用户/来源依据，且最大未知有最小验证方式。

Failure handling：字段缺失则继续留在 inbox，记录下一个关键问题；不能用 `Proposed` 伪装为 `Qualified`。

Evidence：`AGENTS.md` 原始想法流程与合格 GDD 素材硬门槛；`grill-with-docs` 技能。

Owner/version/review date：游戏构思系统引导员 / `0.1.0` / `2026-10-04`。

Review trigger：素材资格模板或用户澄清流程变更。

### ADRULE-ROUTE-003：理论、课程与外部资料

Strength：`SHOULD`

Status：`Proposed`

Trigger：用户提供文章、书、理论、视频、课程或外部研究。

Preconditions：能记录来源入口、作者/讲者或平台、访问日期和当前覆盖状态；缺失字段允许标 `Unknown`，但不能伪造。

Input：外部资料入口、来源元数据、覆盖/分集状态和当前研究问题。

MUST：先登记来源和覆盖状态，再建立逐材料摘要、证据卡、Wiki 候选和项目假设；原始资料与摘要分层保存。

MUST NOT：把单一讲者经验、商业数字或案例结果写成行业共识，或直接写入核心构思。

Procedure：`元数据核对 -> 分集完整性 -> 证据卡 -> 摘要 -> Wiki/规则候选 -> 项目 Hypothesis -> Unknown/冲突`。

Output：`research/` 中带来源 ID、BV/P 或外部 URL 的摘要，必要时链接到 `research/05-design-hypotheses/`。

Pass criteria：重要结论可回指稳定证据 ID；缺失或失败分集明确标出。

Failure handling：来源无法定位或覆盖状态不明，标 `Unknown/Partial`，暂停高强度结论，不用合并稿补齐缺口。

Evidence：知识系统 Spec 第 6、8 节；Wiki `00-sources-and-pilot.md`。

Owner/version/review date：研究维护者 / `0.1.0` / `2026-10-04`。

Review trigger：新增来源类型、分集修复规则或引用政策变化。

### ADRULE-ROUTE-004：产品案例与参考游戏

Strength：`SHOULD`

Status：`Proposed`

Trigger：用户提到某款游戏、竞品、卡牌系统或“像某游戏”。

Preconditions：至少能定位产品名称；涉及版本、平台或当前商业状态时必须能核对来源或标 `Unknown`。

Input：产品名称、版本/平台信息、用户关注点和可核对的案例来源。

MUST：至少记录产品名称、类型/平台、核心循环、相关玩法点、玩家可能喜欢的原因、可借鉴结构、应避免雷同和可转化假设。

MUST NOT：只写“像/不像”，或因产品成功就直接复制其系统、商业结果或目标玩家。

Procedure：顺手提及则追加 `game-design-workflow/market-reference.md`；需要认真拆解则进入 `research/03-product-case-studies/` 或 `game-analysis-orchestra`；多个产品比较进入 `research/04-cross-game-comparisons/`。

Output：产品案例或比较文档，项目转化保持 `Hypothesis`。

Pass criteria：案例事实、作者分析和本项目假设分层，有来源和适用边界。

Failure handling：版本、平台或市场信息可能变化时联网核实并注明访问日期；无法核实则写 `Unknown`。

Evidence：`AGENTS.md` 产品参照流程；`game-analysis-orchestra` 技能；知识系统 Spec 第 12.2 节。

Owner/version/review date：研究维护者 / `0.1.0` / `2026-10-04`。

Review trigger：案例分析流程、平台目标或版权边界变化。

### ADRULE-ROUTE-005：代码与设计分离

Strength：`HARD`（继承自仓库决策）

Status：`Inherited`

Trigger：用户要求实现功能、修复 Bug、询问开发进度、技术架构、构建或发布。

Preconditions：已读取 `docs/code-development-index.md` 和对应代码仓库文档，并能定位相关 GDD、规则、Proposal 或明确的设计来源；没有来源时先回到设计流程。

Input：开发请求、相关 GDD/规则/Proposal、代码进度索引和实现证据。

MUST：确认对应的 GDD/规则/Proposal 来源；实现状态和技术细节写入 `docs/code-development-index.md` 或代码仓库，并在需要时记录与 GDD 的偏差。

MUST NOT：在 GDD 中写类、函数、模块、脚本路径、API、构建命令、CI、Bug 列表或代码完成度；不得因代码存在就把设计假设升级为 `Confirmed`。

Procedure：`定位设计来源 -> 读取代码进度和实现证据 -> 更新代码仓库/进度索引 -> 记录与 GDD 的偏差 -> 设计影响交回素材资格与决策流程`。

Output：开发进度索引更新、实现仓库链接、设计偏差或待决问题。

Pass criteria：读者能分别找到玩法设计结论与代码实现证据，且两者状态没有互相覆盖。

Failure handling：没有明确设计来源时，先回到 Proposal/GDD/资格流程；技术约束会改变玩法时，先记录实现偏差和 `research/06-prototype-insights/` 观察；形成的新设计输入进入 `idea-inbox/`，经 `grill-with-docs` 晋级合格素材后，方可进入 Proposal、Evaluation 或 Draft Change。

Evidence：`AGENTS.md` 标准流程八；`decision-log.md` 的 GDD/代码隔离决策；GDD 模板边界。

Owner/version/review date：设计/开发总控 / `0.1.0` / `2026-10-04`。

Review trigger：代码仓库、进度索引或设计交接协议变化。

## 4. 路由后回复模板

```text
意图：<Raw Idea / Research / GDD / Proposal / Evaluation / Development Progress / ...>
当前状态：<状态轴，不用“已完成”一词替代>
目标位置：<路径>
不会写入：<越界目录或未确认结论>
下一步：<一个最关键的澄清、资格检查或阶段门动作>
```
