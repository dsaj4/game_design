# 设计原则与推理规范

文档 ID：`AGS-DESIGN-001`

状态：`Proposed / Rule Candidate`

版本：`0.1.2`

更新时间：`2026-09-05`

复审日期：`2026-10-04`

## 1. 原则的作用

设计原则用于在多个可行方案之间保持一致判断。它不是口号、审美偏好或课程摘录；只有能约束可观察选择、说明取舍并接受反例审查，才值得成为规则候选。

原则状态与强度分开：`Candidate/Proposed/Accepted/Superseded` 描述是否被评审，`HARD/SHOULD/EXPERIMENT` 描述 agent 应如何执行。

## 2. 原则条目模板

```text
Principle ID: DP-<NNN>
Name:
Intent:
Player-observable behavior:
Design constraints:
Positive signals:
Negative signals:
Trade-offs/exceptions:
Evidence:
Status: Candidate / Proposed / Accepted / Superseded
Owner/version/review date:
Review trigger:
```

“玩家优先”“保持简单”“快速迭代”不能直接作为执行规则；必须翻译成玩家处境、动作、信息、代价、反馈或可测试的生产行为。

## 3. 规则条目

### ADRULE-DESIGN-001：原则必须落到可观察约束

Strength：`SHOULD`

Status：`Proposed`

Trigger：新增原则、引用原则解释设计取舍，或评估两个方案。

Preconditions：已有目标玩家、体验/生产目标和至少一条可追溯来源或项目观察；没有时只能创建 `Candidate`。

Input：原则候选、目标玩家、体验/生产目标、可追溯来源或项目观察。

MUST：填写玩家可观察行为、受约束的规则/范围、正负信号、代价/例外、证据和复审触发；为每项原则至少给出一个反例。

MUST NOT：把“更好玩”“更专业”“符合行业惯例”当作通过条件；不得用原则替代目标玩家和测试。

Procedure：`声明意图 -> 写玩家可观察行为 -> 写约束与正负信号 -> 列取舍/例外 -> 绑定证据 -> 用正反方案审查 -> 设置复审触发`。

Output：完整原则卡、受影响方案列表和验证/复审条件。

Pass criteria：另一位设计者能据此预测至少一个应采用和一个应排除的方案。

Failure handling：字段缺失标 `Candidate/Unknown`，不阻塞无关探索，也不得标 `Accepted`。

Evidence：知识系统 Spec 第 11 节；`E-SJ002-P007-001`、`E-SJ003-P002-001`。

Owner/version/review date：设计维护者 / `0.1.0` / `2026-10-04`。

Review trigger：出现反例、玩家证据或项目目标改变。

### ADRULE-DESIGN-002：从体验目标推导机制和动态

Strength：`SHOULD`

Status：`Proposed`

Trigger：提出新机制、卡牌效果、资源或界面方案。

Preconditions：输入已按仓库流程路由；若是新想法，先完成 `idea-inbox` 保存和素材资格确认，不把本规则当作晋级捷径。

Input：合格设计输入、目标玩家处境、体验目标、设计支柱/反支柱和现有约束。

MUST：先写目标玩家处境与体验，再说明机制允许什么、可能诱发什么行为、如何反馈；检查方案是否支持至少一个设计支柱并违反至少一个反支柱时被拒绝或标例外。

MUST NOT：先列大量内容或参数，再事后声称它们“自然产生策略”；不得把成功产品的机制直接复制为原则。

Procedure：`写体验目标/处境 -> 列玩家动作与代价 -> 定义 Mechanics -> 推演 Dynamics -> 明确 Aesthetics/反面信号 -> 设计最小验证`。

Output：MDA 推理、方案比较、假设和最小验证。

Pass criteria：玩家的反复动作、选择代价和可见反馈清晰，且有可证伪的体验信号。

Failure handling：推导链断裂时标 `Unknown`，回到 S0/S1 澄清体验目标。

Evidence：`E-SJ004-P007-001`、`E-SJ004-P009-001`；GDD 模板第 4.3 节。

Owner/version/review date：系统设计负责人 / `0.1.0` / `2026-10-04`。

Review trigger：核心循环、目标玩家或支柱变化。

### ADRULE-DESIGN-003：理论迁移必须保留语境

