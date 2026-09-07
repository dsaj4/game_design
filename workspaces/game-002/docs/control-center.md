# game-002 总控

最后更新：2026-09-07

| 事项 | 状态 |
| --- | --- |
| 工作区 | Active / Numerical Design & Archetype Definition |
| 类型、方向、目标玩家 | 用户强调卡组构筑定位，已选择 A 抽弃循环继续细化；首轮 F01 已明确单人读牌规划与桌面验证场景；正式核心尚未采纳 |
| 原始想法记录、素材、正式 GDD | 7 / 39 / 0（前三份初稿与循环记录，加灵活句式、商店金币、全局收口及基础数值记录；素材均为 Hypothesis） |
| 提案、评估、正式玩法决定 | 无 |
| 原型与代码 | 无 |
| 生产阶段、排期 | 未确定 |

当前材料：[《言咒》初稿与首轮审查](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md)，Raw Idea / Unqualified。

已晋级：[时间预算与施法打断](../game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md)及[时间补牌与多张牌序预览](../game-design-workflow/idea-materials/M-2026-09-05-timeline-draw-preview.md)，均为 Qualified GDD Material / Hypothesis。其余循环规则与干预扩展仍需资格确认。

构句素材：[固定词类与语义兼容](../game-design-workflow/idea-materials/M-2026-09-05-fixed-grammatical-roles.md)，Qualified GDD Material / Hypothesis；确认当前不跨类使用、两层兼容、已有状态的词卡引用要求、引用不自带消耗原则、材料未出现时的提前启动权限及基础版暂不启用独立字数上限，不包含完整语义系统。

澄清进度：用户已确认“火焰 吞噬 护甲”的护甲来源与火焰承受者为同一选定对象；具体数值与其他组合仍待澄清。

当前战斗方向：用户提出直接引入时间轴与施法预算。每轮两句的 agent 建议未采用。Q3 已确认构句暂停、确认施法后推进时间；Q4 已确认预算为距下一次会打断施法的敌方行动所剩时间，不因开始下一句重置；Q5 已确认敌方攻击命中玩家才打断，自我强化、加护甲与召唤本身不打断；Q6 已确认完成后整句结算，打断则整句不生效且时间不退。

Q7 已确认：法术完成与敌方攻击同一时点时，玩家法术先结算，不被追溯打断，敌方攻击不自动取消。已同步时间机制素材。

Q8 已确认：“火焰 吞噬 护甲”完成施法、开始结算时读取目标当前护甲，包含吟唱期间已经发生的护甲变化；实际消耗量与火焰效果仍待澄清。

当前范围：用户要求先确定整体机制，具体卡牌数值后续讨论。Q9 吞噬量及全量消耗建议已后置，未采纳；已有 Q1-Q8 确认保持原有范围。

路线记录：[词汇循环双路线评议草案](../game-design-workflow/idea-inbox/2026-09-05-vocabulary-cycle-alternatives.md)。A 继续细化，B 整套循环暂不推进；用户明确要求在 A 中预留联想、回忆的牌序干预，不自动引入语义继承或 B 的其他规则。

当前候选：[方案 A 词汇卡组循环](../game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md)，整页 Raw Idea / Unqualified，供给与多张预览已局部晋级。基础删牌的本场移除范围已确认，下场按本局卡组恢复参与；具体目标与其余干预规则待确认，无原型、实现或试玩。

最新确认：开战及弃牌洗回时随机洗牌，随后按序抽取，只有明确效果才改变顺序；已同步供给与预览素材。

满手规则：用户要求新牌正常补入，超限后立即选择弃至上限；已同步供给素材，跳过补牌建议未采纳。

最新确认：超限弃牌暂停战斗时间、仅允许弃牌，完成后继续原行动；正在施法不能借此改句、取消或另起施法。已同步素材。

最新确认：普通投入词在施法成功或被打断后均进入弃牌堆，结束不额外补牌；已同步素材，A 草案新增当前循环汇总。

最新确认：投入词确认施法时立即离手进入临时施法区，不占手牌上限且不可用于超限弃牌；已同步素材及普通流程核对。

最新确认：起手至少能用自有词卡组成一条合法基础句，不保证最优解或后续每次补牌成句；已同步素材，保障方法与牌数后置。

