# game-002 优化探索运行控制

本文件是 `game-002-optimization` 的单轮探索控制面。它只约束本项目内的研究、候选、模拟、原型和评估记录；不能授权直接修改 game-002。每次自动探索开始前先填写“当前运行”，结束后补齐结果和下一步。

## 当前运行：局内／局外策略循环（2026-09-20）

```yaml
project_id: game-002-optimization
source_project_id: game-002
run_id: OPT-20260920-001
context_pack: baseline-2026-09-09-001
explicit_source: GDD-G002-FULL-001@1.0-RC1
source_commit: f5a32c384e77ab1c2bc912fde2f7dc6cd2c4e788
active_question: Q-20260920-strategic-run-and-meta-loops
candidate_ids: [C-informed-expedition-v01, C-committed-trial-v01, C-wave-workshop-v01, C-puzzle-circuit-v01]
autonomy_level: L1-supervised
status: Completed
review: Needs Human Review
round_budget: 1 local design pass; at most 4 raw loop architectures; 0 external research; 0 gameplay simulations; 0 playable prototypes
max_rounds: 1
stop_conditions: deliver loop comparison, recommended architecture, concrete player choices and validation plan; no automatic qualification or RC1 writeback
```

- 授权：用户明确进入 exploration、目标 game-002、不阅读其他探索方向，指定全游戏 GDD，并要求围绕策略深度与独特机制设计局内／局外循环。本次请求足以启动上述有限设计工作，不沿用历史问题或候选推荐。
- 阅读边界：必要路由／治理文件、项目 README／运行控制的导航信息、活动包摘要和用户指定 RC1 及相关正文分册。没有打开其他探索方向的候选、问题、素材或研究正文；导航中的历史摘要不作为本轮设计依据。
- 当前来源的工作树内容与上述 HEAD 一致；GDD 原始提交及逐文件 SHA-256 登记在本轮来源记录。旧包只用于版本识别，不以旧补牌、起手或 Unknown 覆盖 RC1。
- 交付范围：四种循环的研究性比较、一份原始创意记录、一份问题及项目导航。局内含战斗内和战间；局外单指跨局。用户没有要求直接采纳、制作原型或修改正式 GDD。
- 产物：[四种循环原始设计](idea-inbox/2026-09-20-strategic-run-and-meta-loops.md)、[适配与来源](insights/2026-09-20-strategic-loop-fit-and-sources.md)、[主要问题](questions/Q-20260920-strategic-run-and-meta-loops.md)及README／本控制文件。
- 已完成：1轮本地设计分析、4个替代主循环、A的跨局知识反馈与A0／A1／A2验证计划。外部调研、游戏模拟、可玩原型与真人测试均为0；静态实体与币值例只核对来源，不视为获胜／成型证据。
- 当前结果：优先建议A知情远征，但四项均保持`Agent Proposal / Raw Idea / Unqualified`。没有用户主方向选择、资格晋级或正式设计回写；此前历史问题不自动成为本轮前置条件。
- 文档验证：5份文件UTF-8严格解码、85个本地链接、6份来源SHA-256和代码围栏检查通过；任务范围内`git diff --check`通过。实体分配、阶段价格及币值例经静态核对；没有把这些检查记成玩法测试。
- 下一步：交付推荐及完整候选；后续由用户选择主要体验，再按`grill-with-docs`逐项确认。A优先从一个两战分岔拆分验证“提前信息”和“路线影响成长机会”，不同时叠加其他循环。

## 历史运行：时间轴与战场表现及交互（2026-09-14）

```yaml
project_id: game-002-optimization
run_id: OPT-20260914-003
context_pack: baseline-2026-09-09-001
explicit_source: GDD-G002-FULL-001@1.0-RC1
source_commit: 87840a221af330a2c715fc9c390eae982a00aebd
active_question: Q-20260914-timeline-battlefield
candidate_ids: [C-field-time-projection-v01, C-pending-spell-circle-v01, C-patrol-cast-range-v01]
autonomy_level: L1-supervised
status: Completed
review: Needs Human Review
round_budget: 1 local design pass; at most 4 raw directions; 1 explanatory visualization; 0 external research; 0 gameplay simulations; 0 playable prototypes
max_rounds: 1
stop_conditions: deliver visible battlefield concepts, costs and rule boundaries; no automatic qualification or RC1 writeback
```

