# GDD 规范

文档 ID：`AGS-GDD-001`

状态：`Proposed / Phase 4 draft`

版本：`0.1.0`

更新时间：`2026-09-04`

复审日期：`2026-10-04`

## 1. 唯一基线

本仓库继续使用 [`gdd-writing-requirements-and-template.md`](../../game-design-workflow/templates/gdd-writing-requirements-and-template.md) 作为 GDD v1 模板。本文件解释 agent 如何选成熟度、审查素材和验收正文，不创建第二套模板。

GDD 是玩家体验与玩法设计合同，不是代码设计、项目排期或构建记录。技术状态只链接 [`docs/code-development-index.md`](../../archive/2026-09-05-core-card-project/docs/code-development-index.md)。

## 2. 成熟度选择

| 成熟度 | 适用阶段 | 必须回答 | 不能代替 |
| --- | --- | --- | --- |
| `GDD-0` | S0-S1 | 玩家、体验承诺、支柱、核心循环、范围、最大风险 | 完整数值和制作交接 |
| `GDD-1` | S2-S3 | 玩家旅程、原型范围、状态/时序、反馈、测试和验收 | 未验证的全量生产承诺 |
| `GDD-2` | S4-S6 | 系统依赖、内容规格、可读性、异常、回归和风险 | 类、函数、API 和代码完成度 |

用户没有指定成熟度时，agent 根据目标决定推荐等级，并一次询问一个会改变范围的问题；不因“完整 GDD”字样自动选择 `GDD-2`。

## 3. 正文必答链

每个当前范围内的系统都必须形成：

```text
玩家处境 -> 可见信息 -> 可选动作 -> 代价/限制 -> 系统状态 -> 规则结算 -> 反馈 -> 下一步选择
```

规则描述优先写玩家可观察状态，不下沉到工程实现。涉及顺序、叠加、随机、取消、并发、超时和边界时必须明示优先级与替代结果。

## 4. 规则条目

### ADRULE-GDD-001：写作前审查两层素材库

Strength：`HARD`（继承自 `AGENTS.md`）

Status：`Inherited`

Trigger：创建或更新任意 GDD。

Preconditions：已明确目标 GDD、目标成熟度和本版要支持的决定；能读取核心构思、决策记录、当前问题及两层想法库。

Input：目标 GDD/章节、成熟度、当前核心构思与决策、当前问题、两层想法库候选。

MUST：先阅读当前 GDD、`core-concept.md`、`decision-log.md`、`current-questions.md`，检索 `idea-materials/` 和相关 `idea-inbox/`；在素材审查表中写 Include/Omit/Park 或继续资格确认。

MUST NOT：静默跳过相关正式素材；把 inbox 原始想法直接写入正文；把写入 GDD 等同于采纳核心设定。

Procedure：`选择 GDD-0/1/2 -> 读取正式上下文 -> 检索两层想法库 -> 建立素材审查表 -> 资格不足项继续 grill -> 只把合格来源写入正文并双向链接`。

Output：目标 GDD 文件、素材审查表、双向来源链接和缺口清单。

Pass criteria：正文中每个项目想法都能追溯到合格素材或已接受决策；未确认候选只出现在审查表。

Failure handling：素材缺少资格字段时回到 `idea-inbox/` 并使用 `grill-with-docs`，不能自行补全。

Evidence：`AGENTS.md` 标准流程一、二；现有 GDD 模板。

Owner/version/review date：GDD 维护者 / `0.1.0` / `2026-10-04`。

Review trigger：想法库、GDD 模板或核心构思流程变化。

### ADRULE-GDD-002：每个系统必须闭环且分开 MDA

Strength：`HARD`（继承自现有 GDD 模板第 4.2、4.3 节）

Status：`Inherited`

Trigger：GDD 新增或修改一个玩法系统、卡牌模块、资源、战斗规则或玩家流程。

Preconditions：该设计输入已通过素材资格闸门或能链接到现有 Accepted 决策；系统目的、目标玩家和当前 GDD 成熟度已知。

Input：合格设计输入/Accepted 决策、系统目的、目标玩家、体验承诺和当前规则草案。

MUST：写设计目的、玩家承诺、输入/触发、前置状态、规则顺序、输出/状态变化、成本/限制、失败/取消/异常、交互/信息/反馈、正反例、规则验收和体验验收；分别说明 Mechanics、Dynamics、Aesthetics。

MUST NOT：只写“增加策略性/爽感/平衡”等空泛目标；用代码结构、接口或数据格式代替玩法规则。

Procedure：`写玩家处境/承诺 -> 填 MDA -> 写输入/状态/规则/输出/反馈 -> 补成本/异常/边界 -> 写正反例 -> 分开验收 -> 登记 Unknown/依赖`。

