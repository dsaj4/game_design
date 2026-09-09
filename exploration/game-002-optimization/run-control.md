# game-002 优化探索运行控制

本文件是 `game-002-optimization` 的单轮探索控制面。它只约束本项目内的研究、候选、模拟、原型和评估记录；不能授权直接修改 game-002。每次自动探索开始前先填写“当前运行”，结束后补齐结果和下一步。

## 当前运行：纵向时间背包（2026-09-09 用户新输入）

```text
project_id: game-002-optimization
run_id: OPT-20260909-003
context_pack: baseline-2026-09-09-001
active_question: Q-20260909-timeline-backpack
candidate_id: C-timeline-backpack-v01
autonomy_level: L1-supervised
status: Completed
review: Needs Human Review
round_budget: 1 source review, 1 user candidate, 0 simulation runs, 0 prototypes
max_rounds: 1
stop_conditions: current scoped round complete; defer concrete card effects per user scope SC1
```

- 依据：用户要求探索“纵向时间轴的大巴扎式管理系统”，并明确不阅读其他探索方向。本轮范围按该明确输入建立，不沿用历史候选的研究预算或推荐。
- 已完成：保存原话、背景差异与候选推演；用户逐项确认 TB1（战前编排）、TB2（覆盖）、TB3（普通打断）、TB4（词卡独占），编排部分按资格清单独立晋级。状态效果与数值未晋级，无玩法 Accepted。
- 产物：[原始候选](idea-inbox/2026-09-09-timeline-backpack-spells.md)、[局部合格编排素材](idea-materials/M-2026-09-09-timeline-backpack-scheduling.md)、[验证问题](questions/Q-20260909-timeline-backpack.md)。
- 消耗：1 轮背景核对、1 份新候选、1 份局部合格素材，依次提出的 7 次单问题澄清均已回答（TB1–TB6 与 SC1）；模拟/原型执行 0 次。没有外部付费调用。
- 当前范围：用户明确“先不涉及具体卡片效果”（SC1），继续时间轴边界、编排容量与战斗节奏。
- 新确认：TB5 采用有限首次启动窗口、各法术之后独立循环整场；TB6 限制编入战斗的词卡总张数、法术数量自然受其约束。已增补素材与抽象 A/B 时序表，未设定具体卡片效果。
- 结果：本轮编排骨架整理完成，TS1–TS7 来自原始输入与 TB1–TB6；状态 `Qualified GDD Material / Hypothesis`。其余候选保持 `Raw Idea / Unqualified`；所有模拟/体验验收均为 `Untested`。
- 下一步：下一轮建议确认战前敌方信息范围，再选择容量/启动窗口参数进行抽象调度验证；该问题尚未发问，当前无未回答的已发问题。

## 历史运行（本轮不展开其探索候选）

```yaml
project_id: game-002-optimization
autonomy_level: L1-supervised
active_context_pack: baseline-2026-09-09-001
active_question: Q-20260909-001
current_candidate: H-20260909-002@v1
round: 2
round_budget: 1 research pass, 1 candidate, 1 desk-simulation plan; no executable runner
max_rounds: 2
status: Completed
review: Needs Human Review
last_artifact: insights/2026-09-09-roguelike-mode-fit-analysis.md
next_action: 先用 grill-with-docs 确认奖励第一优先级，再决定是否晋级 Raw Idea 或执行 OPT-20260909-002
```

`active_context_pack` 只能填写 `context/README.md` 中登记为 Active 的版本。当前问题和候选仅属于本轮探索记录，不是 game-002 已采纳方向。

## 自动权限

### 自动可执行

- 在本项目 `questions/`、`insights/`、`idea-inbox/`、`simulations/`、`prototypes/`、`evaluations/` 创建或更新本轮记录。
- 按共享研究方法进行网络调研，记录来源、证据和适用范围。
- 提出候选并标记 `Agent Proposal / Raw Idea / Unqualified`。
- 设计模拟或原型计划；运行结果按[模拟/原型契约](../shared/simulation-contracts/README.md)记录，规则验收项才使用 `Pass/Fail`。
- 起草本地 Proposal、Evaluation 或 GDD 文件，但必须停在草稿/人工复核状态，不把草稿视为晋级或采纳。

### 必须人工闸门

- 确认活动问题、候选范围、预算和停止条件后，才开始下一轮。
- 原始想法晋级 `Qualified GDD Material`，以及进入 Proposal、Evaluation 或 GDD 正文。
- 任何写入 `draft-changes/` 或回写 game-002 的动作。
- 改变 Context Pack、项目边界、共享契约或自动权限。
- 将 `Hypothesis`、`Experimental` 或 `Pass` 结论提升为 `Confirmed` 或 `Accepted`。

## 轮次与产物

每轮使用唯一运行 ID：`OPT-YYYYMMDD-NNN`。运行记录建议保存为 `simulations/OPT-...-run.md` 或 `insights/OPT-...-run.md`，并链接到本轮产生的全部文件。

每轮至少记录：

1. 活动问题、候选及其来源。
2. 使用的 context pack、共享框架版本和输入文件哈希（如有）。
3. 本轮预算：时间、最大候选数、模拟/原型次数和人工复核次数。
4. 实际动作、证据链接、未解决 Unknown 和结果状态。
5. 规则验收项 `Pass` 只表示该实验的验收条件通过，不表示玩法已采纳。

## 停止与阻塞

- 达到 `max_rounds`、预算或候选上限时停止，状态为 `Completed`，并将 `review` 设为 `Needs Human Review`。
- 证据不足、输入哈希变化、背景包不匹配或契约无法满足时，状态为 `Blocked / Needs Human Review`。
- 连续结果未改善、出现明显伪涌现或违反评判框架时，停止扩展候选并记录原因。
- 用户撤回问题、候选或背景包时，立即停止并保留已有记录。

## 失败回流

- 研究失败回 `questions/`，把缺失来源或待核实断言写成下一问题。
- 候选不合格回 `idea-inbox/`，状态保持 `Raw Idea / Unqualified`，不得直接进入 GDD。
- 模拟失败回 `simulations/` 的配置或失败记录，保留种子、输入和错误分类。
- 原型失败回 `prototypes/` 的范围/观察记录；不得以“未实现”替代体验结论。
- 评估不通过回 `proposals/` 或 `questions/`，只有人工确认后才可开启新版本。

## 版本规则

- 运行版本：`OPT-YYYYMMDD-NNN`，同一轮重跑使用 `-r2`、`-r3` 后缀，不覆盖原记录。
- 候选版本：`C-<slug>-vNN`；修改核心假设、玩家动作或验收条件必须递增版本。
- 模拟/原型输入改变时必须生成新运行 ID，并记录旧运行的 superseded 关系。
- Context Pack 只引用已登记版本；换包必须新开运行并注明迁移原因。

## 结束记录模板

```yaml
run_id: OPT-YYYYMMDD-NNN
project_id: game-002-optimization
question: <本轮问题或 Unknown>
candidate_ids: []
context_pack: baseline-2026-09-09-001
framework_versions: []
budget: <计划/实际>
status: Planned / Running / Completed / Blocked
review: None / Needs Human Review
artifacts: []
unknowns: []
failure_return: <回流目录或 None>
next_action: <下一步或 Awaiting Human Gate>
```
