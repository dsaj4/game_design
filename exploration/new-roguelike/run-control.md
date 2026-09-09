# 独立肉鸽探索运行控制

本文件是 `new-roguelike` 的单轮探索控制面。项目从空白背景开始，任何具体子类型、玩家、核心动作、平台、题材和数值都必须由证据或用户决定；不得从 game-002 或优化项目补全未知。

## 当前运行

```yaml
project_id: new-roguelike
autonomy_level: L1-supervised
active_context_pack: Not Applicable
active_question: Unknown
current_candidate: None
round: 0
round_budget: Unknown
max_rounds: Unknown
status: Ready
review: Awaiting Question
last_artifact: None
next_action: 等待用户指定一个探索问题
```

没有活动问题时，agent 可以整理明确外部来源或记录用户给出的原始想法，但不得自行宣布某种肉鸽设计为目标。

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
- 将任何假设或实验结果提升为 `Confirmed`、`Accepted` 或项目背景。
- 修改本项目 `context/README.md` 的已知范围，或新增跨项目来源/回写权限。
- 改变共享契约、自动权限或创建外部实现仓库。

## 轮次与产物

每轮使用唯一运行 ID：`ROG-YYYYMMDD-NNN`。运行记录建议保存为 `simulations/ROG-...-run.md` 或 `insights/ROG-...-run.md`，并链接到本轮产生的全部文件。

每轮至少记录：

1. 活动问题、候选及其来源；未知字段保持 `Unknown`。
2. 使用的共享框架/方法版本和输入文件哈希（如有）。
3. 本轮预算：时间、最大候选数、模拟/原型次数和人工复核次数。
4. 实际动作、证据链接、未解决 Unknown 和结果状态。
5. 规则验收项 `Pass` 只表示该实验的验收条件通过，不表示玩法已采纳。

## 停止与阻塞

- 达到 `max_rounds`、预算或候选上限时停止，状态为 `Completed`，并将 `review` 设为 `Needs Human Review`。
- 证据不足、来源不可核验、输入哈希变化或契约无法满足时，状态为 `Blocked / Needs Human Review`。
- 候选之间无法比较、核心动作仍不清晰或评判框架不适用时，停止扩展并记录缺口。
- 用户撤回问题或候选时，立即停止并保留已有记录。

## 失败回流

- 研究失败回 `questions/`，把缺失来源或待核实断言写成下一问题。
- 候选不合格回 `idea-inbox/`，状态保持 `Raw Idea / Unqualified`，不得直接进入 GDD。
- 模拟失败回 `simulations/` 的配置或失败记录，保留种子、输入和错误分类。
- 原型失败回 `prototypes/` 的范围/观察记录；不得以“未实现”替代体验结论。
- 评估不通过回 `proposals/` 或 `questions/`，只有人工确认后才可开启新版本。

## 版本规则

- 运行版本：`ROG-YYYYMMDD-NNN`，同一轮重跑使用 `-r2`、`-r3` 后缀，不覆盖原记录。
- 候选版本：`C-<slug>-vNN`；修改核心假设、玩家动作或验收条件必须递增版本。
- 模拟/原型输入改变时必须生成新运行 ID，并记录旧运行的 superseded 关系。
- 本项目不生成或引用 game-002 Context Pack；共享框架换版必须新开运行并注明适用范围。

## 结束记录模板

```yaml
run_id: ROG-YYYYMMDD-NNN
project_id: new-roguelike
question: <本轮问题或 Unknown>
candidate_ids: []
context_pack: Not Applicable
framework_versions: []
budget: <计划/实际>
status: Planned / Running / Completed / Blocked
review: None / Needs Human Review
artifacts: []
unknowns: []
failure_return: <回流目录或 None>
next_action: <下一步或 Awaiting Human Gate>
```
