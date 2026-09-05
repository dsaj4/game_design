# S0-S7 阶段门规范

文档 ID：`AGS-STAGE-001`

状态：`Proposed / Phase 4 draft`

版本：`0.1.2`

更新时间：`2026-09-05`

复审日期：`2026-10-04`

## 1. 阶段模型原则

阶段按“减少哪一种未知、留下什么证据”划分，不按文件数量、代码行数或功能名称划分。`S0-S7` 是 Wiki 和 agent 规范共用的暂定唯一基线；它不是某一个课程、MDA、Agile 或平台文档单独宣布的行业标准。

阶段可以回退，阶段门不能省略。阶段门一旦作出决定，只允许 `Go / Iterate / Park / Stop` 四种结果；证据不足而尚未作出决定时，另记 `Decision state: Pending`，结果写 `N/A`，不能用 `Unknown` 伪装成第五种结果：

| 结果 | 含义 | 必须保留 |
| --- | --- | --- |
| `Go` | 退出证据足够，下一阶段可承担剩余风险 | 证据、负责人、进入条件 |
| `Iterate` | 方向可能成立，但问题或证据不足 | 要改的假设/范围、下一次测试 |
| `Park` | 当前不值得继续投入，但未来可能重启 | 未解问题、保留资产、复议条件 |
| `Stop` | 价值、成本或可行性不可接受 | 停止理由、失败路径、不可再用假设 |

## 2. 阶段总览

| 阶段 | 核心问题 | 主要产出 | 退出证据 | 不能据此推出 |
| --- | --- | --- | --- | --- |
| `S0 研究与问题定义` | 哪个玩家/体验问题值得解决？ | 问题陈述、目标玩家线索、来源/竞品/用户证据、风险和研究问题 | 问题足够具体，未知可测试 | 市场已经验证或概念一定成功 |
| `S1 概念与预制作` | 为谁解决什么体验问题，核心循环和边界能否复述？ | 一句话概念、支柱/反支柱、范围、GDD-0、术语、循环和假设 | 未参与设计者能复述玩家体验和范围 | 所有规则、数值和内容已确定 |
| `S2 原型与趣味验证` | 玩家是否会做目标动作并得到目标反馈？ | 最小原型、测试任务、观察记录、成功/失败/停止信号 | 有核心行为证据，或明确改向 | 单次好评证明长期体验或商业价值 |
| `S3 垂直切片` | 一条代表性体验链能否达标并证明生产方式？ | 可完成体验链、代表性内容、流程试验、GDD-1 | 质量目标和生产成本可接受 | 灰盒片段或演示视频足以代表全项目 |
| `S4 制作与内容生产` | 在范围内能否稳定生产完整内容？ | GDD-2、内容清单、依赖、版本计划、持续测试 | 内容和关键系统按计划完成 | 设计已全部 `Accepted` 或技术已完成 |
| `S5 Alpha / 功能完整` | 关键系统是否接通，连锁风险是否暴露？ | 功能完整构建、系统回归、平衡/可读性问题清单 | 系统接通，风险已分级 | 功能完整等于平衡、无障碍和发布合格 |
| `S6 Beta / 发布候选` | 内容、稳定性、可访问性和平台要求是否达标？ | 内容冻结、发布候选、QA/兼容性/无障碍检查、已知问题分级 | 阻断项关闭，回退和平台检查完成 | 平台审核通过等于玩家喜欢或已上线 |
| `S7 发布、运营与复盘` | 如何安全发布并把真实反馈带回设计？ | 发布清单、支持/监测、复盘、下一版本决策 | 有真实反馈和明确下一步 | 单次市场结果可概括所有玩家和项目 |

## 3. 阶段规则

### ADRULE-STAGE-001：阶段必须绑定未知和证据

Strength：`SHOULD`

Status：`Proposed`

Trigger：创建阶段报告、更新里程碑、判断“完成”或准备过门。

Preconditions：已有目标问题或设计对象；如果没有，先按路由进入 S0。

Input：当前阶段声明、主要未知、阶段活动、退出证据及其链接。

