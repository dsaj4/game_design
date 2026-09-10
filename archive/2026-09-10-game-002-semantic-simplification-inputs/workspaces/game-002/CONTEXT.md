# game-002 领域词汇

当前核心：Core Concept v0.6 / Stable Design Baseline。本文只定义领域术语；证据状态为Hypothesis。

| 术语 | 定义 | 依据 |
| --- | --- | --- |
| 战前构句 | 从完整战外库存分配实体词卡，依据词性、句式和语义形成完整法术；配置不推进战斗时间。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-05-grammar-and-semantic-compatibility.md) |
| 战外词卡库存 | 本局战斗外持有的普通词卡集合，供每场战前配置；同名普通词最多三张。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-05-word-inventory-and-copies.md) |
| 实体词卡分配 | 一张实体卡在本次配置中只归属一条法术且占一个位置；同名重复需要对应副本。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-05-word-inventory-and-copies.md) |
| 循环法术 | 一个组合定义的完整法术，按既定冷却与释放周期持续尝试。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md) |
| 首次冷却起点 | 战前为各法术选择的第0–10刻内开始第一次冷却的时刻。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md) |
| 循环周期 | 冷却时长加释放时长；冷却由实际词卡时间贡献合计形成，释放时长单独设计。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md) |
| 共享释放槽 | 所有法术在每刻竞争一次释放开始机会的共同约束；直接效果在开始时结算一次，持续作用由过程或状态承载。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-05-timeline-schedule-preview.md) |
| 法杖顺序与覆盖 | 战前设置的法杖前后顺序；同刻靠后法术覆盖靠前法术，被覆盖者本次无效果、无特效，后续周期保持。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-05-timeline-schedule-preview.md) |
| 生命伤害打断 | 玩家实际承受生命伤害时取消当时正在冷却的普通法术本次机会，后续周期保持，已结算结果不回退。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-06-damage-armor-and-interruption.md) |
| 对象引用 | 法术指向战斗对象的方式，支持固定实例身份和战前固定条件两种绑定；对象仍须满足当前作用条件。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-10-instance-and-conditional-binding.md) |
| 对象失效 | 对象不再具备该法术的作用条件；释放时跳过并继续其他合法对象，失效尝试仍保留释放特效。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md) |
| 环境对象 | 长方形场景中有位置且可操作、没有生命值和攻击行为的对象，例如大树和溪流。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md) |
| 法杖与镶嵌 | 每根法杖承载一条法术；镶嵌是范围、特殊效果的配置层，具体槽位、资格和效果Unknown。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-07-wand-inlay-configuration.md) |
| 名词、动词与句法角色 | 名词、动词是固定词性；主语、谓语、宾语是位置职责，名词跨角色使用须符合词义。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-05-grammar-and-semantic-compatibility.md) |
| 执行者、操作内容与受术目标 | 谁执行、直接处理什么以及结果落在谁身上三个语义关系，具体词义分别声明。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-06-flexible-sentences-and-subject-roles.md) |
| 简易类型 | 省略显式主语的合法法术类型，默认玩家语义补全不改变该分类。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-06-spell-types-and-effect-conditions.md) |
| 召唤类型 | 包含召唤操作或具体召唤物直接参与的法术特征，可与其他类型并存。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-06-spell-types-and-effect-conditions.md) |
| 状态引用 | 配置对应词卡后操作战场状态的语义权限；引用本身不自动消耗材料。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-05-battle-state-persistence.md) |
| 护甲 | 按数量累积的防护状态，普通伤害先等量消耗护甲，溢出扣生命；无自然到期与自动周期。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-06-armor-identity-generation-and-persistence.md) |
| 状态重施 | 同目标同种合并，可累积数量相加、有限剩余时长相加，保留原周期和排序位置。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-06-status-reapplication-and-stacking.md) |
| 状态周期 | 自生效起经过完整正周期后首次触发，随后按周期推进；每次开始读取当前量。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-06-status-timing-and-expiration.md) |
| 状态内部顺序 | 按首次生效、产生效果先后及效果固定顺序逐状态处理，周期和到期后分别检查。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-06-status-values-and-resolution-order.md) |
| 源方修正 | 实际执行者自身适用的强度修正，每次法术开始结算时读取；不自动共享到其他单位。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-06-spell-effect-sources-and-modifiers.md) |
| 周期强化继承 | 适用增幅先计入新增状态量，周期使用当前合并量，不重复应用这份增幅。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-07-periodic-state-modifier-inheritance.md) |
| 召唤种类词与单位身份 | 种类词表达一类单位，身份引用只指具体单位；当前不新增专属引用词卡，战前占位的具体机制后置。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-06-summon-unit-and-reference.md) |
| 战斗胜负 | 完整事件后的结果检查：全部敌人击败且玩家存活则胜利，玩家生命耗尽则失败；同检查点失败优先。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-05-normal-combat-outcomes.md) |
| 整体收益包 | 战后金币与法术产生的卡牌共同组成的领取对象，玩家整体领取或放弃。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-06-normal-combat-word-rewards.md) |
| 战斗耗时奖金 | 按共用战斗时间从0到胜利的经过量及遭遇预设基准计算，有上限、最低0。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-07-combat-gold-and-efficiency-bonus.md) |
| 休整取舍 | 在独立休整节点选择一次有限恢复或可用的词卡三候选选一；选词后拒收不返还恢复机会。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-05-rest-recovery-and-word-choice.md) |
| 商店货架 | 到店后公开且本次固定的商品与标价，每条目一份，售出不补货，交易检查资格和余额。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-07-shop-shelves-and-transactions.md) |
| 单向分叉路线 | 本局开始按约束生成且保持稳定的路线；分叉可选，进入后不撤回，完成节点不回访。 | [对应素材](game-design-workflow/idea-materials/M-2026-09-06-branching-run-routes.md) |
| 生命支付 | 由效果明确声明的生命代价，不自动归类为伤害。 | [接口素材](game-design-workflow/idea-materials/M-2026-09-10-accepted-design-interfaces.md) |
| 法术成功事件 | 完整法术至少有一个对象合法结算时产生的一次事件；合法零值可满足，多个对象不重复计次。 | [接口素材](game-design-workflow/idea-materials/M-2026-09-10-accepted-design-interfaces.md) |
| 待领取产出 | 本场已经合法产生、尚未加入战外持有资源的收益；造卡资格计入其中同名副本。 | [接口素材](game-design-workflow/idea-materials/M-2026-09-10-accepted-design-interfaces.md) |
| 单位占位 | 用于战前明确未来单位身份与出生关系的后续设计方向；具体机制尚未形成。 | [接口素材](game-design-workflow/idea-materials/M-2026-09-10-accepted-design-interfaces.md) |

