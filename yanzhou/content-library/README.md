# 言咒具体内容库

2026-11-14规则增量：[CORE-079字相／物相框架](../design/systems/aspect-system/rules.md)已采纳。**本库仍为CONTENT-LIBRARY-11，尚未完成字相映射。**原物件／配方／仪式按冻结内容合同保留，不从名称自动推断字相、改变效果或授予知识。新内容和迁移按[内容合同](../design/content/cards.md)填写，当前缺口见ZX-G01—05；本轮没有重建展板或把旧检查升级为新框架通过证据。

**[打开仪式内容包](ritual-pack.html)**，查新入库的物件、仪式、补给与六类遭遇；[规则更新总结](../system-design/2026-11-09-ritual-rules-update-summary.md)说明变化与边界。[总展板](index.html)仍支持全部物件和配方检索。

2026-11-09续版：**CONTENT-LIBRARY-11／ritual-minimum-run.2**。新增7条仪式实物与6条敌人身份，12项仪式、补给、调查、委托、目标和传承由catalog的ritualContent统一维护。CORE-078已采纳并入现行GDD4.1，体验NotRun；[资格依据](../sources/materials/M-2026-11-09-ritual-content-pack.md)。

以下为保留的原首战范围。2026-11-05总控集成：**CORE-077／GDD4.0／round-plan.1，CONTENT-LIBRARY-09／first-distillation.4**。每轮5生产拍、整轮确认、回收下轮再用；规则、内容与任务包已对齐。首战两胜两败及重装经静态复核，2D与真人体验NotRun。

当前共82项物件、35配方、3构筑草稿；保留1个原首战，并新增6种仪式包遭遇。原首战69项的身份与限定资格保留。物件ID、资格及几何保留；首战敌生命15，两胜两败和20／22格重装见证已同步。具体来源见[CORE-077集成D](../sources/draft-changes/D-2026-11-05-round-plan-alignment.md)。

| 查什么 | 内容分册 |
| --- | --- |
| 仪式实物与六类敌人 | [物件分册](ritual.md) |
| 仪式、来源、调查、委托、目标及传承 | [完整内容包](ritual-pack.md)／[网页](ritual-pack.html) |
| 法器与炉心实体、P及圈下限 | [格形](artifact-geometry.md)／[网页](artifact-geometry.html) |
| 首战套组、初态、敌表与手动排程 | [首战规格](first-battle.md)／[网页](first-battle.html) |
| 材料、成品、法器、炉心与核心 | [炼金物件](alchemy.md) |
| 投入、产出、器具与排料约束 | [35条配方](recipes.md) |
| 炼金路线组件与取舍 | [构筑草稿](builds.md) |
| 原局部失败与预算语境 | [历史算例](alchemy-notes.md) |

旧接收范围、供料落点、fit和unlockBeat已退出活动数据；八法器本体占形保留。P取该器所承配方的最大材料数，不按实体面积计算。全库11成品的合计D与理想并行首份可用列已重算：根料c1足量、每批独立合法设备与核心、无争料、忽略空间和圈下限抬高，只给乐观下界。法器本体预算不含炉心、辅助与携带物，不等于完整部署。

硫链只采纳首批组合方向，具体配方、D、P和核心配置仍Unknown，不发行可执行配方、不进入首战。其余全库核心兼容、取得、携带、辅助与组合内容沿原资格。CORE-071淘汰的38项及EX-004不恢复；27个有图对象、52条图稿引用保持原件，四件器物02已接受并纳入当前运行选择。

## 各写一处

- 系统目标与取舍写[设计师手册](../system-design/handbook.md)；通用规则仍归`design/`。
- 物件、配方、占形及首战输入只改[catalog.json](catalog.json)，保留ID、资格、来源及Unknown。
- `alchemy.md`、`recipes.md`、`builds.md`、`first-battle.md`／`.html`、`artifact-geometry.md`／`.html`、`ritual.md`、`ritual-pack.md`／`.html`和`index.html`全部派生，不能双写。
- 原资格、失败与旧见证沿来源或固定Git版本取证；历史预算不重新成为现行内容。

## 展板与更新

展板支持搜索、类别／状态筛选、有图筛选、详情、图稿切换和配方关联。P展示用于设计审阅，不要求在战斗界面直显；无图显示类型符号，不代表美术完成。

生成器、模板和检查在[11版构建说明](E:/Project/yanzhou-ui-prototypes/content-library-2026-11-01/content-library-11-generator/README.md)。更新后执行构建、`--check`、现行限定检查及浏览器检查，再更新[manifest](manifest.json)。11版使用`check011.py`、`qa011.cjs`；原`check077.py`／09生成器保存在`content-library-09-generator/`，10版生成器与旧证据不覆盖，新证据单列11。代码与检查脚本不进入设计仓库。

## DM-G002-023

game-002 / main；CONTENT-LIBRARY-11；仅限静态内容检索与审阅。检查数量及结果以当前manifest为准；检查范围及证据见manifest。原09／10证据保持原版本，不覆盖。无引擎、平衡或真人通过结论。

derived-from：DM-G002-019@R09；uses：AS-G002-040@ALCHEMY-ITEM-PILOT-03、AS-G002-041@CARD-FRAME-02、AS-G002-042@FIRST-BATTLE-ART-01／02。图稿原件就地，未移动、改绘或上传；复用沿原项目内部审阅边界。
