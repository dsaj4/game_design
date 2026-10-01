# 效果追踪目录

## TL-1效果应用与新增登记（2026-10-01）

旧FX-001–134的身份与原修订保留，下面“原目录”中的当前关联实体均指RC1或更早来源。新版只按本节登记的应用与[当前系统](../design/README.md)生效。原始语义未因登记被抹去；相同效果身份不等于复用旧载体和旧数值。

| 身份／应用 | 新用途、时点与代价 | 状态／依赖 |
| --- | --- | --- |
| FX-001 / TL-app1 | 行动卡生效时对合法敌人普通伤害，先甲后生命；制造成本已经发生，无目标空放 | 基础结果Accepted；TA-01／04数字Proposed；TL-08／21 |
| FX-002 / TL-app1 | 行动卡生效给予玩家护甲；不自动挡住独立打断 | 基础结果沿用；TA-02数字Proposed；TL-11／12 |
| FX-031 / TL-app1 | TA-03取消已揭示待发敌牌，普通队列且必须早于T；敌方明确中断指定杖则退加工料丢进度 | 结构Accepted；两种载体权限分别声明，不能相互代用；TL-07／10 |
| [FX-135](#fx-135) | 资源卡配方转化 | 结构Accepted，TS-01–03具体配方Proposed |
| [FX-136](#fx-136) | 高阶产物维护与休眠恢复 | 结构Accepted，周期／耗量／托管细则待定 |
| [FX-137](#fx-137) | 消耗材料提升同一高阶产物增幅 | 支持增幅方向，TS-08完整效果Proposed |

<a id="fx-135"></a>

### FX-135 资源卡配方转化

修订r1 / TL-1。分类：资源转换、产物。触发：合法程序取得完整材料后加工，完成后交付资源区，最早下拍使用。目标：配方允许的材料；成本：真实托管与消耗及加工时间。顺序：维护优先再按杖序分料，不能同卡两用。加工中断退料不产物；成功后的材料提交时点和满位退回细则待闭合。叠加按具体资源容量／单位声明，无无限同拍链。正例：灵屑加工火种；边界：缺半份料不得重复分配；反例：免费改线变换已成品。来源：新卡表M，验证TL-V03／04／07／19。Hypothesis / NotRun。

<a id="fx-136"></a>

### FX-136 高阶产物自动维护、休眠与恢复

修订r1 / TL-1。分类：资源支付、运行状态。维护不足休眠并保留身份与增幅，补料自动恢复；维护先于新加工分料。维护周期、量、对象内部争用、托管中是否维护及欠账细则Unknown，不能声明语义完全闭合。多产物不合并身份免费共付一份维护。跨战只保留选中资源数量，运行状态与增幅重置。正例：缺料休眠后恢复；边界：多产物同刻到期；反例：每次缺料弹确认强迫操作。来源：INT-06／08／13与TL-22／23／25；TL-V18／19／22。Hypothesis / NotRun。

<a id="fx-137"></a>

### FX-137 消耗材料增幅同一高阶资源

修订r1 / TL-1。分类：产物强化。候选TS-08托管辉核并付火种、耗时，成功后返还同一身份并加增幅；上限与伤害公式为候选数字，不自动采纳。中断按生产规则退输入，既有增幅不凭返工增加；休眠期能否接受加工待定。达到上限时不吃料空转为候选边界。增幅不复制资源身份，跨战清零。正例：付火种换后续更大攻击；边界：被打断／维护到期；反例：复制两个满级辉核。来源：新卡表M，待输入冻结后同预算比较，NotRun。

新增登记共同来源：[核心M](../exploration/DIR-028-timeline-depth/M-2026-10-01-timeline-production-core.md)／[卡表M](../exploration/DIR-028-timeline-depth/M-2026-10-01-resource-card-pool.md)／[采纳D](../sources/draft-changes/D-2026-10-01-timeline-production-core.md)。具体付费干涉能力按用户要求延期，不在FX中补造能力。

## 原目录：RC1与更早版本

Project ID：game-002。文档角色：Navigation / EffectTrace。2026-09-30 / layout.3。原134个稳定FX身份；本轮另增3个，共137个，不等于137张卡。修订号属于各效果语义历史；当前规则由GDD统一维护。

| 效果 | 原语义修订 | 原版本关联实体（非全部变体采纳） |
| --- | --- | --- |
| [FX-001 造成直接伤害](catalog.md#fx-001) | r3 | S2-V01 |
| [FX-002 获得护甲](catalog.md#fx-002) | r3 | E3-N05、S2-N02、S2-V02 |
| [FX-003 施加燃烧及其状态效果](catalog.md#fx-003) | r9 | E3-N03 |
| [FX-004 施加冰冻及其状态效果](catalog.md#fx-004) | r8 | E3-N04 |
| [FX-005 熄灭燃烧](catalog.md#fx-005) | r3 | E3-V09、S2-V05 |
| [FX-006 解除冰冻等明确状态](catalog.md#fx-006) | r3 | E3-V09、S2-V05 |
| [FX-007 改变状态数量](catalog.md#fx-007) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-008 燃烧加倍](catalog.md#fx-008) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-009 燃烧蔓延](catalog.md#fx-009) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-010 生成与引用火焰](catalog.md#fx-010) | r5 | E3-N01 |
| [FX-011 生成与引用雷电](catalog.md#fx-011) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-012 生成与引用冰霜](catalog.md#fx-012) | r3 | E3-N02 |
| [FX-013 强化元素](catalog.md#fx-013) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-014 削弱元素](catalog.md#fx-014) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-015 抵挡尚未完成的作用](catalog.md#fx-015) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-016 反弹尚未完成的作用](catalog.md#fx-016) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-017 自动转移尚未完成的作用](catalog.md#fx-017) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-018 加速当前冷却](catalog.md#fx-018) | r3 | S2-N05 |
| [FX-019 延迟或加速其他未完成时间](catalog.md#fx-019) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-020 对合格对象收集并掉卡](catalog.md#fx-020) | r2 | 公共规则或历史方向；见条目来源 |
| [FX-021 召唤恶魔及召唤引用](catalog.md#fx-021) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-022 强化已有召唤物](catalog.md#fx-022) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-023 消耗护甲](catalog.md#fx-023) | r5 | E3-V04 |
| [FX-024 寒冷的：护甲通用分支](catalog.md#fx-024) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-025 寒冷的：寒冰适配分支](catalog.md#fx-025) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-026 简易法术隔周期减冷却](catalog.md#fx-026) | r4 | 公共规则或历史方向；见条目来源 |
| [FX-027 燃烧施加范围强化](catalog.md#fx-027) | r4 | 公共规则或历史方向；见条目来源 |
| [FX-028 力量等许可属性的强化](catalog.md#fx-028) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-029 战内恢复及吸血方向](catalog.md#fx-029) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-030 有限产金](catalog.md#fx-030) | r2 | 公共规则或历史方向；见条目来源 |
| [FX-031 取消一次未完成过程](catalog.md#fx-031) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-032 清除护甲](catalog.md#fx-032) | r3 | S2-V05 |
| [FX-033 多次释放方向（待拆清事件）](catalog.md#fx-033) | r4 | S2-A03、S2-I01、S2-N04 |
| [FX-034 叠加爆发方向（待定义累积与兑现）](catalog.md#fx-034) | r4 | S2-I02 |
| [FX-035 施加印记](catalog.md#fx-035) | r3 | S2-N03、S2-V03 |
| [FX-036 获得与蓄积可消耗能量](catalog.md#fx-036) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-037 回响状态授权再次施法](catalog.md#fx-037) | r3 | S2-N04、S2-V02 |
| [FX-038 消耗可引爆状态转为伤害](catalog.md#fx-038) | r3 | E3-V06、S2-V04 |
| [FX-039 轻巧名词使本句冷却更快](catalog.md#fx-039) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-040 充盈名词增强本句所得](catalog.md#fx-040) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-041 锋利生成物对护甲特攻](catalog.md#fx-041) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-042 带电作用附加电击](catalog.md#fx-042) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-043 双生元素生成](catalog.md#fx-043) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-044 延长本句产物存续](catalog.md#fx-044) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-045 生成物在场蓄势](catalog.md#fx-045) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-046 易燃对象增加燃烧施加](catalog.md#fx-046) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-047 生成物消散爆裂](catalog.md#fx-047) | r3 | E3-A05 |
| [FX-048 本杖连续成功增强](catalog.md#fx-048) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-049 强化开战首法术](catalog.md#fx-049) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-050 强化额外复诵](catalog.md#fx-050) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-051 同目标连续作用增强](catalog.md#fx-051) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-052 攻防交替支援](catalog.md#fx-052) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-053 击破护甲后续加速](catalog.md#fx-053) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-054 燃烧目标直接增伤](catalog.md#fx-054) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-055 消耗冰冻强化当次伤害](catalog.md#fx-055) | r3 | S2-I09 |
| [FX-056 被覆盖后续加速](catalog.md#fx-056) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-057 护甲存续冷却加速](catalog.md#fx-057) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-058 元素生成后续加速](catalog.md#fx-058) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-059 温和攻击避开友方](catalog.md#fx-059) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-060 火焰元素邻近施加燃烧](catalog.md#fx-060) | r2 | 公共规则或历史方向；见条目来源 |
| [FX-061 环境元素阈值与形态推进](catalog.md#fx-061) | r3 | 公共规则或历史方向；见条目来源 |
| [FX-062 环境已达形态保留（含烧焦）](catalog.md#fx-062) | r3 | 公共规则或历史方向；见条目来源 |
| [FX-063 元素释放生成、叠层与满位回退](catalog.md#fx-063) | r3 | E3-N01、E3-N02、E3-V01 |
| [FX-064 元素共享状态层数与归零消散](catalog.md#fx-064) | r4 | E3-N01、E3-N02 |
| [FX-065 环境转化元素并继承状态](catalog.md#fx-065) | r9 | 公共规则或历史方向；见条目来源 |
| [FX-066 固有属性克制修正元素状态](catalog.md#fx-066) | r2 | 公共规则或历史方向；见条目来源 |
| [FX-067 单元素状态互斥、抵消与替换](catalog.md#fx-067) | r3 | 公共规则或历史方向；见条目来源 |
| [FX-068 元素邻近施加对应状态](catalog.md#fx-068) | r5 | E3-N01、E3-N02 |
| [FX-069 释放作用下异种元素消散后的补生](catalog.md#fx-069) | r5 | 公共规则或历史方向；见条目来源 |
| [FX-070 消耗火焰爆裂](catalog.md#fx-070) | r3 | E3-V08 |
| [FX-071 消耗冰霜凝甲](catalog.md#fx-071) | r3 | E3-V07 |
| [FX-072 燃烧伤害增强](catalog.md#fx-072) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-073 冰冻护甲收益增强](catalog.md#fx-073) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-074 元素层数自然衰减减缓](catalog.md#fx-074) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-075 元素初始层数与衰减同时增强](catalog.md#fx-075) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-076 缩小邻近范围并增强施加量](catalog.md#fx-076) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-077 扩大邻近范围并降低施加量](catalog.md#fx-077) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-078 提高消耗护甲的元素转层收益](catalog.md#fx-078) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-079 冰霜邻近施加仅限友方](catalog.md#fx-079) | r4 | E3-A01 |
| [FX-080 火焰邻近施加排除友方](catalog.md#fx-080) | r3 | E3-A02 |
| [FX-081 元素少邻居时增强邻近施加](catalog.md#fx-081) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-082 元素多邻居时增强邻近施加](catalog.md#fx-082) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-083 本句环境转化阈值降低](catalog.md#fx-083) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-084 范围内冰冻施加量增强](catalog.md#fx-084) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-085 元素自然消散强化下次同种释放](catalog.md#fx-085) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-086 满位回退时增强状态施加](catalog.md#fx-086) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-087 同种元素叠层增强](catalog.md#fx-087) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-088 元素替换成功加速本杖冷却](catalog.md#fx-088) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-089 环境转化成功强化下次伤害](catalog.md#fx-089) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-090 冰冻为自己增甲后缩短下次释放](catalog.md#fx-090) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-091 消耗护甲强化下次元素直接伤害](catalog.md#fx-091) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-092 对已有冰冻宿主增加护甲增强](catalog.md#fx-092) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-093 主动消耗元素层数加速后续冷却](catalog.md#fx-093) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-094 凝甲后存续冰霜强化下次邻近施加](catalog.md#fx-094) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-095 主动耗尽元素缩短下次元素释放](catalog.md#fx-095) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-096 交替释放火冰增强后次施加量](catalog.md#fx-096) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-097 同种状态转为执行元素层数](catalog.md#fx-097) | r3 | E3-V02 |
| [FX-098 消耗元素层数定向施加对应状态](catalog.md#fx-098) | r3 | E3-V03 |
| [FX-099 场上元素转为法杖封存资源](catalog.md#fx-099) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-100 封存储量供给完整元素释放](catalog.md#fx-100) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-101 敌方护甲转为玩家护甲](catalog.md#fx-101) | r3 | E3-V05 |
| [FX-102 主动火冰抵消兑现玩家护甲](catalog.md#fx-102) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-103 邻近施加提前并扣除未来一次](catalog.md#fx-103) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-104 邻近施加延后并合并后续输出](catalog.md#fx-104) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-105 自动邻近改由主动操控触发](catalog.md#fx-105) | r3 | E3-I01 |
| [FX-106 元素操控改从元素所在格计算范围](catalog.md#fx-106) | r4 | E3-I02 |
| [FX-107 满位回退由状态施加改为直接攻防](catalog.md#fx-107) | r3 | E3-I03 |
| [FX-108 异种抵消的施加消耗回收为封存储量](catalog.md#fx-108) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-109 异种状态抵消触发原状态收尾收益](catalog.md#fx-109) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-110 他人冰冻增甲时玩家同步获得护甲](catalog.md#fx-110) | r3 | E3-I04 |
| [FX-111 消散记录格子供后续生成优先选择](catalog.md#fx-111) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-112 元素替换继承兼容的一次性强化](catalog.md#fx-112) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-113 封存储量跨元素供给解封](catalog.md#fx-113) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-114 主动元素消耗的收益改为后续分次兑现](catalog.md#fx-114) | r1 | 公共规则或历史方向；见条目来源 |
| [FX-115 已有同种时补层替换为邻近施加](catalog.md#fx-115) | r3 | E3-I05 |
| [FX-116 冰冻增甲结果替换为宿主伤害](catalog.md#fx-116) | r3 | E3-I06 |
| [FX-117 异种抵消后禁止新态与补生](catalog.md#fx-117) | r3 | E3-I07 |
| [FX-118 燃烧被清空时伤害原宿主](catalog.md#fx-118) | r3 | E3-I08 |
| [FX-119 燃烧损耗护甲为源火焰补层](catalog.md#fx-119) | r3 | E3-I09 |
| [FX-120 元素直接伤害损耗护甲为己增甲](catalog.md#fx-120) | r3 | E3-I10 |
| [FX-121 元素关闭自动邻近施加](catalog.md#fx-121) | r4 | E3-A03 |
| [FX-122 法术补层触发邻近施加](catalog.md#fx-122) | r3 | E3-A04 |
| [FX-123 自然衰减改由邻近施加支付层数](catalog.md#fx-123) | r4 | E3-A06 |
| [FX-124 破甲触发本杖完整复诵](catalog.md#fx-124) | r3 | S2-I03 |
| [FX-125 本杖直接伤敌与己方护甲收益互换](catalog.md#fx-125) | r3 | S2-I04 |
| [FX-126 无护甲时直接伤敌改为自身护甲](catalog.md#fx-126) | r3 | S2-I05 |
| [FX-127 本杖直接命中附加印记](catalog.md#fx-127) | r3 | S2-I06 |
| [FX-128 本杖冷却免于生命伤害打断](catalog.md#fx-128) | r3 | S2-I07 |
| [FX-129 消耗印记后下个循环跳过冷却](catalog.md#fx-129) | r3 | S2-I08 |
| [FX-130 使指定当前冷却完成](catalog.md#fx-130) | r3 | S2-V06 |
| [FX-131 本句伤害绕过目标护甲](catalog.md#fx-131) | r3 | S2-A01 |
| [FX-132 护甲实际抵伤后反击攻击者](catalog.md#fx-132) | r3 | S2-A02 |
| [FX-133 本句目标筛选为已有印记敌人](catalog.md#fx-133) | r3 | S2-A04 |
| [FX-134 印记引爆后保留](catalog.md#fx-134) | r3 | S2-A05 |

[整理前目录与关系](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/catalog.md)。无实体关联只表示该登记首段未列出首版ID，不能据此判定整个效果被拒绝；公共规则按系统正文检索。


## 登记口径

每个 FX 的身份、原语义修订、适用范围、证据、实体与参数链接集中在本页；134 个 FX 不等于134张现行卡。历史变体不自动采纳。公共执行规则以 design 为准，历史完整文本按固定 Git 提交追溯。

<a id="fx-001"></a>

### FX-001 造成直接伤害

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-001.md) |
| 当前关联实体 | [S2-V01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-v01) |
| 统一参数 | [S2-V01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-v01) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-002"></a>

### FX-002 获得护甲

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-002.md) |
| 当前关联实体 | [E3-N05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-n05)、[S2-N02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-n02)、[S2-V02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-v02) |
| 统一参数 | [E3-N05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-n05)、[S2-N02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-n02)、[S2-V02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-v02) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-003"></a>

### FX-003 施加燃烧及其状态效果

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-003.md) |
| 当前关联实体 | [E3-N03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-n03) |
| 统一参数 | [E3-N03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-n03) |

原语义修订：r9。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-004"></a>

### FX-004 施加冰冻及其状态效果

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-004.md) |
| 当前关联实体 | [E3-N04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-n04) |
| 统一参数 | [E3-N04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-n04) |

原语义修订：r8。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-005"></a>

### FX-005 熄灭燃烧

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-005.md) |
| 当前关联实体 | [E3-V09](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-v09)、[S2-V05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-v05) |
| 统一参数 | [E3-V09](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-v09)、[S2-V05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-v05) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-006"></a>

### FX-006 解除冰冻等明确状态

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-006.md) |
| 当前关联实体 | [E3-V09](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-v09)、[S2-V05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-v05) |
| 统一参数 | [E3-V09](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-v09)、[S2-V05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-v05) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-007"></a>

### FX-007 改变状态数量

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-007.md) |

原语义修订：r1。

来源：
- [M-2026-09-06-status-reapplication-and-stacking.md](../sources/materials/M-2026-09-06-status-reapplication-and-stacking.md)
- [M-2026-09-11-global-rule-boundaries.md](../sources/materials/M-2026-09-11-global-rule-boundaries.md)
- [能力方向](../sources/inbox/2026-09-10-semantic-ability-word-catalog.md)

<a id="fx-008"></a>

### FX-008 燃烧加倍

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-008.md) |

原语义修订：r1。

来源：
- [M-2026-09-11-spell-type-system.md](../sources/materials/M-2026-09-11-spell-type-system.md)

<a id="fx-009"></a>

### FX-009 燃烧蔓延

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-009.md) |

原语义修订：r1。

来源：
- [M-2026-09-11-spell-type-system.md](../sources/materials/M-2026-09-11-spell-type-system.md)
- [M-2026-09-10-simple-object-interactions.md](../sources/materials/M-2026-09-10-simple-object-interactions.md)

<a id="fx-010"></a>

### FX-010 生成与引用火焰

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-010.md) |
| 当前关联实体 | [E3-N01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-n01) |
| 统一参数 | [E3-N01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-n01) |

原语义修订：r5。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-011"></a>

### FX-011 生成与引用雷电

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-011.md) |

原语义修订：r1。

来源：
- [M-2026-09-10-simple-object-interactions.md](../sources/materials/M-2026-09-10-simple-object-interactions.md)
- [M-2026-09-10-semantic-world-executable-rules.md](../sources/materials/M-2026-09-10-semantic-world-executable-rules.md)
- [M-2026-09-11-spell-type-system.md](../sources/materials/M-2026-09-11-spell-type-system.md)
- [Parked词效来源](../sources/inbox/2026-09-10-element-state-drop-wording.md)

<a id="fx-012"></a>

### FX-012 生成与引用冰霜

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-012.md) |
| 当前关联实体 | [E3-N02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-n02) |
| 统一参数 | [E3-N02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-n02) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-013"></a>

### FX-013 强化元素

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-013.md) |

原语义修订：r1。

来源：
- [M-2026-09-10-simple-object-interactions.md](../sources/materials/M-2026-09-10-simple-object-interactions.md)
- [M-2026-09-11-spell-type-system.md](../sources/materials/M-2026-09-11-spell-type-system.md)
- [Parked词效来源](../sources/inbox/2026-09-10-element-state-drop-wording.md)

<a id="fx-014"></a>

### FX-014 削弱元素

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-014.md) |

原语义修订：r1。

来源：
- [M-2026-09-10-simple-object-interactions.md](../sources/materials/M-2026-09-10-simple-object-interactions.md)
- [M-2026-09-11-spell-type-system.md](../sources/materials/M-2026-09-11-spell-type-system.md)
- [Parked词效来源](../sources/inbox/2026-09-10-element-state-drop-wording.md)

<a id="fx-015"></a>

### FX-015 抵挡尚未完成的作用

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-015.md) |

原语义修订：r1。

来源：
- [M-2026-09-10-simple-object-interactions.md](../sources/materials/M-2026-09-10-simple-object-interactions.md)
- [M-2026-09-10-semantic-world-executable-rules.md](../sources/materials/M-2026-09-10-semantic-world-executable-rules.md)
- [Parked词效来源](../sources/inbox/2026-09-10-element-state-drop-wording.md)
- [能力方向](../sources/inbox/2026-09-10-semantic-ability-word-catalog.md)

<a id="fx-016"></a>

### FX-016 反弹尚未完成的作用

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-016.md) |

原语义修订：r1。

来源：
- [M-2026-09-10-simple-object-interactions.md](../sources/materials/M-2026-09-10-simple-object-interactions.md)
- [M-2026-09-10-semantic-world-executable-rules.md](../sources/materials/M-2026-09-10-semantic-world-executable-rules.md)
- [能力方向](../sources/inbox/2026-09-10-semantic-ability-word-catalog.md)

<a id="fx-017"></a>

### FX-017 自动转移尚未完成的作用

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-017.md) |

原语义修订：r1。

来源：
- [M-2026-09-10-simple-object-interactions.md](../sources/materials/M-2026-09-10-simple-object-interactions.md)
- [M-2026-09-10-semantic-world-executable-rules.md](../sources/materials/M-2026-09-10-semantic-world-executable-rules.md)
- [能力方向](../sources/inbox/2026-09-10-semantic-ability-word-catalog.md)

<a id="fx-018"></a>

### FX-018 加速当前冷却

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-018.md) |
| 当前关联实体 | [S2-N05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-n05) |
| 统一参数 | [S2-N05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-n05) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-019"></a>

### FX-019 延迟或加速其他未完成时间

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-019.md) |

原语义修订：r1。

来源：
- [M-2026-09-10-semantic-world-executable-rules.md](../sources/materials/M-2026-09-10-semantic-world-executable-rules.md)
- [M-2026-09-10-simple-object-interactions.md](../sources/materials/M-2026-09-10-simple-object-interactions.md)
- [能力方向](../sources/inbox/2026-09-10-semantic-ability-word-catalog.md)

<a id="fx-020"></a>

### FX-020 对合格对象收集并掉卡

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-020.md) |

原语义修订：r2。

来源：
- [BR v1](../sources/materials/M-2026-09-13-pre-gdd-recommendation-batch.md)
- [M-2026-09-10-simple-object-interactions.md](../sources/materials/M-2026-09-10-simple-object-interactions.md)
- [M-2026-09-11-global-rule-boundaries.md](../sources/materials/M-2026-09-11-global-rule-boundaries.md)
- [Parked词效来源](../sources/inbox/2026-09-10-element-state-drop-wording.md)

<a id="fx-021"></a>

### FX-021 召唤恶魔及召唤引用

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-021.md) |

原语义修订：r1。

来源：
- [M-2026-09-11-spell-type-system.md](../sources/materials/M-2026-09-11-spell-type-system.md)
- [M-2026-09-07-supporting-design-rules.md](../sources/materials/M-2026-09-07-supporting-design-rules.md)

<a id="fx-022"></a>

### FX-022 强化已有召唤物

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-022.md) |

原语义修订：r1。

来源：
- [M-2026-09-11-spell-type-system.md](../sources/materials/M-2026-09-11-spell-type-system.md)

<a id="fx-023"></a>

### FX-023 消耗护甲

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-023.md) |
| 当前关联实体 | [E3-V04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-v04) |
| 统一参数 | [E3-V04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-v04) |

原语义修订：r5。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-024"></a>

### FX-024 寒冷的：护甲通用分支

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-024.md) |

原语义修订：r1。

来源：
- [M-2026-09-11-modifier-card-system.md](../sources/materials/M-2026-09-11-modifier-card-system.md)

<a id="fx-025"></a>

### FX-025 寒冷的：寒冰适配分支

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-025.md) |

原语义修订：r1。

来源：
- [M-2026-09-11-modifier-card-system.md](../sources/materials/M-2026-09-11-modifier-card-system.md)

<a id="fx-026"></a>

### FX-026 简易法术隔周期减冷却

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-026.md) |

原语义修订：r4。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-027"></a>

### FX-027 燃烧施加范围强化

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-027.md) |

原语义修订：r4。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-028"></a>

### FX-028 力量等许可属性的强化

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-028.md) |

原语义修订：r1。

来源：
- [M-2026-09-07-supporting-design-rules.md](../sources/materials/M-2026-09-07-supporting-design-rules.md)
- [M-2026-09-10-simple-object-interactions.md](../sources/materials/M-2026-09-10-simple-object-interactions.md)
- [能力方向](../sources/inbox/2026-09-10-semantic-ability-word-catalog.md)

<a id="fx-029"></a>

### FX-029 战内恢复及吸血方向

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-029.md) |

原语义修订：r1。

来源：
- [M-2026-09-07-supporting-design-rules.md](../sources/materials/M-2026-09-07-supporting-design-rules.md)

<a id="fx-030"></a>

### FX-030 有限产金

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-030.md) |

原语义修订：r2。

来源：
- [BR v1](../sources/materials/M-2026-09-13-pre-gdd-recommendation-batch.md)
- [M-2026-09-07-supporting-design-rules.md](../sources/materials/M-2026-09-07-supporting-design-rules.md)
- [M-2026-09-11-global-rule-boundaries.md](../sources/materials/M-2026-09-11-global-rule-boundaries.md)

<a id="fx-031"></a>

### FX-031 取消一次未完成过程

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-031.md) |

原语义修订：r1。

来源：
- [M-2026-09-10-semantic-world-executable-rules.md](../sources/materials/M-2026-09-10-semantic-world-executable-rules.md)
- [M-2026-09-11-global-rule-boundaries.md](../sources/materials/M-2026-09-11-global-rule-boundaries.md)

<a id="fx-032"></a>

### FX-032 清除护甲

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-032.md) |
| 当前关联实体 | [S2-V05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-v05) |
| 统一参数 | [S2-V05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-v05) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-033"></a>

### FX-033 多次释放方向（待拆清事件）

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-033.md) |
| 当前关联实体 | [S2-A03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-a03)、[S2-I01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-i01)、[S2-N04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-n04) |
| 统一参数 | [S2-A03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-a03)、[S2-I01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-i01)、[S2-N04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-n04) |

原语义修订：r4。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-034"></a>

### FX-034 叠加爆发方向（待定义累积与兑现）

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-034.md) |
| 当前关联实体 | [S2-I02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-i02) |
| 统一参数 | [S2-I02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-i02) |

原语义修订：r4。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-035"></a>

### FX-035 施加印记

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-035.md) |
| 当前关联实体 | [S2-N03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-n03)、[S2-V03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-v03) |
| 统一参数 | [S2-N03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-n03)、[S2-V03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-v03) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-036"></a>

### FX-036 获得与蓄积可消耗能量

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-036.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-037"></a>

### FX-037 回响状态授权再次施法

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-037.md) |
| 当前关联实体 | [S2-N04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-n04)、[S2-V02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-v02) |
| 统一参数 | [S2-N04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-n04)、[S2-V02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-v02) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-038"></a>

### FX-038 消耗可引爆状态转为伤害

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-038.md) |
| 当前关联实体 | [E3-V06](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-v06)、[S2-V04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-v04) |
| 统一参数 | [E3-V06](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-v06)、[S2-V04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-v04) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-039"></a>

### FX-039 轻巧名词使本句冷却更快

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-039.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-040"></a>

### FX-040 充盈名词增强本句所得

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-040.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-041"></a>

### FX-041 锋利生成物对护甲特攻

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-041.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-042"></a>

### FX-042 带电作用附加电击

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-042.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-043"></a>

### FX-043 双生元素生成

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-043.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-044"></a>

### FX-044 延长本句产物存续

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-044.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-045"></a>

### FX-045 生成物在场蓄势

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-045.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-046"></a>

### FX-046 易燃对象增加燃烧施加

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-046.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-047"></a>

### FX-047 生成物消散爆裂

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-047.md) |
| 当前关联实体 | [E3-A05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-a05) |
| 统一参数 | [E3-A05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-a05) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-048"></a>

### FX-048 本杖连续成功增强

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-048.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-049"></a>

### FX-049 强化开战首法术

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-049.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-050"></a>

### FX-050 强化额外复诵

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-050.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-051"></a>

### FX-051 同目标连续作用增强

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-051.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-052"></a>

### FX-052 攻防交替支援

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-052.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-053"></a>

### FX-053 击破护甲后续加速

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-053.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-054"></a>

### FX-054 燃烧目标直接增伤

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-054.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-055"></a>

### FX-055 消耗冰冻强化当次伤害

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-055.md) |
| 当前关联实体 | [S2-I09](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-i09) |
| 统一参数 | [S2-I09](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-i09) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-056"></a>

### FX-056 被覆盖后续加速

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-056.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-057"></a>

### FX-057 护甲存续冷却加速

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-057.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-058"></a>

### FX-058 元素生成后续加速

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-058.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-059"></a>

### FX-059 温和攻击避开友方

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-059.md) |

原语义修订：r1。

来源：
- [第一期创意卡池](../sources/inbox/2026-09-12-simple-spell-creative-card-pool.md)

<a id="fx-060"></a>

### FX-060 火焰元素邻近施加燃烧

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-060.md) |

原语义修订：r2。

来源：
- [通用元素机制](../sources/materials/M-2026-09-12-element-spell-archetype.md)
- [合格素材](../sources/materials/M-2026-09-12-first-person-grid-battlefield.md)

<a id="fx-061"></a>

### FX-061 环境元素阈值与形态推进

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-061.md) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-062"></a>

### FX-062 环境已达形态保留（含烧焦）

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-062.md) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-063"></a>

### FX-063 元素释放生成、叠层与满位回退

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-063.md) |
| 当前关联实体 | [E3-N01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-n01)、[E3-N02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-n02)、[E3-V01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-v01) |
| 统一参数 | [E3-N01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-n01)、[E3-N02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-n02)、[E3-V01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-v01) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-064"></a>

### FX-064 元素共享状态层数与归零消散

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-064.md) |
| 当前关联实体 | [E3-N01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-n01)、[E3-N02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-n02) |
| 统一参数 | [E3-N01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-n01)、[E3-N02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-n02) |

原语义修订：r4。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-065"></a>

### FX-065 环境转化元素并继承状态

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-065.md) |

原语义修订：r9。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-066"></a>

### FX-066 固有属性克制修正元素状态

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-066.md) |

原语义修订：r2。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-067"></a>

### FX-067 单元素状态互斥、抵消与替换

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-067.md) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-068"></a>

### FX-068 元素邻近施加对应状态

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-068.md) |
| 当前关联实体 | [E3-N01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-n01)、[E3-N02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-n02) |
| 统一参数 | [E3-N01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-n01)、[E3-N02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-n02) |

原语义修订：r5。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-069"></a>

### FX-069 释放作用下异种元素消散后的补生

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-069.md) |

原语义修订：r5。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-070"></a>

### FX-070 消耗火焰爆裂

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-070.md) |
| 当前关联实体 | [E3-V08](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-v08) |
| 统一参数 | [E3-V08](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-v08) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-071"></a>

### FX-071 消耗冰霜凝甲

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-071.md) |
| 当前关联实体 | [E3-V07](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-v07) |
| 统一参数 | [E3-V07](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-v07) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-072"></a>

### FX-072 燃烧伤害增强

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-072.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-073"></a>

### FX-073 冰冻护甲收益增强

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-073.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-074"></a>

### FX-074 元素层数自然衰减减缓

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-074.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-075"></a>

### FX-075 元素初始层数与衰减同时增强

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-075.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-076"></a>

### FX-076 缩小邻近范围并增强施加量

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-076.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-077"></a>

### FX-077 扩大邻近范围并降低施加量

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-077.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-078"></a>

### FX-078 提高消耗护甲的元素转层收益

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-078.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-079"></a>

### FX-079 冰霜邻近施加仅限友方

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-079.md) |
| 当前关联实体 | [E3-A01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-a01) |
| 统一参数 | [E3-A01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-a01) |

原语义修订：r4。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-080"></a>

### FX-080 火焰邻近施加排除友方

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-080.md) |
| 当前关联实体 | [E3-A02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-a02) |
| 统一参数 | [E3-A02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-a02) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-081"></a>

### FX-081 元素少邻居时增强邻近施加

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-081.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-082"></a>

### FX-082 元素多邻居时增强邻近施加

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-082.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-083"></a>

### FX-083 本句环境转化阈值降低

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-083.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-084"></a>

### FX-084 范围内冰冻施加量增强

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-084.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-085"></a>

### FX-085 元素自然消散强化下次同种释放

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-085.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-086"></a>

### FX-086 满位回退时增强状态施加

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-086.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-087"></a>

### FX-087 同种元素叠层增强

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-087.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-088"></a>

### FX-088 元素替换成功加速本杖冷却

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-088.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-089"></a>

### FX-089 环境转化成功强化下次伤害

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-089.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-090"></a>

### FX-090 冰冻为自己增甲后缩短下次释放

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-090.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-091"></a>

### FX-091 消耗护甲强化下次元素直接伤害

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-091.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-092"></a>

### FX-092 对已有冰冻宿主增加护甲增强

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-092.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-093"></a>

### FX-093 主动消耗元素层数加速后续冷却

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-093.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-094"></a>

### FX-094 凝甲后存续冰霜强化下次邻近施加

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-094.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-095"></a>

### FX-095 主动耗尽元素缩短下次元素释放

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-095.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-096"></a>

### FX-096 交替释放火冰增强后次施加量

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-096.md) |

原语义修订：r1。

来源：
- [元素创意卡池](../sources/inbox/2026-09-13-element-spell-creative-card-pool.md)

<a id="fx-097"></a>

### FX-097 同种状态转为执行元素层数

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-097.md) |
| 当前关联实体 | [E3-V02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-v02) |
| 统一参数 | [E3-V02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-v02) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-098"></a>

### FX-098 消耗元素层数定向施加对应状态

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-098.md) |
| 当前关联实体 | [E3-V03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-v03) |
| 统一参数 | [E3-V03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-v03) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-099"></a>

### FX-099 场上元素转为法杖封存资源

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-099.md) |

原语义修订：r1。

来源：
- [元素第二期机制卡池](../sources/inbox/2026-09-13-element-spell-mechanism-card-pool-02.md)

<a id="fx-100"></a>

### FX-100 封存储量供给完整元素释放

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-100.md) |

原语义修订：r1。

来源：
- [元素第二期机制卡池](../sources/inbox/2026-09-13-element-spell-mechanism-card-pool-02.md)

<a id="fx-101"></a>

### FX-101 敌方护甲转为玩家护甲

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-101.md) |
| 当前关联实体 | [E3-V05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-v05) |
| 统一参数 | [E3-V05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-v05) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-102"></a>

### FX-102 主动火冰抵消兑现玩家护甲

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-102.md) |

原语义修订：r1。

来源：
- [元素第二期机制卡池](../sources/inbox/2026-09-13-element-spell-mechanism-card-pool-02.md)

<a id="fx-103"></a>

### FX-103 邻近施加提前并扣除未来一次

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-103.md) |

原语义修订：r1。

来源：
- [元素第二期机制卡池](../sources/inbox/2026-09-13-element-spell-mechanism-card-pool-02.md)

<a id="fx-104"></a>

### FX-104 邻近施加延后并合并后续输出

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-104.md) |

原语义修订：r1。

来源：
- [元素第二期机制卡池](../sources/inbox/2026-09-13-element-spell-mechanism-card-pool-02.md)

<a id="fx-105"></a>

### FX-105 自动邻近改由主动操控触发

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-105.md) |
| 当前关联实体 | [E3-I01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-i01) |
| 统一参数 | [E3-I01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-i01) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-106"></a>

### FX-106 元素操控改从元素所在格计算范围

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-106.md) |
| 当前关联实体 | [E3-I02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-i02) |
| 统一参数 | [E3-I02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-i02) |

原语义修订：r4。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-107"></a>

### FX-107 满位回退由状态施加改为直接攻防

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-107.md) |
| 当前关联实体 | [E3-I03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-i03) |
| 统一参数 | [E3-I03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-i03) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-108"></a>

### FX-108 异种抵消的施加消耗回收为封存储量

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-108.md) |