Strength：`SHOULD`

Status：`Proposed`

Trigger：将课程、书籍、MDA、竞品或其他项目方法转化为本项目建议。

Preconditions：来源、版本/访问日期、原始主张和适用语境可以定位；无法定位时保持 `Unknown`，不做强迁移。

Input：原始来源与定位、来源语境、项目目标/平台/玩家/阶段及其约束差异。

MUST：区分来源事实/主张、跨来源推断、项目假设和正式决策；说明目标类型、平台、玩家、阶段和约束的差异；给出最小验证或明确 `Out of Scope`。

MUST NOT：因为来源权威或产品成功就把方法写成普遍定律、固定数值或项目 `Accepted` 规则。

Procedure：`抽取 Source Claim -> 记录来源语境 -> 比较项目差异 -> 形成 Inference -> 写项目 Hypothesis/反证 -> 进入原型或正式设计流程`。

Output：带证据的 `Hypothesis` 或规则候选、适用边界、反例和验证计划。

Pass criteria：读者能说明这条建议在哪些条件下可能失效，以及如何发现失效。

Failure handling：来源适用性不明时保留 `Source Claim/Unknown`，不进入核心构思。

Evidence：知识系统 Spec 第 3、8、12 节；`E-SJ003-P025-001`、`E-SJ003-P026-001`。

Owner/version/review date：研究与设计维护者 / `0.1.0` / `2026-10-04`。

Review trigger：出现跨类型验证、相反证据或项目约束变化。

### ADRULE-DESIGN-004：证据不足时保留否决和未知

Strength：`SHOULD`

Status：`Proposed`

Trigger：方案被否决、原型失败、范围缩减、原则发生冲突或设计者要求“整理得更确定”。

Preconditions：能保留原始假设、当前版本、投入范围和至少一条支持否决/未知的观察；缺失项明确标记。

Input：原始假设、当前版本、投入范围、失败/冲突证据、成本与替代方案。

MUST：保存原始假设、失败证据、成本、替代方案、未解问题和复议条件；已作出的阶段门决定只使用 `Iterate/Park/Stop`，证据未知另记为 `Unknown`，决定未作出则使用 `Decision state: Pending`、`Gate: N/A` 和 `Pending reason`。

MUST NOT：删除失败路径、把搁置改写成完成、用漂亮叙述掩盖冲突或因沉没成本继续扩张。

Procedure：`保存原始状态 -> 记录失败/冲突证据 -> 列替代解释 -> 未决时写 Pending + N/A + reason，已决定时选择 Iterate/Park/Stop -> 写复议条件 -> 链接后续问题`。

Output：决策/阶段门记录、失败路径和下一验证问题。

Pass criteria：未来协作者能理解为什么没有采纳，以及什么新证据会改变判断。

Failure handling：不能区分 `Park` 与 `Stop` 时记录 `Decision state: Pending`、`Gate: N/A` 和 `Pending reason`，升级给项目负责人；未决定前不扩大范围。

Evidence：`E-SJ003-P015-001`、`E-SJ003-P016-001`、`E-SJ003-P020-001`；Spec 第 5、15 节。

Owner/version/review date：项目总控 / `0.1.0` / `2026-10-04`。

Review trigger：新原型证据、复议条件满足或资源约束改变。

## 4. 初始原则候选（均非 Accepted）

| ID | 候选原则 | 当前状态 | 最小验证 |
| --- | --- | --- | --- |
| `DP-CAND-001` | 核心循环先于内容规模 | `Candidate` | 比较小核心原型与大内容原型的规则返工和玩家理解 |
| `DP-CAND-002` | 原型回答一个主要未知 | `Candidate` | 检查测试合同是否能指出一个主要问题和明确停止信号 |
| `DP-CAND-003` | 选择必须有可理解代价和反馈 | `Candidate` | 观察玩家能否说明保留/放弃选择的原因 |
| `DP-CAND-004` | 规则和例外显式化 | `Candidate` | 用边界用例让未参与设计者复述结算结果 |
| `DP-CAND-005` | 证据胜过断言，失败路径保留 | `Candidate` | 审查材料、测试和决策是否保留反例与未知 |

这些候选原则须在目标工作区独立验证，不能直接推出任何具体游戏规则。
