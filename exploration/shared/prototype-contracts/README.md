# 原型测试文件契约

版本：`v1.0`。状态：`Reference Ready / Schema Not Executable`。更新日期：2026-09-09。

本页规定探索项目如何登记最小可玩原型、桌面推演和试玩证据。它连接设计候选与可观察行为，不是客户端架构或测试脚本规范。原型“能运行”只证明实现达到指定范围；规则成立、玩家理解和体验价值必须分别验收。

## 适用范围与保存位置

- 适用于自动代理试玩、桌面/纸笔推演、开发者试玩、外部测试包和真人试玩。
- 原型计划、版本和验证索引写入目标项目的 `P/prototypes/`，建议按 `PRO-YYYY-MM-DD-short-name/` 建立一组文件；项目 README 维护入口。
- 代码、构建产物、测试脚本和运行说明留在明确登记的外部实现仓库；`P/prototypes/` 只保存链接、版本、哈希、范围、偏差和结果索引。
- 观察与复盘写入目标项目 `P/insights/`，沿仓库登记的原型洞察模板记录；共享目录不保存具体项目的玩家结论。

## 原型文件关系

```text
prototype-brief.md + design-source + build/version + test-protocol.md
                               |
                               v
                    prototype-session.md
                      /       |        \\
              observations  rule-check  experience-check
                               |             |
                               v             v
                       P/insights/      P/evaluations/
```

一次原型可以有多场 session。每次 session 都要绑定明确的候选版本、构建/纸面规则版本和参与者类型，不能用“最新版本”代替版本号。

## 共同信封字段

每个原型计划、试玩记录和验收文件至少包含：

| 字段 | 要求 |
| --- | --- |
| `schema_id` / `schema_version` | 例如 `prototype-contract@v1.0` |
| `project_id` | 注册表中的唯一 Project ID；不得跨项目复用结果 |
| `prototype_id` / `session_id` | 原型与单次试玩的稳定 ID；改范围或构建时新建版本/Session |
| `candidate_id` / `candidate_version` | 对应素材、提案或 GDD 章节的候选版本 |
| `source_refs` | idea-material、proposal、question、evaluation 或外部来源的路径、版本和适用范围 |
| `evaluation_framework_refs` | 规则/体验验收采用的评判框架 ID/版本；不使用时写 `N/A` 并说明原因 |
| `prototype_version` | 原型规则/内容/可玩包版本；外部仓库记录 commit 或构建号 |
| `actor_type` | `Automation`、`Desk Simulation`、`Developer Playtest`、`Human Playtest` |
| `status` | 使用本页定义的原型状态；规则验收和体验验收另列 |
| `created_at` / `session_at` | ISO 8601 时间；试玩结束时间可另列 |
| `input_hashes` | brief、规则、构建包或纸面材料的 SHA-256；不可计算时写明原因 |

## 输入契约

### `prototype-brief.md`

原型目标应保持最小范围，至少写明：

```markdown
# PRO-YYYY-MM-DD-short-name

- Project ID：
- 原型状态：Proposed / Experimental
- 候选与设计来源：路径、版本、状态
- 要回答的一个主要问题：
- 玩家任务与起始情境：
- 可见信息：
- 允许的行动与禁止范围：
- 最小规则范围：
- 明确不实现/不评估：
- 成功信号与失败/停止信号：
- 预计 session、参与者类型与样本：
- 实现仓库/构建或纸面版本：
- 已知实现偏差：
```

目标必须能通过玩家任务或观察项判断。若候选仍为 `Raw Idea / Unqualified`，原型只能作为探索性证据，不得跳过资格确认直接写入 GDD 或 Proposal。

### `test-protocol.md`

记录每次试玩前后保持一致的条件：招募/参与者筛选、说明文字、可见信息、操作和暂停规则、场景/关卡起点、允许重试次数、观察者角色、记录方式和停止条件。不同参与者获得不同提示时必须注明，避免把引导差异误判为规则效果。

## 输出契约

### `prototype-session.md`

每次 session 至少记录：session ID、参与者类型与数量（匿名即可）、原型和构建版本、场景、实际可见信息、任务说明、操作/决策序列摘要、完成/退出/阻塞原因、耗时或回合数、观察者和材料哈希。不要只写“好玩/不好玩”，保留能复查的行为和原话（得到授权时）。