原语义修订：r1。

来源：
- [元素第二期机制卡池](../sources/inbox/2026-09-13-element-spell-mechanism-card-pool-02.md)

<a id="fx-109"></a>

### FX-109 异种状态抵消触发原状态收尾收益

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-109.md) |

原语义修订：r1。

来源：
- [元素第二期机制卡池](../sources/inbox/2026-09-13-element-spell-mechanism-card-pool-02.md)

<a id="fx-110"></a>

### FX-110 他人冰冻增甲时玩家同步获得护甲

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-110.md) |
| 当前关联实体 | [E3-I04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-i04) |
| 统一参数 | [E3-I04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-i04) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-111"></a>

### FX-111 消散记录格子供后续生成优先选择

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-111.md) |

原语义修订：r1。

来源：
- [元素第二期机制卡池](../sources/inbox/2026-09-13-element-spell-mechanism-card-pool-02.md)

<a id="fx-112"></a>

### FX-112 元素替换继承兼容的一次性强化

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-112.md) |

原语义修订：r1。

来源：
- [元素第二期机制卡池](../sources/inbox/2026-09-13-element-spell-mechanism-card-pool-02.md)

<a id="fx-113"></a>

### FX-113 封存储量跨元素供给解封

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-113.md) |

原语义修订：r1。

