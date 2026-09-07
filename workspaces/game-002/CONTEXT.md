# game-002 领域词汇

本词汇表记录构思澄清中已明确的术语，不代表整份初稿已经晋级或核心玩法已采纳。共享流程名词见[仓库词汇](../../CONTEXT.md)。

2026-09-06：[本轮改动](game-design-workflow/idea-inbox/2026-09-06-flexible-grammar-and-spell-types.md)调整句式与卡牌位置，并引入多法术类型。SG1-SG5、FG1-FG5、ST1-ST6、SL1-SL6、SH1-SH6、SC1-SC6、SN1-SN5 和 SR1-SR6 已分别通过资格确认；旧分类、对象及卡包术语保留相应范围，WC1-WC5 已明确名动词性与卡包适配，OH1-OH5 已明确开局保障，SM1-SM3 已明确整句效果与词义复用，PA1-PA3 已明确防护状态与生成，ER1-ER3 已明确效果修正归属与读取，PS1-PS3 于 2026-09-07 明确周期状态的强化继承，GI1-GI3 已明确全局道具的基础持有与生效，道具同种持有上限已于 2026-09-07 由 MQ2 独立补齐，道具奖励方式已由 GR1-GR4 独立补齐，初始资源已由 NR1-NR3 明确，首轮剩余全局建议集中在收口确认包中等待确认。

## Language

**新局初始资源**：

基础版每次新局以同一预设基础生命上限、满生命、零金币、无初始全局道具开始；不继承旧局剩余生命或上限变化。与既有预设起始卡组共同构成起点，同局普通胜利与休整仍按原规则处理。来源见[NR1-NR3](game-design-workflow/idea-materials/M-2026-09-07-new-run-starting-resources.md)。
_Avoid_：与每战重置生命、已完成初始卡表平衡或自动采纳全局收口候选混称。

**战斗道具奖励机会**：

本局终点前少数预设战斗首次有效胜利后的额外免费道具选择，选路前标明下一步战斗是否具备该机会。最多三个不同种未持有候选，领一件或全部拒收；不足提供实际候选，空池或拒收不重抽、不保留、不额外补偿。来源见[GR1-GR4](game-design-workflow/idea-materials/M-2026-09-07-combat-item-rewards-and-settlement.md)。
_Avoid_：与每战必发、逐敌人发放、替代原有金币词卡或拒收自动补金币混称。

**战后奖励处理顺序**：

同次胜利先金币，再完成该节点原有词卡奖励，最后生成并处理适用道具候选；不适用环节跳过。新道具按取得后条件生效，不追溯此前收益或补触发刚结束战斗的事件。来源同[GR4](game-design-workflow/idea-materials/M-2026-09-07-combat-item-rewards-and-settlement.md)。
_Avoid_：与界面必须逐屏点击、词卡拒收就停止全部奖励、新道具只能下一战生效或未定义的领取连锁混称。

**独立商店节点**：

占一次路线推进的非战斗购物节点，不附带自动回血、免费词卡或战斗收益；交易后继续后续路线，不并入休整的恢复、拿牌分支。来源见[MN1-MN4](game-design-workflow/idea-materials/M-2026-09-07-shop-nodes-and-spending-opportunities.md)。
_Avoid_：与战后免费附加商店、休整第三选项或无机会成本的成长混称。

**商店位置预知与可选机会**：

选路前知道各分支下一次可达商店的位置，或后续已无商店；具体商品到店才公开。尚未获得购物机会的正常通关路线在终点前至少提供一次可选商店，之前安排能取得金币的战斗；主动绕过不保证补发。来源同[MN 素材](game-design-workflow/idea-materials/M-2026-09-07-shop-nodes-and-spending-opportunities.md)。
_Avoid_：与强制到店、全图公开、别处不可达商店也算机会或绕过后动态改图混称。

**首次基础购买力目标**：

首次商店前保留固定战斗收入、且仍有合格基础商品时，无需耗时奖金也应能负担一次基础购买的设计目标；以预设收入、间隔、商品池与价格配合，尚未验证。来源同[MN4](game-design-workflow/idea-materials/M-2026-09-07-shop-nodes-and-spending-opportunities.md)。
_Avoid_：与按当前余额改价、保证买到适配商品、所有商品都买得起或空池必补货混称。

**商店商品资格与类别名额**：

同店普通词卡不重名、道具种类不重复，排除本局同名满三张的词与当前已持有道具；词卡和道具各有预设名额，具体数量后定，不保底名动覆盖或流派适配。某类不足就少提供，其他类不补位，两类空时无商品、可离开且无额外补偿。来源见[MQ1-MQ4](game-design-workflow/idea-materials/M-2026-09-07-merchandise-eligibility-and-item-limits.md)。
_Avoid_：与免费奖励必须完整卡包、余额不足就刷新商品或跨店禁止词卡副本混称。

**道具同种单件上限**：

基础版同种道具同时最多持有一件，各获取途径均遵守；商店生成和成交分别检查当前持有，不以重复购买升级或叠加。同种按身份判断，曾经持有但现已失去不自动永久禁售，仍须满足当次资格。来源同[MQ 素材](game-design-workflow/idea-materials/M-2026-09-07-merchandise-eligibility-and-item-limits.md)。
_Avoid_：与全部道具合计只能一件、词卡三张额度、已有道具必须装备或把商店规则自动当作战斗奖励规则混称；战斗奖励由 GR 独立明确。

**商店货架**：

每家商店首次到访时随机生成的公开单张词卡与具体被动道具集合，本次商品与标价固定，每个条目售一份，售出不补货，基础版不提供刷新或随机卡包。来源见[MS1-MS5](game-design-workflow/idea-materials/M-2026-09-07-shop-shelves-and-transactions.md)。
_Avoid_：与整店三选一或必定适配当前构筑混称；同店不重名和道具单件分别由 MQ 补齐，库存与持有上限分别判断。

**商店购买与离开**：

一次到访可连续购买合格且金币足额的商品，成功才扣款并取得；买词即入本局卡组并受三张额度约束，买道具沿 GI 持有。可不买离开，剩余金币保留，不能回访补买，基础商店不提供出售、退款或付费删牌。来源同[商店素材](game-design-workflow/idea-materials/M-2026-09-07-shop-shelves-and-transactions.md)。
_Avoid_：与离开返还货款、买入即保证起手、免费奖励被购物替代或已确认商店节点分布混称。

**本局金币**：

用于本局商店购买词卡与道具的货币，跨战斗、休整和商店累积，本局结束不带入下一局；初始金币已由 NR2 独立确认为零。来源见[EC1-EC4](game-design-workflow/idea-materials/M-2026-09-07-combat-gold-and-efficiency-bonus.md)。
_Avoid_：与施法费用、跨局存款或依据货币范围推定全部商店资格规则混称。

**战斗基础金币与耗时奖金**：

每个战斗节点首次有效胜利后结算一次该遭遇预设基础金币加有上限、最低为零的耗时奖金；基础金币不随久战扣减，奖金按遭遇预设效率基准计算，不随玩家当前构筑临时抬高基准。来源同[金币素材](game-design-workflow/idea-materials/M-2026-09-07-combat-gold-and-efficiency-bonus.md)。
_Avoid_：与逐敌人发奖、所有遭遇同额、拒收词卡补偿或每缩短任意微小时间都增加金币混称。

**金币奖励计时**：

从本场起点到有效胜利判定的一份实际战斗时间轴经过时间，含施法、等待与打断前已花时间，排除暂停期间的现实思考时间；并行敌方准备不重复相加。来源同[金币素材](game-design-workflow/idea-materials/M-2026-09-07-combat-gold-and-efficiency-bonus.md)。
_Avoid_：与现实操作速度、仅成功法术耗时之和或敌人数乘以经过时间混称。

**全局道具的本局持有**：

