# 需要用户处理的设计接口

状态：Needs Decision / Unknown。日期：2026-09-10。核心依据：[Core Concept v0.5](../game-design-workflow/core-concept.md)。

本文集中呈现本次逐份审查无法仅靠已确认内容消除的接口缺口。建议均未采纳，具体候选保存在[inbox](../game-design-workflow/idea-inbox/2026-09-10-design-interface-questions.md)。当前正文只使用明确规则与Unknown，不会同时执行两个互斥裁定。

优先处理C02、C03、C06、C08；C04跟随C03。C05与C07遵守已明确的后置范围，C01仅在对应效果或表现进入设计时处理。文档统一已完成，完整玩法实现与平衡尚需相应决定。

| 编号 | 需要决定的接口 | 当前明确前提 | 建议（未采纳） | 其他可选方向与代价 | 状态 |
| --- | --- | --- | --- | --- | --- |
| C01 | 特殊生命变化的伤害分类与打断表现 | 实际生命伤害才打断正在冷却的普通法术；来源名称不能自行豁免伤害，护甲全挡不打断 | 特殊效果逐条声明“伤害”或“支付生命”；为打断使用独立反馈，正常释放特效仅在实际释放时播放 | 将生命支付也定义为伤害，会影响代价类法术的运行；需要明确设计意图 | Deferred：效果与表现细化时决定 |
| C02 | 多对象法术的材料检查、内部顺序与成功事件 | 战前固定直接对象，失效对象跳过并继续合法对象，完整事件后检查胜负 | 对每个对象独立检查所需材料，材料不足只跳过该对象；目标使用公开固定顺序；处理完完整法术后检查，至少一对象合法结算才满足成功事件 | 整条法术统一预检与原子执行能避免部分消耗，但需解释与逐对象跳过的关系；逐对象检查胜利则改变完整法术边界 | Needs Decision |
| C03 | 战中生成单位如何被战前法术引用，以及循环召唤容量 | 配置与直接目标整场固定；单位模型有独立生命、场上容量和身份；敌方整场攻击默认公开 | 先保留召唤为类型与单位设计素材；完整指挥流程暂缓。若推进，单独设计可在战前明确绑定的单位占位和出生位置 | 每轮选择当前单位会扩展固定目标规则；仅使用预置单位较简单，但改变实际召唤的成长方式。满员后继续尝试或停用也要随循环规则决定 | Needs Decision |
| C04 | 单位专属引用是否需要独立资源形态 | 本场词卡分配固定，卡牌收益战后领取；普通种类词与具体单位身份有区别 | 若C03采用战前单位占位，用占位身份记录指向关系，先不增加额外词卡资源 | 保留专属资源需说明获得时机、战后用途、单位离场清理及实体额度；不能生成后立即改写本场配置 | Dependent：等待C03 |
| C05 | 法杖起点、镶嵌持有、获取、槽位和触发 | 一法术一法杖，范围与特殊效果由法杖配置表达；镶嵌细则明确后置 | 具体镶嵌出现时再决定；可复用公开固定货架、同种候选去重、一层事件响应与计数每战重置作为评议方案 | 同种最多一件、每根可装同种、独立奖励选一件或并入整体收益会形成不同构筑；法杖是否免费配发也尚无依据 | Deferred：按用户要求后置 |
| C06 | 造卡收益与同名上限、产金循环的衔接 | 普通词卡同名持有最多三张；战斗金币与法术产生的卡牌整体领取或放弃 | 在造卡效果中约束产出资格与次数，让结果在进入收益包前已合法；为产金效果明确有限触发或其他实质成本 | 自动转币、溢出舍弃或允许持有超过三张都会新增规则；长时间循环产出可能压过耗时奖金，须由用户选择边界 | Needs Decision |
| C07 | 战场表现与实际环境机制 | 已确认对象变化的发生、发展和结果表现；传播、敌我影响和恢复机制明确后置 | 继续做对象变化描述，BF1–BF3随具体机制重新提出时再确认 | 直接赋予环境伤害、传播或持续收益会新增规则，需要局部资格确认 | Deferred：表现工作可继续 |
| C08 | 词卡时间贡献、循环段长和数值锚点 | 周期＝冷却＋释放；0起点、4冷却、1释放在4刻首释；词卡时间按实际词数贡献合成 | 校准时把词卡合计时间作为冷却候选、释放先用1刻；候选生命100、伤害10、护甲8、敌人40生命且8刻/8伤害、恢复24仅作重新验证输入 | 合计时间作为完整周期会改变释放密度；多刻释放还须确定逐刻覆盖与效果时点。库存18、总编入容量和法杖数量也必须分别决定 | Needs Decision |

## 各组来源与受影响文件

- C01：[伤害关系的原始确认](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-damage-armor-and-interruption.md)；现用[伤害素材](../game-design-workflow/idea-materials/M-2026-09-06-damage-armor-and-interruption.md)。
- C02：[对象关系来源](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md)、[材料与结果检查来源](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-07-first-pass-global-design-baseline.md)；现用[目标素材](../game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md)。
- C03–C04：[容量来源](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-summon-coexistence-and-field-capacity.md)、[承伤与敌方选取来源](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-summon-health-damage-and-enemy-targeting.md)、[专属引用来源](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-summon-reference-generation-and-hand-entry.md)、[单位绑定来源](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-summon-word-references-and-target-locking.md)；现用[召唤素材](../game-design-workflow/idea-materials/M-2026-09-06-summon-unit-and-reference.md)。
- C05：[持有与生效来源](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-07-global-item-ownership-and-passive-effects.md)、[获取来源](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-07-combat-item-rewards-and-settlement.md)、[事件响应来源](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-07-first-pass-global-design-baseline.md)；现用[镶嵌边界](../game-design-workflow/idea-materials/M-2026-09-07-wand-inlay-configuration.md)及[inbox获取候选](../game-design-workflow/idea-inbox/2026-09-07-inlay-acquisition-boundary.md)。
- C06：[普通词卡额度来源](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-new-word-deck-inclusion.md)、[金币来源](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-07-combat-gold-and-efficiency-bonus.md)及[战后收益](../game-design-workflow/idea-materials/M-2026-09-06-normal-combat-word-rewards.md)。
- C07：[用户对表现范围的确认](../game-design-workflow/idea-inbox/2026-09-10-battlefield-physical-transformations.md)。
- C08：[数值输入来源](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-07-core-numerical-framework-v01.md)；现用[校准候选](../game-design-workflow/idea-inbox/2026-09-07-numerical-calibration-candidates.md)。

## 处理方式

可按编号批量确认或修改建议。处理顺序建议为C02、C08、C06，再根据是否推进召唤处理C03和C04；镶嵌与环境具体机制继续后置。确认后先更新对应inbox和合格素材，需要改变核心规则时再走Draft Change与决策记录。
