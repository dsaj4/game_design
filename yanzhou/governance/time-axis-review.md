# 时间轴资料导航与一致性审查

Project ID：game-002 / game-002-optimization。文档角色：TopicNavigation / DocumentationAudit。日期：2026-09-30。状态：文档整理；没有新增玩法采纳、资格晋级或验证结果。

本页把“时间轴”作为主题，把现行规格、原始来源、探索候选、历史版本、效果身份、实现证据与视觉表现连起来。规则仍由[现行设计](../design/README.md)维护，本页摘要不能成为第二套规则。

本次使用READ-1 **CUSTOM**：任务授权横向整理言咒主系统、全部探索方向、项目自身历史、兼容路径及明确关联的共享入口。固定起始HEAD为`e540b0fd6885992e9701abe2e461316d07c2021f`。普通方向后续仍按自己的既定来源阅读；本次横向审查不替它们升级背景。

完整盘点及阅读边界见[覆盖说明](time-axis-review/coverage.md)。[资料定位目录](time-axis-review/sources.md)连接全部主题命中来源；[文件清单](time-axis-review/inventory.json)保存Git blob、SHA、原工作树差异及阅读状态，[章节目录](time-axis-review/catalog.json)保存精确定位行与章节范围。文件盘点、机器检索、主题摘录审查和全文阅读是不同状态。

## 现行规则从哪里读

| 问题 | 权威入口与定位 | 本次核对的口径 |
| --- | --- | --- |
| 一刻多长、何时暂停 | [GDD §3](../design/GDD.md)、[UX04](../design/systems/07-interaction-save.md) | 1×下逻辑刻0.5秒；战斗前停在第0刻之前，单步推进下一完整刻。速度和动画不改变规则顺序；终局可以在事件后提前结束当刻。 |
| 什么是起点 | [SYS-002](../design/systems/02-wands.md)、[PG-T01](../design/parameters.md) | 每杖首次冷却开始在0–10整数刻；不是直接指定第一次效果发生刻，也不是公共循环板的长度。 |
| 冷却与释放段 | [GR02](../design/systems/03-combat.md)、[PG-T01及时间例](../design/parameters.md) | 词卡贡献τ相加为基础C，L另列且为正整数。冷却`[s,u)`，释放`[u,u+L)`；普通直接效果在u一次结算。无修正时首次`u=s+C`，以后间隔C＋L。 |
| 同刻怎样争用 | [R24／BR03／RC02](../design/systems/03-combat.md) | 共享槽仲裁**开始释放**；后配置法杖优先。覆盖丢失本次，不排队补发。已经开始的有限过程可并存；没有额外忙碌锁。 |
| 命中打断什么 | [基本时序／GR02／BR08](../design/systems/03-combat.md) | 普通实际生命伤害取消当前冷却机会；护甲完全抵挡不打断，不撤销已完成动作。取消仍保留已确定的名义段及续排边界；疲劳独立处理。 |
| 加速、完成与跳冷却 | [GR02／CG-T01](../design/systems/03-combat.md)、[PG-T01](../design/parameters.md)、[实体卡](../design/content/cards.md) | 改当前未完成冷却与改基础C不同；改期最早下一刻。完成冷却不会立即再占当刻槽，也不能复活已取消机会。普通C下限1；复诵与明确跳冷却才许可C＝0。 |
| 节律与计数 | [法杖固定芯](../design/systems/02-wands.md)、[PG-T01](../design/parameters.md) | 节律按正常冷却周期第2、4…次计，覆盖和打断仍计；复诵不推进正常周期，跳冷却仍属于正常循环。不是按成功次数减C。 |
| 复诵怎样调度 | [RC02／BR03](../design/systems/03-combat.md)、[PG](../design/parameters.md) | 每杖最多一份待复诵；从原释放段结束后、最早原开始下一刻尝试完整再释放，C＝0、L沿原法术。仍争开始槽；同杖同刻复诵优先正常机会；丢失不另排队，不推迟正常循环。 |
| 持续释放在做什么 | [RC07／RC10](../design/systems/03-combat.md)、[SYS-004](../design/systems/04-elements-environment.md) | 释放类L＝3，每有效刻按当时合法性补层／出生／回退；不是每刻重复一次完整法术成功事件。普通L＝1；每个完整法术最多一次成功通知。 |
| 名单、来源、触发与胜负 | [GR06／RC01–12／BR05](../design/systems/03-combat.md) | 一次直接名单先固定、逐对象复查，不追加补位。完整根事件后先检查胜负，再即时处理最多一层特殊响应；派生事件不递归触发新特殊层。来源顺序、对象顺序与开始槽优先级各有职责。 |
| 四阶段是什么 | [同刻四阶段](../design/systems/03-combat.md) | 法术→敌人→环境→状态。环境先联合疲劳，再元素自动邻近及环境检查；状态先燃烧后冰冻，同类沿公开宿主顺序。阶段内的全部事件顺序仍受AUD-010限制。 |
| 状态计时与环境生成 | [ST01–04](../design/systems/03-combat.md)、[SYS-004](../design/systems/04-elements-environment.md)、[PG](../design/parameters.md) | 燃烧伤害／冰冻增甲每刻末；自然衰减保留小数进度。源、宿主与元素本体分开；环境转化继承对应层数／进度，抵消补生用正余量。固定名单阻止同阶段无限新增处理。 |
| 疲劳怎样结束等待 | [BR08／RG06](../design/systems/03-combat.md)、[路线系统](../design/systems/05-route-encounters.md) | 普通F＝56、首领F＝96，首扣F＋4，此后每4刻；第k次名义损耗ceil(Hf×k/20)，联合交付再判胜负。同亡玩家失败，无视甲、不算伤害打断。80／120上界依赖明确的无治疗、复活、增上限及新增敌人等前提。 |
| 计划预览能承诺什么 | [UX03–05](../design/systems/07-interaction-save.md)、[术语](../CONTEXT.md)、[验证输入](../design/validation.md) | 区分名义计划、已知改期与实际事件；未知未来条件不能画成必定成功。战中只读；速度、复盘和查看范围不授予移动施法时点的权限。 |

