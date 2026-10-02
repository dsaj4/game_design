# TL-1 兼容规则复用记录

Project ID：game-002。2026-10-01。文档角色：DocumentationAudit。决策G002-CORE-048；当前规则TL-26–37，Accepted；体验Hypothesis / NotRun。

## 任务、输入与判定方法

用户原话：“将之前材料中不冲突且可以复用的部分合并，完善当前设计中，将对应表述更新确保兼容一致”。

本轮以 `ed013948f6c5379fc984413ffd08ae8e7ce0f0c9` 的TL-1为基准，复核旧Qualified材料的相关规范化章节；需要理解旧系统语境时固定读取RC1提交 `d6e54af395518401fb4d8466b2302a1271da557a`。已有INT-01–13确认优先。来源资格沿原记录，不将本次整理冒充新的用户逐条答复。

选择标准：原条款已有资格和采纳基础，能在新程序／制造／行动／战外层级明确落位，不恢复已否决机制，不替Unknown作重大取舍。只改含义落点或时点即可兼容的条款作适配；无法确定的部分留待设计。用户这次明确授权合并兼容部分，构成本范围采纳依据。

## 逐来源复用与限制

| 原Qualified来源 | 当前落点 | 合并内容 | 适配或不迁入部分 |
| --- | --- | --- | --- |
| [09-05-grammar-and-semantic-compatibility](../../sources/materials/M-2026-09-05-grammar-and-semantic-compatibility.md) | TL-26／27 | 词性、角色、明确权限和读取／消费区分 | 材料位置按TL-20，不沿旧主语执行者或材料禁令 |
| [09-05-word-inventory-and-copies](../../sources/materials/M-2026-09-05-word-inventory-and-copies.md) | TL-26／33 | 实体占用、本局库存、副本独立 | 同名3张和旧库存数量不迁入 |
| [09-06-compositional-spells-and-word-meaning](../../sources/materials/M-2026-09-06-compositional-spells-and-word-meaning.md) | TL-26 | 完整程序、词义稳定、无隐藏整句解锁 | 制造成功、行动生效与命中分阶段，不照抄旧施法成功时点 |
| [09-10-instance-and-conditional-binding](../../sources/materials/M-2026-09-10-instance-and-conditional-binding.md) | TL-27 | 实例／条件绑定、名单不补位、逐项复查 | 己方选取改为生效时；旧冻结全场与空间范围不迁入 |
| [09-11-modifier-card-system](../../sources/materials/M-2026-09-11-modifier-card-system.md) | TL-28 | 直接挂接、实体占用、兼容检查与专属适配 | 旧修饰卡、τ、空间效果及复杂叠加公式另审 |
| [09-06-armor-identity-generation-and-persistence](../../sources/materials/M-2026-09-06-armor-identity-generation-and-persistence.md) | TL-29 | 按宿主累计、先甲后生命、耗尽与战终清理 | 普通掉血不打断；护甲不是可携带资源 |
| [09-06-defeated-enemy-target-and-state-lifecycle](../../sources/materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md) | TL-29 | 死亡失去存活资格、宿主状态清理、无凭空尸体 | 已揭示敌牌是否随来源死亡取消仍待决 |
| [09-10-accepted-design-interfaces](../../sources/materials/M-2026-09-10-accepted-design-interfaces.md) | TL-30 | 完整支付、实际权限、不能共享一份消费 | 制造托管与生效支付分开，不移植无目标免制造成本或材料禁令 |
| [09-06-prebattle-expressibility](../../sources/materials/M-2026-09-06-prebattle-expressibility.md) | TL-31 | 用真实库存与规则审可表达性 | 加入新资源初态和供给链，不凭旧配置证明可达 |
| [09-06-branching-run-routes](../../sources/materials/M-2026-09-06-branching-run-routes.md) | TL-32 | 单向固定路线、分叉选择、节点一次性及消费机会 | 只揭示遭遇摘要；完整暗牌仍待揭示，旧19节点不迁入 |
| [09-05-post-victory-health-persistence](../../sources/materials/M-2026-09-05-post-victory-health-persistence.md) | TL-33 | 普通胜利生命延续、无自动恢复 | 生命上限和恢复量重定，不新增战斗回血能力 |
| [09-07-new-run-starting-resources](../../sources/materials/M-2026-09-07-new-run-starting-resources.md) | TL-33 | 新局满预设生命、0金币、局间重置 | 旧12词／四杖不开启；0金币不影响固定干涉费用 |
| [09-06-normal-combat-word-rewards](../../sources/materials/M-2026-09-06-normal-combat-word-rewards.md) | TL-33 | 胜利一次收益包、整包领取／放弃 | 资源携带单独选择；旧不产卡禁令仅不开放永久词卡／产金 |
| [09-05-rest-recovery-and-word-choice](../../sources/materials/M-2026-09-05-rest-recovery-and-word-choice.md) | TL-34 | 恢复／拿词互斥、3个不同名候选、放弃不回退恢复 | 3选1不是副本上限；候选只来自新正式池，池不足只恢复或跳过 |
| [09-07-shop-shelves-and-transactions](../../sources/materials/M-2026-09-07-shop-shelves-and-transactions.md) | TL-35 | 固定货架、明价、足额且合法才扣款交付 | 商品池、价格与额度重定，不按构筑暗改 |
| [09-07-merchandise-eligibility](../../sources/materials/M-2026-09-07-merchandise-eligibility.md) | TL-35 | 同店词名不重复、每项一件、缺货不补偿 | 词卡／法杖资格分开，资源身份不等于商品 |
| [09-07-shop-nodes-and-spending-opportunities](../../sources/materials/M-2026-09-07-shop-nodes-and-spending-opportunities.md) | TL-32／35 | 可选商店及此前金币机会、店外不知货架 | 可负担是待核对目标，旧货架期数与报价不迁入 |
| [09-14-interface-platform-and-experience](../../sources/materials/M-2026-09-14-interface-platform-and-experience.md) | TL-31／36 | UX03配置校验、UX05决策保存、UX07信息可达性；UX02菜单边界 | 战中改为结清时点恢复，旧4杖／9词、倍速与0.5秒不继承 |
| [09-06-spell-effect-sources-and-modifiers](../../sources/materials/M-2026-09-06-spell-effect-sources-and-modifiers.md) | TL-37 | 普通数量计算、实际来源、基础量与结果分开 | 材料不当执行者；旧释放起点快照不自动迁入 |
| [09-10-semantic-world-executable-rules](../../sources/materials/M-2026-09-10-semantic-world-executable-rules.md) | TL-26／27／29／37 | 对象能力、去重配对、条件非事件与可解释结果 | 材料生产、卡牌行及战中控制以新确认优先 |
| [09-11-global-rule-boundaries](../../sources/materials/M-2026-09-11-global-rule-boundaries.md) | TL-29／30／37 | 参数域、零值、原子支付、独立生命周期与有限事件 | 旧总时序、RC06层数和时间公式不继承 |

