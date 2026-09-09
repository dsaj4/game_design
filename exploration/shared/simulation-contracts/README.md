# 数值模拟文件契约

版本：`v1.0`。状态：`Reference Ready / Schema Not Executable`。更新日期：2026-09-09。

本页规定探索项目如何登记可重复的规则模拟。它是文件格式和证据边界，不是统一运行器，也不规定某个游戏的规则、数值或实现语言。模拟只能回答“在给定模型、输入和策略下发生了什么”，不能单独证明设计好玩、可理解或应被采纳。

## 适用范围与保存位置

- 适用于 `game-002-optimization` 和 `new-roguelike` 的离线数值实验、桌面推演的机器化记录，以及外部模拟器适配。
- 每次实验写入目标项目的 `P/simulations/`。建议按 `SIM-YYYY-MM-DD-short-name/` 建立一组文件；项目 README 维护入口索引。
- 原始运行输出可放在该目录的 `runs/<run-id>/`，但代码、运行器、测试脚本和构建说明留在明确登记的外部代码仓库。共享目录只维护本契约。
- `legacy-combat`、`legacy-semantic-generation` 等旧实验只能通过已登记适配器引用，不能把旧结果当作当前项目基线。

## 文件关系

一次最小运行由四类输入和四类输出组成：

```text
candidate-spec.json + scenario-set.json + policy-set.json + run-config.json
                                |
                                v
                    simulation-run-manifest.json
                         /              \\
                raw-results.jsonl     summary.json
                                      |
                                      v
                              项目 evaluations / insights
```

文件名可以因项目调整，但字段语义和追踪关系不能省略。大文件只保存路径、大小和 SHA-256，不在 Markdown 中复制整份结果。

## 共同信封字段

所有输入、运行清单和汇总输出都必须能独立识别以下字段：

| 字段 | 要求 |
| --- | --- |
| `schema_id` / `schema_version` | 例如 `simulation-contract@v1.0`；版本变化不得静默改写历史运行 |
| `project_id` | 必须是注册表中的唯一 ID，禁止留空或写 `shared` |
| `experiment_id` / `run_id` | 实验计划与单次运行的稳定 ID，重跑使用新 `run_id` |
| `candidate_id` / `candidate_version` | 被测试规则或内容的版本，不能只写文件名 |
| `source_refs` | 提案、合格素材、问题、跨项目来源或背景包的路径、版本/提交和适用范围 |
| `evaluation_framework_refs` | 使用的评判框架 ID/版本；不使用时写 `N/A` 并说明原因 |
| `created_at` / `completed_at` | ISO 8601 时间；未完成时 `completed_at: null` |
| `status` | 使用本页定义的状态；不要把设计结论塞进运行状态 |
| `input_hashes` | 每个输入文件的 SHA-256；缺失时标记 `Unknown`，不得声称可复现 |

## 输入契约

### `candidate-spec.json`

描述要测试的候选规则，至少包含：

```json
{
  "schema_id": "simulation-candidate@v1",
  "schema_version": "1.0",
  "project_id": "new-roguelike",
  "candidate_id": "C-2026-09-09-risk-reward",
  "candidate_version": "0.1",
  "source_refs": ["../idea-materials/M-...md", "../proposals/P-...md"],
  "design_status": "Experimental / Unqualified",
  "rules": {"...": "候选规则的可执行表达" },
  "invariants": ["必须保持的边界或不变量"],
  "known_unknowns": ["尚未决定的规则"],
  "out_of_scope": ["本轮不模拟的系统"]
}
```

`rules` 必须足以让运行器或人工执行者知道输入、结算和状态变化；无法表达的部分写入 `known_unknowns`，不能由运行器自行补全。候选仍可处于 `Raw Idea / Unqualified`，但此时运行结果只能作为探索证据，不能成为 Proposal、Evaluation 或 GDD 正文结论。

### `scenario-set.json`

列出状态空间和对照组，至少包含：场景集 ID/版本、每个场景的初始状态、可见信息、约束、目标、终止条件、预期样本数和是否为对照。至少保留一个能检验候选差异的对照或说明为什么没有对照。

### `policy-set.json`

列出自动代理、启发式策略或人工策略的版本与可见信息，至少包含：`policy_id`、版本、决策规则、允许的行动、信息限制、随机性来源和策略假设。策略偏差、未知策略和未覆盖行动必须显式记录。

### `run-config.json`

