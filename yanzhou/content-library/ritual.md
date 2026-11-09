# 仪式物件与敌人内容条目

2026-11-09 · CONTENT-LIBRARY-10。从[catalog.json](catalog.json)生成；请修改数据源后重建，勿双写。

[展板](index.html) · [维护方式](README.md)

<a id="ritual-incense"></a>

## 香料

`ritual.incense` · 仪式材料 · **已确认内容 · 待规则迁移**

多项仪式共用的基础投入。

适用范围：仅仪式最小完整局工作包；已审核并授权内容入库，Qualified，未替换现行GDD／首战；实现与体验NotRun。

| 信息 | 内容 |
| --- | --- |
| 取得 | 每段第1固定2份；其他来源见仪式内容包。 |
| 用途 | 按具体仪式实付；暂没有炼金或战斗用途。 |
| 携带 | 跨战／跨段实际保留；带回本局仓库，整局实体清理。 |

分项资格：身份／用途＝Qualified / 用户确认；本包具体参数＝用户审核通过；未迁移现行GDD；验证＝Hypothesis / NotRun。
占形（资格见分项）：一格；实体格 [[0, 0]]。
每份独立占格，数量合并显示不压缩实体。 仪式实体留在共用背包；非战斗卡，不入手牌，不嵌法器，不计战斗卡8种上限。
未定：美术与叙事文案未制作；平衡和真人体验未验证。
来源：[仪式内容入库资格与本轮授权](../sources/materials/M-2026-11-09-ritual-content-pack.md) · [已审核仪式工作设计（固定版本）](https://github.com/dsaj4/game_design/blob/d880c1f3308046952ea0fa30867f871b7b7845cf/yanzhou/system-design/2026-11-08-ritual-roguelite-overview.md#ritual-gap-review)


<a id="ritual-ember"></a>

## 烬核

`ritual.ember` · 仪式材料 · **已确认内容 · 待规则迁移**

仪式核心材料；普通余核与唯一终局核分别核验。

适用范围：仅仪式最小完整局工作包；已审核并授权内容入库，Qualified，未替换现行GDD／首战；实现与体验NotRun。

| 信息 | 内容 |
| --- | --- |
| 身份 | 不是铭文核心，不可嵌入法器免占格。 |
| 终局X3 | 终试第3实际取得并绑定的同一实例，第6改变状态；不另生成凭证，丢失不能用余核补造。 |
| 携带 | 每份独立占格；其他仪式不自动选入X3。 |

分项资格：身份／用途＝Qualified / 用户确认；本包具体参数＝用户审核通过；未迁移现行GDD；验证＝Hypothesis / NotRun。
占形（资格见分项）：一格；实体格 [[0, 0]]。
每份独立占格，数量合并显示不压缩实体。 仪式实体留在共用背包；非战斗卡，不入手牌，不嵌法器，不计战斗卡8种上限。
未定：美术与叙事文案未制作；平衡和真人体验未验证。
来源：[仪式内容入库资格与本轮授权](../sources/materials/M-2026-11-09-ritual-content-pack.md) · [已审核仪式工作设计（固定版本）](https://github.com/dsaj4/game_design/blob/d880c1f3308046952ea0fa30867f871b7b7845cf/yanzhou/system-design/2026-11-08-ritual-roguelite-overview.md#ritual-gap-review)


<a id="ritual-stone-fold"></a>

## 折纹门纹石

`ritual.stone-fold` · 仪式材料 · **已确认内容 · 待规则迁移**

折纹目标的仪式适配材料。

适用范围：仅仪式最小完整局工作包；已审核并授权内容入库，Qualified，未替换现行GDD／首战；实现与体验NotRun。

| 信息 | 内容 |
| --- | --- |
| 纹样 | 折纹 |
| 用途 | 同纹引路／解缚／覆痕／断契；首次缚门客交付两纹均收。 |
| 消费 | 覆痕对照保留，其他上述投入各自实际消费；一石不可重复支付。 |
| 来源 | 具体节点在生成时固定一种纹样；不免费改纹。 |

分项资格：身份／用途＝Qualified / 用户确认；本包具体参数＝用户审核通过；未迁移现行GDD；验证＝Hypothesis / NotRun。
占形（资格见分项）：二格长条；实体格 [[0, 0], [0, 1]]。
每份独立占格，数量合并显示不压缩实体。 仪式实体留在共用背包；非战斗卡，不入手牌，不嵌法器，不计战斗卡8种上限。
未定：美术与叙事文案未制作；平衡和真人体验未验证。
来源：[仪式内容入库资格与本轮授权](../sources/materials/M-2026-11-09-ritual-content-pack.md) · [已审核仪式工作设计（固定版本）](https://github.com/dsaj4/game_design/blob/d880c1f3308046952ea0fa30867f871b7b7845cf/yanzhou/system-design/2026-11-08-ritual-roguelite-overview.md#ritual-gap-review)


<a id="ritual-stone-ring"></a>

## 环纹门纹石

`ritual.stone-ring` · 仪式材料 · **已确认内容 · 待规则迁移**

环纹目标的仪式适配材料。

适用范围：仅仪式最小完整局工作包；已审核并授权内容入库，Qualified，未替换现行GDD／首战；实现与体验NotRun。

| 信息 | 内容 |
| --- | --- |
| 纹样 | 环纹 |
| 用途 | 同纹引路／解缚／覆痕／断契；首次缚门客交付两纹均收。 |
| 消费 | 覆痕对照保留，其他上述投入各自实际消费；一石不可重复支付。 |
| 来源 | 具体节点在生成时固定一种纹样；不免费改纹。 |

分项资格：身份／用途＝Qualified / 用户确认；本包具体参数＝用户审核通过；未迁移现行GDD；验证＝Hypothesis / NotRun。
占形（资格见分项）：二格长条；实体格 [[0, 0], [0, 1]]。
每份独立占格，数量合并显示不压缩实体。 仪式实体留在共用背包；非战斗卡，不入手牌，不嵌法器，不计战斗卡8种上限。
未定：美术与叙事文案未制作；平衡和真人体验未验证。
来源：[仪式内容入库资格与本轮授权](../sources/materials/M-2026-11-09-ritual-content-pack.md) · [已审核仪式工作设计（固定版本）](https://github.com/dsaj4/game_design/blob/d880c1f3308046952ea0fa30867f871b7b7845cf/yanzhou/system-design/2026-11-08-ritual-roguelite-overview.md#ritual-gap-review)


<a id="ritual-shell"></a>

## 空壳

`ritual.shell` · 仪式材料 · **已确认内容 · 待规则迁移**

招客、驻影和夺火共用的可消耗承载物。

适用范围：仅仪式最小完整局工作包；已审核并授权内容入库，Qualified，未替换现行GDD／首战；实现与体验NotRun。

| 信息 | 内容 |
| --- | --- |
| 用途 | 三种用途分别付1份，不可重复使用。 |
| 容器边界 | 不提供内部仓库，不套叠压缩。 |
| 取得 | 第7既有互斥选项。 |

分项资格：身份／用途＝Qualified / 用户确认；本包具体参数＝用户审核通过；未迁移现行GDD；验证＝Hypothesis / NotRun。
占形（资格见分项）：二格长条；实体格 [[0, 0], [0, 1]]。
每份独立占格，数量合并显示不压缩实体。 仪式实体留在共用背包；非战斗卡，不入手牌，不嵌法器，不计战斗卡8种上限。
未定：美术与叙事文案未制作；平衡和真人体验未验证。
来源：[仪式内容入库资格与本轮授权](../sources/materials/M-2026-11-09-ritual-content-pack.md) · [已审核仪式工作设计（固定版本）](https://github.com/dsaj4/game_design/blob/d880c1f3308046952ea0fa30867f871b7b7845cf/yanzhou/system-design/2026-11-08-ritual-roguelite-overview.md#ritual-gap-review)


<a id="ritual-handbook"></a>

## 仪式手记

`ritual.handbook` · 书籍 · **已确认内容 · 待规则迁移**

实体求知载体，已学方法可永久保留。

适用范围：仅仪式最小完整局工作包；已审核并授权内容入库，Qualified，未替换现行GDD／首战；实现与体验NotRun。

| 信息 | 内容 |
| --- | --- |
| 取得 | 每局初试第3可选留。 |
| 释读 | 仅文字界主动免费释读，保留书；问兆／引路／招客基础方法及条件方法见内容包。 |
| 条件内容 | 覆痕→断契；逆流→夺火；启阶后实际解缚→定址／驻影；定址后实际驻影→升界。 |
| 携带 | 可实际带回存仓；已学方法不要求每次随身带书。 |

分项资格：身份／用途＝Qualified / 用户确认；本包具体参数＝用户审核通过；未迁移现行GDD；验证＝Hypothesis / NotRun。
占形（资格见分项）：二格长条；实体格 [[0, 0], [0, 1]]。
每份独立占格，数量合并显示不压缩实体。 仪式实体留在共用背包；非战斗卡，不入手牌，不嵌法器，不计战斗卡8种上限。
未定：美术与叙事文案未制作；平衡和真人体验未验证。
来源：[仪式内容入库资格与本轮授权](../sources/materials/M-2026-11-09-ritual-content-pack.md) · [已审核仪式工作设计（固定版本）](https://github.com/dsaj4/game_design/blob/d880c1f3308046952ea0fa30867f871b7b7845cf/yanzhou/system-design/2026-11-08-ritual-roguelite-overview.md#ritual-gap-review)


<a id="ritual-unbind-page"></a>

## 解缚页

`ritual.unbind-page` · 书籍 · **已确认内容 · 待规则迁移**

缚门客履约后授予的实体知识页。

适用范围：仅仪式最小完整局工作包；已审核并授权内容入库，Qualified，未替换现行GDD／首战；实现与体验NotRun。

| 信息 | 内容 |
| --- | --- |
| 取得 | 有效联系中，具真实亲自驱离经历并交1任意纹样门纹石。 |
| 释读 | 文字界主动免费释读，学会解缚；查看或仅取得不算学会。 |
| 补领 | 履约后未学即失去：下一局有效联系可免重复石／经历补领；每局最多发一次、持有不再发、学会停止；需要招客时仍付原费用。 |
| 禁止用途 | 无出售、加工或供物用途。 |

分项资格：身份／用途＝Qualified / 用户确认；本包具体参数＝用户审核通过；未迁移现行GDD；验证＝Hypothesis / NotRun。
占形（资格见分项）：一格；实体格 [[0, 0]]。
每份独立占格，数量合并显示不压缩实体。 仪式实体留在共用背包；非战斗卡，不入手牌，不嵌法器，不计战斗卡8种上限。
未定：美术与叙事文案未制作；平衡和真人体验未验证。
来源：[仪式内容入库资格与本轮授权](../sources/materials/M-2026-11-09-ritual-content-pack.md) · [已审核仪式工作设计（固定版本）](https://github.com/dsaj4/game_design/blob/d880c1f3308046952ea0fa30867f871b7b7845cf/yanzhou/system-design/2026-11-08-ritual-roguelite-overview.md#ritual-gap-review)


<a id="ritual-enemy-patrol"></a>

## 旧径普通巡守

`ritual.enemy-patrol` · 敌人 · **已确认内容 · 待规则迁移**

每轮五次小额伤害，治疗过早可能溢出。

适用范围：仅仪式最小完整局工作包；已审核并授权内容入库，Qualified，未替换现行GDD／首战；实现与体验NotRun。

| 信息 | 内容 |
| --- | --- |
| 生命 | 9 |
| 防护与其他 | 无额外护甲／治疗／暴击／死亡追加。 |
| 完整程序 | 见仪式内容包同名敌表；不是原首战敌人替换。 |
| 信息 | 出发前公开压力类型，原生暗牌不全部亮数值，已生成后续公开。 |

分项资格：身份／用途＝Qualified / 用户确认；本包具体参数＝用户审核通过；未迁移现行GDD；验证＝Hypothesis / NotRun。
未定：美术与叙事文案未制作；平衡和真人体验未验证。
来源：[仪式内容入库资格与本轮授权](../sources/materials/M-2026-11-09-ritual-content-pack.md) · [已审核仪式工作设计（固定版本）](https://github.com/dsaj4/game_design/blob/d880c1f3308046952ea0fa30867f871b7b7845cf/yanzhou/system-design/2026-11-08-ritual-roguelite-overview.md#ritual-gap-review)


<a id="ritual-enemy-gatekeeper"></a>

## 灰井封门守卫

`ritual.enemy-gatekeeper` · 敌人 · **已确认内容 · 待规则迁移**

开场重击，随后蓄势与重击交替。

适用范围：仅仪式最小完整局工作包；已审核并授权内容入库，Qualified，未替换现行GDD／首战；实现与体验NotRun。

| 信息 | 内容 |
| --- | --- |
| 生命 | 9 |
| 防护与其他 | 无额外护甲／治疗／暴击／死亡追加。 |
| 完整程序 | 见仪式内容包同名敌表；不是原首战敌人替换。 |
| 信息 | 出发前公开压力类型，原生暗牌不全部亮数值，已生成后续公开。 |

分项资格：身份／用途＝Qualified / 用户确认；本包具体参数＝用户审核通过；未迁移现行GDD；验证＝Hypothesis / NotRun。
未定：美术与叙事文案未制作；平衡和真人体验未验证。
来源：[仪式内容入库资格与本轮授权](../sources/materials/M-2026-11-09-ritual-content-pack.md) · [已审核仪式工作设计（固定版本）](https://github.com/dsaj4/game_design/blob/d880c1f3308046952ea0fa30867f871b7b7845cf/yanzhou/system-design/2026-11-08-ritual-roguelite-overview.md#ritual-gap-review)


<a id="ritual-enemy-pressure"></a>

## 旧径深层积压者

`ritual.enemy-pressure` · 敌人 · **已确认内容 · 待规则迁移**

多轮持续施压，并生成公开后续。

适用范围：仅仪式最小完整局工作包；已审核并授权内容入库，Qualified，未替换现行GDD／首战；实现与体验NotRun。

| 信息 | 内容 |
| --- | --- |
| 生命 | 12 |
| 防护与其他 | 无额外护甲／治疗／暴击／死亡追加。 |
| 完整程序 | 见仪式内容包同名敌表；不是原首战敌人替换。 |
| 信息 | 出发前公开压力类型，原生暗牌不全部亮数值，已生成后续公开。 |

分项资格：身份／用途＝Qualified / 用户确认；本包具体参数＝用户审核通过；未迁移现行GDD；验证＝Hypothesis / NotRun。
未定：美术与叙事文案未制作；平衡和真人体验未验证。
来源：[仪式内容入库资格与本轮授权](../sources/materials/M-2026-11-09-ritual-content-pack.md) · [已审核仪式工作设计（固定版本）](https://github.com/dsaj4/game_design/blob/d880c1f3308046952ea0fa30867f871b7b7845cf/yanzhou/system-design/2026-11-08-ritual-roguelite-overview.md#ritual-gap-review)


<a id="ritual-enemy-rush"></a>

## 灰井深层急袭者

`ritual.enemy-rush` · 敌人 · **已确认内容 · 待规则迁移**

首轮集中伤害，后续缓息。

适用范围：仅仪式最小完整局工作包；已审核并授权内容入库，Qualified，未替换现行GDD／首战；实现与体验NotRun。

| 信息 | 内容 |
| --- | --- |
| 生命 | 9 |
| 防护与其他 | 无额外护甲／治疗／暴击／死亡追加。 |
| 完整程序 | 见仪式内容包同名敌表；不是原首战敌人替换。 |
| 信息 | 出发前公开压力类型，原生暗牌不全部亮数值，已生成后续公开。 |

分项资格：身份／用途＝Qualified / 用户确认；本包具体参数＝用户审核通过；未迁移现行GDD；验证＝Hypothesis / NotRun。
未定：美术与叙事文案未制作；平衡和真人体验未验证。
来源：[仪式内容入库资格与本轮授权](../sources/materials/M-2026-11-09-ritual-content-pack.md) · [已审核仪式工作设计（固定版本）](https://github.com/dsaj4/game_design/blob/d880c1f3308046952ea0fa30867f871b7b7845cf/yanzhou/system-design/2026-11-08-ritual-roguelite-overview.md#ritual-gap-review)


<a id="ritual-enemy-projection-entry"></a>

## 入口驻影

`ritual.enemy-projection-entry` · 敌人 · **已确认内容 · 待规则迁移**

集中压力与蓄势交替，安排在第2位置。

适用范围：仅仪式最小完整局工作包；已审核并授权内容入库，Qualified，未替换现行GDD／首战；实现与体验NotRun。

| 信息 | 内容 |
| --- | --- |
| 生命 | 12 |
| 防护与其他 | 无额外护甲／治疗／暴击／死亡追加。 |
| 完整程序 | 见仪式内容包同名敌表；不是原首战敌人替换。 |
| 信息 | 出发前公开压力类型，原生暗牌不全部亮数值，已生成后续公开。 |

分项资格：身份／用途＝Qualified / 用户确认；本包具体参数＝用户审核通过；未迁移现行GDD；验证＝Hypothesis / NotRun。
未定：美术与叙事文案未制作；平衡和真人体验未验证。
来源：[仪式内容入库资格与本轮授权](../sources/materials/M-2026-11-09-ritual-content-pack.md) · [已审核仪式工作设计（固定版本）](https://github.com/dsaj4/game_design/blob/d880c1f3308046952ea0fa30867f871b7b7845cf/yanzhou/system-design/2026-11-08-ritual-roguelite-overview.md#ritual-gap-review)


<a id="ritual-enemy-projection-deep"></a>

## 深层驻影

`ritual.enemy-projection-deep` · 敌人 · **已确认内容 · 待规则迁移**

持续交错施压，安排在第6位置。

适用范围：仅仪式最小完整局工作包；已审核并授权内容入库，Qualified，未替换现行GDD／首战；实现与体验NotRun。

| 信息 | 内容 |
| --- | --- |
| 生命 | 12 |
| 防护与其他 | 无额外护甲／治疗／暴击／死亡追加。 |
| 完整程序 | 见仪式内容包同名敌表；不是原首战敌人替换。 |
| 信息 | 出发前公开压力类型，原生暗牌不全部亮数值，已生成后续公开。 |

分项资格：身份／用途＝Qualified / 用户确认；本包具体参数＝用户审核通过；未迁移现行GDD；验证＝Hypothesis / NotRun。
未定：美术与叙事文案未制作；平衡和真人体验未验证。
来源：[仪式内容入库资格与本轮授权](../sources/materials/M-2026-11-09-ritual-content-pack.md) · [已审核仪式工作设计（固定版本）](https://github.com/dsaj4/game_design/blob/d880c1f3308046952ea0fa30867f871b7b7845cf/yanzhou/system-design/2026-11-08-ritual-roguelite-overview.md#ritual-gap-review)
