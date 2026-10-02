# 探索研究与实验工作流

2026-10-01 / layout.4。仅用于用户明确指定问题、范围和预算的研究/实验任务；日常构思按各项目exploration/AGENTS保留方向README，不强制run-control或运行记录。

先由[项目登记](registry/project-registry.md)选择唯一项目并读本地AGENTS；本地路径映射优先。W为项目根，P为所选方向或明确实验范围；下文idea-inbox、questions、gdd等是职责名，实际放sources、governance、design/development或所选DIR，禁止在仓库根重建exploration。运行控制用目标项目指定位置，肉鸽为governance/run-control.md。

资格、读取和执行仍按[设计流程](design-workflow.md)；一次批量澄清相关缺口，用户已有授权不重复索取。Raw不能进入Proposal/Evaluation/GDD/Draft Change；合格且已授权的正式输出可直接推进，正式采纳仍独立记录。L1不自动授权联网、跨项目材料、玩法实验或外部仓库创建。

## 1. 启动输入

每轮开始前必须得到或读取一份运行控制文件 `项目登记的run-control.md`，至少确认：

- `project_id`：只能来自[探索项目注册表](registry/project-registry.md)。
- `active_question`：一个可验证的主要问题；没有问题时先在目标项目governance/questions或所选方向README登记问题，不直接生成正式玩法。
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
  -> Read P/README, P/AGENTS, project CONTEXT and selected reading contract
  -> Select or create Question
  -> Research / media analysis
  -> Record evidence and Unknown
  -> Create Raw Idea / Unqualified candidates
  -> [人工资格闸门]
  -> Proposal / Evaluation candidate
  -> Simulation or Prototype plan; run only with explicit task authorization
  -> Write project research records and evaluation evidence
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

以下事项需要明确依据；已有授权直接执行，缺口集中成组确认，并继续独立工作：

1. 需要把 `Raw Idea / Unqualified` 晋级为合格素材。
2. 正式输出所需资格或任务授权缺失；不把已经具备条件的生成工作再次设为审批。
3. 需要把任何内容写入 game-002 正式工作区或修改目标项目正式核心。
4. 需要跨项目读取、引用或共享来源。
5. 预算、停止条件、外部媒体许可或参与者隐私边界不明确。
6. 只能靠猜测补齐关键规则、玩家体验或实验输入。

人工确认后，agent 在对应文件记录决定者、日期、范围和引用来源；确认不追溯改变旧证据状态。

## 7. 轮次交付清单

每轮结束至少留下：

- 更新后的 `项目登记的run-control.md`：当前问题、候选、最近产物、阻塞、预算消耗和下一步。
- 一个问题、来源或研究/实验产物，能够反查版本/哈希和证据。
- 明确的 `Unknown`、限制、成功/失败信号和停止条件。
- 若产生新玩法，仅进入所选DIR的README或目标项目sources/inbox 并保持 `Raw Idea / Unqualified`。
- 若本轮无法继续，记录 `Blocked` 或 `Needs Human Review`，不虚报完成。