例：C＝4、L＝1、s＝0，无其他影响时释放开始为4、9、14。释放火焰C＝5、L＝3、s＝0，在5、6、7刻维持过程，8刻释放段结束并开始下一冷却，下一次开始13。数字来自PG；它们不是旧TS的第5／10刻示例。

UX默认配置起点0／1／2／2，对应4／5／7–9／8刻首轮；第8刻的旧火释放过程与新操控开始可相遇，这种布局不证明所有阶段内先后都已闭合。

## 来源演变与适用范围

| 来源阶段 | 可追溯记录 | 与今天的关系 |
| --- | --- | --- |
| 早期逐句施法／时间成本 | [施法耗时素材](../sources/materials/M-2026-09-05-casting-time-and-interruption.md)、[编排预览素材](../sources/materials/M-2026-09-05-timeline-schedule-preview.md)及各自原始存档 | 历史的逐句构句、词卡周转与时间含义经过后续重组。现行素材中的归一化字段和历史原文必须分别解释。 |
| 09-09 时间背包TS1–8 | [原始确认TB1–7](../history/exploration-2026-09-24/idea-inbox/2026-09-09-timeline-backpack-spells.md)、[局部合格素材](../history/exploration-2026-09-24/idea-materials/M-2026-09-09-timeline-backpack-scheduling.md)、[CORE-002拟修改](../sources/draft-changes/D-2026-09-09-timeline-backpack-core.md) | 战前编排、实体独占、循环、有限首次窗口及公开敌情部分进入主系统。原TS的首轮第5刻、命中同刻先取消、容量自然约束法术数等不能整包带入RC1。AUD-014已登记部分吸收。 |
| CORE-006／007 | [战前构句拟修改](../sources/draft-changes/D-2026-09-09-prebattle-spell-wand-assembly.md)、[接口素材](../sources/materials/M-2026-09-10-accepted-design-interfaces.md)、[决定记录](decision-log.md) | 当前四阶段、0–10首次冷却、词卡时间求C、实际生命伤害取消冷却及独立失败反馈的依据。 |
| R23／R24及GR02 | [R01–32素材](../sources/materials/M-2026-09-10-semantic-world-executable-rules.md)、[GR素材](../sources/materials/M-2026-09-11-global-rule-boundaries.md) | 取消不复活、改期续排、开始槽与多刻过程分离；旧GR07-C01在S2／E3内已被RC06替代。 |
| ST与RC | [ST01–04](../sources/materials/M-2026-09-13-end-tick-status-rulings.md)、[RC01–12](../sources/materials/M-2026-09-13-card-pool-rule-rulings.md) | CORE-018改为每刻末状态并保留小数衰减；CORE-019明确有限完整复诵、一层即时触发与逐刻持续过程。旧每3刻实验不能外推。 |
| BR与最终首版包 | [BR](../sources/materials/M-2026-09-13-pre-gdd-recommendation-batch.md)、[CG](../sources/materials/M-2026-09-14-card-interface-completion.md)、[PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)、[RG](../sources/materials/M-2026-09-14-run-route-encounters-and-fatigue.md)、[UX](../sources/materials/M-2026-09-14-interface-platform-and-experience.md) | CORE-029的正L／并存／保存等接口，加CORE-032–036的具体词效、时间、路线、疲劳和表现。对应现行正文，不由旧实验参数替代。 |
| doc.1／layout.1–2／CORE-SUM-1 | [文档合同](document-contract.md)、[基准](../design/baseline.md)、[摘要](../design/core-design.md) | 文档权威与路径管理；不重新采纳玩法。摘要自身依据0591fa5…，本次实际读取HEAD另列，两者不混写。 |

