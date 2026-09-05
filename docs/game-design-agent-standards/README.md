# 游戏设计 Agent 规范

## 独立工作区适用范围

本规则库不绑定任何游戏。先按[工作区地图](../workspace-map.md)确定工作区根 W；正文中的项目路径相对 W，模板和生效协作协议相对仓库根。Markdown 链接按所在文件解析。
原始想法、素材审查、项目转化、原型观察与开发进度只读写该工作区。共享知识不包含项目设定，历史项目状态不跨项目继承。
2026-09-05 已移除旧游戏专属建议；Inherited / Proposed 状态保持原义，不因共享复用自动采纳。

文档集 ID：`AGS-README-001`

状态：`Proposed / Phase 4 draft`

版本：`0.1.2`

更新时间：`2026-09-05`

复审日期：`2026-10-04`

## 1. 这套规范是什么

这是一套供游戏设计 agent 查阅的规则草案。它把仓库已有的流程、证据、GDD、原型、试玩和协作边界写成可执行的检查项，目标是让 agent：

- 先判断输入属于哪条工作流，再决定写入位置；
- 区分材料、证据、推断、假设和正式决策；
- 以 `S0-S7` 追踪正在减少的未知，而不是以文件数量判断进度；
- 使用 `GDD-0 / GDD-1 / GDD-2` 逐步加深文档，不把代码进度塞进 GDD；
- 在核心文档、原始想法和用户未确认内容之间保持边界。

本目录是 Phase 4 的候选规则承载区，尚未自动集成进 `AGENTS.md`，也不改变 `core-concept.md`、GDD 或 `decision-log.md` 的现有状态。`HARD` 仅表示已由仓库现有协议继承的硬约束；新课程或新研究内容默认只能成为 `SHOULD` 或 `EXPERIMENT` 的 `Proposed` 候选。

## 2. 规则优先级与强度

### 2.1 冲突优先级

从高到低依次为：

1. 安全、权限、用户授权范围和不可逆操作约束。
2. `AGENTS.md`、Windows 安全要求、GitHub 协作规范及其他现行 `Inherited / HARD` 协议。
3. 用户当前目标、偏好和明确设计决定；用户确认可以满足流程中的确认条件，但不会静默取消素材资格、Draft Change、Decision Log、分支或提交条件。只有用户明确要求修改协议本身时，才把它作为协议变更处理。
4. 已接受的项目流程决策和决策记录。
5. 本目录中已评审并集成的新增规则。
6. 本目录的 `SHOULD` 建议和 `EXPERIMENT` 试验候选。

发现冲突时必须保留冲突、说明影响并请求决策；不得悄悄选择对自己最方便的一条。

### 2.2 强度定义

| Strength | 含义 | agent 行为 |
| --- | --- | --- |
| `HARD` | 已被上层协议明确要求的约束 | 违反时停止越界动作，报告缺口或回退到允许状态 |
| `SHOULD` | 默认应遵守的工作方式 | 偏离时记录理由、影响和复审条件 |
| `EXPERIMENT` | 尚未形成政策的可验证候选 | 只用于明确试验，不得阻塞不相关工作 |

规则的 `Status` 与 `Strength` 是两条不同的轴。本文档中的新条目通常为 `Status: Proposed`；它们不能因为写在这里就变成 `HARD`、`Confirmed` 或 `Accepted`。

## 3. 文件地图

| 文件 | 规则类别 | 主要回答的问题 |
| --- | --- | --- |
| [routing.md](routing.md) | `Routing` | 输入属于什么意图，应该写到哪里？ |
| [stage-gates.md](stage-gates.md) | `Stage Gate` | 当前处于哪个 S 阶段，什么证据才能 Go？ |
| [evidence-and-citations.md](evidence-and-citations.md) | `Evidence` | 结论从哪里来，强度和缺口是什么？ |
| [gdd-rules.md](gdd-rules.md) | `GDD` | 如何选择 GDD 成熟度并保持设计/代码边界？ |
| [design-principles.md](design-principles.md) | `Design Reasoning` | 如何把原则写成玩家可观察、可复审的约束？ |
| [prototype-and-playtest.md](prototype-and-playtest.md) | `Prototype / Playtest` | 原型和试玩要回答什么，怎样记录结果？ |
| [collaboration-and-safety.md](collaboration-and-safety.md) | `Collaboration / Safety` | 如何在共享仓库中安全修改和交接？ |
| [rule-index.md](rule-index.md) | 索引与评审 | 当前有哪些规则、状态和待评审项？ |

## 4. 一次请求的最短路径

```text
用户输入
  -> 路由（意图、状态、目标目录）
  -> 证据与素材闸门
  -> 阶段/成熟度检查
  -> 设计、原型或协作动作
  -> 生成记录、链接和下一步
```

agent 每次至少回答：