- 用户将活动问题转向“时间轴和战场表现相关的设计、新表现、新交互”。上一轮优先级问题保留历史，本轮不要求先回答，也不将新请求视为采纳冷却重排、候发或跟随。
- 来源继续限于用户指定RC1，补读其正文UX分册；只在本探索根记录创意。保持战前编辑、战中自动；本轮交互指战前配置与法术在场上的相互作用，不默认开放战中点击干预。
- 本轮示意仅表达巡行范围与名义时刻，不能作为战斗、胜率、伤害或目标必然存活的证据。
- 已完成：[三方向原始创意](idea-inbox/2026-09-14-timeline-battlefield.md)、[当前问题](questions/Q-20260914-timeline-battlefield.md)、[巡行解释示意](insights/visuals/timeline-field-patrol.html)，以及README／运行控制更新。实际3方向、1份交互说明图；外部研究、游戏模拟、可玩原型与真人验证均为0。
- 验证：Markdown本地链接与编码检查通过；说明图脚本语法、6种范围状态及两个控制事件通过独立DOM替身核对。未执行浏览器渲染验收，不宣称像素或实际产品UI验收通过。
- 当前结论：Raw Idea / Unqualified。推荐未来投影作为阅读基础，优先独立讨论巡行范围；待发法阵保留新对象与双阶段成本问题。无资格晋级、正式GDD或目标项目回写。

## 历史运行：时间轴施法构筑的跨品类研究（2026-09-14）

```yaml
project_id: game-002-optimization
run_id: OPT-20260914-002
context_pack: baseline-2026-09-09-001
explicit_source: GDD-G002-FULL-001@1.0-RC1
source_commit: 87840a221af330a2c715fc9c390eae982a00aebd
active_question: Q-20260914-timeline-construction
candidate_ids: [C-rhythm-budget-v01, C-bounded-ready-window-v01, C-wand-follow-clock-v01]
autonomy_level: L1-supervised
status: Completed
review: Needs Human Review
round_budget: 1 cross-genre research pass; at most 10 web calls; at most 3 raw candidates; 0 gameplay simulations; 0 playable prototypes
max_rounds: 1
stop_conditions: deliver primary-source comparison and concrete timeline alternatives; no automatic qualification or RC1 writeback
```

- 授权依据：用户要求在核心时间轴施法构筑上创新并调研其他品类。本轮活动问题转为时间调度；上一轮优先体验问题不再作为当前待答问题，也不把本次转向记成采纳上一轮任何候选。
- 读取边界：继续使用用户指定 RC1 及相关构句／战斗正文；活动包保持原登记。仅检索外部产品的公开资料，不读其他本地探索方向。
- 预期产物：跨品类研究、三项时间轴原始候选、当前问题、导航与控制更新。既有完成冷却、复诵、蓄势和节律杖作为差异检查，不换名声称新增。
- 已完成：[研究与来源](insights/2026-09-14-timeline-cross-genre-research.md)、[三项原始候选](idea-inbox/2026-09-14-timeline-construction.md)、[当前问题](questions/Q-20260914-timeline-construction.md)、README与本控制文件。实际8次web调用，核心采用4个产品的官方来源；没有执行游戏模拟、原型或真人试玩。
- 文档验证：5份任务文件的本地Markdown链接可解析，无Unicode替换字符；核对R1示例的三组释放序列及两间隔和均为12刻。这只是算术核对，不是玩法验收或可用构筑证明。
- 结论：研究Provisional，3项设计仍Raw Idea / Unqualified。已提出优先级问题，未答时保持开放；推荐R1，不自动视为用户采纳，也不回写RC1。