[资料目录](time-axis-review/sources.md)还包含inbox、Proposal、Evaluation、Draft Change、旧冻结背景及对应FX历史。Qualified只授予明确素材范围的正式引用资格；Proposal／Evaluation与技术实现不自动授予Accepted。

## 全部30个探索方向的时间轴关系

下表是本次治理任务的主题定位与Research / Provisional比较，不替各方向确认细则或合并机制。早期方向沿原固定背景；09-14与09-20候选沿各自显式RC1；028–030沿各自固定CORE。每个页首与阅读表中的完整提交／blob是其实际依据，不能用本次HEAD统一覆盖。

| 方向 | 时间轴相关内容与主要边界 | 原资格／采纳 |
| --- | --- | --- |
| [001 战场编译器](../exploration/DIR-001-battlefield-compiler/README.md) | Now／Commit／Echo时间姿态；含早期战中选择，延迟兑现与成本未定。 | Raw |
| [002 法术远征](../exploration/DIR-002-spell-expedition/README.md) | 整体冒险中的即时构句；不能自动套现行战前锁定循环。 | Raw |
| [003 时间背包](../exploration/DIR-003-timeline-backpack/README.md) | TS1–8、TB确认、错峰与循环；首轮、敌我先后、容量及长释放须按后续主系统决定读。 | 局部Qualified；部分吸收 |
| [004 敌方相位窗口](../exploration/DIR-004-enemy-phase-windows/README.md) | 将公开攻击安排组织成阶段机会；窗口价值及行为尚待确认。 | Raw |
| [005 有限调速](../exploration/DIR-005-limited-cycle-tuning/README.md) | 战前付成本改变后续周期；不是现行首次起点权限，成本载体未定。 | Raw |
| [006 战后重组](../exploration/DIR-006-postbattle-reconfiguration/README.md) | 跨战换词、拆装、重排首次起点；不增加战中重排。 | Raw |
| [007 空档储备](../exploration/DIR-007-idle-reserve/README.md) | 空档变储备；何为空档、取消／覆盖是否获益及支付未定。 | Raw |
| [008 视觉施法音乐](../exploration/DIR-008-spell-music/README.md) | 实际视觉释放触发独有音乐；不能按名义循环播放成功音，也不等于规则成功通知。 | 局部Qualified；未采纳 |
| [009 条件敌意](../exploration/DIR-009-conditional-intent/README.md) | 预定敌攻刻读取公开条件；要明确法术阶段后、攻击前的读取边界。 | Raw |
| [010 封词借词](../exploration/DIR-010-bound-enemy-word/README.md) | 绑定临时词贡献C、占真实位置；不是闲置卡免费封技。 | Raw |
| [011 痕迹牵动敌人](../exploration/DIR-011-scar-linked-enemy/README.md) | 当前环境痕迹影响敌技，保留释放覆盖与环境末检查；不是任意火伤立即改敌技。 | Raw |
| [012 两杖接句](../exploration/DIR-012-sentence-handoff/README.md) | 同刻配对移交作用，改变一次冲突；第三杖及被取消后触发须独立规定。 | Raw |
| [013 周期预算](../exploration/DIR-013-rhythm-budget/README.md) | 相邻两次正常冷却短／长重新分配；覆盖／打断仍计正常周期，成本和其他时间修正未定。 | Raw |
| [014 有限候发](../exploration/DIR-014-bounded-ready-window/README.md) | 无合法对象时最多等2刻，不先占槽，等待推迟周转；取消／覆盖不进入候发，支付不足不在当前例内。 | Raw |
| [015 法杖跟随](../exploration/DIR-015-wand-follow-clock/README.md) | 上游实际正常成功控制下游启动，最早下一刻；忙碌时信号丢弃、无队列，不借复诵或子事件无限发信号。 | Raw |
| [016 场地时间投影](../exploration/DIR-016-field-time-projection/README.md) | 空间显示当前／名义未来计划，不能承诺未知生命、命中或胜负结果。 | Raw |
| [017 预置法阵](../exploration/DIR-017-pending-spell-circle/README.md) | 注册与兑现两步、仍竞争开始槽；提前兑现最早下一刻，付费时点与清理未定。 | Raw |
| [018 巡行范围](../exploration/DIR-018-patrol-cast-range/README.md) | 正常周期推动锚点、释放段范围保持；不等于单位移动，复诵／跳冷却关系待审。 | Raw |
| [019 知情远征](../exploration/DIR-019-informed-expedition/README.md) | 取得资源后的生成先于操控与冲突安排；永久复盘与预告是新候选。 | Raw |
| [020 限额整备](../exploration/DIR-020-committed-trial/README.md) | 战间限制改句，首次起点仍可调整；改变整备权限，不改变开始槽。 | Raw |
| [021 波次工坊](../exploration/DIR-021-wave-workshop/README.md) | 各波按新战斗重置还是状态继承需区分；单场80刻上界不能证明无限波整局有限。 | Raw |
| [022 谜题巡回](../exploration/DIR-022-puzzle-circuit/README.md) | 用护甲保冷却、先生成再操控、避槽冲突形成题目；重试／解锁结构未采纳。 | Raw |
| [023 双面战利品](../exploration/DIR-023-dual-reward/README.md) | 公开早攻／初甲挑战与成长机会绑定；改奖励来源，不凭奖励倒推时序改变。 | Raw |
| [024 借词布阵](../exploration/DIR-024-borrow-word-formation/README.md) | 封存实体词换初始元素，节省生成过程但失去循环补生；不是免费提前释放。 | Raw |
| [025 咒式委托](../exploration/DIR-025-spell-commission/README.md) | 胜前分阶段留下环境痕迹，承担耗时／疲劳及奖金代价；不得推迟正常胜负检查。 | Raw |
| [026 自编遗迹](../exploration/DIR-026-self-built-ruins/README.md) | 间接环境布场方向；未新增可直接沿用的时间调度规则。 | Raw |
| [027 咒理试炼](../exploration/DIR-027-spell-principle-trial/README.md) | 规则理解／验证方向；不能以题目或陈述存在当作玩家已理解时间轴。 | Raw |
| [028 时间轴深化](../exploration/DIR-028-timeline-depth/README.md) | 节奏形状、时间邻接、持续存储窗、周期会合、借未来五类新候选；未证明成为新核心范式。 | Raw |
| [029 时间轴铺卡](../exploration/DIR-029-timeline-card-battle/README.md) | 每杖同一完整法术按冷却生成行动牌；默认允许同刻开始、效果同时生效、强力独占、敌方暗牌有线索。明确替代RC1局部约束，独占／同亡／资源同刻交互未定。 | 整体Raw；部分UI Confirmed |
| [030 卡牌规则](../exploration/DIR-030-card-rule-design/README.md) | 当前优先时间轴有限容量、构句可重做。保留十版V01–10及Spark三版；Agent推荐不等于用户选择。 | Raw；未选具体规则 |