额外核对但未新增采纳：[数值重设计约束](../../sources/materials/M-2026-09-10-numerical-redesign-constraints.md)用于确认旧数值不当锚点；[路线／遭遇／疲劳素材](../../sources/materials/M-2026-09-14-run-route-encounters-and-fatigue.md)仅核对RG04／05，旧12场和恢复24不搬入。首批类型卡及元素体系未整包恢复。

## 十二组规则与玩家影响

| 规则 | 玩家选择／反馈 | 代价或失败路径 | 尚未确定 |
| --- | --- | --- | --- |
| TL-26 实体与词义 | 用真实副本分配程序，卡义一致 | 同实体不能多处使用 | 卡池和副本额度 |
| TL-27 绑定与名单 | 实例精确引用或条件适应变化 | 实例消失不换人，名单内失效不补位 | 各词选择优先级 |
| TL-28 修饰挂接 | 明确只改变哪个词 | 要占实体，不兼容不能装 | 首批修饰词及叠加细则 |
| TL-29 身份与护甲 | 分辨存在、归零、失效与累计护甲 | 死亡失去资格，护甲不跨战 | 敌牌来源死亡后的行为 |
| TL-30 分阶段支付 | 看到制造成本与生效支付各属哪步 | 缺料不部分开工，空放仍损失制造成本 | 托管在战终的归属 |
| TL-31 配置可表达性 | 自己编排合法程序，看到缺料提示 | 真实实体不足不能虚构组件 | 初始组合与资源供给 |
| TL-32 路线 | 到分叉再选择，知道休整／消费机会 | 前进不可回店刷货 | 路线规模与节奏 |
| TL-33 库存与收益 | 区分收益包领取与携带筛选 | 生命不免费恢复，资源有携带容量 | 奖励、容量和资源结算集合 |
| TL-34 休整 | 恢复或3选1拿词，也可跳过 | 看词后不能反悔拿恢复 | 新词池和恢复量 |
| TL-35 商店 | 固定明价，决定买哪些或存钱 | 每项一件，无退款／刷新 | 新货架与价格 |
| TL-36 决策与可达性 | 已揭示、已付与已选内容可继续 | 不靠退出重抽；读写失败保留原结果 | 实际UI方案 |
| TL-37 数量与来源合同 | 参数、来源和结果可解释 | 无隐含递归或跨来源借加成 | 特殊数量与事件总排序 |

## 适配例与冲突边界

1. “开始施法选目标”改为己方行动生效时按已承诺规则选目标；敌牌仍揭示锁定。
2. “主语是执行者”不覆盖材料位置。编程用火种词卡和被加工的火种资源分账。
3. 旧“无目标不付费”不能免掉已发生制造成本。未发生的额外效果支付与制造成本分别记录。
4. 旧金币／词卡整包收益只约束该收益包，不能强迫携带资源随整包一起放弃。
5. 休整3选1与新局0金币是本轮明确复用的结构常量；同名上限3、开局12词／四杖、恢复24及旧价格仍Unknown或历史。
6. 保存节点选择／交易／候选固定的原则继续，战斗恢复必须包含材料、进度、费用与已揭示敌牌。
7. 宿主死亡失去资格可复用；已揭示倒计时是否随其来源敌人死亡取消不能自动裁定，列入TL-Q05。

不恢复2×5、旧范围、复诵、共享开始槽覆盖、名义续排、掉血全杖打断、只读战斗、整场重播、旧卡池和旧疲劳上界。单向路线与保存不妨碍战中暂停、合法改线及独立干涉接口。

## 证据与后续

本轮是静态来源与规则核对，没有玩法测试、真人样本或实现完成结论。新预期TL-V23–37登记在[验收计划](../../design/validation.md)，均NotRun。仍需确认的边界集中在[当前问题](../../governance/questions.md)，不为复用旧材料而新增一套旧参数。

[当前系统](../../design/README.md)是权威正文；原素材添加适用范围说明并保留原文，供追溯形成过程。[P](P-2026-10-01-timeline-production-system.md)／[E](E-2026-10-01-timeline-production-system.md)追加第9轮论证；[D](../../sources/draft-changes/D-2026-10-01-compatible-rules-reuse.md)记录本次采纳。

静态复核：361份活动Markdown、5084条本地链接检查无错误；21份直接复用来源除新增适用说明外，原正文与输入版本一致。TL-26–37各有唯一权威定义，TL-V01–37没有重号，新增15条仍为NotRun。文件索引更新为418份；差异空白检查通过。以上不包含玩法运行、平衡或真人验证。