## 历史运行：基于全游戏 RC1 的策略深度与独特机制（2026-09-14）

```yaml
project_id: game-002-optimization
source_project_id: game-002
run_id: OPT-20260914-001
context_pack: baseline-2026-09-09-001
explicit_source: GDD-G002-FULL-001@1.0-RC1
source_commit: 87840a221af330a2c715fc9c390eae982a00aebd
active_question: Q-20260914-rc1-strategy-depth
candidate_ids: [C-conditional-intent-v01, C-bound-enemy-word-v01, C-scar-linked-enemy-v01, C-sentence-handoff-v01]
autonomy_level: L1-supervised
status: Completed
review: Needs Human Review
round_budget: 1 local creative design pass; at most 4 raw candidates; 0 external research; 0 simulations; 0 prototypes
max_rounds: 1
stop_conditions: deliver source-grounded raw designs and one priority question; no automatic qualification, adoption or writeback
```

- 授权依据：用户明确进入 exploration、目标 game-002、禁止阅读其他探索方向，并指定 2026-09-14 全游戏 GDD，要求围绕策略深度与独特机制进行创意设计。本轮据此建立问题与有限候选预算，未继承历史运行的活动问题或探索结论。
- 来源边界：注册路由仍为 `game-002-optimization`。用户指定的 GDD 及其自述属于正文的相关分册作为本轮显式补充来源；没有更换活动背景包、扩大共享注册权限或取得目标项目写入权限。来源版本与摘要见[来源记录](insights/2026-09-14-rc1-strategy-source-record.md)。
- 阅读边界：读取必要的路由、项目 README、运行控制及旧活动包；其中历史摘要只用于路由和版本识别。没有打开其他候选正文、其他探索项目或归档；不将历史运行的推荐及授权当作本轮设计依据。
- 产物：[本轮问题](questions/Q-20260914-rc1-strategy-depth.md)、[四项原始创意](idea-inbox/2026-09-14-rc1-strategy-depth.md)、上述来源记录及项目 README 导航。
- 本轮不生成正式素材、Proposal、Evaluation、GDD 或 Draft Change。候选写得具体不等于通过资格闸门；是否优先探索及是否进入首版均待用户决定。
- 实际完成：1轮本地来源与规则核对、4项原始候选（合并1份inbox）、1份来源记录、1份问题及2份导航／控制更新。外部研究、模拟、原型和真人测试均为0；已检查5份任务文件的本地链接和文本编码，玩法验收仍为NotRun。
- 当前结果：已交付有限创意设计，下一项优先体验选择已向用户提出，尚未收到回答时保持开放；不会默认采纳推荐。其余历史运行与原始方向保留。

## 历史运行：视觉释放触发独有音乐（2026-09-10）

```yaml
project_id: game-002-optimization
run_id: OPT-20260910-003
context_pack: baseline-2026-09-09-001
active_question: Q-20260910-spell-music
candidate_ids: [C-spell-music-feedback-v01]
autonomy_level: L1-supervised
status: Completed
review: Needs Human Review
round_budget: 1 qualification pass; 1 material; 0 external calls; 0 audio prototypes
max_rounds: 1
stop_conditions: record user-confirmed trigger and experience; stop before audio specification, prototype or rule changes
```

- 授权依据：用户确认“可以在视觉上看见法术释放效果时播放独有的音乐，增加施法的核心体验感”。本轮仅据此完成素材资格晋级，不扩大到节奏输入、数值收益或音频制作。
- 资格结果：触发时机、辨识单位（法术）和体验目标已经清楚；独有片段的音频形式、叠听、打断和疲劳保留为 `Unknown`。
- 产物：[合格音乐素材](idea-materials/M-2026-09-10-spell-release-music.md)，同步更新[原始候选](idea-inbox/2026-09-10-spell-music.md)与[验证问题](questions/Q-20260910-spell-music.md)。
- 实际消耗：1 轮用户回答后的资格确认、1 份合格素材；外部调用、模拟、音频生成、原型与真人试听均为 0。没有 Proposal、Evaluation、GDD 或 Draft Change。
- 结论：`Qualified GDD Material / Hypothesis`。该素材可被后续 GDD 或 Proposal 引用，但不代表音乐方案已被采纳或已经好听、耐听。
- 下一步：按既有可行性分析制作最小声音对照，先验证视觉释放与独有音乐是否同步、可辨认且不掩盖打断信息。