1. 这是什么类型的输入，当前状态是什么？
2. 它要减少哪一种未知，属于 `S0-S7` 哪一阶段？
3. 哪些内容是来源事实，哪些是 `Inference`、`Hypothesis` 或 `Decision`？
4. 准备创建/更新哪些文件，哪些目录明确不应写入？
5. 完成或失败的可观察信号是什么，下一步由谁负责？

信息不足时，优先保留 `Unknown`，不要让 agent 用“通常”“应该”或自造细节填空。

## 5. 状态轴

状态轴必须分开报告，不能用“已完成”一个词代替：

| 轴 | 允许值 | 说明 |
| --- | --- | --- |
| 材料 | `Extracted / Reviewed / Partial / Failed / Unknown` | 转写或外部资料覆盖情况 |
| 证据 | `E0-E4` | 结论能支持到什么强度 |
| 结论类型 | `Observed Fact / Source Claim / Inference / Hypothesis / Decision / Unknown / Out of Scope` | 当前句子是什么性质 |
| 设计 | `N/A / Raw Idea / Qualified GDD Material / GDD / Proposal / Evaluation / Draft Change / Accepted / Parked / Rejected` | 项目工作流处于哪里 |
| 生产阶段 | `S0-S7` | 正在减少哪一种开发未知 |
| GDD 成熟度 | `GDD-0 / GDD-1 / GDD-2` | 文档写到什么深度 |
| 代码 | `N/A / Planned / In Progress / Implemented / Verified / Blocked / Parked` | 只在项目开发进度索引或代码仓库维护 |

典型报告格式：

```text
Material=Reviewed; Evidence=E1; Conclusion=Source Claim;
Design=N/A; Production Stage=N/A; GDD=N/A; Code=N/A
```

## 6. 规则条目最小格式

每条可执行规则都应包含下列字段；索引只保留摘要，正文文件保留完整条目：

```text
Rule ID: ADRULE-<CATEGORY>-<NNN>
Strength: HARD / SHOULD / EXPERIMENT
Status: Inherited / Proposed / Accepted / Superseded
Trigger: 何时触发
Preconditions: 前置状态和适用范围
Input: 执行规则所需的来源、状态、对象或证据
MUST: agent 必须做什么
MUST NOT: agent 不得做什么
Procedure: 顺序化操作
Output: 应生成或更新什么
Pass criteria: 如何判定通过
Failure handling: 不通过时的状态、保留内容和升级路径
Evidence: 来源、证据 ID 和边界
Owner/version/review date: 负责人、版本、复审日期
Review trigger: 何时复审或废止
```

若某字段没有答案，写 `Unknown` 并说明负责人和下一步；缺字段不能被默认为“规则不适用”。

## 7. 与仓库流程的边界

- 原始想法只能先进入 `game-design-workflow/idea-inbox/`，通过 `grill-with-docs` 资格闸门后才能进入 `idea-materials/`、GDD 或 Proposal。
- GDD 只写玩家体验、玩法规则、设计决策和验证；引擎、类、函数、API、构建、Bug 和代码完成度进入 `docs/code-development-index.md` 或实现仓库。
- 理论和课程材料进入 `research/`，先成为带证据的摘要或假设；不能直接改 `core-concept.md`。
- 正式核心设定变更必须经过 Proposal、Evaluation、Draft Change、用户确认和 Decision Log；本目录不替代这条流程。
- 本目录中 `Status: Proposed` 的新增规则尚未写入 `AGENTS.md`。在 Phase 5 集成前，agent 应把这些新增条目当作可评审草案，不声称系统已经自动执行；`Status: Inherited` 的规则始终通过其上游 `AGENTS.md`、GDD 模板或协作协议生效。

## 8. 评审与发布

规则从 `Proposed` 变为可集成条目，至少需要：

1. 有明确来源、适用阶段、反例和边界；
2. 能指向仓库中的实际产物和状态变化；
3. 至少完成一次人工反例演练；
4. 通过与现有 `AGENTS.md`、GDD 模板、双层想法库和代码开发索引的冲突检查；
5. 记录版本、影响范围、回退方式和下一次复审日期。

规则发布不等于玩法设计采纳。任何影响核心构思的决定仍须遵守核心文档保护协议。

## 9. 来源与审计

- [游戏设计知识与构思辅助系统升级 Spec](../game-design-knowledge-system-spec.md)
- [GDD 写作要求与模板](../../game-design-workflow/templates/gdd-writing-requirements-and-template.md)
- [Agent 操作手册](../../AGENTS.md)
- [游戏设计与开发 Wiki](../../research/02-theory-digests/game-design-development-wiki/README.md)
- [GitHub 协作规范](../github-collaboration.md)

课程证据只作为规则候选来源，例如 `E-SJ002-P009-001`、`E-SJ002-P017-001`、`E-SJ002-P018-001`、`E-SJ002-P019-001`、`E-SJ003-P001-001`、`E-SJ003-P007-001`、`E-SJ003-P010-001` 和 `E-SJ003-P021-001`。课程主张默认是 `Source Claim`，不能自动升级为项目 `Accepted`。