来源：
- [元素第二期机制卡池](../sources/inbox/2026-09-13-element-spell-mechanism-card-pool-02.md)

<a id="fx-114"></a>

### FX-114 主动元素消耗的收益改为后续分次兑现

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 公共规则或历史方向；不按此ID自动开放可获得内容 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-114.md) |

原语义修订：r1。

来源：
- [元素第二期机制卡池](../sources/inbox/2026-09-13-element-spell-mechanism-card-pool-02.md)

<a id="fx-115"></a>

### FX-115 已有同种时补层替换为邻近施加

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-115.md) |
| 当前关联实体 | [E3-I05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-i05) |
| 统一参数 | [E3-I05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-i05) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-116"></a>

### FX-116 冰冻增甲结果替换为宿主伤害

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-116.md) |
| 当前关联实体 | [E3-I06](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-i06) |
| 统一参数 | [E3-I06](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-i06) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-117"></a>

### FX-117 异种抵消后禁止新态与补生

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-117.md) |
| 当前关联实体 | [E3-I07](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-i07) |
| 统一参数 | [E3-I07](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-i07) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-118"></a>

### FX-118 燃烧被清空时伤害原宿主

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-118.md) |
| 当前关联实体 | [E3-I08](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-i08) |
| 统一参数 | [E3-I08](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-i08) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-119"></a>