## 历史运行：循环施法与音乐元素（2026-09-10）

```yaml
project_id: game-002-optimization
run_id: OPT-20260910-002
context_pack: baseline-2026-09-09-001
active_question: Q-20260910-spell-music
candidate_ids: [C-spell-music-feedback-v01]
autonomy_level: L1-supervised
status: Completed
review: Needs Human Review
round_budget: 1 local feasibility review; 1 raw candidate; 0 external calls; 0 simulation runs; 0 audio prototypes
max_rounds: 1
stop_conditions: deliver a provisional assessment and listening comparison proposal; leave unresolved music goals and rule changes unqualified
```

- 授权依据：用户要求进入 game-002 的 exploration，在已有底层设计上评估音乐元素；随后明确“继续”。本轮据此完成一次本地可行性分析与记录，不重复请求启动许可。
- 设计依据：活动背景包、本地时间背包素材 TS1–TS8 与 SC1。已有素材的使用记录记载合入目标 Core Concept v0.2；较早背景包的空白核心描述仅代表其固定版本，不当作目标项目实时状态。
- 范围审计：前段读取中误读了一份其他探索方向分析，另读取了上一轮增趣候选记录；这些内容不进入本轮证据链。后续只使用时间背包已确认部分、当前用户输入及共享方法。本轮未读取另一探索项目或目标工作区实时正文。
- 当前输入：用户报告“有节奏的施法产生了音效的配合”。尚无音频、录像或独立试听，因此记为 `User Reported`，不记为已验证的音乐体验。
- 输出范围：原始候选、研究性可行性判断、一个关键问题和试听对照建议。音乐作用尚未确定，先不晋级正式素材或 Evaluation；这不妨碍完成本轮咨询判断。
- 产物：[原始候选](idea-inbox/2026-09-10-spell-music.md)、[可行性分析](insights/2026-09-10-spell-music-feasibility.md)、[关键问题](questions/Q-20260910-spell-music.md)，并更新项目 README 导航。
- 实际完成：一轮本地设计分析、一份原始候选，比较三种音乐介入程度并提出四类试听对照场景。使用共享评判框架入口 v1.0 / emergent-strategy-game-framework v0.1 的可读性、协同与退化检查，不输出无证据分数。
- 实际消耗：外部调用、模拟、音频生成、音频原型和真人试听均为 0。新增合格素材、Proposal、正式 Evaluation、GDD、Draft Change 均为 0。
- 结论：推荐推进小规模音乐反馈验证，依据为现有编排与声音事件的结构匹配；悦耳、疲劳、玩家期待与规则理解仍为 `Unknown / Untested`。达到本轮分析与候选预算后完成，不自动启动音频制作。
- 下一步单一澄清：加入音乐后，用户最希望玩家获得什么新体验？Agent 推荐先让玩家听见自己的编排形成一段演奏，该目标未获用户确认。

## 历史运行：底层设计上的增趣机制（2026-09-10）

```yaml
project_id: game-002-optimization
run_id: OPT-20260910-001
context_pack: baseline-2026-09-09-001
active_question: Q-20260910-timeline-mechanism-depth
candidate_ids: [C-enemy-phase-windows-v01, C-limited-cycle-tuning-v01, C-postbattle-reconfiguration-v01, C-idle-reserve-v01]
autonomy_level: L1-supervised
status: Completed
review: Needs Human Review
round_budget: 1 local design review; at most 4 raw candidates; 0 external calls; 0 simulation runs; 0 prototypes
max_rounds: 1
stop_conditions: deliver scoped recommendations and raw records; stop before qualification or formal design promotion
```

