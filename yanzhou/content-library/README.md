# 言咒具体内容库

**[打开 HTML 内容展板](index.html)**，查炼金物件、图稿、配方与实际占形。

2026-11-02 · CONTENT-LIBRARY-07 · game-002。设计手册指导如何设计，内容库存储具体产物；入库不等于玩法采纳或制作完成。

## 内容与边界

本版包含67项alchemy具体内容：32材料、11成品、8法器、10核心、1个炼金咒标记、1个新敌人与4张敌牌；另有35配方、3构筑草稿及1份冻结首战。CORE-072已采纳35配方的逐条D／承载／各项投入1份／产1张／额外制造费0、43卡权限与11成品合同、新的咒定义。CORE-073已限定冻结[首战完整规格](first-battle.md)（[网页版](first-battle.html)）：实际套组、核心副本、启动料、初态、有限补给、五列敌程序与合法布局。其他全库配置仍按原资格；旧效果只留历史对照。CORE-074进一步采纳一格接触与唯一链接、资源卡组本拍解封资格及[八法器格形](artifact-geometry.md)（[可切换范围展示](artifact-geometry.html)）；首战更新为first-distillation.2。

| 查什么 | 内容分册 |
| --- | --- |
| 当前法器本体与宽供料范围 | [八法器格形](artifact-geometry.md)／[范围展示](artifact-geometry.html) |
| 首战具体用什么、打什么 | [冻结首战规格](first-battle.md)／[网页](first-battle.html) |
| 材料、成品、法器、核心、文案与占形 | [炼金物件](alchemy.md) |
| 投入、产出、器具、职责与已有装载 | [35条具体配方](recipes.md) |
| 炼金路线的具体组件与取舍 | [构筑草稿](builds.md) |
| 局部部署见证与旧预算边界 | [配置与历史算例](alchemy-notes.md) |

用户已明确淘汰全部38项非alchemy条目，包括两件独立造型稿；条目、关系、专属来源引用及四个分册均已删除，不保留为储备或候选。现行库不再读取旧首战、敌人储备、信息小样或独立造型内容。决定与固定历史版本见[CORE-071采纳记录](../sources/draft-changes/D-2026-11-01-alchemy-only-content.md)。原EX-004完整首战输入随之撤下，新的首战套组与敌表由[CORE-073](../sources/draft-changes/D-2026-11-01-alchemy-first-battle.md)另行冻结，未恢复任何退役身份。

原内容来源仍沿catalog登记的B01／R09及其固定版本；本版限定采纳见[CORE-072](../sources/draft-changes/D-2026-11-01-alchemy-executable-content.md)。具体数值只维护于catalog，各分项资格可查；成品合计D工时按已采纳配方求和，不是完工拍。原身份、配方连接与图稿保持；CORE-074替换八法器本体／接收范围及对应几何见证，新增炼金咒使用新身份，不恢复退役首战标记。五种材料15张图仍指向原件。

不收录抽象规则、算法、UI组件、纯世界观分类、空系统或FX追踪身份。缺失内容保留Unknown，历史名称不补作当前发行内容。

## 各写一处

- **设计方法、目标与取舍**：写[系统设计手册](../system-design/handbook.md)及对应分册。
- **具体物件、文案、规格、配方与构筑**：只改[catalog.json](catalog.json)，保留稳定ID、资格、适用域与必要来源。
- **通用行为与内容字段合同**：仍在`design/`；具体内容出现某个字段不扩展规则权限。
- **历史输入与资格**：仍按`sources/`及固定版本追溯；已淘汰条目不重新作为活动来源。

`alchemy.md`、`recipes.md`、`builds.md`、`first-battle.md`／`.html`、`artifact-geometry.md`／`.html`和`index.html`由同一数据源生成；`alchemy-notes.md`保留其原局部算例边界。更新catalog后重建派生页，避免双写。Raw仅可作为明确标注工作稿，正式资格与采纳沿项目流程；未知不补0。

## 展板与更新

展板可直接打开，无网络依赖，支持搜索、类别／状态筛选、仅看有图、详情、图稿切换、配方投入职责与装载、关联跳转。无图时显示类型符号；外部本机图片不可访问时保留文字和几何。

生成器、模板和浏览器检查位于[外部构建说明](E:/Project/yanzhou-ui-prototypes/content-library-2026-11-01/README.md)。本仓库保存数据、派生交付与登记；更新后执行构建、`--check`及浏览器检查，交付身份见[manifest](manifest.json)。

## DM-G002-023 具体内容库展板

game-002 / main；CONTENT-LIBRARY-07；用途为炼金内容检索与审阅，ReadyForScope / PresentLocal仅限静态页面。程序源码和检查证据留外部目录，具体资格沿条目，页面可用不证明玩法可行。

derived-from：DM-G002-019@R09；uses：AS-G002-040@ALCHEMY-ITEM-PILOT-02、AS-G002-041@CARD-FRAME-02。现行库已解除两件独立造型的引用。图稿原件就地，未移动、改绘或上传；页面和符号原创，源图仅沿原项目内部审阅边界使用。
