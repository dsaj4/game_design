# TL-1 + INS-1 素材使用审查

Project ID：game-002。文档角色：SourceReview。2026-10-05。当前GDD-0 / 2.1 / processing.2；原RC1审查见[固定版本](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/source-review.md)。

## TL-1当时正式使用（2026-10-01）

以下至第9轮保留原使用记录；当前覆盖范围见后续INS-1、routing.1与processing.1／2章节，旧材料句法和直接资源输出不再作为现行入口。

| 来源 | 资格／采纳 | 用途与限制 |
| --- | --- | --- |
| [DIR-028核心素材](../sources/materials/M-2026-10-01-timeline-production-core.md) | Qualified；确认结构Accepted | 自动产线、有限队列、敌牌倒计时、自动维护恢复、保存与本轮INT边界 |
| [DIR-028新卡表](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/M-2026-10-01-resource-card-pool.md) | Qualified；通用边界局部Accepted，具体内容Proposed | 材料句法等仅按用户答复采纳；13词／4资源／4行动及全部数字没有整包采纳 |
| [P](../sources/proposals/P-2026-10-01-timeline-production-system.md)／[E](../sources/evaluations/E-2026-10-01-timeline-production-system.md)／[D](../sources/draft-changes/D-2026-10-01-timeline-production-core.md) | 正式过程记录 | 结构替代关系、风险、用户授权；不是实验结果 |
| DIR-028第7轮UI与HTML | Raw / Unqualified | 仅展示候选；发布网站不等于采纳页面布局 |

## 旧来源逐类处置

原68份素材与47份inbox的资格、形成过程及原采纳结论保留；本轮不从未读旧inbox抽取新规则。其现行适用性以本表与[逐文件清单](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/reading-log.md)为准，而非文件里的历史“当前”。

| 旧规则来源族 | TL-1处置 | 原因 |
| --- | --- | --- |
| 实体词卡分配、完整法术、同名与实例、词义明确权限 | 有限保留；内容接口重设计 | 仍支持程序配置，不继承旧卡池或副本额度 |
| 目标名单、合法性、已付成本不复制、已成结果不回滚 | 保留原则；己方选目标改为生效时 | 制造成本不能套旧无目标免付；空放已明确 |
| 普通伤害先甲后生命、完整事件终局 | 保留明确基础 | 掉血全杖打断已替代；普通伤害与疲劳分开 |
| 冷却、释放、复诵、开始槽、名义续排 | 由生产／交付／排队／实际顺延替代 | 旧法术过程与新批次不等价 |
| 格子、锚点、宿主距离、邻近脉冲、环境形态 | 退出默认规则，内容重设计 | 用户选择卡牌主战场 |
| 元素本体、火冰层数、镶嵌及53实体 | 保留原设计记录；不列入新版发行池 | 用户要求重新设计卡表 |
| 19节点、三款杖、12场、旧开局与PG值 | 保留历史；新结构下重新评估 | 不能凭旧完整度填充新规格 |
| 路线、休整、商店、单局库存 | TL-32–36补齐路线、库存、节点选择、交易及保存；新参数和可达性重审 | 部分资源跨战引入新的经济关系 |
| 疲劳 | 递增方向再次确认，参数与上界重定 | 不再宣称80／120刻上界适用 |
| 同场开头锁定重播、只读战斗 | 已替代 | 需要保存信息与已提交的战中决策 |
| TH／CAL／Demo及视觉评审 | 原版本证据 | 不证明新机制、卡表或UI成立 |

## 审查深度与尚缺项

已逐页核对现行系统、内容接口、参数与验收；卡表按53实体结构字段审查，历史来源与证据按索引、角色和全文关键词筛查，未把222份全部声称为全文语义复审。每文件的实际覆盖、固定blob与修改／保留理由见reading-log。完整同拍顺序、具体发行池、跨战边界及参数仍Unknown。独立付费干涉能力按用户要求延期。

## 第9轮兼容复用审查