- 授权依据：用户于 2026-09-10 要求进入 game-002 的 exploration，不阅读其他探索方向，并探索已有底层设计上增加什么机制能更好玩。本轮只执行这项请求内的一次本地分析与原始候选整理。
- 活动设计：沿用本地时间背包素材 TS1–TS8 与 SC1（先不涉及具体卡片效果），不继承其他候选的研究结论。活动背景包之外仅核对本候选 inbox、合格素材和验证问题。
- 状态边界：本地编排素材使用记录已记载 2026-09-09 合入 game-002 Core Concept v0.2 的历史。本轮不读取目标项目实时正文，不把较早背景包的“无 Accepted”描述当作实时状态，也不把已有采纳扩大到新增机制。
- 产物：[增趣机制原始记录](idea-inbox/2026-09-10-timeline-mechanism-depth.md)、[本轮问题](questions/Q-20260910-timeline-mechanism-depth.md)、项目 README 导航。
- 已完成：一次本地背景核对，整理四项 `Agent Proposal / Raw Idea / Unqualified` 候选，标明保留规则、增量代价、未知项及最小对照建议。建议先改变公开敌方攻击节奏，再单独探索有限调速；这不是用户选定或正式评估结论。
- 实际消耗：1 轮本地分析、4 项候选（合并为 1 份 inbox）、1 份问题；外部调用、模拟、原型、真人测试均为 0。未新增合格素材、Proposal、Evaluation、GDD 或 Draft Change。
- 结果与边界：本轮建议整理完成；乐趣与收益结论保持 `Unknown / Untested`。达到一轮候选预算后结束，没有启动后续实验。
- 下一步单一澄清：用户希望玩家在战前编排时，最有成就感的那个瞬间是什么？推荐先增强看懂敌方时间表、调整后让关键释放如期成功的体验；候选选择和关键规则留待后续逐项确认。

## 历史运行：纵向时间背包（2026-09-09 用户新输入）

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
- 已完成：保存原话、背景差异与候选推演；用户逐项确认 TB1（战前编排）、TB2（覆盖）、TB3（普通打断）、TB4（词卡独占），编排部分按资格清单独立晋级；补做一次外部案例检索并形成[机制相似度研究](insights/2026-09-09-timeline-backpack-similarity-review.md)。状态效果与数值未晋级，无玩法 Accepted。
- 产物：[原始候选](idea-inbox/2026-09-09-timeline-backpack-spells.md)、[局部合格编排素材](idea-materials/M-2026-09-09-timeline-backpack-scheduling.md)、[验证问题](questions/Q-20260909-timeline-backpack.md)。
- 消耗：1 轮背景核对、1 份新候选、1 份局部合格素材、1 轮外部来源审查，依次提出的 8 次单问题澄清均已回答（TB1–TB7 与 SC1）；模拟/原型执行 0 次。没有外部付费调用。
- 当前范围：用户明确“先不涉及具体卡片效果”（SC1），继续时间轴边界、编排容量与战斗节奏。
- 新确认：TB5 采用有限首次启动窗口、各法术之后独立循环整场；TB6 限制编入战斗的词卡总张数、法术数量自然受其约束；TB7 默认公开敌方整场攻击安排。已增补素材与抽象 A/B 时序表，未设定具体卡片效果。
- 结果：本轮编排骨架整理完成，TS1–TS8 来自原始输入与 TB1–TB7；状态 `Qualified GDD Material / Hypothesis`。用户确认 `Moment to Moment` 已放弃开发，仅作为历史检索证据保留，不纳入当前重复风险；外部研究的整体相似度总结为低，状态为 `Research / Needs Human Review`。其余候选保持 `Raw Idea / Unqualified`；所有模拟/体验验收均为 `Untested`。
- 下一步：下一轮用完整公开攻击表和抽象法术验证周期冲突、危险刻规划、空档价值，以及词卡组句是否真正改变构筑选择。具体容量/启动窗口参数仍待设计，当前无未回答的已发问题。

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