最新确认：补牌遇空抽牌堆时洗回当时弃牌，继续本次抽取，不额外耗时；其他牌区不参与，已同步素材。

最新确认：用户确认本场移除也受安全下限约束，不能把仍参与循环的牌数降到下限以下；该约束已复审并同步供给素材，证据仍为 Hypothesis。双空堆跳过补牌建议未采纳。

最新确认：移除量最多执行到安全下限，超出部分不执行，并提前展示实际可移除量；已同步素材，关联收益仍待具体魔法设计。

最新确认：跨洗回预览仅展示当前确定牌序，其后标为待洗回，不提前洗牌，实际洗回后更新序列；已同步素材。

最新确认：同刻依次处理已完成法术及弃牌、敌方行动及打断弃牌、固定补牌及超限弃牌；中间不开放新施法，战斗结束则停止后续流程。已同步两份素材。

最新范围：用户要求“交互界面后续设计，先设计机制”。逐事件等待操作与停点建议为 Parked / Deferred，未采纳；已确认机制保留。

最新确认：目前主谓宾不能混用，有限跨位建议未采纳，固定分类已晋级。

最新确认：谓语能处理宾语、主语能承接谓语结果，两层要求必须同时满足。已扩充构句素材并同步术语；完整类型、具体词义与战场适用条件仍未定。

最新确认：以已有状态为宾语进行操作仍需投入对应宾语卡，制造状态本身不自动获得词卡；已扩充构句素材并同步术语。状态生成、持续与消耗机制尚未随之确定。

最新确认：词卡各自带施法耗时，整句基础耗时为投入词卡耗时之和，汉字数量不直接换算时间；已扩充时间机制素材。整句完成后结算与打断规则保持，具体数值和特殊修正尚未确定。

最新确认：基础版暂不启用独立字数上限，原稿系统保留，待可变句长或修饰词阶段再评估；已扩充构句素材并同步术语，不取消固定句式。

最新确认：战斗之间选择收下的普通新词直接加入本局卡组，基础版不另设每战可免费换入换出的备用词库；已独立晋级为[新词入组素材](../game-design-workflow/idea-materials/M-2026-09-05-new-word-deck-inclusion.md)，Qualified GDD Material / Hypothesis。此次未确认普通奖励的跳过权限、数量、同名副本或永久删牌。

最新确认：用户允许普通战斗后的词卡奖励全部跳过；跳过不把候选词加入本局卡组，也不移除已有词卡，已扩充入组合格素材。具体数量、补偿与特殊奖励规则未定，体验仍待验证。

最新确认：用户确认同名词卡的独立副本，并指定“长期卡组”同名最多三张；承接上一问沿用为本局卡组，已扩充入组合格素材。三张为用户明确约束，未通过平衡测试；满三张后的奖励处理未定。