DIR-030十版分别是：连续时间拼排、截止时刻、时间邻接、空档蓄力、占空穿插、同刻合奏、单出口错峰、循环时间盘、插队推挤、时间借贷。Spark A按忙碌点穿插、B按防御区间对敌攻刻、C以本段容量换下一段债务；三者的占用、合法性与跨段状态不同，不能混成统一RC1增补。原第一轮拼接匹配保留为历史讨论，已不再是当前核心约束。

## 表现资料与实际证据

| 资料 | 可支持的结论 | 不能支持的结论 |
| --- | --- | --- |
| [TH-001 r1](../development/reports/TH-2026-09-11-001-r1-run-01.md)／[r2](../development/reports/TH-2026-09-11-001-r2-run-01.md) | 冻结Candidate v0.1、两杖六词、C5／L1下726组事件的有限复核；r2登记demo与局部边界。 | 全元素／环境／状态／路线正确，玩家能读懂，完整RC1验收。96刻截止不是正式疲劳规则。 |
| [TH-003](../development/reports/TH-2026-09-13-003-r1-run-01.md) | 单目标几何、两杖、L1、每3刻状态及临时疲劳包的有限实验，并保留规则分支。 | 当前L3满位重试、每刻末状态、多来源、全卡池和完整战场通过。 |
| [CAL r1–r3](../development/reports/CAL-2026-09-13-001-r3-run-01.md) | 训练／留出任务下CalibratedCandidate的限定达标，保留失败修订。 | 参数21／16／5等变成当前PG；普通低损耗自动说明体验平衡；80／120样本终局替代全规则证明。 |
| [RC1验证计划](../design/validation.md)与[冻结输入](../development/inputs/pre-gdd-2026-09-14.md) | V01–20、720单场、20整局切片及U01–08的未来输入／预期。 | 已实跑；这些切片穷举全部合法配置。AUD-010场景先明确结果再作实现／平衡判断。 |
| [主系统09-19视觉](../visual/reviews/2026-09-19/style-guide.md) | 战前配置、计划轴、C／L／起点与实际事件应区分；静态图只作表现参照。 | 图中数字／连线准确即证明结算；旧构图或动画给新权限。01／02图的首轮4／5／7–9／8与UX例一致；05-v2局部刻轴不能替代PG时序。 |
| [DIR-029主UI](../exploration/DIR-029-timeline-card-battle/UI-2026-09-25-timeline-flip-structure.md)／[运动选择](../exploration/DIR-029-timeline-card-battle/UI-2026-09-25-pawn-and-card-motion.md) | 固定两枚敌我棋子、牌列左移、局部点压、共同中轴已在方向内确认；词卡／行动牌／同刻组身份明确。 | 同刻组逐张推进、动画先后规定结算优先级，棋子演出成为战场位移，折叠合成新法术。 |
| DIR-029两份既有研究、v1–v9图稿及提示词 | 研究身份、构图演变、风格参照。11张方向PNG含两张用户参考均已查看；v3／v4紧排与共同时间对齐问题已由UI文字保留。 | 原游戏产品规则全部被核实／视频逐帧看过，图中的示例牌名／刻数成为正式参数，v7／v9候选布局整体已采纳。 |
| [DIR-029动效索引](../development/README.md) | 09-30四刻局部翻牌演示，既有说明／verification.json记录同步、暂停、重播、固定基座及窄窗口等检查。 | 新实跑、战斗结算／真实冷却／独占／构句实现或真人验证。本次仅读两份被索引的证据文件，没有进入外部实现源码。 |

