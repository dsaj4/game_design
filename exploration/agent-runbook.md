# 玩法探索 Agent 运行手册

版本：v1.0。状态：`Ready for Supervised Exploration`。更新日期：2026-09-09。

本手册是玩法探索区的最小执行入口。它把共享契约串成单轮工作流，允许 agent 在明确的 Project ID、研究问题和预算内自动推进文件产物；资格晋级、正式设计采纳和跨项目回写仍是人工闸门。

## 1. 启动输入

每轮开始前必须得到或读取一份运行控制文件 `P/run-control.md`，至少确认：

- `project_id`：只能来自[探索项目注册表](registry/project-registry.md)。
- `active_question`：一个可验证的主要问题；没有问题时先创建 `P/questions/` 文件，不直接生成正式玩法。
- `autonomy_level`：默认 `L1 / Supervised`。
- `budget`：最大轮数、时间/调用成本、允许创建的候选数量，以及模拟/原型样本上限。
- `stop_conditions`：达到预算、关键未知无法回答、出现安全/权限边界或需要人工决定时停止。

没有明确 Project ID 时不得扫描两个项目；没有问题时不得把“自由探索”写成已确认目标。`new-roguelike` 的空白背景是允许提出候选的起点，不是具体玩法约束。

## 2. 自主等级

| 等级 | agent 可做 | 必须暂停的事项 |
| --- | --- | --- |
| `L0 / Manual` | 按用户逐步指令读写文件 | 每个产物都等用户确认 |
| `L1 / Supervised`（默认） | 建立问题、登记来源、网络搜索、生成 `Raw Idea / Unqualified`、形成实验/原型计划、记录失败和研究洞察 | 资格确认、Proposal/Evaluation 晋级、GDD 正文采纳、`Accepted`、修改核心构思、跨项目读取/回写 |
| `L2 / Unattended` | 本轮未启用；待有运行器、队列、预算和纵向样例后单独批准 | 所有正式设计晋级和跨项目动作仍须人工闸门 |

agent 可以在 L1 内连续完成文件整理，但不能用模拟通过、一次试玩或自身判断替代 `grill-with-docs` 和用户/项目采纳。

## 3. 单轮工作流

```text
Route Project
  -> Read P/README, P/AGENTS, P/context/README
  -> Select or create Question
  -> Research / media analysis
  -> Record evidence and Unknown
  -> Create Raw Idea / Unqualified candidates
  -> [人工资格闸门]
  -> Proposal / Evaluation candidate
  -> Simulation or Prototype plan/run (if capability exists)
  -> Write P/insights and evaluation evidence
  -> Decide: Iterate / Parked / Rejected / Needs Human Review
  -> Create new question or candidate version
```

每一步都在本轮产物中写 `project_id`、来源/版本、状态、限制和下一步。共享方法文件只提供规则，不存放项目结果。

## 4. 统一状态词汇

不同文件的状态属于不同维度，不能互换：

| 维度 | 规范状态 | 适用文件 | 含义 |
| --- | --- | --- | --- |
| 设计晋级 | `Raw Idea / Unqualified` → `Qualified GDD Material` → `Proposal` → `Evaluation` → `GDD Draft` → `Draft Change` → `Accepted` / `Parked` / `Rejected` | idea、proposal、evaluation、gdd、draft-change | 设计是否通过项目闸门；只能按项目规则晋级 |
| 研究证据 | `Research` → `Reviewed` / `Superseded`；结论可为 `Provisional`、`Supported`、`Unknown`、`Rejected` | questions、insights、evidence | 证据是否整理及其适用范围，不代表玩法采纳 |
| 执行运行 | `Planned` → `Running` → `Valid Run` / `Invalid` / `Crash` / `Timeout` / `Insufficient Sample` → `Archived` | simulations | 运行是否可复算；技术失败不等于设计失败 |
| 原型 session | `Proposed` → `Ready` → `Running` → `Completed` / `Blocked` / `Invalid` → `Archived` | prototypes | 原型和试玩记录是否完成；规则与体验验收另列 |
| 验收项 | `Pass` / `Fail` / `Blocked` / `Untested` | rule-check、experience-check | 某一条规则或体验观察是否完成验收，不是总体设计状态 |

运行控制文件还可使用 `Ready`、`Awaiting Question`、`Active`、`Completed`、`Blocked` 表示本轮调度状态；它不替代上述设计、证据、运行或验收状态。

`Needs Human Review`、`Insufficient Evidence` 是证据结论，不是自动晋级状态。`Passed` 不作为模拟或原型总体状态。

## 5. 失败回流与版本规则

- 研究证据不足：保留原报告，更新问题为 `Open` 或新建子问题，不把 `Unknown` 改成结论。
- 候选被拒或失效：保留旧候选和原因，创建新 `candidate_id` 或递增 `candidate_version`，重新建立实验/原型引用。
- 模拟 `Invalid / Crash / Timeout / Insufficient Sample`：保留 manifest、日志摘要和输入哈希；修复或补样本时创建新 `run_id`，不覆盖旧运行。
- 原型 `Blocked / Invalid`：记录阻塞或协议偏差；改范围、构建或协议时创建新 `prototype_version`/`session_id`。
- `Parked`：保留当前问题、候选和下一次唤醒条件；恢复时从新问题或新版本开始。
- `Rejected`：不删除失败路径；只有新的证据、范围或候选版本才能重新进入队列。

## 6. 人工闸门

agent 必须在以下情况停止并请求用户或项目负责人决定：

1. 需要把 `Raw Idea / Unqualified` 晋级为合格素材。
2. 需要生成 Proposal、Evaluation、GDD 正文或 Draft Change。
3. 需要把任何内容写入 game-002 正式工作区或修改 `core-concept.md`。
4. 需要跨项目读取、引用或共享来源。
5. 预算、停止条件、外部媒体许可或参与者隐私边界不明确。
6. 只能靠猜测补齐关键规则、玩家体验或实验输入。

人工确认后，agent 在对应文件记录决定者、日期、范围和引用来源；确认不追溯改变旧证据状态。

## 7. 轮次交付清单

每轮结束至少留下：

- 更新后的 `P/run-control.md`：当前问题、候选、最近产物、阻塞、预算消耗和下一步。
- 一个问题、来源或研究/实验产物，能够反查版本/哈希和证据。
- 明确的 `Unknown`、限制、成功/失败信号和停止条件。
- 若产生新玩法，仅进入 `P/idea-inbox/` 并保持 `Raw Idea / Unqualified`。
- 若本轮无法继续，记录 `Blocked` 或 `Needs Human Review`，不虚报完成。