Output：系统规格表、MDA 表、Given/When/Then 规则验收和测试型体验验收。

Pass criteria：另一位协作者能据此复述玩家选择、代价、结果和下一步，不依赖口头补充。

Failure handling：缺字段写 `Unknown`，列影响、负责人、验证方式和决策时点；不得把猜测写成默认值。

Evidence：`E-SJ002-P010-001`、`E-SJ002-P012-001`、`E-SJ004-P007-001`、`E-SJ004-P009-001`；GDD 模板第 4 节。

Owner/version/review date：系统设计负责人 / `0.1.0` / `2026-10-04`。

Review trigger：规则模型、MDA 解释或目标体验变化。

### ADRULE-GDD-003：规则验收与体验验收分离

Strength：`HARD`（继承自现有 GDD 模板第 4.5 节）

Status：`Inherited`

Trigger：准备标记 GDD 章节可交接、原型规则完成或设计“已验证”。

Preconditions：目标规则、目标体验、原型/构建版本和测试范围已固定；若尚无目标玩家或任务，先保持 `Unknown`。

Input：规则 ID、体验假设、固定原型/构建版本、目标玩家、测试任务和观察范围。

MUST：规则验收用确定的 Given/When/Then 或等价边界用例；体验验收写目标玩家、任务、版本、样本、观察字段及成功/失败信号；两者分别报告。

MUST NOT：用代码通过、设计者自测、单次好评或功能数量替代体验证据；用玩家体验反馈宣称规则必然按规格执行。

Procedure：`列规则用例 -> 执行确定性验收 -> 建立体验测试合同 -> 记录目标玩家行为 -> 分别判定两层结果 -> 更新假设/阶段门`。

Output：验收总表、测试链接、未通过项和阶段门建议。

Pass criteria：审阅者能分别回答“规则是否正确”和“玩家是否感知目标体验”。

Failure handling：任一层证据缺失则保留 `Hypothesis/Unknown`，回到 S2/S3 设计验证，不标 `Confirmed`。

Evidence：`E-SJ002-P018-001`、`E-SJ003-P001-001`、`E-SJ003-P014-001`；GDD 模板第 4.5 节。

Owner/version/review date：设计与测试负责人 / `0.1.0` / `2026-10-04`。

Review trigger：验收标准、玩家群体或测试目标改变。

### ADRULE-GDD-004：设计与代码边界不可互相覆盖

Strength：`HARD`（继承自仓库决策）

Status：`Inherited`

Trigger：GDD 或开发记录同时涉及实现状态、技术约束和玩法判断。

Preconditions：能定位相关 GDD/规则 ID、开发进度条目和实现仓库；若没有设计来源，先停止把实现描述为正式玩法。

Input：相关 GDD/规则 ID、实现事实、开发进度条目、偏差记录和玩家可见影响。

MUST：GDD 只记录玩家体验、规则、设计决策、验证和范围；代码仓库记录技术细节，`docs/code-development-index.md` 记录状态、证据、阻塞和偏差。

MUST NOT：在 GDD 写类、函数、模块、脚本路径、API、构建、CI、Bug 列表、排期或代码完成度；不得因代码已经存在把假设升级为确认。

Procedure：`分离设计判断与实现事实 -> GDD 保留玩家/规则内容 -> 技术内容写进代码仓库/进度索引 -> 记录偏差 -> 新设计输入通过素材资格与决策流程`。

Output：分离的 GDD/开发进度链接和偏差记录。

Pass criteria：玩法结论和实现证据各有唯一承载位置，状态轴没有互相覆盖。

Failure handling：技术约束会改变玩家体验时，先在代码进度索引记录实现偏差，并把试玩/实现观察写入 `research/06-prototype-insights/`；若形成新的设计输入，先进入 `idea-inbox/`，通过 `grill-with-docs` 晋级 `idea-materials/` 后，才能进入 Proposal、Evaluation 或 Draft Change。

Evidence：`AGENTS.md` 标准流程八；`decision-log.md`；GDD 模板边界。

Owner/version/review date：设计/开发总控 / `0.1.0` / `2026-10-04`。

Review trigger：代码仓库、进度索引或交接协议变化。

## 5. GDD 自检

- [ ] 文档成熟度、设计状态、生产阶段和代码状态分别填写。
- [ ] 本版范围和明确不包含项清楚。
- [ ] 正式素材与 inbox 候选已审查，正文没有越过资格闸门的想法。
- [ ] 一句话概念和核心循环能说明玩家动作、目标、代价、反馈和退出/失败。
- [ ] 每个当前系统都有输入、状态、规则、输出、反馈、异常和未知项。
- [ ] MDA 的三层都写成可观察行为或体验，不用形容词代替证据。
- [ ] 规则验收、体验验收、风险、回归和决策链接完整。
- [ ] 没有技术实现或开发进度内容。