具体FX追踪：当前冷却[018](../effects/entries/FX-018.md)、其他未完成时间[019](../effects/entries/FX-019.md)、隔周期加速[026](../effects/entries/FX-026.md)、完整复诵[033](../effects/entries/FX-033.md)、跳冷却[129](../effects/entries/FX-129.md)。轻巧039、被覆盖后加速056、护甲存续057、生成后加速058、替换成功088、冰甲后缩时090、消耗层加速093及耗尽后缩时095等历史候选由[FX目录](../effects/catalog.md)和各历史来源追踪；有稳定ID不意味着首版可获得或已采纳。

## 一致性结论与本次修订

| 审查项 | 结论／动作 |
| --- | --- |
| 起点、C／L、开始槽与过程并存 | 主系统摘要、SYS-002／003、PG及归一化R23／R24／BR03在核对主题范围内一致。原TS差异保留为历史，没有重写原确认。 |
| 状态、疲劳及旧实验 | ST／RG与PG为当前口径；旧TH／CAL均有冻结输入和限定范围，不能把历史待决项重开为当前缺口或把实验通过升级为RC1通过。 |
| AUD-010 | **Open / DesignClarification**保持：新开始动作与已有持续过程子事件同刻的总先后未唯一确定。后杖赢开始槽、四阶段或R08对象顺序均不足以代替这一裁决。 |
| DIR-029规则差异 | 是主动探索替代规则，整体仍Raw；局部UI确认不消除同刻资源生成／消耗、防护／伤害、打断、同亡与独占边界。保留Unknown，不“修成”RC1。 |
| DIR-030范围 | 用户已把核心转为时间容量，三版推荐与早期匹配记录有各自状态。没有把构句重新当作已选核心，没有跨方向嫁接规则。 |
| 方向数量／导航 | 首页29改30；比较页“27方向索引”改为“全部方向索引”，原27方向比较范围保持。 |
| DIR-014摘要 | 原正文和原始R2只讨论无合法对象候发，旧摘要“取消与有限等候”易暗示救回覆盖。改为准时／晚1／晚3供给对照，明确覆盖／打断不补发；不新增规则。 |
| AUD-008旧问题路径 | 改为layout.1现行`yanzhou/governance/questions.md`，不改原问题Resolved状态。 |
| 来源断链 | 修复6份Draft Change中的17处已唯一对应的相对链接，恢复到同项目现行M／D；历史文字和原始存档不变。逐项见[修订记录](time-axis-review/corrections.json)。 |
| 缺失引用图片 | 09-12第一人称战场来源所指旧兼容jpg在起始工作树缺失，登记为缺口；没有恢复或替换用户文件。它不能补充时间规则或视觉验收。 |

审查结论限于下述可追溯覆盖，不能描述为全部历史文本逐句阅读、全部链接锚点验证、外部代码复核或全部合法组合正确。详细阅读状态、非主题排除及未实跑边界见[coverage](time-axis-review/coverage.md)；检查结果见[verification](time-axis-review/verification.json)。

后续最自然的设计动作仍是按[原最小场景](conflict-register.md#aud-010最小澄清场景)裁决AUD-010，再冻结相应规则验收输入；本次没有替用户选择先后，也没有执行新的玩法实验。
