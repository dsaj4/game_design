# game-002 总控

最后更新：2026-09-05

| 事项 | 状态 |
| --- | --- |
| 工作区 | Active / Idea Qualification |
| 类型、方向、目标玩家 | 用户强调卡组构筑定位，已选择 A 抽弃循环继续细化；正式核心尚未采纳，目标玩家 Unknown |
| 原始想法记录、素材、正式 GDD | 3 / 7 / 0（包含双路线评议与 A 细化草案） |
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

下一步：澄清护甲、燃烧等临时战场状态的战后处理。推荐默认在战斗结束时清除，下一场按起始规则建立状态；[状态清除候选](../game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#当前整体机制评议战场状态的战后清除)仍为 Raw Idea / Unqualified。生命与本局卡组沿用各自已确认规则；恢复途径、固有初始状态、特殊跨战斗效果、具体能力、数值与界面后置。