MUST：记录阶段 ID、要减少的主要未知、输入、活动、产出、退出证据、负责人、可逆性和下一次复审时间。

MUST NOT：用“文件写完”“有代码”“功能很多”“Demo 很漂亮”代替阶段证据。

Procedure：`声明未知 -> 设计活动 -> 收集阶段特定证据 -> 记录未解释项 -> 判断能否决定 -> 未决时写 Pending + N/A + reason，已决定时四选一`。

Output：阶段卡或阶段报告，链接材料、GDD、原型、测试、开发索引或发布检查。

Pass criteria：任何读者都能说明本阶段减少的未知和下一阶段要承担的风险。

Failure handling：尚未形成阶段门决定时记录 `Decision state: Pending`、`Gate: N/A` 和 `Pending reason`；决定为证据不足时只能选择 `Iterate` 或 `Park`，不能标 `Go`，必要时回退到相邻阶段。

Evidence：知识系统 Spec 第 5.2、5.3 节；Wiki `01-process/overview.md`。

Owner/version/review date：项目总控 / `0.1.0` / `2026-10-04`。

Review trigger：阶段模型、项目规模或验证方式变化。

### ADRULE-STAGE-002：只使用四种阶段门结果

Strength：`SHOULD`

Status：`Proposed`

Trigger：任何阶段过门、暂停、放弃或发布判断。

Preconditions：当前阶段、主要未知、进入条件和已收集退出证据均有记录；证据不足时允许保持待决。

Input：阶段 ID、进入条件、退出证据、未解问题、负责人和复审条件。

MUST：决定已经作出时在 `Go / Iterate / Park / Stop` 中选择一个，并记录证据、理由、责任人、可逆性和复审日期；尚不能决定时记录 `Decision state: Pending`、`Gate: N/A` 和待补证问题。

MUST NOT：用“差不多完成”“Hold”“Revise”作为新记录的替代状态；旧记录别名需解释为 `Park` 或 `Iterate`。

Procedure：`核对阶段与退出证据 -> 标记 Decision state -> 已决定时四选一 -> 写理由/责任人/可逆性 -> 建立下一步或复议触发`。

Output：可追踪的阶段门记录。

Pass criteria：结果与退出证据及下一步动作一致。

Failure handling：无法做四选一时，保持 `Decision state: Pending`、`Gate: N/A`，把未知写在 `Pending reason / Unresolved unknowns`，并升级给项目负责人；不得默认为 `Go`，也不得把 `Unknown` 记作阶段门结果。

Evidence：知识系统 Spec 第 5.1.1 节；Wiki 阶段门表。

Owner/version/review date：知识系统维护者 / `0.1.0` / `2026-10-04`。

Review trigger：上层 Spec 修改阶段门定义。

### ADRULE-STAGE-003：不得跳阶段或伪造完成

Strength：`SHOULD`

Status：`Proposed`

Trigger：用户或 agent 试图因已有代码、计划、内容数量或外观完成而标记 S3-S7。

Preconditions：能读取当前阶段记录、原型/构建/测试证据和相关状态轴；缺失证据本身记为门槛差距。

Input：阶段声明、对应进入/退出条件、原型/构建/测试证据和各状态轴。

MUST：检查当前阶段进入条件和退出证据；缺口写入未知或风险。尚未作出决定时使用 `Decision state: Pending`、`Gate: N/A` 和 `Pending reason`；已决定继续修正或暂缓时，阶段门分别记为 `Iterate` 或 `Park`。

MUST NOT：

- 用不可玩的灰盒片段宣称通过 S3；
- 用功能堆积宣称进入 S4；
- 用未分级问题的构建宣称 Alpha；
- 用未冻结内容、无平台检查或无回退方案宣称 Beta；
- 把代码实现当作设计确认。

Procedure：`识别阶段声明 -> 对照专属进入/退出条件 -> 分离文档/设计/代码状态 -> 列差距 -> 未决时写 Pending + N/A + reason，已决定时四选一`。

Output：阶段门差距表、阻塞项和下一步验证。

Pass criteria：每个声称的阶段均有该阶段专属证据，而非上一阶段或其他状态轴的替代证据。

