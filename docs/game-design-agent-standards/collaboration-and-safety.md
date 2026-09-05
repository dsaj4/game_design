# 协作与安全规范

文档 ID：`AGS-COLLAB-001`

状态：`Proposed / Inherited protocol map`

版本：`0.1.0`

更新时间：`2026-09-04`

复审日期：`2026-10-04`

## 1. 适用范围

本文件把仓库已有的分支、核心文档保护、共享工作区和资料版权边界汇总为 agent 检查项。它不授予 agent 修改核心设定或外部系统的额外权限。

## 2. 规则条目

### ADRULE-COLLAB-001：修改前检查分支和工作区

Strength：`HARD`（继承自 `docs/github-collaboration.md`）

Status：`Inherited`

Trigger：准备创建、修改、删除或格式化仓库文件。

Preconditions：已进入目标仓库并能读取 Git 状态；若不是 Git 仓库，记录该事实并遵守共享文件保护边界。

Input：目标仓库、当前分支/工作区状态和本轮负责文件范围。

MUST：先检查 `git status --short --branch` 和当前分支；如果在 `main/master`，先创建 `agent/<agent-name>/<date>-<topic>` 分支；识别并保留用户已有未提交改动。

MUST NOT：在默认分支直接修改核心文档；用 reset、checkout 或其他破坏性命令覆盖用户改动。

Procedure：`检查分支/状态 -> 识别用户已有改动 -> 确定本轮负责文件 -> 必要时创建 agent 分支 -> 再开始编辑`。

Output：分支名、工作区基线和本轮负责文件范围。

Pass criteria：修改发生在非默认分支，且无不明来源的改动被删除或覆盖。

Failure handling：发现同一文件存在无法安全协调的用户改动时暂停该文件并说明冲突；无须回滚无关文件。

Evidence：`docs/github-collaboration.md`、`AGENTS.md`。

Owner/version/review date：仓库维护者 / `0.1.0` / `2026-10-04`。

Review trigger：分支策略、托管平台或共享工作区行为变化。

### ADRULE-COLLAB-002：核心设定必须走 Draft Change

Strength：`HARD`

Status：`Inherited`

Trigger：用户表示“确认了”“采纳了”“写进核心构思”，或 agent 准备修改 `core-concept.md`/`decision-log.md`。

Preconditions：设计输入已经过素材资格、Proposal 和 Evaluation，或现有流程明确允许的等价来源；用户已明确采纳拟修改内容。

Input：合格设计来源、Proposal、Evaluation、拟改文本、用户采纳证据和当前核心文档/Decision Log。

MUST：先在 `game-design-workflow/draft-changes/` 写来源、拟改文本、理由、影响、备选和回退；确认后同步核心文档与决策记录，并在本轮提交推送。

MUST NOT：把课程观点、未通过资格的想法、代码现状或 agent 推断直接写进核心构思；不得删除历史失败路径。

Procedure：`核对来源链 -> 创建 Draft Change -> 写拟改文本/影响/回退 -> 获得明确确认 -> 同步 core-concept/decision-log -> 提交并推送`。

Output：Draft Change、核心文档、Decision Log 和提交链接。

Pass criteria：每一项正式变化都有来源、采纳证据、决策 ID、版本和回退位置。

Failure handling：没有明确采纳或前置 Proposal/Evaluation 时保留候选，回到正式设计流程；Proposal、Evaluation 和 Draft Change 只保留追踪，不得提供 `E4` 或 `Accepted`。

Evidence：`AGENTS.md` 标准流程七；`docs/github-collaboration.md` 核心构思修改协议。

Owner/version/review date：项目维护者 / `0.1.0` / `2026-10-04`。

Review trigger：核心文档路径、决策流程或用户授权方式变化。

### ADRULE-COLLAB-003：按职责分离目录

Strength：`HARD`

Status：`Inherited`

Trigger：一个请求同时涉及研究、想法、GDD、代码、测试或发布。

Preconditions：已拆分请求中的独立意图并标出每部分当前状态；模糊部分可以先进入隔离区。

Input：用户请求的独立意图、各部分状态轴、候选唯一事实源和目标目录。

MUST：按内容状态分路由：研究进 `research/`，原始想法进 `idea-inbox/`，合格素材进 `idea-materials/`，GDD/Proposal/Evaluation/变更进入对应工作流，代码状态进 `docs/code-development-index.md` 或实现仓库，原型观察进 `research/06-prototype-insights/`。

MUST NOT：把所有内容写入一个“总文档”；把 GDD 当开发进度表；把代码技术细节复制进研究或 GDD；让 inbox 绕过资格闸门。

Procedure：`拆分意图 -> 分配状态轴 -> 查唯一事实源/目标目录 -> 执行各自前置闸门 -> 写入并建立链接 -> 报告排除项`。

Output：每个文件的职责、状态轴、来源链接和排除项。

Pass criteria：任何结论有唯一事实源，下游只通过链接/ID引用，状态轴没有混淆。

Failure handling：路由有多种高风险解释时保留候选并一次询问一个关键问题。

Evidence：`AGENTS.md` 用户意图识别；知识系统 Spec 第 4、12 节。

Owner/version/review date：游戏构思系统引导员 / `0.1.0` / `2026-10-04`。