接口处理范围见[设计决定与后续工作](docs/design-decisions-needed.md)，具体参数按[数值任务](docs/numerical-redesign.md)重新设计。

## 语义世界对象范围

**语义世界**：具有明确对象结构、交互能力与执行规则的战斗世界，玩家构成的法术句子在其中产生结果。范围包括实体、部件、材料、属性状态、空间关系与过程对象。
_避免_：以画面出现的任何内容都能接受任意动词，代替明确的对象能力。

**过程对象**：战斗中发生或持续的一项作用及其进程，例如飞行物、敌方攻击与法术冷却；具体引用和可操作内容由对应机制定义。
_避免_：把一次真实过程、整个循环规则和释放演出视为同一个对象。

**世界基础规则**：战斗世界的共同约束，包括胜负判定和全局结算顺序；SW01范围中保持固定。
_避免_：把改变某次攻击或冷却等同于修改整个战斗的结算规则。

依据：[已确认的SW01范围](game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md)。

## 对象引用

**实例绑定**：战前明确所指对象身份、后续释放持续尝试该对象的引用方式；对象失效时跳过。
_避免_：将同名新对象视为原实例，或失效时隐式转为条件搜索。

**条件绑定**：战前固定选择条件、每次释放匹配当前符合条件对象的引用方式；符合条件的新生对象可以参与。
_避免_：把绑定条件固定等同于匹配结果整场固定。

依据：[SW02引用模型](game-design-workflow/idea-materials/M-2026-09-10-instance-and-conditional-binding.md)。SW02-A名单时点及R05–R11引用、排序与成本规则均已确认。

**单次直接对象名单**：每次完整法术开始处理时确定的直接作用对象。本次不重选、追加或补位；逐对象仍读取当前合法性与材料，新符合条件对象留到后续释放。名单不冻结世界状态，也不预留材料。依据：[SW02-A采纳](game-design-workflow/draft-changes/D-2026-09-10-single-release-target-list.md)。

## 对象交互与执行

以下术语依据[已采纳R01–R32](game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md)。

| 术语 | 定义 |
| --- | --- |
| 语义身份 | 区分具体对象及延续关系的身份；同名不代表同一对象。 |
| 对象粒度 | 内容明示的可独立引用层级，包括单位、部件、表面、材料、状态、关系和过程。 |
| 交互能力 | 由材料、结构和当前状态共同决定，允许对应词义作用的资格；能力变化须有明确来源。 |
| 复合对象短语 | 在基础句式名词位置表达结构、条件或关系的组合；新增词义由实际实体词卡承担。 |
| 选择优先级 | 在符合条件的对象中选择单个或限量对象的明示方式，与处理已选对象的顺序分别定义。 |
| 公开对象顺序 | 初始对象的公开顺序及新生对象按确定生成先后获得的位置；不意味着本次直接名单持续追加。 |
| 一次性成本 | 一次法术在首个可结算对象前支付一次的成本，无合法对象不支付；与逐对象成本区别。 |
| 范围锚点 | 战前指定、用于确定法杖范围实际覆盖的位置参照；运行时读取其当前位置。 |
| 独立遗体或残留物 | 内容明确在单位死亡后生成的环境对象，具备自己的身份与能力；不等于原单位继续存活。 |
| 当前剩余冷却 | 某次尚未完成冷却还需要经过的时间，可被适用法术修改；区别于词卡贡献决定的基础冷却。 |
| 可介入窗口 | 尚未完成的过程允许指定操作生效的阶段或时段；演出与已完成记录不提供回滚权限。 |
| 反应根因 | 一次传播或反应链的来源，用于追踪同根因、同对象、同规则的同刻重复作用。 |
| 运行状态与配置 | 运行状态是当前对象与过程情况；配置是战前词卡分配、绑定条件、法杖顺序和镶嵌安排。 |