道具作为被动构筑物，不参与抽弃牌、不占手牌或句子位置，无需额外装备，持有期间按条件生效；战中不提供主动开关、卸下或丢弃。本局跨战斗与休整保留，直到明确移除或本局结束，不自动带入下一局。来源见[GI1-GI3](game-design-workflow/idea-materials/M-2026-09-07-global-item-ownership-and-passive-effects.md)。
_Avoid_：与持有即无条件触发、上场临时产物跨战继承、同种道具无限叠加或道具内部进度全部保留混称。

**周期状态的施加量强化**：

明确适用于本次状态施加数量的源方修正，在施法结算时计入新增数量，再与已有同种状态合并；源方后续变化不追溯重算旧量，周期读取当前量且不重复计入该增幅。来源见[PS1-PS3](game-design-workflow/idea-materials/M-2026-09-07-periodic-state-modifier-inheritance.md)（2026-09-07）。
_Avoid_：与所有伤害加成都增加层数、每批状态独立保留倍率、固定初始周期数量或来源离场使宿主状态永不清除混称。

**源方自身效果修正**：

明确影响执行者产生效果的强化或削弱；默认玩家与非单位载体采用玩家自身的适用修正，召唤物执行时采用该单位自身的适用修正，双方不自动互相继承。来源见[施法效果的来源与修正](game-design-workflow/idea-materials/M-2026-09-06-spell-effect-sources-and-modifiers.md)。
_Avoid_：与材料来源、受术者防御、全局道具、击杀或状态来源奖励归因混称。

**本句源方强度读取**：

法术完成、开始结算整句时读取适用的源方效果强度修正，本句结算中保持这份读取；来源同[ER3](game-design-workflow/idea-materials/M-2026-09-06-spell-effect-sources-and-modifiers.md)。
_Avoid_：与确认施法时计算耗时、冻结战场材料数量或周期效果的全部属性继承混称。

**战斗胜利**：
普通战斗中，检查时全部敌人已被击败且玩家生命未耗尽所对应的本场结果。来源见[普通战斗胜负素材](game-design-workflow/idea-materials/M-2026-09-05-normal-combat-outcomes.md)；普通法术、敌方行动或一次状态周期效果、到期处理完整结算后立即检查，普通战斗同时满足胜负条件时失败优先已确认，普通敌人检查时生命耗尽即被击败已确认，首领等特殊击败规则与特殊检查位置仍待明确。
_Avoid_：与单句施法成功、整局通关或自动获得奖励混称。

**战斗失败**：
普通战斗中，玩家生命耗尽所对应的本场结果，并触发当前 Roguelike 一局结束。来源同[胜负素材](game-design-workflow/idea-materials/M-2026-09-05-normal-combat-outcomes.md)。
_Avoid_：与单句被打断或材料缺失落空混称，或据此推定局外进度损失。