记录运行参数：随机种子（单个或种子列表）、样本量、并发/超时限制、停止条件、度量名称与单位、评判框架 ID/版本（或 `N/A`）、环境标识、运行器/代码仓库提交、输入文件哈希和预期输出格式。样本量不足时不能用“运行完成”掩盖证据不足。

## 输出契约

### `simulation-run-manifest.json`

这是每次运行的审计入口，至少记录：共同信封字段、四类输入路径和哈希、实际种子、实际样本数、开始/结束时间、运行器版本、代码提交、环境、输出文件哈希、资源限制、异常摘要和结果状态。运行器崩溃也必须写出尽可能完整的 manifest。

### `raw-results.jsonl`

一行一个样本或一个明确失败事件。每行至少包含 `run_id`、`scenario_id`、`policy_id`、`seed`、`sample_index`、初始状态摘要、行动/结算摘要、终止原因、指标和可追溯日志位置。不得只保留最终均值而丢弃样本量、失败样本或异常分布。

### `summary.json`

只做可复算的汇总，至少包含：有效样本数、无效/失败样本数及分类、各场景/策略的指标、分布或置信区间（若适用）、对照差异、停止条件是否触发、输入/输出哈希和 `evidence_limits`。任何指标都写明计算口径；没有统计依据的精确小数不要伪装成测量。

### `simulation-report.md`（可选但推荐）

用于人类阅读，引用 manifest、summary 和关键 raw 行号。应分开写自动结果、人工解释、未知项和下一步验证；可链接到项目 `evaluations/` 或 `insights/`，但不能替代原始输出。

## 状态边界

运行状态与设计判断分开保存：

| 状态 | 含义 | 允许的结论 |
| --- | --- | --- |
| `Planned` | 输入或运行计划已登记，尚未运行 | 只有待测问题 |
| `Experimental` | 候选或模型尚未通过资格确认 | 可产出探索证据，不得晋级设计状态 |
| `Running` | 运行尚未结束 | 不能引用部分结果为结论 |
| `Valid Run` | 输入、版本和样本满足契约，结果可复算 | 可供 Evaluation 使用 |
| `Invalid Candidate` | 候选不满足规则/Schema/边界 | 修复候选后新建版本；不计为设计失败 |
| `Crash` / `Timeout` | 技术执行失败 | 保留日志和 manifest；不计为设计胜负 |
| `Insufficient Sample` | 完成但样本、策略或场景不足 | 结论为 `Insufficient Evidence` 或 `Needs Human Review` |
| `Archived` | 历史记录冻结 | 不原地更新；重跑创建新 run |

`Passed` 只可作为项目评估中的“某项规则验收通过”字段，不能作为模拟运行状态，也不能自动把 Hypothesis 变成 Confirmed/Accepted。模拟报告至少注明 `model_scope`、未测情境和是否需要原型/真人证据。

## 追踪与晋级

从运行清单可以反查：`project_id → experiment_id → candidate/source → scenario/policy → seed → code commit → input/output hash → summary → evaluation/insight`。跨项目引用必须写明来源项目和适用性判断；优化结果回写 game-002 仍须目标项目复审和 Draft Change。

结果进入项目 `evaluations/` 前，评估记录应引用框架版本，并分别列出自动测量、人工判断和未知/未测。运行成功不等于策略有意义，胜率也不能替代可理解性、取舍和趣味性的证据。

## 最小运行索引模板

```markdown
# SIM-YYYY-MM-DD-short-name

- Project ID：
- 状态：Planned / Experimental / Valid Run / Insufficient Sample / ...
- 问题与候选：
- Candidate：路径、版本、SHA-256
- Evaluation framework：ID、版本或 `N/A`
- Scenario set：路径、版本、SHA-256
- Policy set：路径、版本、SHA-256
- Run config：种子、样本量、停止条件、代码提交
- Manifest：
- Raw results：
- Summary：
- 自动证据：
- 人工解释：
- 未知/限制：
- 下一步：补样本 / 改候选 / 原型 / 人工评议 / 暂缓
```

## 禁止内容

- 不把运行器源码、类/函数/API、构建命令或环境密钥复制进共享契约；这些属于实现仓库。
- 不把旧项目的参数、胜率、测试结论或背景包内容默认当作当前项目事实。
- 不删除失败运行、异常样本或历史版本；修复后新建 candidate/run 版本。
- 不用 agent 猜测补齐缺失输入、样本或玩家体验，不把模拟分数直接写进 `core-concept.md`、GDD 或 Accepted 决定。
- 不以随机种子、样本量或指标选择掩盖模型范围；所有重要缺口保留为 `Unknown` 或 `Insufficient Evidence`。