以TL-1提交`ed013948f6c5379fc984413ffd08ae8e7ce0f0c9`继续复核旧Qualified材料的相关规范化章节。[21份直接复用来源表](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/compatible-rules-reuse.md)逐项列出TL-26–37的当前落点和禁止迁入部分；另两份数值／遭遇素材只作边界对照。旧材料页添加当前适用范围，原文保留。没有把68份素材或47份inbox声称为本轮全文重审。

采用用户明确授权合并的兼容条款，通过既有[P/E第9轮](../sources/proposals/P-2026-10-01-timeline-production-system.md)及[新D](../sources/draft-changes/D-2026-10-01-compatible-rules-reuse.md)记录CORE-048。改变的是当前使用范围，不重写原资格或补造原确认。具体阅读覆盖和固定blob见[reading-log第9轮](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/reading-log.md)。

由此补回构句／绑定／修饰、护甲／支付、真实配置、路线／库存／节点经济及保存约束。旧“施法开始”“执行者”“无目标免付”“整包收益”均按新阶段限定，不覆盖材料句法、空放制造损失、资源携带和战中恢复。没有新的发行卡、效果身份、玩法实测或UI采纳。

## INS-1法器铭刻局部复审（2026-10-04）

[DIR-036局部M](../sources/materials/M-2026-10-04-artifact-inscription-core.md) Qualified、[P](../sources/proposals/P-2026-10-04-artifact-inscription-core.md)／[E](../sources/evaluations/E-2026-10-04-artifact-inscription-core.md)与[D／CORE-049](../sources/draft-changes/D-2026-10-04-artifact-inscription-core.md)记录限定采纳。比较输入`a4a7aea8500970ef3504a62e576fc99f08c566db`，逐文件blob与全文／局部覆盖在E；本轮不声称全读历史、其他方向或所有旧候选卡表。

上表及第9轮记录保留当时使用情况；当前适用按以下覆盖：TL-20入口与CORE-041材料—动作—目标已替代；实体占用、耗材分账和卡效绑定继续适用；修饰目的地改为法器辅槽预设；法器直接资源输出退出，高阶材料来源／加工Unknown，资源维护与携带只在内容明确提供时成立。TL-38–45以用户确认结构为来源，不纳入模型推荐或发行例子。

原Qualified卡表保持原资格与历史含义，但完整程序、材料／目标角色与直接资源生产内容须按INS-1复审后才能发行。未更改其原文或声称整池重新合格。原CORE背景不刷新，没有新FX、实验或实现证据。


## 2026-10-04探索退役后的来源状态