**普通战斗失败优先**：
普通战斗在同一检查点同时满足全部敌人被击败与玩家生命耗尽时，按失败结束本局，不进入普通胜利流程。来源见[失败优先确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#普通战斗同时满足条件时失败优先确认记录)。
_Avoid_：与同刻事件先后、合并同刻全部行动或首领战特殊裁定混称；较早检查已判定普通胜利后，不追算未执行的后续伤害。

**本局结束**：
当前 Roguelike 游玩流程的终止；已确认普通战斗失败会触发，继续游玩时重新开局；基础版赢下本局终点首领战则通关并结束本局。来源见[胜负与本局结束素材](game-design-workflow/idea-materials/M-2026-09-05-normal-combat-outcomes.md)。
_Avoid_：与单句结束、本场移除或所有永久进度清除混称。

**局内分叉路线**：

一局途中供玩家在分叉处选择下一段路的推进结构，选择影响后续遭遇与休整安排；让当前生命、本局卡组和已知休整位置参与取舍。来源见[分叉路线素材](game-design-workflow/idea-materials/M-2026-09-06-branching-run-routes.md)。
_Avoid_：与每战免费换牌、全图公开或可随意回退重选混称；普通推进的回退与回访限制已由下方单向推进术语明确；具体布局及超出基础预告的信息范围仍待定。

**路线单向推进**：

基础版进入一次遭遇后不能撤回该次选路，完成后只能从当前位置允许的后续路线继续，不能回访或重复触发已完成节点，包括其中的战斗、休整和奖励；后续遇到新分叉仍可按当前处境选择。来源见[单向推进确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#路线单向推进确认记录)。
_Avoid_：与开局锁定全程路径、查看预告即进入遭遇混称；特殊效果、存读档和具体进入交互未因此确定。

**每局路线生成**：

每局开局按预设约束随机确定路线连接与遭遇分布，并在本局内保持稳定，不因查看、等待或改选尚未进入的路线而刷新；正常可选的前进路线能够继续通往终点，既有休整及预告规则继续有效。来源见[每局生成确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#每局路线生成确认记录)。
_Avoid_：与全图公开、开局锁定全程选路、每局绝不重复或冻结敌人行动及牌库循环混称；具体生成与难度分布约束未定。

**选路前遭遇预告**：

选择路线前公开各条可选路线下一步的活动类型；下一步为战斗时，同时公开敌人类型与主要机制，用于判断当前卡组是否适合。来源见[遭遇信息确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#选路前遭遇信息确认记录)。
_Avoid_：与精确阵容、完整行动序列、全图公开或提前查看休整卡包混称；下一次休整位置预知仍按既有范围生效。

**终点首领战**：
本局最后的目标战斗；基础版赢下该战斗即通关并结束本局。来源见[终点通关确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#终点首领战通关确认记录)。
_Avoid_：与途中首领战或首领的单个阶段混称，或由此推定每局首领身份固定及战斗细则已确定。

**本局通关**：
基础版赢下本局终点首领战后，对当前一局成功完成的判定；判定后本局结束。来源同[胜负与本局结束素材](game-design-workflow/idea-materials/M-2026-09-05-normal-combat-outcomes.md)。
_Avoid_：与普通单场胜利、局外解锁或自动获得通关奖励混称。

**战后生命保留**：
普通战斗获胜后，剩余生命继续进入后续流程、胜利本身不自动回满的原则；恢复途径另行设计。来源见[生命保留素材](game-design-workflow/idea-materials/M-2026-09-05-post-victory-health-persistence.md)。
_Avoid_：与护甲或燃烧等其他状态继承混称，或认为下一场生命不能被明确效果改变。

**战斗间休整**：
当前一局途中提供的、位于战斗之间的准备机会；恢复生命与改善卡组在同次休整中互斥，选择一项即放弃另一项。来源见[休整素材](game-design-workflow/idea-materials/M-2026-09-05-rest-recovery-deck-choice.md)。
_Avoid_：与每战自动回血、普通词卡奖励或随时可用的恢复能力混称；位置、频率、恢复量与未选分支时直接跳过休整的权限尚未确定。

**休整位置预知**：

玩家在进入通往下一次休整的战斗段前，知道该次休整在局内流程中所处位置的信息规则；具体路线和间隔后定，来源见[位置预知确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#休整位置提前可知确认记录)。
_Avoid_：与卡包内容预览、全局地图公开或固定布局混称，或理解为可以提前使用休整。

**休整恢复分支**：

选择本次休整的恢复收益，获得一次有限生命补充，最多补至当前生命上限，轻伤可以补满；不保证每次清除全部累计损耗。具体恢复量与计算公式后定，仍与本次拿牌互斥。来源见[有限生命恢复确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#休整有限生命恢复确认记录)。

_Avoid_：理解为每次必定回满、必须始终留有伤势，或在同次休整反复回血；满生命时能否选择恢复尚未决定。

**休整构筑分支**：
先选择拿牌并放弃本次恢复机会，随后开启随机卡包；可以收下一张候选加入本局卡组，也可以全部放弃，放弃不返还恢复机会。来源同[休整素材](game-design-workflow/idea-materials/M-2026-09-05-rest-recovery-deck-choice.md)。
_Avoid_：将拿牌等同于必然增强；升级暂不引入，永久删牌或换牌未因此获得采用。

**休整随机卡包**：
选择拿牌后才开启的三候选卡包：一个随机名词、一个随机动词及一个剩余合格随机词，三个名称不同，排除本局同名满三张的词与单位绑定临时关联卡；跨包可出现未满额已有词。来源见 [WC1-WC5](game-design-workflow/idea-materials/M-2026-09-06-word-classes-and-reward-packs.md)，词池权重、稀有度及重抽规则后定。
_Avoid_：理解为三个卡包选一个、一次拿走三张候选，或将类别覆盖等同于语义兼容；同包不重名不禁止跨卡包收集副本，休整候选规则不自动推广到所有获取场景。

**休整拿牌可用条件**：

过滤后至少有三个不同名合格词，名词、动词各至少有一个，才能生成完整卡包。休整在选收益前检查，不提前公开候选；不可用时仅保留恢复分支，不自动回血。来源见 [WC3](game-design-workflow/idea-materials/M-2026-09-06-word-classes-and-reward-packs.md) 及[休整素材](game-design-workflow/idea-materials/M-2026-09-05-rest-recovery-deck-choice.md)。

_Avoid_：与候选不喜欢或语义不兼容混称；不以不完整卡包、跨类或满额词补位，不自动获得重抽或补偿。

**休整开包后拒收**：
选定拿牌分支并开启卡包后，一张候选都不收下的选择；本局卡组不增减，已放弃的恢复机会不返还。来源见[开包与过滤确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#休整先选分支开包与候选过滤确认记录)。
_Avoid_：与改选恢复、未选分支时直接跳过休整、重抽或补偿混称。

**普通战斗词卡奖励**：
每次普通胜利提供一次独立词卡奖励机会：可用时直接公开符合 WC 的三张候选，拿一张或全部放弃；无法组成完整包则不提供候选，不自动回血或补偿，不占休整选择。来源见[普通奖励素材](game-design-workflow/idea-materials/M-2026-09-06-normal-combat-word-rewards.md)与[词性卡包素材](game-design-workflow/idea-materials/M-2026-09-06-word-classes-and-reward-packs.md)。
_Avoid_：与卡包不可用时强行发牌、强制入组、逐个敌人发奖或先选收益再开包的休整流程混称；额外跳过补偿和特殊奖励尚未确定。

**词卡奖励跳过**：
普通战斗后不收下任何候选词卡的选择；该次候选词不加入本局卡组，也不移除已有词卡。来源见[跳过确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#普通词卡奖励跳过确认记录)，普通奖励的候选及领取数量已由[普通奖励素材](game-design-workflow/idea-materials/M-2026-09-06-normal-combat-word-rewards.md)独立补齐，额外跳过补偿与特殊奖励规则未定。
_Avoid_：与战斗中的超限弃牌、本场移除或永久删牌混称，或认为跳过自动提供重抽和其他收益。

**预设起始卡组**：
基础版每次新局开始时使用的同一套词卡集合，上局构筑和局内获得的词卡不带入；具体卡表后定。来源见[起始卡组素材](game-design-workflow/idea-materials/M-2026-09-06-preset-starting-deck.md)。
_Avoid_：与固定起手牌、固定牌序、当前本局卡组或局外收藏混称；不据此推定生命及其他资源的重置。

**本局卡组**：
一局 Roguelike 中跨战斗保留的词卡集合，本轮所称“长期卡组”依上一问上下文沿用此义，同名词卡最多三张。战斗之间选择收下的普通词直接加入其中，本场移除不改变其成员归属，临时复制也不增加其成员，且不另设每战免费换牌的备用词库，来源见[新词入组素材](game-design-workflow/idea-materials/M-2026-09-05-new-word-deck-inclusion.md)。
_Avoid_：与当前手牌、抽牌堆或可自由配置出战子集的收藏库混称，或把加入卡组等同于立即抽到。

**同名词卡副本**：
同一普通词卡的独立份数，各张沿用相同的词类与规则，分别按既有流程抽取、投入与弃置。本局卡组同名最多三张；临时副本仅限本场，允许使本场同名数量超过三张，来源见[副本与上限确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#同名副本与三张上限确认记录)及[临时副本权限确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#临时副本超过三张确认记录)。
_Avoid_：与自动升级、合成或单张卡无限调用混称，或将同名三张理解为每个牌区各有三张名额。

**临时词卡副本**：
由复制效果产生的本场词卡，默认正常弃置并参与洗回，明确的本场移除效果可使其提前退出循环，战后消失；其不成为本局卡组成员，不占同名三张名额，允许使本场同名数量超过三张。来源见[持续范围确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#临时变化持续范围确认记录)、[超限权限确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#临时副本超过三张确认记录)与[循环确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#临时副本正常循环确认记录)；复制对象、初始进入位置与费用待相关卡牌出现后讨论，见[后置记录](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#复制效果设计后置记录)。
_Avoid_：与通过普通奖励收下的独立副本或指向具体单位的召唤关联卡混称，或将“仅限本场”理解为“使用一次即消失”。

**固定词类（旧版约束）**：
旧版将词卡固定分为主语、谓语、宾语，并禁止跨位；2026-09-06 用户提出同一卡可用于主语和宾语后，这项限制已被新方向替代。历史来源见[固定词类素材](game-design-workflow/idea-materials/M-2026-09-05-fixed-grammatical-roles.md)，新方向见[本轮改动](game-design-workflow/idea-inbox/2026-09-06-flexible-grammar-and-spell-types.md)。
_Avoid_：继续用旧禁令排除新版跨位用法，或从放开跨位推定所有词在所有位置都合法。

**词性与句法角色**：
词性描述词本身的类别；基础版为名词、动词，每张卡固定属于一类。句法角色描述它在具体句子中的作用，同一卡可按词义用于主语或宾语，每张实际投入卡只占一个出现位置。来源见[基础句式素材](game-design-workflow/idea-materials/M-2026-09-06-flexible-sentences-and-subject-roles.md)与[WC1](game-design-workflow/idea-materials/M-2026-09-06-word-classes-and-reward-packs.md)；其他词性与逐词兼容范围后定。
_Avoid_：把主语、宾语继续当作互斥词性，或把角色复用等同于多出一张实体卡。

**基础省略句**：
当前支持的“动词 + 名词”句式，省略显式主语，以玩家为默认执行者；具体合法性仍取决于词义和战场条件。来源见[基础句式素材](game-design-workflow/idea-materials/M-2026-09-06-flexible-sentences-and-subject-roles.md)。
_Avoid_：与任意省略、任意语序或无组件施法混称。

**默认执行者**：
合法省略主语句中由语义补全的玩家“我”，不要求持有或投入实体“我”卡，也不取得未投入卡牌的专属效果；玩家已有状态与适用全局道具照常生效。来源同[基础句式素材](game-design-workflow/idea-materials/M-2026-09-06-flexible-sentences-and-subject-roles.md)。
_Avoid_：与免费实体主语卡或取消玩家全部已有能力混称。

**显式主语**：
“名词 + 动词 + 名词”中实际投入、按词义指定执行者或作用载体的首个名词；承担自身卡牌耗时。来源同[基础句式素材](game-design-workflow/idea-materials/M-2026-09-06-flexible-sentences-and-subject-roles.md)。
_Avoid_：与所有法术的受术目标或统一结果容器混称。

**宾语与受术目标**：
宾语提供动词直接处理的内容，受术目标是结果作用的对象；当前基础句需要另选时，至多选一个符合词义的玩家、己方有效召唤物或存活普通敌人，宾语已指明受术者时不再另选。来源见 [FG3](game-design-workflow/idea-materials/M-2026-09-06-flexible-sentences-and-subject-roles.md) 及 [SR3](game-design-workflow/idea-materials/M-2026-09-06-summon-word-references-and-target-locking.md)。
_Avoid_：将宾语位置等同于最终受术目标，或据此推定任意跨对象权限。

**法术类型**：
依据整句特征形成、可被全局道具识别且可以并存的类别；构句时条件可知，确认施法时固定，普通施法期间不变。来源见[类型与道具触发素材](game-design-workflow/idea-materials/M-2026-09-06-spell-types-and-item-triggers.md)。
_Avoid_：与词性、单词语义属性或互斥职业混称。

**简易法术**：
合法句式省略显式主语所具有的类型，系统补默认“我”后仍保留；实际投入显式主语后不满足该条件，也可同时满足其他类型。来源见[ST1](game-design-workflow/idea-materials/M-2026-09-06-spell-types-and-item-triggers.md)，例如“获得 护甲”，基础防护术语按后续 [PA1](game-design-workflow/idea-materials/M-2026-09-06-armor-identity-generation-and-persistence.md) 统一。
_Avoid_：把省略主语理解为没有语义上的执行者，或把按实际卡牌相加的基础耗时误作固定折扣及强度结论。

**召唤法术**：
包含召唤操作，或具体召唤物直接作为执行者、被操作对象参与的法术类型；“召唤 恶魔”“强化 恶魔”同时属于简易和召唤，“恶魔 释放 火焰”属于召唤。来源见[ST2](game-design-workflow/idea-materials/M-2026-09-06-spell-types-and-item-triggers.md)；单凭场上存在召唤物或词名字样不能使无关法术归类。
_Avoid_：与每次都生成新单位混称，或认为场上有召唤物就使所有法术自动属于召唤类。

**道具类型匹配**：
道具依据某次法术的类型满足适用条件；同一项“简易或召唤”条件双命中仍只匹配一次，兼具条件须全部满足，不同道具分别检查。来源见[ST4](game-design-workflow/idea-materials/M-2026-09-06-spell-types-and-item-triggers.md)。
_Avoid_：与效果已经发生、多个真实事件合并或所有道具统一相乘混称。

**成功施法奖励**：
以法术成功结算为条件的道具收益，被打断或整句落空不触发，合法零伤害不因此算失败；耗时等施法参数修正在确认时计算，特殊开始或失败触发须明示。来源见[ST5](game-design-workflow/idea-materials/M-2026-09-06-spell-types-and-item-triggers.md)。
_Avoid_：把类型固定、完成计时或存在适用道具等同于成功奖励已获得。

**实际召出单位**：
法术确实生成了召唤单位的事件，与“召唤法术成功结算”分开判断；强化现有单位不满足此事件条件。来源见[ST6](game-design-workflow/idea-materials/M-2026-09-06-spell-types-and-item-triggers.md)，具体生成数量及计次方式后定。
_Avoid_：把所有召唤类型法术都当成新单位生成。

**召唤种类词**：
指明新召唤种类、也可按动词含义引用一只己方有效同种单位的普通词卡；新召唤、强化或指挥均须满足对应词义，引用不改变其普通卡身份或本局归属。来源见 [SG2](game-design-workflow/idea-materials/M-2026-09-06-summoned-unit-reference-card-cycle.md)、[SC2](game-design-workflow/idea-materials/M-2026-09-06-summon-reference-generation-and-hand-entry.md) 及 [SR1-SR6](game-design-workflow/idea-materials/M-2026-09-06-summon-word-references-and-target-locking.md)。
_Avoid_：与召唤完成后生成的单位及指向单位的临时卡混称。

**种类词的本句引用**：
普通种类词在构句中选择一个有效同种单位、确认施法时为本句固定的指向；它不使卡变成永久绑定的关联卡，单位离场也不清理该普通词。来源见 [SR2、SR4、SR6](game-design-workflow/idea-materials/M-2026-09-06-summon-word-references-and-target-locking.md)。
_Avoid_：与一词指向全体、召唤新单位或专属关联卡改绑混称。

**召唤关联卡**：
每个实际新召出的基础单位所对应的一张专属临时卡，指向该具体单位，可用于强化、指挥等合法操作而不能作为新召唤种类材料；进入普通手牌并参与弃置洗回，不加入本局卡组或占其同名三张额度。循环依据见 [SG1-SG5](game-design-workflow/idea-materials/M-2026-09-06-summoned-unit-reference-card-cycle.md)，生成入手见 [SC1-SC6](game-design-workflow/idea-materials/M-2026-09-06-summon-reference-generation-and-hand-entry.md)，离场与战后清理见 [SL1-SL6](game-design-workflow/idea-materials/M-2026-09-06-summon-departure-and-reference-invalidation.md)。
_Avoid_：与本局原有种类词、普通临时复制品或场上单位本身混称，或把卡被弃置等同于单位消失。

**关联卡直接入手**：
本次召唤完整结算并完成击败及胜负检查后，战斗继续且新单位仍在场时，将它的关联卡加入普通手牌；生成不改变抽牌堆和固定补牌进度，超限则立即暂停弃至上限，再继续同刻事件。来源见 [SC3-SC5](game-design-workflow/idea-materials/M-2026-09-06-summon-reference-generation-and-hand-entry.md)。
_Avoid_：与抽牌、施法结束补满、生成原种类词副本或立即开始新施法混称。

**召唤指令**：
玩家通过组织句子让基础召唤物执行动作的方式，相关施法共用玩家的时间投入；基础单位不自行发起攻击。来源见[召唤基础循环](game-design-workflow/idea-materials/M-2026-09-06-summoned-unit-reference-card-cycle.md)中的 SG5。
_Avoid_：与召唤后自动获得额外行动、独立准备时间轴或随时免费调用关联卡混称。

**基础召唤与同种共存**：
一次基础召唤成功产生一个独立单位，同种单位可以共存；每只分别保有生命、护甲、状态和专属关联，重复召唤不合并、刷新或治疗旧单位。来源见 [SN1-SN2](game-design-workflow/idea-materials/M-2026-09-06-summon-coexistence-and-field-capacity.md)。
_Avoid_：与同名卡副本、群体指挥或额外自主行动混称。

**召唤物场上容量**：
玩家基础召唤物共用的在场总上限，每只占一个名额，实际离场时释放；关联卡在何牌区或是否弃置不影响占用。来源见 [SN3](game-design-workflow/idea-materials/M-2026-09-06-summon-coexistence-and-field-capacity.md)，具体上限数字后定。
_Avoid_：与手牌上限、本局同名三张、删牌安全下限或场上格位混称。

**召唤容量检查**：
基础召唤在确认施法时要求有真实空位，满员不能启动且不会自动替换旧单位；启动不预占名额，结算时无空位则整句落空，普通词弃置且时间不返还。来源见 [SN4-SN5](game-design-workflow/idea-materials/M-2026-09-06-summon-coexistence-and-field-capacity.md)。
_Avoid_：把预计单位将离场视为当前已有空位，或把普通状态材料可提前等待推广为满员召唤许可。

**基础召唤物存在范围**：
玩家召唤的基础单位默认持续存在于本场，没有通用自动倒计时；明确离场或战斗结束时清除，单位及临时关联卡不跨战斗。来源见[SL1](game-design-workflow/idea-materials/M-2026-09-06-summon-departure-and-reference-invalidation.md)，生命承伤已由[SH1-SH6](game-design-workflow/idea-materials/M-2026-09-06-summon-health-damage-and-enemy-targeting.md)独立明确。
_Avoid_：与无敌、无需指挥或可以积攒跨战斗单位混称。

**关联卡失效清理**：
单位离场后清理绑定它的临时关联卡，已投入施法的卡延至该句结束清理；不补偿抽牌、不产生使用或主动弃牌收益，剩余牌序与补牌计时保持。来源见[SL2-SL3](game-design-workflow/idea-materials/M-2026-09-06-summon-departure-and-reference-invalidation.md)。
_Avoid_：与清理全部同名卡、本局永久删词或为守住删牌下限保留失效卡混称。

**召唤指令失效**：
必需单位在结算前离场后，在途法术不自动停止或改指；正常完成时整句落空、不退时间、不额外补牌，若先被打断或整场结束则依各自规则处理。来源见[SL3](game-design-workflow/idea-materials/M-2026-09-06-summon-departure-and-reference-invalidation.md)。
_Avoid_：与受击即打断、自动退款或追溯取消本句正常效果导致的离场混称。

**召唤离场后的状态归属**：
离场单位自身附着的状态清除，它施加给其他有效对象的状态依自身规则继续，除非明确要求来源在场。来源见[SL4](game-design-workflow/idea-materials/M-2026-09-06-summon-departure-and-reference-invalidation.md)。
_Avoid_：与自动转移自身状态或取消该单位施加的所有效果混称。

**再次召唤与原有种类词**：
单位离场不删除或自动抽回本局原有种类词，重新合法召唤建立新单位与新关联；旧关联卡不自动恢复或改绑。来源见[SL5](game-design-workflow/idea-materials/M-2026-09-06-summon-departure-and-reference-invalidation.md)。
_Avoid_：与免费重召唤、特殊复活或撤销此前本场移除效果混称。

**召唤物独立生命与防御**：
玩家的基础召唤物拥有自己的当前生命和生命上限，按自身上限生命入场；普通伤害由自身护甲抵挡后扣自身生命，不自动继承或共用玩家护甲和状态。来源见[SH1-SH2](game-design-workflow/idea-materials/M-2026-09-06-summon-health-damage-and-enemy-targeting.md)，具体数值后定。
_Avoid_：与玩家额外生命、默认初始护甲或全部状态都可作用于单位混称。

**敌方对召唤物选取**：
敌方可选择玩家召唤物作为攻击目标，准备开始时确定并公开，准备中仅因明确效果变更；新单位不自动接走已瞄准其他对象的攻击。来源见[SH3](game-design-workflow/idea-materials/M-2026-09-06-summon-health-damage-and-enemy-targeting.md)，唯一目标离场的单目标攻击保持准备、到点落空，不自动转火。
_Avoid_：与通用嘲讽、站位挡刀或敌方必定选择召唤物混称。

**召唤物受击与玩家施法**：
单纯命中召唤物不直接打断玩家施法，即使它正在执行指令；单位被击败离场则按 SL3 使依赖它的在途指令失效，命中玩家仍依既有规则打断。来源见[SH4](game-design-workflow/idea-materials/M-2026-09-06-summon-health-damage-and-enemy-targeting.md)。
_Avoid_：把命中玩家拥有的单位当作命中玩家，或把预算充足当作执行者存活与法术成功的保证。

**玩家召唤物被击败**：
在完整法术、敌方行动或单次状态处理后的既有检查点，生命耗尽即被击败并按 SL 离场，不另要求清空护甲；召唤物全灭本身不算战败，玩家生命耗尽仍按原规则失败。来源见[SH5-SH6](game-design-workflow/idea-materials/M-2026-09-06-summon-health-damage-and-enemy-targeting.md)。
_Avoid_：与逐词中途死亡、存活单位替玩家续战或敌方召唤物的胜利资格混称。

**独立字数上限**：
依据句中文字总数限制句子是否可用的额外门槛，旧三词基础范围已确认暂不启用；本轮灵活句式的容量限制尚待复审，未自动开启字数上限。原稿中的字数系统保留，待可变句长或修饰词阶段再评估，来源见[范围确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#基础版独立字数上限确认记录)。
_Avoid_：将暂不启用字数上限等同于可任意加词，或将它与词卡施法耗时混称；新句式权限以本轮独立改动为来源。

**基础句施法对象（旧三词范围）**：
旧三词基础句唯一选定的战场对象，承载本句需要读取或操作的状态，并承受本句结果；可为玩家自身或尚未被击败的普通敌人，但须满足具体句义和对象条件。来源见[对象选择素材](game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md)。
_Avoid_：将旧单对象关系直接推广至召唤物执行的法术；新版关系依已确认的 [SR1-SR6](game-design-workflow/idea-materials/M-2026-09-06-summon-word-references-and-target-locking.md)，旧吞噬例句保留自身范围。

**施法对象身份锁定**：
构句时可调整尚未固有绑定的选择，确认施法时锁定本句引用单位和受术目标的身份，施法中不提供通用改选；不冻结状态数值、不预留状态材料，也不改变专属卡绑定。旧对象范围见[对象素材](game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md)，新版独立来源见 [SR4](game-design-workflow/idea-materials/M-2026-09-06-summon-word-references-and-target-locking.md)。
_Avoid_：与状态数值锁定、材料预留、通用取消或目标失效后自动改选混称；普通敌人被击败仍按既有落空规则处理。

**语义兼容**：
句内各词的作用能够衔接的要求；旧版具体表述是谓语能处理宾语、主语能承接谓语结果，来源见[构句素材](game-design-workflow/idea-materials/M-2026-09-05-fixed-grammatical-roles.md)。本轮加入省略主语和召唤物执行后，执行者与动作、输入之间的具体兼容关系需重议，见[本轮改动](game-design-workflow/idea-inbox/2026-09-06-flexible-grammar-and-spell-types.md)。
_Avoid_：将词性齐全等同于语义兼容，或将语义兼容等同于任何战况下都可施法。

**战场状态留存**：
可被后续法术引用的状态在本场跨施法、跨敌方行动保留的原则；变化与消失依状态自身规则或明确效果。来源见[状态素材](game-design-workflow/idea-materials/M-2026-09-05-battle-state-persistence.md)。
_Avoid_：将留存等同于冻结、永不过期或跨战斗继承，或忽视具体操作对状态的消耗和改变。

**状态承载对象与施加来源**：
承载对象是状态当前附着的战场对象；施加来源是产生该状态的对象。普通敌人被击败时，其自身附着状态完全清除，但它施加在其他存活对象上的状态默认继续按自身规则运行。来源见[击败后果素材](game-design-workflow/idea-materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md)。
_Avoid_：把来源被击败当作清除全部状态，或把同种状态合并当作混同承载对象与来源；特殊来源依赖另议。

**普通敌人击败后的对象失效**：
普通敌人在已确认检查点上被判定击败后，失去普通施法对象资格，基础版不保留可施法遗体。只指向它的单目标在途法术在战斗继续时保持原过程，不自动终止或换目标；若正常完成则落空，若先被打断或整场先结束则按各自规则处理。来源同[击败后果素材](game-design-workflow/idea-materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md)。
_Avoid_：与所有目标失效、完整目标选择与锁定、自动取消退款或首领阶段变化混称。

**状态合并**：
同一目标的同一种基础状态共用数量和计时，不因重复施加或来源不同保留多份独立倒计时；不同目标或不同状态分别管理。同种状态由规则定义，不仅凭名称，基础合并采用相同周期。来源见[重施与叠加素材](game-design-workflow/idea-materials/M-2026-09-06-status-reapplication-and-stacking.md)。
_Avoid_：与不同状态转化或各批数量分别到期混称，或据此取消施加来源的所有其他用途。

**状态数量叠加**：
对明确可累积数量或层数的状态，将新增数量加入现有数量；只有有无之分的状态不因重施自动增强。来源同[重施与叠加素材](game-design-workflow/idea-materials/M-2026-09-06-status-reapplication-and-stacking.md)。
_Avoid_：与持续时长相加混称，或推定所有效果都按层数线性增强；具体公式和上限后定。

**状态时长叠加**：
有限持续状态重施生效时，新的剩余时间等于当时剩余时间加本次新增时长；合并后的数量共用新的到期时刻，已经过去的时间不重复计入。来源同[重施与叠加素材](game-design-workflow/idea-materials/M-2026-09-06-status-reapplication-and-stacking.md)。
_Avoid_：与取较大值、重置下一次周期或使所有状态自然到期混称。

**状态重施与重建**：
对仍存在的状态再次施加为重施，依已确认规则处理数量和剩余时间，但保持原周期、不额外立即触发。完全清除后再次施加为新生效，重新计算首次完整周期。仅减少数量而状态仍存在时，剩余周期和到期时间不刷新。来源同[重施与叠加素材](game-design-workflow/idea-materials/M-2026-09-06-status-reapplication-and-stacking.md)。
_Avoid_：把每次重施视为重新开始状态，或把部分消耗等同于完全清除；重施保留首次生效排序位置，清除重建按新状态排序，来源见[状态读值与顺序素材](game-design-workflow/idea-materials/M-2026-09-06-status-values-and-resolution-order.md)。

**周期当前数量读值**：
状态每次周期效果开始结算时读取它当前的数量或层数，先前已经完成的叠加和消耗影响本次读取。来源见[状态读值与顺序素材](game-design-workflow/idea-materials/M-2026-09-06-status-values-and-resolution-order.md)。
_Avoid_：与首次施加量锁定、数量与伤害线性换算或所有法术的通用读取时点混称。

**状态同刻内部顺序**：
状态阶段内，有到时事项的有效状态按当前这一份状态首次生效的先后处理；同刻首次生效按产生效果的结算先后，同一效果同时产生多个状态时按该效果事先明确的固定顺序。重施保留位置，完全清除后重建按新状态排序。来源同[状态读值与顺序素材](game-design-workflow/idea-materials/M-2026-09-06-status-values-and-resolution-order.md)。
_Avoid_：与不同事件阶段的优先级、多个敌人的行动顺序、每层各有位置或按阵营临时改序混称。

**逐状态到时处理**：
按状态内部顺序逐个处理到时事项；本状态周期效果后立即检查，仍应到期且战斗继续才处理到期并再检查，再处理下一个状态。轮到前已清除或不再到期的事项不执行，整场结束停止后续流程。来源同[状态读值与顺序素材](game-design-workflow/idea-materials/M-2026-09-06-status-values-and-resolution-order.md)。
_Avoid_：与所有周期先于所有到期、同刻所有效果同时发生或本状态周期与到期只检查一次混称。

**状态周期计时**：
具有周期效果的状态从生效起独立计算战斗时间，经过完整周期首次触发，之后按自身周期继续；构句和超限弃牌暂停时计时也暂停。来源见[状态计时素材](game-design-workflow/idea-materials/M-2026-09-06-status-timing-and-expiration.md)。
_Avoid_：与全场固定补牌节拍、现实思考时间或生效时立即触发混称；不使所有状态具有周期；已确认仍存在的状态重施保持原周期，完全清除后重建才重新计时，来源见[重施素材](game-design-workflow/idea-materials/M-2026-09-06-status-reapplication-and-stacking.md)。

**状态自然到期**：
具有明确持续时长的状态到达自身期限后的处理；若与该状态末次周期触发同刻，先完整触发并检查，战斗继续才到期并再检查。来源同[状态计时素材](game-design-workflow/idea-materials/M-2026-09-06-status-timing-and-expiration.md)。
_Avoid_：与普通行动结束统一清除、战后清理或提前完全清除混称，或据此使护甲自动衰减。

**状态提前完全清除**：
状态在其尚未执行的周期触发或自然到期处理之前已完全消失，因而取消该份状态未来处理、不补发；既有伤害与效果不撤销，部分数量减少但状态仍在不算完全清除。来源同[状态计时素材](game-design-workflow/idea-materials/M-2026-09-06-status-timing-and-expiration.md)。
_Avoid_：与自动获得移除能力或撤销既有结果混称；普通敌人被击败会清除其自身附着状态，其他宿主失效另议，见[击败后果素材](game-design-workflow/idea-materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md)。

**战后状态清除**：
战斗中获得的护甲、燃烧等临时战场状态，默认在整场战斗结束时清除的规则；生命与词卡沿用各自已确认的持续范围。来源见[战后清除确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#临时战场状态战后清除确认记录)。
_Avoid_：与每次施法结束清空状态混称，或认为清除状态会清空本局卡组、恢复生命、撤销既有伤害。

**状态引用**：
把战场上已有的状态作为宾语进行操作，需要从手牌投入对应的宾语词卡；状态提供材料，词卡提供引用它的能力。制造状态本身不自动获得同名词卡，来源见[状态引用确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#宾语卡与世界状态确认记录)。引用这一步本身不附加消耗，是否消耗或改变状态由具体操作的明确规则决定；词卡弃置不自动消耗对应状态，来源见[引用与消耗确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#状态引用与消耗关系确认记录)。
_Avoid_：将状态出现等同于词卡入手，将拥有词卡等同于已拥有该状态，把引用已有状态与生成状态混称，或把引用不自带消耗理解为整句免费、任何操作都不消耗状态。

**施法选定对象**：
玩家为当前句子明确选中的战场对象；它与句中的主语词是不同概念。当前已确认的用例为“火焰 吞噬 护甲”，定义依据见 [Q1 确认记录](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#q1法术的来源与去向)。
_Avoid_：将“主语”与“施法选定对象”混称。

**施法耗时**：
一项法术完成施放所需的战斗时间，基础值为实际投入词卡各自耗时之和；省略主语不收隐藏主语费用，显式主语承担自身耗时，汉字数量不直接换算时间。来源见[耗时组成确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#施法耗时的组成确认记录)及[FG5](game-design-workflow/idea-materials/M-2026-09-06-flexible-sentences-and-subject-roles.md)。
_Avoid_：用“字数”“专注”或“施法预算”直接替代施法耗时，或把词卡耗时相加理解为逐词产生效果。

**构句阶段**：
玩家选择词语、组织句子且尚未确认施法的阶段，此时战斗时间轴暂停。来源见 [Q3 确认记录](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#q3构句时是否计时)。
_Avoid_：将构句用时算作施法耗时。

**通用主动取消**：
玩家在确认投入词卡、开始施法后，仅因改变计划主动撤回在途法术的权限；当前基础版不提供，包括补入更合适组件或预判材料可能缺失时。尚未开始施法的构句阶段仍可调整。来源见[主动取消权限确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#基础版不提供通用主动取消确认记录)。
_Avoid_：与构句阶段改选、敌方命中打断或材料缺失落空混称，或从通用取消权限推定目标失效及特殊控制的处理。

**提前施法**：
满足其他施法条件时，即使所引用状态尚未出现，也允许先投入词句并开始施法，预判材料会在需要时出现。词卡、语义兼容与目标合法性要求仍在，法术照常耗时并受命中打断约束；启动不提前制造、预留或保证获得状态，必需材料完全缺失时按后续确认的法术落空规则处理（见下文），其余材料条件仍待明确。来源见[提前施法确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#提前施法确认记录)。
_Avoid_：把缺少状态等同于可缺少词卡，把启动许可等同于必然生效，或把本权限当作所有操作采用同一读取时点。

**本场时间起点**：
每场普通战斗独立建立的计时起点；开战在场普通敌人的首次准备与固定补牌计时均从这里开始，不承接上一场补牌剩余进度。来源见[O1-O4 开局确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#战斗开局与初始节拍整组确认记录)。
_Avoid_：与一局 Roguelike 的开局、现实时间或跨战生命及卡组重置混称。

**起手准备**：
首次施法或等待决策前完成的洗牌与形成起手过程，不推进战斗时间，也不因该过程触发普通敌方行动或定时补牌；沿用起手合法句保障。来源同[O1-O4 开局确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#战斗开局与初始节拍整组确认记录)。
_Avoid_：与首张定时补牌、玩家自由选牌或保证起手法术安全完成混称；具体起手牌数与随机选择权重未定，保障方法见 OH1-OH5。

**多敌人独立行动**：
基础版普通战斗允许单敌人和多敌人遭遇；每个敌人各自准备并公开下一次行动及执行时间，与玩家施法和固定补牌共用一条战斗时间轴。某个敌人行动后只接续自己的准备，不统一重置其他敌人的准备。来源见[多敌人确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#多敌人独立行动确认记录)。
_Avoid_：与多条独立时间流、每个敌人各补一份牌、每场必须多敌人或某敌人行动后全体重置混称；同刻内部先后见下方固定序术语，在场数量尚未确定，击败后的普通行动取消见下方术语。

**普通敌人击败**：
基础版普通敌人在已确定的检查点上，当前生命耗尽所对应的判定；无需额外清空护甲或其他状态。判定后取消待执行普通行动并停止后续准备，按既有规则检查整场胜负。来源见[生命耗尽即击败确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#普通敌人生命耗尽即击败确认记录)。
_Avoid_：与护甲归零、所有状态消失、句内中途判定或首领阶段结束混称；不由此推定伤害必须经过护甲或自动清除已造成的全部状态。

**击败后的行动取消**：
普通敌人被判定击败后，立即取消尚未执行的普通行动，并停止后续准备；战斗继续时其他敌人的准备、玩家施法与补牌仍按既有规则推进。来源见[击败取消行动确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#击败敌人取消行动确认记录)。
_Avoid_：与命中打断玩家施法、撤销已执行效果或清除全部遗留状态混称；普通完整行动后的检查位置与普通敌人生命耗尽条件已确认，特殊敌人及特殊效果仍待定。

**敌方行动准备**：
单个敌人一次行动执行前的阶段；开战在场普通敌人的首次准备从本场时间起点开始，需经过各自非零准备时间，首次决策前公开行动与执行时间，来源见[O1-O4 开局确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#战斗开局与初始节拍整组确认记录)。普通连续行动中，从该敌人上一次行动结算结束开始，具体时长未定。来源见[时间轴延续确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#敌方行动后时间轴延续确认记录)。
_Avoid_：将开始准备等同于立即再行动，或将新准备阶段视为全场时间轴与补牌计时归零。

**敌方意图**：
各个敌人当前准备中的下一次行动及其预定执行时间，准备开始时确定并向玩家公开；准备中仅因明确效果变更，变化须让玩家知道。来源见[意图确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#敌方意图确定与变更确认记录)。
_Avoid_：将预定行动等同于最终效果数值锁定或必然命中，或将公开下一步等同于公开整场行动序列。

**普通敌人同刻固定序**：
开战时由本场遭遇确定、在首次决策前公开并持续可查的普通敌人先后顺序，仅用于实际执行时间相同的行动；本场不因接续准备、明确改时或敌人退出而重排其余敌人的相对顺序。来源见[E1-E3 确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#多敌人同刻行动顺序整组确认记录)。
_Avoid_：与行动速度、所有事件优先级、状态生效排序或玩家自行排序混称；不同时点仍按时间先后，击败取消与逐行动检查保持。

**施法预算**：
依据所有敌人当前公开、可能命中玩家的攻击时点估算最近风险所剩的战斗时间，随时间与公开威胁变化，构句不消耗、开始下一句不重置。它不限制其他条件合法的长法术启动，也不承诺未知后续行动安全，来源见[Q4 定义](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#q4施法预算的含义)及[B1-B3 边界确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#施法预算与未知后续行动整组确认记录)。
_Avoid_：与独立法力、固定施法次数、启动硬上限或安全保证混称，或只考虑所选敌人的攻击。

**无已知打断时点**：
当前公开意图中没有相关攻击可作为施法风险截止点的情况；仍可开始其他合法法术，但后续新公开的攻击照常影响在途施法。来源同[B1-B3 确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#施法预算与未知后续行动整组确认记录)。
_Avoid_：与无限安全时间、暂停敌方准备、禁止施法或起手后获得额外保护混称。

**护甲抵伤**：
玩家与普通敌人的基础防御关系：普通直接伤害先由护甲等量抵消并消耗相应护甲，溢出扣生命；持续伤害默认沿用同样流程。来源见[伤害素材](game-design-workflow/idea-materials/M-2026-09-06-damage-armor-and-interruption.md)。
_Avoid_：与每次行动自动清空护甲、护甲不消耗的减伤率、抗打断或吞噬护甲的消耗比例混称。

**持续伤害**：
由具体规则明确的持续性伤害效果，默认经过护甲，但本身不视为一次攻击命中，不因扣除生命而打断正在施放的法术。来源同[伤害素材](game-design-workflow/idea-materials/M-2026-09-06-damage-armor-and-interruption.md)。
_Avoid_：与所有战场状态、持续施法或免于战败混称；周期与到期的通用过程和检查位置已由[状态计时素材](game-design-workflow/idea-materials/M-2026-09-06-status-timing-and-expiration.md)补齐；基础重施与叠加已由[独立素材](game-design-workflow/idea-materials/M-2026-09-06-status-reapplication-and-stacking.md)补齐，周期当前数量读值与状态内部顺序已由[独立素材](game-design-workflow/idea-materials/M-2026-09-06-status-values-and-resolution-order.md)补齐；普通敌人被击败时的承载对象与施加来源区别已由[击败后果素材](game-design-workflow/idea-materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md)补齐；具体参数、其他宿主失效和特殊连锁仍待定。

**施法打断**：
玩家正在施放法术时遭敌方攻击命中而发生的中断；攻击即使被护甲完全抵消、没有损失生命仍会打断尚未完成的法术。敌方自我强化、增加护甲或召唤本身不属于打断，持续伤害本身也不打断。来源见 [Q5 确认记录](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#q5打断的触发范围)及[伤害板块确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#伤害护甲与打断整组确认记录)。
_Avoid_：将所有敌方行动都称为打断。

**组合式法术**：
实际投入的词卡共同定义的一条完整法术；可以产生多个相关变化，不按词卡张数算作多次施法。来源见 [SM1](game-design-workflow/idea-materials/M-2026-09-06-compositional-spells-and-word-meaning.md)。
_Avoid_：与多张独立技能依次释放、吟唱中逐词生效或把多个真实事件全部合并为一个道具触发机会混称。

**词义复用**：
以稳定的核心词义及明确的角色、输入或战场条件解释不同句子的作用；符合规则的新组合无需额外解锁整句配方，基础版不设整句隐藏配方奖励，已明确的类型与道具联动保留。来源见 [SM2-SM3](game-design-workflow/idea-materials/M-2026-09-06-compositional-spells-and-word-meaning.md)。
_Avoid_：与任意自然语言都合法、只凭日常词名猜效果、同名显示的种类词与绑定卡完全互换，或取消当前启动条件混称。

**护甲**：
基础防护状态，原稿“护盾”在当前规则中统一为此名称；同一对象上一份可累积数量，无自然到期或自动周期效果，普通伤害等量消耗、溢出扣生命，整场结束按临时状态清除。来源见 [PA1-PA3](game-design-workflow/idea-materials/M-2026-09-06-armor-identity-generation-and-persistence.md) 与[伤害素材](game-design-workflow/idea-materials/M-2026-09-06-damage-armor-and-interruption.md)。
_Avoid_：与额外护盾词卡、抗打断、共享防护或跨战资源混称；是否需要数量上限及数值后定。

**生成护甲**：
“获得 护甲”基础句成功时产生新的护甲数量，省略主语时由玩家获得，施放前不要求已有护甲，也不从其他对象转移或扣取；仍需实际投词与施法。来源见 [PA2](game-design-workflow/idea-materials/M-2026-09-06-armor-identity-generation-and-persistence.md)。
_Avoid_：与操作已有护甲、状态出现即获得词卡，或“获得”能够搭配任意名词混称。

**整句结算**：
法术完整施放后，按句内词义顺序和具体操作条件结算整句的过程；完成前被打断则整句不生效，已经经过的时间不退。完成也不保证生效，当前基础三词句的必需材料完全缺失时整句落空；H4 范围内的单目标法术正常完成时所指普通敌人已被击败，也整句落空，见[击败后果素材](game-design-workflow/idea-materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md)。来源见 [Q6 确认记录](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#q6被打断的一句如何结算)及[材料缺失落空确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#必需材料缺失落空确认记录)。
_Avoid_：把开始施法视为已经产生部分效果，或把打断视为时间回退。

**法术落空**：
法术正常完成但整句不产生效果的结果；已确认原因包括必需状态材料完全缺失、H4 范围内普通敌人目标已被击败、[SL3](game-design-workflow/idea-materials/M-2026-09-06-summon-departure-and-reference-invalidation.md) 的必需召唤物已离场，以及 [SN5](game-design-workflow/idea-materials/M-2026-09-06-summon-coexistence-and-field-capacity.md) 的基础召唤结算时无空位，各依对应范围判断。普通投入词进入弃牌堆、已耗时间不返还、结束不额外补牌；若先被打断或整场先结束，沿用对应规则。材料缺失不自动延长施法等待材料，是否必需依具体操作判断；对象被击败不自动终止或换目标。来源见[材料缺失落空确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#必需材料缺失落空确认记录)及[击败后果素材](game-design-workflow/idea-materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md)。
_Avoid_：与未完成时的命中打断混称，把任何状态不存在都判为失败，或推定材料数量不足、其他目标失效及扩展句式也遵循同一结果。

**击败与胜负检查点**：
当前已确认的普通检查位置为每句法术、每次敌方行动、每份状态的一次周期效果或一次到期处理完整结算之后、处理下一事件之前；在此判断击败与整场结果，处理已成立的结果，不在句内逐词检查，也不等同刻全部敌人行动完成才检查。来源见[完整行动后检查确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#完整行动后检查击败与胜负确认记录)及[状态时序确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#单份周期状态计时与到期整组确认记录)。
_Avoid_：与玩家操作窗口、整个同刻事件组或胜负条件本身混称；普通战斗同时满足条件时失败优先已确认，特殊效果检查位置尚未确定。

**同刻结算顺序**：
同一战斗时点先结算已完成法术并弃置普通投入词、完成检查；基础召唤按 [SC3-SC4](game-design-workflow/idea-materials/M-2026-09-06-summon-reference-generation-and-hand-entry.md)处理有效关联卡入手及超限弃牌，再处理敌方行动及可能的打断弃置，然后处理到时的状态，最后处理固定节拍补牌与超限弃牌；中间不开放新施法，战斗结束则停止后续流程。状态内部先后按首次生效及固定平局规则处理，见[状态读值与顺序素材](game-design-workflow/idea-materials/M-2026-09-06-status-values-and-resolution-order.md)；普通敌人同刻行动按开战公开的固定序，见[E1-E3 确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#多敌人同刻行动顺序整组确认记录)；特殊新增敌人及触发仍待定。来源见[同一时点顺序确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#同一时点顺序确认)及[状态时序确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#单份周期状态计时与到期整组确认记录)。
_Avoid_：把画面播放的先后当作新的行动机会，或用同刻刚补入的词抢在敌方行动前施法。

**时间补牌**：
词卡随战斗时间流逝按固定速度补充的供给方式；每场普通战斗从本场起点重新计时，首张定时牌经过一个完整间隔后到来，起点不额外补牌，暂停也暂停计时，来源见[O1-O4 开局确认](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md#战斗开局与初始节拍整组确认记录)；来源见[时间补牌与多张预览素材](game-design-workflow/idea-materials/M-2026-09-05-timeline-draw-preview.md)。具体速度尚未确定。
_Avoid_：将现实中的思考时间计入补牌进度，或将它等同于施法结束补满。

**牌序预览**：
玩家对多张即将补入的词卡及其先后顺序的可见信息；抽牌堆剩余不足时仅展示当前确定牌序，其后标为“待洗回”，实际洗回后才显示新序列。来源同[时间补牌与多张预览素材](game-design-workflow/idea-materials/M-2026-09-05-timeline-draw-preview.md)。具体可见张数尚未确定，不为填满预览提前洗牌。
_Avoid_：将可见牌当作已经到手，或将可见顺序等同于可免费修改顺序。

**基础牌序**：
开战建立牌库及弃牌洗回时随机洗牌所形成的抽取顺序，之后按序抽取，只有明确效果才改变顺序。来源见[基础牌序确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#基础牌序确认)。
_Avoid_：把每次查看或构句当作重新随机牌序，或将洗牌等同于恢复本场移除牌。

**超限弃牌**：
补牌正常进入手牌后，若超过手牌上限，玩家立即选择弃牌至上限。选择时战斗时间暂停，只允许完成弃牌，随后继续原行动；正在施法的句子不能借此修改、取消或另起施法。来源见[满手补牌确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#满手补牌确认)。
_Avoid_：把满手当作停止补牌或自动丢弃新牌，将超限弃牌等同于本场移除，或把弃牌暂停称为施法打断。

**本场移除**：
词卡退出当前战斗的循环，本场不再参与正常抽取或弃牌洗回；原有词下一场按本局卡组恢复参与，临时副本则战后消失。原有词的本局拥有关系不因该效果删除，来源见[删牌范围确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#删牌范围确认)及[副本循环确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#临时副本正常循环确认记录)。
_Avoid_：与普通弃牌、本局永久删牌混称；把移除范围确认当作目标区域或具体词卡效果已确认。

**施法投入词**：
已确认投入当前法术的词卡，确认施法时立即离手进入临时施法区。基础版施法开始后不能通用主动撤回，权限见上文。普通投入词在本次施法成功、被打断或因已确认原因落空后均进入弃牌堆，结束本身不触发额外补牌。来源见[投入词去向确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#施法投入词去向确认)与[临时施法区确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#临时施法区确认)。
_Avoid_：把结束弃牌等同于本场移除，或把弃牌与法术生效混为一谈。

**临时施法区**：
存放已经确认投入当前法术的词卡的位置；其中的词卡不占手牌上限，也不能用于超限弃牌。普通投入词在施法成功、被打断或因已确认原因落空后从这里进入弃牌堆。来源见[临时施法区确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#临时施法区确认)。
_Avoid_：将施法区视为另一组可自由使用的手牌，或认为移入施法区会立即补满空位。

**弃牌洗回**：
补牌时抽牌堆为空且弃牌堆有牌，将当时弃牌随机洗回抽牌堆并继续本次抽取的过程；不额外耗时，手牌、施法区和本场移除牌不参与。来源见[空抽牌堆洗回确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#空抽牌堆洗回确认)。
_Avoid_：把洗回等同于所有词卡归库、立即补满手牌，或认为抽走最后一张就须提前洗回。

**安全下限**：
为防止抽牌堆和弃牌堆同时为空而设置的本场可循环词卡数量下限；本场移除最多执行到该下限，超出余量的部分不执行，并提前展示实际可移除量。计数包括手牌、施法区、抽牌堆与弃牌堆，不含已本场移除的词。其中会随单位离场清理的召唤关联卡不增加可删牌余量，失效清理也不因下限而保留无效卡；具体数值及牌区占用验证后定，来源见[卡组下限确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#卡组下限方向与资格追问)及[SL6](game-design-workflow/idea-materials/M-2026-09-06-summon-departure-and-reference-invalidation.md)。
_Avoid_：只计算抽牌堆张数，将已移除词计入安全余量，或将数量保障等同于合法句保障。

**起手补正**：
随机起手不满足保障时，从本局实际卡牌可组成的合格组合中随机选一组，保留已在手组件并等量交换缺少组件的初始化处理；换出牌回抽牌堆并洗剩余堆，最终确定后才公开首次预览。来源见 [OH3-OH5](game-design-workflow/idea-materials/M-2026-09-06-opening-hand-guarantees.md)。
_Avoid_：与自选换牌、卡组外补卡、战中重抽或普通定时补牌混称；自然达标的起手及剩余牌序保留，准备不耗时。

**起手保障**：
开局手牌至少用本局自有词卡具备一条语义兼容、当前可启动且必需状态材料齐备的基础句；不保证最优、收益大小、安全完成或后续补牌成句。来源见[最初确认](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md#起手保障确认)与[OH1-OH5](game-design-workflow/idea-materials/M-2026-09-06-opening-hand-guarantees.md)；手牌数量后定。
_Avoid_：将其等同于任意选牌、无限重抽、卡组外补词，或只凭词类齐全就判定语义合法。