### FX-119 燃烧损耗护甲为源火焰补层

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-119.md) |
| 当前关联实体 | [E3-I09](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-i09) |
| 统一参数 | [E3-I09](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-i09) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-120"></a>

### FX-120 元素直接伤害损耗护甲为己增甲

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-120.md) |
| 当前关联实体 | [E3-I10](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-i10) |
| 统一参数 | [E3-I10](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-i10) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-121"></a>

### FX-121 元素关闭自动邻近施加

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-121.md) |
| 当前关联实体 | [E3-A03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-a03) |
| 统一参数 | [E3-A03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-a03) |

原语义修订：r4。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-122"></a>

### FX-122 法术补层触发邻近施加

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-122.md) |
| 当前关联实体 | [E3-A04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-a04) |
| 统一参数 | [E3-A04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-a04) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-123"></a>

### FX-123 自然衰减改由邻近施加支付层数

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-123.md) |
| 当前关联实体 | [E3-A06](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#e3-a06) |
| 统一参数 | [E3-A06](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-e3-a06) |

原语义修订：r4。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-124"></a>

### FX-124 破甲触发本杖完整复诵

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-124.md) |
| 当前关联实体 | [S2-I03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-i03) |
| 统一参数 | [S2-I03](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-i03) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-125"></a>