### `observations.md` 或 `P/insights/` 洞察卡

将事实观察、参与者解释、分析推断和未知项分开。每条观察包含时间点/步骤、行为或原话、触发情境、影响的规则/体验假设、证据强度和后续问题。模拟或开发者试玩不能伪装成真人证据；样本为零时写 `Unobserved`。

### 规则验收（`rule-check.md`）

逐条用 Given/When/Then 检查候选规则、状态变化、边界、取消/异常、反馈和终止条件。状态只能是 `Pass`、`Fail`、`Blocked` 或 `Untested`，并链接 session 或日志证据。`Pass` 表示原型按规格工作，不代表设计已确认。

### 体验验收（`experience-check.md`）

记录测试任务、参与者/场景、观察指标和成功/失败信号，例如：玩家是否能说出当前目标、预测行动结果、识别失败原因、主动复现策略、感受到取舍。结论必须注明证据类型和限制；没有真人或足够观察时写 `Unknown / Needs Human Review`。

## 状态边界

| 状态 | 含义 | 允许的结论 |
| --- | --- | --- |
| `Proposed` | 已登记问题和最小范围，尚未准备试玩 | 只有计划 |
| `Experimental` | 候选或实现仍未完成资格确认/校准 | 可观察，不可晋级正式设计 |
| `Ready` | 输入、版本、任务和验收标准齐全 | 可开始 session |
| `Running` | session 进行中或记录尚未封存 | 不引用中途印象为结论 |
| `Completed` | session 结束，记录和材料已封存 | 可进入 insights/evaluations |
| `Blocked` | 构建、规则、参与者或材料阻塞 | 记录阻塞原因，不计作 Fail |
| `Invalid` | 未按协议执行或输入版本不可确认 | 重新执行，新建 session |
| `Archived` | 历史原型/版本冻结 | 不原地覆盖；新范围建新 prototype |

原型总体状态不要使用 `Passed` 代替设计结论。可分别记录 `rule_acceptance: Pass/Fail/...` 与 `experience_evidence: Sufficient/Insufficient/Unknown`。即使规则验收通过，仍可能因为可理解性、趣味性、策略深度或样本限制而进入 `Needs Human Review`。

## 追踪与晋级

从 session 可以反查：`project_id → prototype/candidate/source → prototype/build version → actor/scenario → observations → rule/experience checks → insight/evaluation`。外部实现只通过仓库 URL、commit/build ID 和哈希引用；不要把构建产物复制到共享方法目录。

原型洞察进入项目 `insights/` 后，若要形成正式素材，必须回到 `idea-inbox → grill-with-docs → idea-materials`；若要写 Proposal、Evaluation 或 GDD，仍需按项目规则审查来源和状态。优化项目拟回写 game-002 时必须生成 Draft Change，并保留本项目证据链。原型结果不会自动修改任何 `core-concept.md`。

## 最小原型索引模板

```markdown
# PRO-YYYY-MM-DD-short-name

- Project ID：
- 状态：Proposed / Experimental / Ready / Completed / Blocked / Invalid
- 主要问题与候选版本：
- 设计来源与适用范围：
- 评判框架：ID、版本或 `N/A`
- 玩家任务/情境/可见信息：
- 最小范围与明确不评估：
- 原型/构建/纸面版本及 SHA-256：
- Actor type：Automation / Desk Simulation / Developer Playtest / Human Playtest
- Test protocol：
- Session IDs：
- 观察与洞察：
- 规则验收：Pass / Fail / Blocked / Untested
- 体验证据：Sufficient / Insufficient / Unknown / Needs Human Review
- 实现偏差与阻塞：
- 下一步：补试玩 / 改规则 / 改原型 / 模拟 / 评估 / 暂缓
```

## 禁止内容

- 不把客户端类、函数、脚本、构建命令、Bug 列表或工程完成度写成设计结论；这些留在实现仓库和项目开发索引。
- 不把模拟胜率、开发者一次试玩或代理成功率当作真人可理解性和趣味性的证明。
- 不删除失败、阻塞或负面观察；版本变化或协议修复应创建新 session，并保留旧记录。
- 不把未授权参与者的个人信息、密钥或私密录音复制进共享目录；使用匿名 ID 和受控链接。
- 不因原型可运行就跳过素材资格、评估框架或 Draft Change；未知项保持 `Unknown`，不要由 agent 补造。