用户明确审查后决定删除全部现有方向，测试、UI等信息可后续重做。DIR-001–036的未采纳候选不再进入当前待审清单；上述表格保留原轮次资格与使用事实。DIR-028、036的六份已采纳M/P/E已迁入sources，其原始答复、兼容审查和覆盖记录通过固定Git链接取证。CORE-037–049与现行规则未因清理撤销，未知内容不由旧试点补齐。详情见[清理记录](../governance/cleanup-report.md#2026-10-04探索方向退役)。

## routing.1：敌情、资源优先级与供料调时澄清

[原话与答复](../sources/inbox/2026-10-04-routing-response-clarification.md)中第1–3项及供料调时答复已形成[局部Qualified M](../sources/materials/M-2026-10-04-routing-response-clarification.md)、[E](../sources/evaluations/E-2026-10-04-routing-response-clarification.md)与[CORE-050采纳D](../sources/draft-changes/D-2026-10-04-routing-response-clarification.md)。这是现有机制的限定澄清，沿M→E→D回写，不另作完整新系统提案。

比较输入`b0754e5c08273201f4b04639a371ff2da16cafe6`。使用本轮用户说明、当前系统及其审查，不扩读退役方向或借历史实现补规则；受影响条款为TL-05／06／09／16／23／30及对应展示／验收。所有敌方行动牌Δ＞0；供料去向与优先级可临时调整，只影响未来未承诺批次；规避打断先通过供料间接改未来开工。维护优先、托管、战前争入行顺序与普通队列保留。

第4项关于拥堵是玩家操作后果的意见用于修订AUD-022；其中付费调牌序能力仍Raw / Unqualified，仅保存在inbox，未进入本次Qualified玩法范围。三端不固定物理端口或卡类，“5回合”不固化数值，运转具体配方与资源来源、恢复触发／重叠及额外调时均未决。无Observed玩家证据，全部NotRun。

## processing.1：单一处理耗时与开工预留（2026-10-05）

输入提交`cb5bea76595d3a7bff057a15332f5148effa84c2`。[原话及Q6–8答复](../sources/inbox/2026-10-05-single-processing-time.md#2026-10-05批量确认与晋级)经[Qualified M](../sources/materials/M-2026-10-05-single-processing-time.md)、[E](../sources/evaluations/E-2026-10-05-single-processing-time.md)和[CORE-051 D](../sources/draft-changes/D-2026-10-05-single-processing-time.md)进入现行规则；用户本批明确确认，不重复索取采纳许可。

Include：仅D且整数≥1，取消J／R／独立周期／冷却／S；开工预留所需容量，无位不开工，完工即入行。Replace：旧完工成品滞留与之后争空位的路径；同期入行处理的战前法器序保留。Park／Unknown：预留排位、开工争用与中断释放、具体卡数／Q／D、最早翻开及临时供料恢复。正式范围不包含额外付费干涉或模型未列出的新规则。

实际阅读清单与新增blob见E；此前已读主系统按固定输入复用，增补内容合同与验收相关页，未全量重审旧来源、退役方向、SYS-006或整个GDD包。外部课程仍为研究材料，不作为此生产规则的采纳依据。旧来源与验收按原版本保留，不改原始资格或运行结果。

## processing.2：生产与队列接口（2026-10-05）

输入提交`0c511dd7f8c1e2dda84a65e2b540a2517456771d`。[五项推荐及用户“下一批全部按推荐”](../sources/inbox/2026-10-05-single-processing-time.md#2026-10-05第二批确认与晋级)经[Qualified M](../sources/materials/M-2026-10-05-production-queue-interfaces.md)、[E](../sources/evaluations/E-2026-10-05-production-queue-interfaces.md)和[CORE-052 D](../sources/draft-changes/D-2026-10-05-production-queue-interfaces.md)限定采纳，M→E→D不另建完整P。

Include：S1-Q9／10／11／1／5的容量预留不排牌序、按有效供料优先级联合检查开工、中断释放下拍可用、入行最早下拍翻开、单份临时供料及结束拍恢复。Replace：当前正文中这五项仍为Unknown的表述。Park／Unknown：完整总序、普通离队容量复用、多牌内部关系、到期与新操作受理先后、维护内部顺序、内容及数值。未新增免费撤销、公平轮转、插队或重铭能力。

上节processing.1及原M／E／D保留当轮未决范围，不改写原确认。实际阅读及blob见本轮E；只对相关系统和来源作限定复核，不宣称全量旧素材或完整GDD包重审。课程仍Raw研究输入，未晋级为本规则来源；全部体验与新增验收预期NotRun。

## timing.1：阶段一共同拍序（2026-10-05）

输入提交`dfc844a41f2cd6a9d78d01abafc43b3340745664`。[原推荐与“Q12–14全部按推荐”](../sources/inbox/2026-10-05-stage-one-closure.md#2026-10-05第三批确认与阶段一完成)经[Qualified M](../sources/materials/M-2026-10-05-stage-one-common-timing.md)、[E](../sources/evaluations/E-2026-10-05-stage-one-common-timing.md)和[CORE-053 D](../sources/draft-changes/D-2026-10-05-stage-one-common-timing.md)进入正文，现有局部接口按M→E→D处理。

Include：仅Q12–14的拍末一次开工、a+D、正常空位当拍复用、条件齐备同拍续开／其他材料空位重开、到期—揭示—观察输入关系、基础补给下拍可用与初始库存第0拍可用。Replace：当前正文中对应Unknown。Park／Unknown：复杂总序、维护、多牌内部关系、失效目标与来源死亡、真实内容／参数与UI自动暂停表现。Omit from CurrentSpec：工作包中的临时数值、分析代号和单效果／单张案例限制；它们只用于条件推演，不是发行内容。

八组案例文档复核见E，案例丙入行历史已订正；阶段一交付与未知移交完成，不新增玩法运行证据。前轮M／E／D和本文旧增量保留当时未决范围，当前状态以CORE-053为准。实际读取覆盖与固定blob见E；未全量重审旧素材，不借课程或外部实现替规则作决定。

## enemy.1：阶段二敌情合同与卡面种类（2026-10-05）

输入提交`95c136ed954f70c9d5336552ee5cd30b3e9fcc69`。[阶二Q01–24及各轮答复](../sources/inbox/2026-10-05-stage-two-enemy-pressure.md#2026-10-05第五轮确认与晋级)经[Qualified M](../sources/materials/M-2026-10-05-stage-two-enemy-pressure.md)、[E](../sources/evaluations/E-2026-10-05-stage-two-enemy-pressure.md)和[CORE-054 D](../sources/draft-changes/D-2026-10-05-stage-two-enemy-pressure.md)进入正文，现有接口细化按M→E→D处理。

Include：固定循环时间表与翻开表公开、四类卡面种类与地域变体规则、打断锁定剩余最长施法及落空、单一来源死亡即胜、伤害与打断大类内敌方先结算、危险开工带展示、首版内容约束与表现方向。Replace：TL-13“敌人全灭判胜”、TL-29来源死亡Unknown。Omit from CurrentSpec：候选敌人的具体数值、分析套组和逐拍路线（只作条件推演）。Park：「字身」、三本原卡背、“战前法器序中D最长”目标规则、“工序不止／随身”、特色扩展表中的新规则类形态。神秘学意象出处未核实，不作为规则依据。


## action-framework.1：行动卡与标记通用框架（2026-10-08）

固定输入 `6dd669d6d2ee17d3362a12b029da5d2dec884b27`；用户指定本地未提交主材料完整读取，相关阶段文件局部核对。具体覆盖、三个原件 SHA-256、Q-MARK 既有确认、ACT-Q1／2 本轮答复及冲突处理见 [来源记录](../sources/inbox/2026-10-08-action-card-framework-review.md)。

Include as QualifiedFramework：[局部素材](../sources/materials/M-2026-10-08-action-card-framework.md)中的标记宿主／极性／叠层／上限方向、禁止转移、周期停止、简单条件、独立定时效果和行动读取支付。Inherited：既有生产、队列、目标、护甲、支付与终局 TL 规则。Omit：Raw 卡池、推荐数值、减料增产的辅槽例、未确认事件链和支付优先级。Unknown：同拍总序、复合步骤、期限叠加、上限／溢出、绑定失效与退款。

新增通用内容未成为完整 CurrentSpec；既有条款不因排版迁移重新采纳。示例独立保存并标为说明性推导，不当作实体、默认数值或玩家观察。阶段完成前提不变，本轮没有执行玩法实验或导入外部实现。

## artifact-framework.1：法器系统整理（2026-10-08）

固定输入 `71e7a0a18709e19e85ea171feb10b2ba2b432097`。本轮 CUSTOM 只整理法器五文件及必要接口；已提交来源 blob、局部原输入哈希、实际覆盖和逐类处置见 [法器来源记录](../sources/inbox/2026-10-08-artifact-framework-review.md)。未全读 inbox、GDD 包、其他方向或历史正文。

Inherited：TL-03—07／38／45 保留 Accepted；供料情境移入独立示例。Include as Qualified interface：既有 [辅槽素材](../sources/materials/M-2026-10-08-augment-framework.md)与 [行动／标记素材](../sources/materials/M-2026-10-08-action-card-framework.md)中的生成时间、行动量值、标记协同、足额支付、实际状态与未来预告边界，权威正文仍留相邻系统。Experience：原目标展开为假设与观察方式，全部 NotRun。

Omit：Raw 具体法器／辅槽、减料／虚拟材料、单批多产、压缩预留、开工或完工绕队列收益，以及未确认数字。Park / Unknown：D 的读取及叠加、标记不足分支与退款、同拍消费／兑现顺序、契合形式、多牌内部关系、维护及战终未完成批次材料归属。没有新增玩法资格、P／E／D、CORE 采纳、发行实体或实验结果；框架整理记 DOC-015。

## enemy-framework.1：敌人系统整理（2026-10-08）

固定输入 `a23c75d74187f45f04b50376658be0274049f3f8`。CUSTOM 限敌人五文件、内容合同、必要相邻接口及登记来源；五份未提交输入仅检索和局部选读。实际覆盖、blob、原件哈希与差异见 [敌人来源记录](../sources/inbox/2026-10-08-enemy-framework-review.md)。没有全读 GDD 包、历史或其他探索。

Inherited / Accepted：TL-16、CORE-054 的敌程序、首版内容限制及信息合同。内容页的通用字段与约束归 rules，压力定位、取舍和秘仪炼金方向归 design，行为假设和观察方式归 experience，六组已采纳规则说明归 examples；具体敌人程序表与数值留内容目录，仍为候选 / Illustrative。行动结算、返工和可达性只引用相邻权威。

Include as Qualified interface：既有行动／标记素材中的敌我宿主、正负归属、实有层数与未来预告边界。Omit：Raw 改 Δ、提前取消暗牌、新事件链、由辅槽扩展取消类别、敌方施法成本及 10—15 张敌牌计划。Unknown：真实内容配套、复杂同拍、附属物、其他类子类、定时效果绑定失效和表现布局。未新增 M／P／E／D、CORE 采纳、发行实体或运行证据；文档组织记 DOC-016，体验仍 NotRun。

## augment-framework.1与本轮主系统审查（2026-10-08）

[辅槽局部Qualified素材](../sources/materials/M-2026-10-08-augment-framework.md)已用于通用权限：生产侧只改D、行动侧改明示量值、跨法器以标记协同、完整检查后支付、稀有度表达强弱。旧减料、单批增产、直接跨法器加成和统一三阶不作为新版默认；在当轮审查时D快照、叠加、失败分支和退款仍未决定；后续局部采纳见下方commitment.1。该素材的原资格与用户答复不因本节重新评定或升级。

本轮以`cb8c8b2376cfe217e6d65a128d0fbf9909f83edb`完整阅读69份已跟踪design及相关来源，订正阶段入口、旧Unknown与索引，并评审共享状态和内容风险。逐文件版本、全文／局部范围与排除项见[清理映射](../governance/cleanup-map.json)中的`main_system_audit_20261008`；结论见[审查报告](../governance/main-system-review-2026-10-08.md)。没有全读所有sources、未提交阶段原件或历史正文，没有新增玩法采纳或运行结果。

## commitment.1限定采纳（2026-10-08）

固定输入`830c0b063e62c816fe1abe39c7818787d9c4a089`。本轮沿CUSTOM只读受影响系统、核心／治理与相关来源，未提交阶段原件、历史正文和外部代码不纳入。Include：[本轮M](../sources/materials/M-2026-10-08-batch-freeze-consumption-lock.md)中D冻结与FZ-Q1—5，经E→D以CORE-055局部采纳。旧辅槽／行动M保留历史确认，开工立即扣费表述由本轮限定替代。

Omit：开工立即扣费备选、全库存默认锁定、敌方状态锁定、动态重算D、额外输入窗口与强制逐批确认。Unknown：公式、同拍总序、冻结量上限／失效／战终以及完整定时保存。本轮没有发行内容或实验，其他Qualified结构不整体提升。

## time-formula.1耗时公式与外部参照（2026-10-08）

固定言咒输入`614a6e2dd48cfbb4894bfed8a4669703f0004553`，CUSTOM限定相关时间／支付接口与治理。用户明确指定外部本地目录，实际只读SlayTheSpire2恢复工程的局部数值／Buff逻辑，哈希与覆盖见[参考摘要](../../media-analysis-lab/runs/2026-10-08-sts2-numeric-reference/README.md)。未复制第三方代码或资产，未运行／修改外部工程；这不是言咒实现或正式发行版验证。

Include：[本轮M](../sources/materials/M-2026-10-08-processing-time-formula.md)，经E→D以CORE-056采纳。采用先加后乘及有效倍率连乘；向上取整、最低1拍和无收益费用规则是授权内的本项目适配。Omit：助手中途提出的百分比加算方案、把所有Buff层数当乘方、外部遗物／卡池／上限／时长规则。普通行动量值仍沿自己的合同；内容参数、同拍总序和生命周期不被公式代定。
