# 言咒具体内容库

**[打开 HTML 内容展板](index.html)**，查炼金物件、配方、实体占形及首战规格。

2026-11-04 · CONTENT-LIBRARY-08 · game-002。catalog为具体内容单一数据源；内容入库、玩法采纳、程序实现与体验验证分别记录。

## 内容与边界

本版69项alchemy：32材料、11成品、8法器、10核心、2炉心、1咒标记、1敌人、4敌牌；35配方、3构筑草稿及first-distillation.3首战。原67项身份与图稿保留，新增小炉／长炉沿CORE-075；首战只实发1枚小炉。配方与卡效沿CORE-072，r04／05／06基础D沿CORE-075修订为3。

首战已同步CORE-075／076：5列序幕、一小炉、圈下限、P、手动排料和列末补给；四器实际D为3／4／2／2。运输35/40格，配置18格。EX-005已重算两胜一败及战后重装，均为指定操作下的静态推导；主游戏与真人体验NotRun。迁移依据与未决见[本轮记录](../sources/draft-changes/D-2026-11-04-first-battle-table-axis-migration.md)。

| 查什么 | 内容分册 |
| --- | --- |
| 法器与炉心实体、P及圈下限 | [格形](artifact-geometry.md)／[网页](artifact-geometry.html) |
| 首战套组、初态、敌表与手动排程 | [首战规格](first-battle.md)／[网页](first-battle.html) |
| 材料、成品、法器、炉心与核心 | [炼金物件](alchemy.md) |
| 投入、产出、器具与排料约束 | [35条配方](recipes.md) |
| 炼金路线组件与取舍 | [构筑草稿](builds.md) |
| 原局部失败与预算语境 | [历史算例](alchemy-notes.md) |

旧接收范围、供料落点、fit和unlockBeat已退出活动数据；八法器本体占形保留。P取该器所承配方的最大材料数，不按实体面积计算。全库11成品的合计D与理想并行首份可用列已重算：根料c1足量、每批独立合法设备与核心、无争料、忽略空间和圈下限抬高，只给乐观下界。法器本体预算不含炉心、辅助与携带物，不等于完整部署。

硫链只采纳首批组合方向，具体配方、D、P和核心配置仍Unknown，不发行可执行配方、不进入首战。其余全库核心兼容、取得、携带、辅助与组合内容沿原资格。CORE-071淘汰的38项及EX-004不恢复；5种材料15张图稿仍指向原件。

## 各写一处

- 系统目标与取舍写[设计师手册](../system-design/handbook.md)；通用规则仍归`design/`。
- 物件、配方、占形及首战输入只改[catalog.json](catalog.json)，保留ID、资格、来源及Unknown。
- `alchemy.md`、`recipes.md`、`builds.md`、`first-battle.md`／`.html`、`artifact-geometry.md`／`.html`和`index.html`全部派生，不能双写。
- 原资格、失败与旧见证沿来源或固定Git版本取证；历史预算不重新成为现行内容。

## 展板与更新

展板支持搜索、类别／状态筛选、有图筛选、详情、图稿切换和配方关联。P展示用于设计审阅，不要求在战斗界面直显；无图显示类型符号，不代表美术完成。

生成器、模板和检查在[外部构建说明](E:/Project/yanzhou-ui-prototypes/content-library-2026-11-01/README.md)。更新后执行构建、`--check`、`check076.py`和浏览器检查，再更新[manifest](manifest.json)。旧07生成器与证据保留，新证据单列08；代码与检查脚本不进入设计仓库。

## DM-G002-023

game-002 / main；CONTENT-LIBRARY-08；ReadyForScope / PresentLocal仅限静态内容检索与审阅。浏览器210项通过，几何、材料及三条指定路线算术通过；不代表引擎、完整玩法、平衡或真人通过。

derived-from：DM-G002-019@R09；uses：AS-G002-040@ALCHEMY-ITEM-PILOT-02、AS-G002-041@CARD-FRAME-02。图稿原件就地，未移动、改绘或上传；复用沿原项目内部审阅边界。