最新确认：临时复制、删除只影响当前战斗；临时副本战后消失，被本场移除的原有卡下一场按本局卡组恢复，临时变化不写回本局卡组。来源见[持续范围确认](../game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#临时变化持续范围确认记录)，该约束已扩充入组合格素材；完整复制能力仍为 Raw Idea / Unqualified，安全下限保持。

最新确认：临时副本不占本局卡组的同名三张名额，允许使本场同名数量超过三张；已通过 grill-with-docs 复审并扩充入组素材，来源见[超限权限确认](../game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#临时副本超过三张确认记录)。未据此确定复制数量、复制临时副本的权限或具体能力。

最新确认：临时副本默认正常弃置、参与洗回；投入施法成功或被打断后进入弃牌堆，可在本场再次抽到，明确的本场移除效果仍可使其提前退出循环，战后清除。[循环确认](../game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#临时副本正常循环确认记录)已复审并扩充供给素材，证据为 Hypothesis；完整复制能力仍待设计。

范围调整：用户要求“基础复制相关设计留待复制效果相关卡牌出现再讨论”。生成位置、目标、数量、复制链、费用及相关安全余量复核标为 Parked / Deferred；默认置顶建议未采纳，已有持续范围、超限权限及正常循环确认保留，见[后置记录](../game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#复制效果设计后置记录)。

最新确认：敌方行动结束即开始下一次准备，战斗时间轴与固定补牌计时连续；未被打断的法术继续，普通同刻顺序及暂停规则保留。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#敌方行动后时间轴延续确认记录)已扩充[时间素材](../game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md)并同步供给素材，证据为 Hypothesis。

最新确认：敌方准备开始时确定并公开下一次行动及执行时间；准备中仅因明确效果改变，变化须告知玩家。[确认及资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#敌方意图确定与变更确认记录)已扩充时间素材，Qualified GDD Material / Hypothesis。

最新确认：本场战场状态跨施法与敌方行动保留，仅按自身规则或明确效果变化、消失。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#战场状态跨行动保留确认记录)已独立晋级为[状态留存素材](../game-design-workflow/idea-materials/M-2026-09-05-battle-state-persistence.md)，Qualified GDD Material / Hypothesis；该次晋级后素材为 5 份，当前总数见顶部。

最新确认：引用本身不附加消耗，是否消耗或改变状态由具体操作的明确规则决定；词卡弃置不自动消耗对应状态。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#状态引用与消耗关系确认记录)已扩充状态及构句素材，Qualified GDD Material / Hypothesis；具体操作和全量吞噬均未因此确定。

最新确认：满足其他施法条件时，所引用状态尚未出现不统一阻止启动；玩家可提前投入合法词句并开始施法，启动不保证材料如期出现或最终生效。[提前施法确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#提前施法确认记录)已扩充构句素材并同步状态、时间素材，Qualified GDD Material / Hypothesis。

最新确认：当前三词基础句结算时，具体操作必需的状态材料完全缺失则整句落空，普通投入词弃置、已耗时间不返还，结束不额外补牌，也不自动延长施法等待材料。来源与复审见[落空确认](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#必需材料缺失落空确认记录)；已扩充时间与供给素材并同步构句、状态素材，Qualified GDD Material / Hypothesis。材料数量不足、目标失效与特殊触发仍待定，Q8 读取时点范围不变。

最新确认：基础版确认投入词卡、开始施法后，不提供通用主动取消；不能因新牌、改计划或预判材料缺失而随意撤回，构句阶段仍可调整。来源与复审见[权限确认](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#基础版不提供通用主动取消确认记录)，已扩充时间素材并同步供给、构句素材，Qualified GDD Material / Hypothesis；目标失效和外部强制终止等边界仍未定。

最新确认：普通战斗击败全部敌人获胜、玩家生命耗尽则失败。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#普通战斗胜负目标确认记录)已独立晋级为[普通战斗胜负素材](../game-design-workflow/idea-materials/M-2026-09-05-normal-combat-outcomes.md)，Qualified GDD Material / Hypothesis，正式素材共 6 份。终止检查时点、双方同时满足条件及战后衔接仍待定。

最新确认：普通战斗失败即结束当前 Roguelike 一局，继续游玩需重新开局。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#战败结束本局确认记录)已扩充[胜负素材](../game-design-workflow/idea-materials/M-2026-09-05-normal-combat-outcomes.md)并关联本局卡组素材，Qualified GDD Material / Hypothesis；正式素材仍为 6 份。新局资源、局外成长、解锁、存读档和特殊复活规则均未决定。

最新确认：普通胜利不自动回满生命，剩余生命继续保留，恢复途径另行设计。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#普通胜利后生命保留确认记录)已独立晋级为[生命保留素材](../game-design-workflow/idea-materials/M-2026-09-05-post-victory-health-persistence.md)，Qualified GDD Material / Hypothesis；正式素材现为 7 份。

最新确认：战斗中获得的护甲、燃烧等临时战场状态默认在整场战斗结束时清除；本场跨行动留存有效，生命与词卡各自沿用已确认范围。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#临时战场状态战后清除确认记录)已扩充[状态素材](../game-design-workflow/idea-materials/M-2026-09-05-battle-state-persistence.md)，Qualified GDD Material / Hypothesis，素材仍为 7 份。

最新确认：基础版赢下本局终点首领战即通关并结束本局。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#终点首领战通关确认记录)已扩充[胜负与本局结束素材](../game-design-workflow/idea-materials/M-2026-09-05-normal-combat-outcomes.md)，Qualified GDD Material / Hypothesis；素材仍为 7 份。首领战自身的胜负、阶段和其他细则另议。

最新确认：一局途中提供战斗间休整机会，每次恢复生命与改善卡组只能选择一项。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#休整恢复与构筑取舍确认记录)已独立晋级为[休整素材](../game-design-workflow/idea-materials/M-2026-09-05-rest-recovery-deck-choice.md)，Qualified GDD Material / Hypothesis；正式素材现为 8 份。该次确认未决定改善方式；后续已补为随机卡包三选一，见下方。恢复量、机会分布及两项都放弃的权限另议。

最新方向：用户明确“暂时不引入升级，改善卡组设计为从随机卡包中三选一”。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#休整随机卡包三选一确认记录)已扩充休整素材，正式素材仍为 8 份，证据仍为 Hypothesis。卡包提供三张候选词卡，选择一张按既有规则加入本局卡组；同名三张上限和恢复/拿牌互斥继续有效。升级候选为 Parked / Deferred。

最新确认：用户指定先选拿牌或恢复，再开启卡包；开包后可以不拿牌，候选不会开出本局同名已满三张的词。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#休整先选分支开包与候选过滤确认记录)已扩充休整素材并同步入组素材，仍为 8 份 Qualified GDD Material / Hypothesis。开包后拒收不返还已放弃的恢复机会；先公开候选再选分支的建议未采纳。

最新确认：用户对同一卡包三张候选互不重名回答“是”；跨卡包仍可出现本局尚未满三张的已有词。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#同一卡包候选不重名确认记录)已扩充休整素材，同步入组关系与术语，正式素材仍为 8 份，证据状态 Hypothesis。

最新确认：基础版休整卡包主语、谓语、宾语各一张，在各自合格词卡中随机产生。用户回复“确认”，[资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#休整卡包三类各一张确认记录)已扩充休整素材并同步入组关系与术语。类别覆盖不保证语义兼容，仍只能收一张或全部放弃；正式素材仍为 8 份，证据为 Hypothesis。

最新确认：选择休整收益前检查能否组成完整卡包，某类无合格词时本次不提供拿牌、保留恢复。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#休整卡包可用条件确认记录)已扩充休整素材并同步入组关系与术语；不提前公开候选、不自动回血，正式素材仍为 8 份 Qualified GDD Material / Hypothesis。需验证一类满额是否过早限制其他类别获取。

最新确认：选择休整恢复时获得一次有限回血，最多补至当前生命上限，轻伤可补满，具体恢复量后定。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#休整有限生命恢复确认记录)已扩充休整素材并同步生命保留与术语；正式素材仍为 8 份 Qualified GDD Material / Hypothesis，恢复不足影响成长的风险尚未验证。

最新确认（2026-09-06）：下一次休整在流程中的位置提前可知，具体路线和间隔后定。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#休整位置提前可知确认记录)已扩充休整素材并同步生命保留关系与术语；不提前公开卡包候选，正式素材仍为 8 份 Qualified GDD Material / Hypothesis。

最新确认（2026-09-06）：局内采用分叉路线，在分叉处选择下一段路，选择影响后续遭遇与休整安排。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#局内分叉路线确认记录)已独立晋级为[分叉路线素材](../game-design-workflow/idea-materials/M-2026-09-06-branching-run-routes.md)，正式素材增至 9 份 Qualified GDD Material / Hypothesis；具体布局和体验仍待验证。

最新确认（2026-09-06）：选路前公开下一步活动类型，以及战斗的敌人类型与主要机制。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#选路前遭遇信息确认记录)已扩充[分叉路线素材](../game-design-workflow/idea-materials/M-2026-09-06-branching-run-routes.md)，仍为 9 份 Qualified GDD Material / Hypothesis；休整位置预知与开包时点保留，具体敌人数值、界面和远处信息范围后置。

最新确认（2026-09-06）：路线只向前推进，进入遭遇后不可撤回该次选路，完成节点不可回访或重复触发，后续分叉仍可选择。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#路线单向推进确认记录)已扩充[路线素材](../game-design-workflow/idea-materials/M-2026-09-06-branching-run-routes.md)，并同步休整、胜负及术语；仍为 9 份 Qualified GDD Material / Hypothesis。

最新确认（2026-09-06）：每局开局按约束随机确定路线与遭遇安排，本局内保持稳定，正常可选路线可继续通往终点；既有休整与预告规则保持。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#每局路线生成确认记录)已扩充[路线素材](../game-design-workflow/idea-materials/M-2026-09-06-branching-run-routes.md)，并同步休整、胜负及术语，仍为 9 份 Qualified GDD Material / Hypothesis。具体生成分布与平衡后续验证。

最新确认（2026-09-06）：基础版每次新局从同一套预设起始卡组开始，上局构筑不带入。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#新局起始卡组确认记录)已独立晋级为[第 10 份合格素材](../game-design-workflow/idea-materials/M-2026-09-06-preset-starting-deck.md)，证据状态 Hypothesis；具体卡表、数值和重开体验待验证。

最新确认（2026-09-06）：普通战斗词卡奖励复用休整卡包的生成与领取规则，并作为直接开包的独立战后收益。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#普通战斗词卡奖励确认记录)已独立晋级为[第 11 份合格素材](../game-design-workflow/idea-materials/M-2026-09-06-normal-combat-word-rewards.md)，证据状态 Hypothesis；发放频率、额外跳过补偿和特殊奖励未定。

最新确认（2026-09-06）：每次普通战斗胜利后提供一次词卡奖励机会，完整卡包可用时开一包、拿一张或全部放弃；不可用时不提供候选，不自动回血或补偿。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#普通胜利奖励节奏确认记录)已扩充奖励素材，正式素材仍为 11 份，证据 Hypothesis；成长速度与休整价值待验证。

最新确认（2026-09-06）：基础版普通遭遇允许单敌人和多敌人，各自准备并公开下一次行动及时间，共用一条全场时间轴；某敌人行动后只接续自己的准备，不重置其他敌人。补牌仍为同一套固定节拍。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#多敌人独立行动确认记录)已扩充时间素材并同步供给、胜负关系，仍为 11 份，证据 Hypothesis；在场数量、同刻内部先后及实际压力待定或待验证。

最新确认（2026-09-06）：普通敌人被判定击败后，立即取消尚未执行的普通行动，并停止后续准备；其他敌人、玩家施法与补牌在战斗继续时沿用既有规则。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#击败敌人取消行动确认记录)已扩充时间与胜负素材，仍为 11 份，证据 Hypothesis；击败条件、检查时点、已执行效果及特殊触发另议。

最新确认（2026-09-06）：每句法术或每次敌方行动完整结算后立即检查击败与胜负，再处理下一事件；不逐词检查，也不等同刻全部敌人行动后才检查。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#完整行动后检查击败与胜负确认记录)已扩充时间与胜负素材并同步供给，仍为 11 份，证据 Hypothesis；同时满足条件的裁定及特殊检查位置另议。

最新确认（2026-09-06）：普通战斗同一检查点同时满足全部敌人被击败与玩家生命耗尽时，按失败结束本局；不进入普通胜利流程，不追算较早检查已判定胜利后未执行的事件。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#普通战斗同时满足条件时失败优先确认记录)已扩充胜负素材并同步相关引用，仍为 11 份，证据 Hypothesis；特殊战斗和特殊效果另议。

最新确认（2026-09-06）：基础版普通敌人检查时生命耗尽即被击败，无需额外清空护甲或其他状态。[确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#普通敌人生命耗尽即击败确认记录)已扩充胜负素材并同步时间关系，仍为 11 份，证据 Hypothesis。用户同时要求按一个小板块集中对齐问题，已记录[工作区提问方式](../AGENTS.md#提问方式用户更新2026-09-06)。

最新确认（2026-09-06）：用户整组确认 D1-D4，普通直接与持续伤害均等量消耗护甲，溢出扣生命；护甲全挡的攻击仍打断，持续伤害本身不打断。[整组确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#伤害护甲与打断整组确认记录)已独立晋级为[第 12 份合格素材](../game-design-workflow/idea-materials/M-2026-09-06-damage-armor-and-interruption.md)，证据 Hypothesis，已同步时间、状态和胜负关系。

最新确认（2026-09-06）：S1-S5 已整组确认，独立晋级[第 13 份合格素材](../game-design-workflow/idea-materials/M-2026-09-06-status-timing-and-expiration.md)，来源见[整组确认与资格复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#单份周期状态计时与到期整组确认记录)。状态独立计时、完整周期首次触发，同刻状态阶段位于敌方行动后固定补牌前；末次触发先于到期，完全清除取消未来处理，每次完整处理后立即检查。证据 Hypothesis，未执行玩法验证。

最新确认（2026-09-06）：用户确认 R1、R2、R4、R5，与此前修改的 R3 时长相加组成[完整确认](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#同种状态重施与叠加整组确认记录)，独立晋级[第 14 份素材](../game-design-workflow/idea-materials/M-2026-09-06-status-reapplication-and-stacking.md)。同种状态合并、数量按定义叠加、有限剩余时长相加，重施保持周期，部分消耗不刷新，完全清除后重建。证据 Hypothesis，未执行玩法验证。

最新确认（2026-09-06）：用户整组确认 T1-T5，[来源与复审](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#状态读值与同刻内部顺序整组确认记录)已独立晋级[第 15 份素材](../game-design-workflow/idea-materials/M-2026-09-06-status-values-and-resolution-order.md)。周期开始读取当前数量，同刻按首次生效先后及固定平局顺序逐状态处理；重施保位、清除重建重排，周期与到期后分别检查。证据 Hypothesis，未进行玩法验证。

最新确认（2026-09-06）：H1-H4 已完成[整组确认](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#普通敌人被击败后的对象与状态整组确认记录)并独立晋级[第 16 份素材](../game-design-workflow/idea-materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md)。普通敌人被击败后退出施法对象范围，自身状态清除，其他存活对象上的既有状态默认继续；只指向它的单目标在途法术正常完成时落空，先被打断或整场先结束依各自规则。证据 Hypothesis，未进行玩法验证。

最新确认（2026-09-06）：G1-G3 已完成[整组确认](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#基础句的对象选择与锁定整组确认记录)，独立晋级[第 17 份素材](../game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md)。基础句材料与结果归于同一个对象，句义条件内可选自身或普通敌人；构句可改选，确认施法后锁定身份，状态数值仍按具体效果规则读取。证据 Hypothesis，未进行玩法验证。

最新确认（2026-09-06）：E1-E3 已完成[整组确认](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#多敌人同刻行动顺序整组确认记录)并扩充[时间素材](../game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md)。开战在场普通敌人的同刻固定序首次决策前公开，本场保持相对顺序，非同刻仍按时间先后；逐行动检查、击败取消及结束即停止保持。正式素材仍为 17 份，证据 Hypothesis，未进行玩法验证。

最新确认（2026-09-06）：B1-B3 已完成[整组确认](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#施法预算与未知后续行动整组确认记录)并扩充[时间素材](../game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md)。其他条件合法可超预算启动，无已知攻击不等于无限安全；后续新公开攻击按实际时序影响施法，原预算不提供保护或撤回权限。正式素材仍为 17 份，证据 Hypothesis，未进行玩法验证。

最新确认（2026-09-06）：O1-O4 已完成[整组确认](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#战斗开局与初始节拍整组确认记录)，扩充[时间素材](../game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md)及[供给素材](../game-design-workflow/idea-materials/M-2026-09-05-timeline-draw-preview.md)。每场普通战斗重新计时，起手准备不推进时间，开战在场普通敌人从同一起点开始非零首次准备，首张定时牌经过完整间隔后到来；不保证合法起手句能安全完成。正式素材仍为 17 份，证据 Hypothesis，未进行玩法验证。

当前改动（2026-09-07）：新增[基础数值框架 v0.1](../game-design-workflow/idea-inbox/2026-09-07-core-numerical-framework-v01.md)，Raw Idea / Unqualified（参数草案）。完成单敌理想组件的受限算术推演，包括行动节拍、护甲值、击杀阈值、减耗和打断；不是完整战斗原型或玩家测试。正式素材仍为 39 份。

下一步：按参数草案反馈调整初始锚点，落实合法基础词卡并检查真实起手、牌序与多敌人，再推进召唤、状态和道具数值。全局规则继续沿已确认基线，不重新逐项访谈。