Review trigger：目录结构、工作流状态或唯一事实源变化。

### ADRULE-COLLAB-004：提交、推送和报告完整

Strength：`HARD`（核心保护范围）

Status：`Inherited`

Trigger：本轮修改了 `AGENTS.md` 或 `docs/github-collaboration.md` 明确列入核心保护范围、并被上游协议要求提交推送的文件或目录。

Preconditions：当前分支不是 `main/master`；本轮负责文件和核心保护范围已确认，远端可用性已知。

Input：上游核心保护范围、本轮负责文件、当前分支、暂存差异和远端状态。

MUST：对 `docs/github-collaboration.md` 与 `AGENTS.md` 列出的核心保护范围，只暂存本轮负责文件，提交清晰信息并推送当前分支；最终报告分支、提交哈希、文件、状态和下一步。

MUST NOT：把用户未授权的临时文件、第三方原始媒体、密钥或无关改动一并提交；不得以“本地已改”代替推送说明。

Procedure：`复核负责文件 -> 只暂存本轮核心范围 -> 检查暂存差异 -> 提交 -> 推送当前分支 -> 报告分支/哈希/文件/状态`。

Output：可复核提交和推送结果；若推送失败，报告本地提交与具体原因。

Pass criteria：本轮负责的核心保护文件没有遗留未提交改动，提交内容与报告文件一致；用户或其他 agent 的无关改动保持原状。

Failure handling：认证/网络失败时保留本地提交并明确阻塞，不强推、不覆盖远端历史。

Evidence：`docs/github-collaboration.md` 提交与推送要求；仓库 `AGENTS.md`。

Owner/version/review date：仓库维护者 / `0.1.0` / `2026-10-04`。

Review trigger：远端权限、分支保护或发布流程变化。

### ADRULE-COLLAB-006：正式文档提交前质量检查

Strength：`SHOULD`

Status：`Proposed`

Trigger：准备提交 Wiki、规则、研究摘要、模板或其他正式文档。

Preconditions：已确定本轮负责文件列表，且未把用户无关改动加入暂存区。

Input：本轮负责文件、当前差异、链接/ID/状态/结构检查要求和检查工具输出。

MUST：对本轮文件运行 `git diff --check`，检查相对链接、稳定 ID、状态轴和已声明的结构要求；只修正本轮范围内的问题。

MUST NOT：为了让检查通过而清理、暂存、格式化或回滚用户/其他 agent 的无关文件。

Procedure：`列出负责文件 -> 检查差异与链接/ID -> 修正本轮问题 -> 复查负责范围 -> 记录检查结果 -> 交回适用的提交协议`。

Output：检查结果、未解决风险和待提交文件清单；是否必须提交/推送仍由上游协作协议与 `ADRULE-COLLAB-004` 决定。

Pass criteria：本轮负责文件没有空白错误、断链、重复 ID 或已知状态冲突；无法检查的项目已明确报告。

Failure handling：问题属于他人改动时保留现状并报告；问题影响本轮交付时先修复或将对应内容标为 `Blocked/Unknown`。

Evidence：知识系统 Spec 第 14 节；本目录 Phase 4 评审要求。

Owner/version/review date：知识系统维护者 / `0.1.0` / `2026-10-04`。

Review trigger：文档格式、校验工具或共享工作区协议变化。

### ADRULE-COLLAB-005：外部资料和不可逆操作受最小权限约束

Strength：`SHOULD`

Status：`Proposed`

Trigger：下载/复制第三方课程媒体、调用外部服务、删除文件或执行可能覆盖数据的动作。

Preconditions：目标、范围、权限、数据所有者和可恢复方式已知；缺任一高风险条件时不执行不可逆动作。

Input：外部来源/服务或操作目标、授权范围、数据所有者、恢复方式和版权/隐私限制。

MUST：只保存完成研究所需的元数据、转写和改写摘要；确认目标、范围、权限和可恢复性；优先可逆操作；记录来源、访问日期和版权/隐私限制。

MUST NOT：提交第三方原始媒体、暴露凭据、递归删除不明确目录、覆盖用户文件或用外部结果掩盖来源缺失。

Procedure：`确认授权与目标 -> 读取来源/版权边界 -> 选择最小且可逆动作 -> 执行并记录 -> 核对结果/失败 -> 清楚报告恢复方式`。

Output：来源记录、失败/权限记录和可恢复的变更。

Pass criteria：外部输入可追溯，材料边界符合仓库政策，删除/覆盖目标经过明确核对。

Failure handling：目标或权限不清时停止该动作，保留 `Blocked/Unknown` 并请求必要的用户决定。

Evidence：`AGENTS.md` 版权与失败保留要求；系统安全和 Windows 操作约束。

Owner/version/review date：项目维护者 / `0.1.0` / `2026-10-04`。

Review trigger：外部服务、版权政策或工具权限变化。

## 3. 交接清单

- [ ] 已说明本轮负责文件和不负责文件。
- [ ] 已检查分支和用户既有改动。
- [ ] 研究、设计、代码、测试和发布内容已按职责分离。
- [ ] 核心设定没有绕过 Draft Change、Decision Log 和用户采纳。
- [ ] 失败、未知、冲突、搁置和回退位置已保留。
- [ ] 正式文档已完成差异检查、提交、推送或明确报告阻塞。