### FX-125 本杖直接伤敌与己方护甲收益互换

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-125.md) |
| 当前关联实体 | [S2-I04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-i04) |
| 统一参数 | [S2-I04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-i04) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-126"></a>

### FX-126 无护甲时直接伤敌改为自身护甲

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-126.md) |
| 当前关联实体 | [S2-I05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-i05) |
| 统一参数 | [S2-I05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-i05) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-127"></a>

### FX-127 本杖直接命中附加印记

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-127.md) |
| 当前关联实体 | [S2-I06](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-i06) |
| 统一参数 | [S2-I06](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-i06) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-128"></a>

### FX-128 本杖冷却免于生命伤害打断

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-128.md) |
| 当前关联实体 | [S2-I07](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-i07) |
| 统一参数 | [S2-I07](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-i07) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-129"></a>

### FX-129 消耗印记后下个循环跳过冷却

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-129.md) |
| 当前关联实体 | [S2-I08](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-i08) |
| 统一参数 | [S2-I08](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-i08) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-130"></a>

### FX-130 使指定当前冷却完成

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-130.md) |
| 当前关联实体 | [S2-V06](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-v06) |
| 统一参数 | [S2-V06](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-v06) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-131"></a>

### FX-131 本句伤害绕过目标护甲

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-131.md) |
| 当前关联实体 | [S2-A01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-a01) |
| 统一参数 | [S2-A01](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-a01) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-132"></a>

### FX-132 护甲实际抵伤后反击攻击者

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-132.md) |
| 当前关联实体 | [S2-A02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-a02) |
| 统一参数 | [S2-A02](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-a02) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-133"></a>

### FX-133 本句目标筛选为已有印记敌人

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-133.md) |
| 当前关联实体 | [S2-A04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-a04) |
| 统一参数 | [S2-A04](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-a04) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)

<a id="fx-134"></a>

### FX-134 印记引爆后保留

| 字段 | 记录 |
| --- | --- |
| 适用范围 | 有RC1实体关联；仅采用现行条目列明部分 |
| 采纳口径 | 以当前GDD及CORE决定的具体部分为限；未选历史变体维持原状态 |
| 证据 | 本轮仅文档索引；不扩大既有TH/CAL范围，RC1完整验收NotRun |
| 原始语义、历次修订及未选变体 | [完整历史来源](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/effect-registry/entries/FX-134.md) |
| 当前关联实体 | [S2-A05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/content/cards.md#s2-a05) |
| 统一参数 | [S2-A05](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/parameters.md#pg-s2-a05) |

原语义修订：r3。

来源：
- [CG](../sources/materials/M-2026-09-14-card-interface-completion.md)
- [PG](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)
- [EG](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)