Failure handling：报告“不通过”的具体原因、影响和最小修复/验证；尚无决定时使用 `Decision state: Pending`、`Gate: N/A` 和 `Pending reason`，不能为满足里程碑而改写证据状态。

Evidence：知识系统 Spec 第 5.3 节；`AGENTS.md` 阶段流程；Wiki `overview.md`。

Owner/version/review date：项目总控 / `0.1.0` / `2026-10-04`。

Review trigger：项目采用不同阶段名称时，复核职责是否仍被保留。

### ADRULE-STAGE-004：平台发布检查不能替代玩法验证

Strength：`SHOULD`

Status：`Proposed`

Trigger：进入 S6/S7 或用户提出“平台审核通过所以可以发布/完成”。

Preconditions：目标平台、候选版本和发布负责人已知；平台未确定时只建立通用待办，不引用特定平台为通过依据。

Input：目标平台、候选版本、当前官方要求、质量/体验证据和回退方案。

MUST：将商店页面、构建、平台审核、内容冻结、QA、兼容性、无障碍、回退和上线授权分别记录；把玩家体验证据另行链接。

MUST NOT：把 Steamworks 或其他平台清单当作通用游戏开发流程，也不把审核通过写成已发布或好玩。

Procedure：`确认平台/版本 -> 读取当前官方要求 -> 分列页面/构建/审核/质量/回退/授权 -> 链接体验证据 -> 做阶段门判断`。

Output：平台特定发布清单与独立的设计/质量证据。

Pass criteria：平台目标、版本、审核状态和未解决阻断项均可定位。

Failure handling：平台改变或官方要求不确定时，标 `Unknown`，重新读取对应官方文档；阶段门未决时使用 `Decision state: Pending`、`Gate: N/A` 和 `Pending reason`，不复制旧平台规则。

Evidence：Steamworks `Releasing on Steam`；课程 `E-SJ002-P019-001`；Phase 0 外部框架对照。

Owner/version/review date：发布负责人 / `0.1.0` / `2026-10-04`。

Review trigger：目标平台、平台政策或发布计划变化。

### ADRULE-STAGE-005：阶段失败要可逆且可复盘

Strength：`SHOULD`

Status：`Proposed`

Trigger：阶段门结果为 `Iterate`、`Park` 或 `Stop`。

Preconditions：已有阶段、原始假设、投入范围和触发该结果的证据；缺失项明确标 `Unknown`。

Input：阶段门结果、原始假设、投入/成本、失败证据、保留资产和复议线索。

MUST：保存失败路径、原始假设、证据、成本、保留资产、替代解释和复议条件；必要时链接新的 S0-S2 问题。

MUST NOT：删除失败记录、把 `Park/Stop` 改写成“暂时完成”，或为了维护沉没成本继续扩张。

Procedure：`冻结当前判断 -> 保存证据/成本/资产 -> 列替代解释 -> 选择 Iterate/Park/Stop -> 写复议条件或结束边界`。

Output：阶段门记录、复议条件、下一问题或结束说明。

Pass criteria：未来协作者能理解为什么没有继续、什么新证据可以改变判断。

Failure handling：若无法区分暂缓与停止，记录 `Decision state: Pending`、`Gate: N/A` 和 `Pending reason`，并请项目负责人决定；未决定前不扩张范围。

Evidence：`E-SJ003-P015-001`、`E-SJ003-P016-001`、`E-SJ003-P020-001`；知识系统 Spec 第 5.1.1 节。

Owner/version/review date：项目总控 / `0.1.0` / `2026-10-04`。

Review trigger：复议条件满足、新原型证据出现或项目约束改变。

## 4. 阶段门记录模板

```text
Stage: S<0-7>
Decision state: Pending / Decided
Gate: N/A（Pending 时）/ Go / Iterate / Park / Stop（Decided 时）
Pending reason:
Primary unknown:
Entry conditions:
Activities completed:
Exit evidence (links and IDs):
Unresolved unknowns:
Decision rationale:
Owner:
Reversibility:
Next action / next stage:
Review date or trigger:
```
