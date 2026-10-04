# 效果身份与当前应用

Project ID：game-002。文档角色：EffectTrace。2026-10-04 / TL-1 + INS-1。137个稳定历史身份不等于137张可用卡；规则唯一维护在design，当前没有已采纳的新发行池。登记不授予效果权限，也不证明实现或体验。

## 当前应用范围

| 身份／应用 | 已采纳部分与权威来源 | 内容／证据边界 |
| --- | --- | --- |
| FX-001 / TL-app1 | 普通伤害先甲后生命；[TL-12／29／30](../design/systems/03-combat.md) | 具体行动、量和制造映射待设计；旧TA-01／04已退役 |
| FX-002 / TL-app2 | 合格宿主累计护甲、耗尽消失、战终清理；[TL-29](../design/systems/03-combat.md) | 具体赋予内容与量未定；旧TA-02已退役 |
| FX-031 / TL-app1 | 提前取消敌牌与指定法器中断是不同权限；[TL-07](../design/systems/02-wands.md)、[TL-10](../design/systems/03-combat.md) | 不从同一FX推导权限互通；旧TA-03已退役 |
| [FX-135](#fx-135) | 资源转化的历史身份 | 原直接资源交付路径已由INS-1替代；新来源／加工途径Unknown |
| [FX-136](#fx-136) | 明确存在的高阶产物维护不足休眠、补料恢复；[TL-22／23](../design/systems/04-elements-environment.md) | 参数、内部争料与托管维护未定；没有默认发行“辉核” |
| [FX-137](#fx-137) | 高阶资源增幅的历史身份；[TL-15](../design/systems/04-elements-environment.md)保留接口方向 | 具体效果待设计；不同于TL-45核心契合，旧TS-08已退役 |

全部Hypothesis / NotRun。没有新增FX身份或效果修订；此次只同步既有CORE-049及探索退役的适用范围。

<a id="fx-135"></a>

### FX-135 资源卡配方转化

r1 / TL-1是原登记，保留原语义。INS-1撤销法器直接交付资源卡；行动若明示生成资源，必须经过普通战斗行生效，但当前尚无具体来源／配方。原TS-01–03、灵屑加工火种例子不再是当前待审内容。不得把新路径自动登记为该身份的新修订。

<a id="fx-136"></a>

### FX-136 高阶产物自动维护、休眠与恢复

r1 / TL-1身份保留。当前只在内容明确提供维护资源时应用TL-22／23／25：保留身份与增幅、自动恢复、维护先于新加工；跨战仅选中资源数量保留。周期、耗量、内部顺序、托管与休眠可加工范围仍Unknown。

<a id="fx-137"></a>

### FX-137 消耗材料增幅同一高阶资源

r1 / TL-1及TS-08原具体候选按固定版本取证。当前保留资源增幅接口目标，尚未采纳新获取链、耗材、托管强化、上限或伤害公式。法器与核心铭文的契合另属TL-45，不继承该资源的生命周期。

## 原身份索引：RC1及更早版本

下表逐项保留原名称、修订和实体关联，仅是历史索引；FX-001／002／031的新应用见上表。每个原ID锚点保留，链接进入固定版本的完整条目与更早来源，未删除未选变体、失败路径或参数。

| 效果与固定原记录 | 原语义修订 | 原版本关联实体（非全部变体采纳） |
| --- | --- | --- |
| <a id="fx-001"></a>[FX-001 造成直接伤害](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-001) | r3 | S2-V01 |
| <a id="fx-002"></a>[FX-002 获得护甲](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-002) | r3 | E3-N05、S2-N02、S2-V02 |
| <a id="fx-003"></a>[FX-003 施加燃烧及其状态效果](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-003) | r9 | E3-N03 |
| <a id="fx-004"></a>[FX-004 施加冰冻及其状态效果](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-004) | r8 | E3-N04 |
| <a id="fx-005"></a>[FX-005 熄灭燃烧](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-005) | r3 | E3-V09、S2-V05 |
| <a id="fx-006"></a>[FX-006 解除冰冻等明确状态](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-006) | r3 | E3-V09、S2-V05 |
| <a id="fx-007"></a>[FX-007 改变状态数量](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-007) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-008"></a>[FX-008 燃烧加倍](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-008) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-009"></a>[FX-009 燃烧蔓延](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-009) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-010"></a>[FX-010 生成与引用火焰](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-010) | r5 | E3-N01 |
| <a id="fx-011"></a>[FX-011 生成与引用雷电](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-011) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-012"></a>[FX-012 生成与引用冰霜](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-012) | r3 | E3-N02 |
| <a id="fx-013"></a>[FX-013 强化元素](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-013) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-014"></a>[FX-014 削弱元素](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-014) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-015"></a>[FX-015 抵挡尚未完成的作用](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-015) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-016"></a>[FX-016 反弹尚未完成的作用](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-016) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-017"></a>[FX-017 自动转移尚未完成的作用](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-017) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-018"></a>[FX-018 加速当前冷却](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-018) | r3 | S2-N05 |
| <a id="fx-019"></a>[FX-019 延迟或加速其他未完成时间](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-019) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-020"></a>[FX-020 对合格对象收集并掉卡](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-020) | r2 | 公共规则或历史方向；见条目来源 |
| <a id="fx-021"></a>[FX-021 召唤恶魔及召唤引用](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-021) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-022"></a>[FX-022 强化已有召唤物](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-022) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-023"></a>[FX-023 消耗护甲](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-023) | r5 | E3-V04 |
| <a id="fx-024"></a>[FX-024 寒冷的：护甲通用分支](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-024) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-025"></a>[FX-025 寒冷的：寒冰适配分支](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-025) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-026"></a>[FX-026 简易法术隔周期减冷却](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-026) | r4 | 公共规则或历史方向；见条目来源 |
| <a id="fx-027"></a>[FX-027 燃烧施加范围强化](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-027) | r4 | 公共规则或历史方向；见条目来源 |
| <a id="fx-028"></a>[FX-028 力量等许可属性的强化](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-028) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-029"></a>[FX-029 战内恢复及吸血方向](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-029) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-030"></a>[FX-030 有限产金](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-030) | r2 | 公共规则或历史方向；见条目来源 |
| <a id="fx-031"></a>[FX-031 取消一次未完成过程](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-031) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-032"></a>[FX-032 清除护甲](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-032) | r3 | S2-V05 |
| <a id="fx-033"></a>[FX-033 多次释放方向（待拆清事件）](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-033) | r4 | S2-A03、S2-I01、S2-N04 |
| <a id="fx-034"></a>[FX-034 叠加爆发方向（待定义累积与兑现）](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-034) | r4 | S2-I02 |
| <a id="fx-035"></a>[FX-035 施加印记](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-035) | r3 | S2-N03、S2-V03 |
| <a id="fx-036"></a>[FX-036 获得与蓄积可消耗能量](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-036) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-037"></a>[FX-037 回响状态授权再次施法](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-037) | r3 | S2-N04、S2-V02 |
| <a id="fx-038"></a>[FX-038 消耗可引爆状态转为伤害](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-038) | r3 | E3-V06、S2-V04 |
| <a id="fx-039"></a>[FX-039 轻巧名词使本句冷却更快](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-039) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-040"></a>[FX-040 充盈名词增强本句所得](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-040) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-041"></a>[FX-041 锋利生成物对护甲特攻](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-041) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-042"></a>[FX-042 带电作用附加电击](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-042) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-043"></a>[FX-043 双生元素生成](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-043) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-044"></a>[FX-044 延长本句产物存续](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-044) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-045"></a>[FX-045 生成物在场蓄势](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-045) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-046"></a>[FX-046 易燃对象增加燃烧施加](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-046) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-047"></a>[FX-047 生成物消散爆裂](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-047) | r3 | E3-A05 |
| <a id="fx-048"></a>[FX-048 本杖连续成功增强](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-048) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-049"></a>[FX-049 强化开战首法术](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-049) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-050"></a>[FX-050 强化额外复诵](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-050) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-051"></a>[FX-051 同目标连续作用增强](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-051) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-052"></a>[FX-052 攻防交替支援](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-052) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-053"></a>[FX-053 击破护甲后续加速](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-053) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-054"></a>[FX-054 燃烧目标直接增伤](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-054) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-055"></a>[FX-055 消耗冰冻强化当次伤害](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-055) | r3 | S2-I09 |
| <a id="fx-056"></a>[FX-056 被覆盖后续加速](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-056) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-057"></a>[FX-057 护甲存续冷却加速](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-057) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-058"></a>[FX-058 元素生成后续加速](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-058) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-059"></a>[FX-059 温和攻击避开友方](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-059) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-060"></a>[FX-060 火焰元素邻近施加燃烧](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-060) | r2 | 公共规则或历史方向；见条目来源 |
| <a id="fx-061"></a>[FX-061 环境元素阈值与形态推进](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-061) | r3 | 公共规则或历史方向；见条目来源 |
| <a id="fx-062"></a>[FX-062 环境已达形态保留（含烧焦）](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-062) | r3 | 公共规则或历史方向；见条目来源 |
| <a id="fx-063"></a>[FX-063 元素释放生成、叠层与满位回退](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-063) | r3 | E3-N01、E3-N02、E3-V01 |
| <a id="fx-064"></a>[FX-064 元素共享状态层数与归零消散](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-064) | r4 | E3-N01、E3-N02 |
| <a id="fx-065"></a>[FX-065 环境转化元素并继承状态](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-065) | r9 | 公共规则或历史方向；见条目来源 |
| <a id="fx-066"></a>[FX-066 固有属性克制修正元素状态](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-066) | r2 | 公共规则或历史方向；见条目来源 |
| <a id="fx-067"></a>[FX-067 单元素状态互斥、抵消与替换](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-067) | r3 | 公共规则或历史方向；见条目来源 |
| <a id="fx-068"></a>[FX-068 元素邻近施加对应状态](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-068) | r5 | E3-N01、E3-N02 |
| <a id="fx-069"></a>[FX-069 释放作用下异种元素消散后的补生](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-069) | r5 | 公共规则或历史方向；见条目来源 |
| <a id="fx-070"></a>[FX-070 消耗火焰爆裂](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-070) | r3 | E3-V08 |
| <a id="fx-071"></a>[FX-071 消耗冰霜凝甲](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-071) | r3 | E3-V07 |
| <a id="fx-072"></a>[FX-072 燃烧伤害增强](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-072) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-073"></a>[FX-073 冰冻护甲收益增强](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-073) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-074"></a>[FX-074 元素层数自然衰减减缓](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-074) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-075"></a>[FX-075 元素初始层数与衰减同时增强](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-075) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-076"></a>[FX-076 缩小邻近范围并增强施加量](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-076) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-077"></a>[FX-077 扩大邻近范围并降低施加量](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-077) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-078"></a>[FX-078 提高消耗护甲的元素转层收益](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-078) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-079"></a>[FX-079 冰霜邻近施加仅限友方](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-079) | r4 | E3-A01 |
| <a id="fx-080"></a>[FX-080 火焰邻近施加排除友方](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-080) | r3 | E3-A02 |
| <a id="fx-081"></a>[FX-081 元素少邻居时增强邻近施加](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-081) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-082"></a>[FX-082 元素多邻居时增强邻近施加](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-082) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-083"></a>[FX-083 本句环境转化阈值降低](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-083) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-084"></a>[FX-084 范围内冰冻施加量增强](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-084) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-085"></a>[FX-085 元素自然消散强化下次同种释放](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-085) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-086"></a>[FX-086 满位回退时增强状态施加](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-086) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-087"></a>[FX-087 同种元素叠层增强](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-087) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-088"></a>[FX-088 元素替换成功加速本杖冷却](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-088) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-089"></a>[FX-089 环境转化成功强化下次伤害](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-089) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-090"></a>[FX-090 冰冻为自己增甲后缩短下次释放](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-090) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-091"></a>[FX-091 消耗护甲强化下次元素直接伤害](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-091) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-092"></a>[FX-092 对已有冰冻宿主增加护甲增强](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-092) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-093"></a>[FX-093 主动消耗元素层数加速后续冷却](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-093) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-094"></a>[FX-094 凝甲后存续冰霜强化下次邻近施加](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-094) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-095"></a>[FX-095 主动耗尽元素缩短下次元素释放](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-095) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-096"></a>[FX-096 交替释放火冰增强后次施加量](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-096) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-097"></a>[FX-097 同种状态转为执行元素层数](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-097) | r3 | E3-V02 |
| <a id="fx-098"></a>[FX-098 消耗元素层数定向施加对应状态](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-098) | r3 | E3-V03 |
| <a id="fx-099"></a>[FX-099 场上元素转为法杖封存资源](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-099) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-100"></a>[FX-100 封存储量供给完整元素释放](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-100) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-101"></a>[FX-101 敌方护甲转为玩家护甲](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-101) | r3 | E3-V05 |
| <a id="fx-102"></a>[FX-102 主动火冰抵消兑现玩家护甲](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-102) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-103"></a>[FX-103 邻近施加提前并扣除未来一次](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-103) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-104"></a>[FX-104 邻近施加延后并合并后续输出](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-104) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-105"></a>[FX-105 自动邻近改由主动操控触发](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-105) | r3 | E3-I01 |
| <a id="fx-106"></a>[FX-106 元素操控改从元素所在格计算范围](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-106) | r4 | E3-I02 |
| <a id="fx-107"></a>[FX-107 满位回退由状态施加改为直接攻防](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-107) | r3 | E3-I03 |
| <a id="fx-108"></a>[FX-108 异种抵消的施加消耗回收为封存储量](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-108) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-109"></a>[FX-109 异种状态抵消触发原状态收尾收益](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-109) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-110"></a>[FX-110 他人冰冻增甲时玩家同步获得护甲](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-110) | r3 | E3-I04 |
| <a id="fx-111"></a>[FX-111 消散记录格子供后续生成优先选择](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-111) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-112"></a>[FX-112 元素替换继承兼容的一次性强化](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-112) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-113"></a>[FX-113 封存储量跨元素供给解封](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-113) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-114"></a>[FX-114 主动元素消耗的收益改为后续分次兑现](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-114) | r1 | 公共规则或历史方向；见条目来源 |
| <a id="fx-115"></a>[FX-115 已有同种时补层替换为邻近施加](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-115) | r3 | E3-I05 |
| <a id="fx-116"></a>[FX-116 冰冻增甲结果替换为宿主伤害](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-116) | r3 | E3-I06 |
| <a id="fx-117"></a>[FX-117 异种抵消后禁止新态与补生](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-117) | r3 | E3-I07 |
| <a id="fx-118"></a>[FX-118 燃烧被清空时伤害原宿主](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-118) | r3 | E3-I08 |
| <a id="fx-119"></a>[FX-119 燃烧损耗护甲为源火焰补层](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-119) | r3 | E3-I09 |
| <a id="fx-120"></a>[FX-120 元素直接伤害损耗护甲为己增甲](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-120) | r3 | E3-I10 |
| <a id="fx-121"></a>[FX-121 元素关闭自动邻近施加](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-121) | r4 | E3-A03 |
| <a id="fx-122"></a>[FX-122 法术补层触发邻近施加](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-122) | r3 | E3-A04 |
| <a id="fx-123"></a>[FX-123 自然衰减改由邻近施加支付层数](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-123) | r4 | E3-A06 |
| <a id="fx-124"></a>[FX-124 破甲触发本杖完整复诵](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-124) | r3 | S2-I03 |
| <a id="fx-125"></a>[FX-125 本杖直接伤敌与己方护甲收益互换](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-125) | r3 | S2-I04 |
| <a id="fx-126"></a>[FX-126 无护甲时直接伤敌改为自身护甲](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-126) | r3 | S2-I05 |
| <a id="fx-127"></a>[FX-127 本杖直接命中附加印记](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-127) | r3 | S2-I06 |
| <a id="fx-128"></a>[FX-128 本杖冷却免于生命伤害打断](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-128) | r3 | S2-I07 |
| <a id="fx-129"></a>[FX-129 消耗印记后下个循环跳过冷却](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-129) | r3 | S2-I08 |
| <a id="fx-130"></a>[FX-130 使指定当前冷却完成](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-130) | r3 | S2-V06 |
| <a id="fx-131"></a>[FX-131 本句伤害绕过目标护甲](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-131) | r3 | S2-A01 |
| <a id="fx-132"></a>[FX-132 护甲实际抵伤后反击攻击者](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-132) | r3 | S2-A02 |
| <a id="fx-133"></a>[FX-133 本句目标筛选为已有印记敌人](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-133) | r3 | S2-A04 |
| <a id="fx-134"></a>[FX-134 印记引爆后保留](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md#fx-134) | r3 | S2-A05 |

[清理前完整目录](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/effects/catalog.md) · [来源范围](source-audit.md) · [待验证覆盖](case-coverage.md) · [就绪状态](readiness-review.md)。原记录中的“当前”按其原日期解释，不能补齐新版Unknown。
