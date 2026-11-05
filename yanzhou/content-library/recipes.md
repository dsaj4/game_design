# 具体配方

2026-11-05。从[catalog.json](catalog.json)生成。35配方的投入、产出、承载与卡效继承CORE-072；r04／05／06的D沿CORE-075。战中按工序行排料，不再使用局部供料装载；实际D受炉心圈下限约束，P为材料张数上限。其他全链取得与部署不因迁移采纳。

[展板](index.html#recipes) · [物件](alchemy.md)

<a id="alchemy-r01"></a>

## 硫 · 转化

`alchemy.r01` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[燃烧木炭](alchemy.md#alchemy-fire) × 1（激发入口）

产出：硫 × 1；D2；器具：[初相坩埚](alchemy.md#alchemy-artifact-crucible)。

将原热与激发语义收束为硫原质；仍为本作给定平炼。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料1张；器具P=1。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r02"></a>

## 汞 · 转化

`alchemy.r02` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[清泉水](alchemy.md#alchemy-water) × 1（流转入口）

产出：汞 × 1；D2；器具：[初相坩埚](alchemy.md#alchemy-artifact-crucible)。

将原流动语义收束为汞原质；不改成矿源。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料1张；器具P=1。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r03"></a>

## 盐 · 转化

`alchemy.r03` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[黏土团](alchemy.md#alchemy-earth) × 1（固持入口）

产出：盐 × 1；D2；器具：[初相坩埚](alchemy.md#alchemy-artifact-crucible)。

将原土质的承载语义收束为盐原质。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料1张；器具P=1。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r04"></a>

## 滚烫蒸汽 · 精炼

`alchemy.r04` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[清泉水](alchemy.md#alchemy-water) × 1（流体）；[燃烧木炭](alchemy.md#alchemy-fire) × 1（热源）

产出：滚烫蒸汽 × 1；D3；器具：[盘管萃炼器](alchemy.md#alchemy-artifact-extractor)。

流体被受热展开，得到滚烫蒸汽。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r05"></a>

## 轻盈雾团 · 精炼

`alchemy.r05` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[清泉水](alchemy.md#alchemy-water) × 1（流体载体）；[风息羽毛](alchemy.md#alchemy-air) × 1（轻散定向）

产出：轻盈雾团 × 1；D3；器具：[盘管萃炼器](alchemy.md#alchemy-artifact-extractor)。

羽毛保留轻散方向，使水体成为雾团。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r06"></a>

## 草药汁液 · 精炼

`alchemy.r06` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[疗伤草](alchemy.md#alchemy-herb) × 1（生机来源）；[清泉水](alchemy.md#alchemy-water) × 1（浸取载体）

产出：草药汁液 × 1；D3；器具：[盘管萃炼器](alchemy.md#alchemy-artifact-extractor)。

将药草的生机提取为可混合汁液。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r07"></a>

## 精铁砂砾 · 精炼

`alchemy.r07` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[生铁块](alchemy.md#alchemy-iron) × 1（坚固来源）；[黏土团](alchemy.md#alchemy-earth) × 1（颗粒基体）

产出：精铁砂砾 × 1；D3；器具：[刻纹研钵](alchemy.md#alchemy-artifact-mortar)。

坚固金属被处理为可继续组合的颗粒。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r08"></a>

## 日辉晶粉 · 精炼

`alchemy.r08` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[日光晶石](alchemy.md#alchemy-light) × 1（显现来源）；[燃烧木炭](alchemy.md#alchemy-fire) × 1（显发激发）

产出：日辉晶粉 × 1；D3；器具：[刻纹研钵](alchemy.md#alchemy-artifact-mortar)。

显现方向被激发为细粉形态。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r09"></a>

## 夜影尘粉 · 精炼

`alchemy.r09` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[夜影蘑菇](alchemy.md#alchemy-shadow) × 1（幽抑来源）；[黏土团](alchemy.md#alchemy-earth) × 1（附着基体）

产出：夜影尘粉 × 1；D2；器具：[刻纹研钵](alchemy.md#alchemy-artifact-mortar)。

幽暗方向附着在可混合粉尘中。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r10"></a>

## 水银溶剂 · 精炼

`alchemy.r10` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[汞](alchemy.md#alchemy-mercury) × 1（汞系携效）；[清泉水](alchemy.md#alchemy-water) × 1（液体载体）

产出：水银溶剂 × 1；D3；器具：[盘管萃炼器](alchemy.md#alchemy-artifact-extractor)。

明确流转载体，为后续传导或蚀解留入口。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r11"></a>

## 草本灵液 · 精炼

`alchemy.r11` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[汞](alchemy.md#alchemy-mercury) × 1（汞系携效）；[疗伤草](alchemy.md#alchemy-herb) × 1（生机定向）

产出：草本灵液 × 1；D3；器具：[盘管萃炼器](alchemy.md#alchemy-artifact-extractor)。

汞负责携带，药草指定生机方向。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r12"></a>

## 硫磺火种 · 精炼

`alchemy.r12` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[硫](alchemy.md#alchemy-sulfur) × 1（硫系激发）；[燃烧木炭](alchemy.md#alchemy-fire) × 1（热源延续）

产出：硫磺火种 × 1；D3；器具：[封相炼炉](alchemy.md#alchemy-artifact-phase-furnace)。

把激发稳定为能继续投入的火种。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r13"></a>

## 辉光灵火 · 精炼

`alchemy.r13` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[硫](alchemy.md#alchemy-sulfur) × 1（硫系激发）；[日光晶石](alchemy.md#alchemy-light) × 1（显现定向）

产出：辉光灵火 × 1；D4；器具：[封相炼炉](alchemy.md#alchemy-artifact-phase-furnace)。

把激发向显发方向稳定为灵火。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r14"></a>

## 盐晶核 · 精炼

`alchemy.r14` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[盐](alchemy.md#alchemy-salt) × 1（盐系固持）；[黏土团](alchemy.md#alchemy-earth) × 1（结构基体）

产出：盐晶核 × 1；D3；器具：[封相炼炉](alchemy.md#alchemy-artifact-phase-furnace)。

固持原理形成可承载其他性质的晶核。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r15"></a>

## 幽影封盐 · 精炼

`alchemy.r15` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[盐](alchemy.md#alchemy-salt) × 1（盐系固持）；[夜影蘑菇](alchemy.md#alchemy-shadow) × 1（幽抑封存）

产出：幽影封盐 × 1；D3；器具：[封相炼炉](alchemy.md#alchemy-artifact-phase-furnace)。

使固持带上束缚和封存方向。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r16"></a>

## 再生精华液 · 精炼

`alchemy.r16` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[草本灵液](alchemy.md#alchemy-spirit-fluid) × 1（携效前料）；[疗伤草](alchemy.md#alchemy-herb) × 1（再生定向）

产出：再生精华液 × 1；D5；器具：[盘管萃炼器](alchemy.md#alchemy-artifact-extractor)。

已有生机载体再接受药草，收束到再生。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r17"></a>

## 清醒凝露 · 精炼

`alchemy.r17` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[草本灵液](alchemy.md#alchemy-spirit-fluid) × 1（携效前料）；[日辉晶粉](alchemy.md#alchemy-radiance) × 1（清明显发）

产出：清醒凝露 × 1；D3；器具：[盘管萃炼器](alchemy.md#alchemy-artifact-extractor)。

把生机载体转向清醒；尚未成为可用药水。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r18"></a>

## 蚀解溶液 · 精炼

`alchemy.r18` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[水银溶剂](alchemy.md#alchemy-solvent) × 1（携效前料）；[夜影尘粉](alchemy.md#alchemy-shadow-dust) × 1（蚀解定向）

产出：蚀解溶液 × 1；D4；器具：[盘管萃炼器](alchemy.md#alchemy-artifact-extractor)。

溶剂携带解除结合方向，供离解使用。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r19"></a>

## 金刚晶砂 · 精炼

`alchemy.r19` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[盐晶核](alchemy.md#alchemy-crystal-core) × 1（固持骨架）；[精铁砂砾](alchemy.md#alchemy-iron-sand) × 1（坚固颗粒）

产出：金刚晶砂 × 1；D4；器具：[刻纹研钵](alchemy.md#alchemy-artifact-mortar)。

将坚固颗粒固持为更明确的防护前料。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r20"></a>

## 浮空晶石 · 精炼

`alchemy.r20` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[盐晶核](alchemy.md#alchemy-crystal-core) × 1（固持骨架）；[轻盈雾团](alchemy.md#alchemy-mist) × 1（轻散载形）

产出：浮空晶石 × 1；D3；器具：[封相炼炉](alchemy.md#alchemy-artifact-phase-furnace)。

将轻散性质固定在投射载体中，不授予飞行。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r21"></a>

## 封魔结晶 · 精炼

`alchemy.r21` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[幽影封盐](alchemy.md#alchemy-sealing-salt) × 1（封存前料）；[日辉晶粉](alchemy.md#alchemy-radiance) × 1（显发限定）

产出：封魔结晶 × 1；D5；器具：[封相炼炉](alchemy.md#alchemy-artifact-phase-furnace)。

把幽抑封存固定为明确结晶，不自动封魔。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r22"></a>

## 日冕之火 · 精炼

`alchemy.r22` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[辉光灵火](alchemy.md#alchemy-spirit-fire) × 1（显发激发）；[日辉晶粉](alchemy.md#alchemy-radiance) × 1（聚合显发）

产出：日冕之火 × 1；D4；器具：[封相炼炉](alchemy.md#alchemy-artifact-phase-furnace)。

聚合硫系显发方向，供日轮或红化。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r23"></a>

## 爆鸣火核 · 精炼

`alchemy.r23` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[硫磺火种](alchemy.md#alchemy-fire-seed) × 1（激发内核）；[滚烫蒸汽](alchemy.md#alchemy-steam) × 1（受热展开）

产出：爆鸣火核 × 1；D4；器具：[封相炼炉](alchemy.md#alchemy-artifact-phase-furnace)。

使火种接入受热展开方向，成为爆发前料。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-r24"></a>

## 幽冥磷火 · 精炼

`alchemy.r24` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[硫磺火种](alchemy.md#alchemy-fire-seed) × 1（激发内核）；[夜影尘粉](alchemy.md#alchemy-shadow-dust) × 1（幽抑定向）

产出：幽冥磷火 × 1；D3；器具：[封相炼炉](alchemy.md#alchemy-artifact-phase-furnace)。

把激发导向幽暗与侵蚀，保留法术输入。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-recipe-life"></a>

## 生命灵药 · 白化

`alchemy.recipe-life` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[草本灵液](alchemy.md#alchemy-spirit-fluid) × 1（汞系携效）；[草药汁液](alchemy.md#alchemy-herb-juice) × 1（生机定向）

产出：生命灵药 × 1；D2；器具：[白瓷曲颈瓶](alchemy.md#alchemy-artifact-retort)。

白化把药草生机留在汞系载体中，得到既定恢复药水。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-recipe-skin"></a>

## 铁肤药水 · 白化

`alchemy.recipe-skin` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[草本灵液](alchemy.md#alchemy-spirit-fluid) × 1（汞系携效）；[精铁砂砾](alchemy.md#alchemy-iron-sand) × 1（坚固定向）

产出：铁肤药水 × 1；D2；器具：[白瓷曲颈瓶](alchemy.md#alchemy-artifact-retort)。

白化携带坚固意义；按铁肤卡合同结算，不继承全部前料性质。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-recipe-wake"></a>

## 醒神药水 · 白化

`alchemy.recipe-wake` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[清醒凝露](alchemy.md#alchemy-mind-dew) × 1（清醒定向）；[清泉水](alchemy.md#alchemy-water) × 1（流体载体）

产出：醒神药水 × 1；D3；器具：[白瓷曲颈瓶](alchemy.md#alchemy-artifact-retort)。

清醒凝露完成白化成为醒神药水，前料本身仍不能施放。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-recipe-missile"></a>

## 水银飞弹 · 黑化

`alchemy.recipe-missile` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[浮空晶石](alchemy.md#alchemy-floating-stone) × 1（盐系投射器体）；[水银溶剂](alchemy.md#alchemy-solvent) × 1（汞系流转传导）

产出：水银飞弹 × 1；D3；器具：[黑铁铸模](alchemy.md#alchemy-artifact-mold)。

盐负责器体，汞辅助传导，黑化完成器物。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-recipe-bomb"></a>

## 炼金爆弹 · 黑化

`alchemy.recipe-bomb` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[盐晶核](alchemy.md#alchemy-crystal-core) × 1（盐系封装）；[爆鸣火核](alchemy.md#alchemy-thunder-core) × 1（硫系释放）

产出：炼金爆弹 × 1；D4；器具：[黑铁铸模](alchemy.md#alchemy-artifact-mold)。

器体与激发前料分工，黑化产出爆弹，不自动增加范围。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-recipe-charm"></a>

## 结晶护符 · 黑化

`alchemy.recipe-charm` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[盐晶核](alchemy.md#alchemy-crystal-core) × 1（盐系骨架）；[金刚晶砂](alchemy.md#alchemy-diamond-sand) × 1（坚固定向）

产出：结晶护符 × 1；D4；器具：[黑铁铸模](alchemy.md#alchemy-artifact-mold)。

把坚固前料固定为护符；回收与费用仍由卡合同决定。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-recipe-ignite"></a>

## 引燃术 · 黄化

`alchemy.recipe-ignite` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[硫磺火种](alchemy.md#alchemy-fire-seed) × 1（硫系激发）；[燃烧木炭](alchemy.md#alchemy-fire) × 1（热源延续）

产出：引燃术 × 1；D3；器具：[黄铜显咒灯](alchemy.md#alchemy-artifact-lamp)。

黄化把火种兑现为引燃术；保留原效果与费用定位。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-recipe-sun"></a>

## 日轮术 · 黄化

`alchemy.recipe-sun` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[日冕之火](alchemy.md#alchemy-solar-fire) × 1（硫系集中激发）；[水银溶剂](alchemy.md#alchemy-solvent) × 1（汞系传导）

产出：日轮术 × 1；D4；器具：[黄铜显咒灯](alchemy.md#alchemy-artifact-lamp)。

黄化兑现集中激发，汞辅料不改变法术分类。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-recipe-dissolve"></a>

## 离解术 · 黄化

`alchemy.recipe-dissolve` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[幽冥磷火](alchemy.md#alchemy-nether-fire) × 1（硫系激发）；[蚀解溶液](alchemy.md#alchemy-erosive-fluid) × 1（汞系蚀解携效）

产出：离解术 × 1；D3；器具：[黄铜显咒灯](alchemy.md#alchemy-artifact-lamp)。

激发与解除结合分工，黄化形成原离解术。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料2张；器具P=2。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-recipe-stone"></a>

## 贤者之石 · 红化

`alchemy.recipe-stone` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[再生精华液](alchemy.md#alchemy-regen-fluid) × 1（汞系再生）；[日冕之火](alchemy.md#alchemy-solar-fire) × 1（硫系激发）；[封魔结晶](alchemy.md#alchemy-sealing-crystal) × 1（盐系封存）；[日光晶石](alchemy.md#alchemy-light) × 1（显发限定）

产出：贤者之石 × 1；D6；器具：[红玻璃合一炉](alchemy.md#alchemy-artifact-athanor)。

三原质派生料汇流并以日光限定显发，红化无单一主原质。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料4张；器具P=4。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。

<a id="alchemy-recipe-elixir"></a>

## 万灵药 · 红化

`alchemy.recipe-elixir` · Accepted / CORE-072：投入身份与份数、产出、承载、额外制造费；基础D沿CORE-072及CORE-075限定修订。CORE-076列时序；材料张数不得超过P，实际D受圈下限约束。全链配置与取得仍按原资格。

投入：[生命灵药](alchemy.md#alchemy-life) × 1（白化成品）；[结晶护符](alchemy.md#alchemy-charm) × 1（黑化成品）；[引燃术](alchemy.md#alchemy-ignite) × 1（黄化成品）；[再生精华液](alchemy.md#alchemy-regen-fluid) × 1（再生协同）

产出：万灵药 × 1；D5；器具：[红玻璃合一炉](alchemy.md#alchemy-artifact-athanor)。

消费三类真实成品与再生前料，合炼为原万灵药。

额外制造费：0（不另收咒／金币／燃料费）。

排料：本批材料4张；器具P=4。材料格形仅用于运输，战中不做局部装载。实际D＝max(配方公式结果, 炉心圈下限)；c开工、c+D−1列末入手、c+D可用。
