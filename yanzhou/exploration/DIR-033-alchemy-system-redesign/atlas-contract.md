# DIR-033 展示册接口

2026-10-02 / ALC-ATLAS-01。这是设计与展示工作者的交付接口，不是正式游戏规则。协调者独占修改。

## 展示目的

“玩家搭建一套会自行取料、加工并产出行动卡的炼金系统。”可见地展示工具、实际占用的构筑卡、耗材、中间产物、行动卡与效果协同。至少三个系统例子必须用同一套卡义，不能隐藏整句奖励或凭组合名称赋予额外权限。

推荐候选表达：从单一“材料—动作—目标”句转为端口化配方结构，基础配方仍可读成材料／操作／产出（行动则含目标预设）；额外端口只来自真实构筑卡。工具与法阵是同一自动生产体系的载体和连接关系。不要把资源卡当成构筑卡实体。

## JSON交付

文件atlas-data.json，UTF-8，无外部依赖。根字段：version、status、sourceCommit、summary、rules、cards、blueprints。status必须明确Raw / Hypothesis。

- rules：数组，每项id、title、body、boundary（字符串）。
- cards：数组，每项id、name、kind、role、text、cost、timing、ports、tags、limit、example（字符串或字符串数组；kind为build/resource/action/tool）。每张卡有明确输入／输出及有限触发边界。至少18张，覆盖四种kind。
- blueprints：数组，至少3项。每项id、name、promise、tradeoff、nodes、links、steps、breakthrough、ledger。nodes为{id, toolCardId, buildCardIds, label}数组；links为{from,to,resourceId,label}数组，from/to须存在于本系统nodes中；steps为字符串数组。ledger为字符串数组，明确共同初始输入、成本、产出和时序，不能把算例当平衡结论。
- 构筑卡名称／数值不得在展示代码里另维护一套规则。显示以本数据为准。

数据驱动增补：允许根字段demo，其中inventory为{instanceId,cardId}实体库存，tools为{instanceId,cardId,slots:[{id,label,acceptKinds,acceptTags}]}执行单元；portSpec按cardId声明结构化输入／输出资源与装配角色；simulation声明真实输入、成本、时间、触发次数／上限和预期输出。设计与展示工作者共同对齐字段，协调者冻结最终结构。机器字段只是候选卡义的派生表达，不能独立创造规则。

最终ALC-ATLAS-01.1结构：portSpec是以cardId为键的对象，roles使用core/feed/out/aux，requiredFeeds／requiredOutputs表示必需端口数量，allowedFeeds／allowedOutputs／compatibleAuxIds声明允许实体。blueprints.nodes补充toolInstanceId、placements与instancePlacements（槽位→卡义／真实实体映射）、start、rest与priority。demo另含grammar、initialResources、environmentSupply；simulation包含parameters、operations、traces、alternatives与invariantCases。每个operation明确耗材、托管保留方式、D/J/R及资源／行动输出；trace独立保存起始资源、逐时点账与expected。alternatives是另外的候选计划，不能偷换当前trace的结果；invariantCases是待检查边界，不是执行通过记录。

展示包复制本方向atlas-data.json作为固定输入，SHA-256必须一致；重建单文件仅为交付封装，不产生第二套可编辑规则。机制与卡册正文是本版数据的解释，后续改动需同时复核它们，避免卡面、机器字段和例子分叉。

## 最小交互

机制页、卡牌页、系统页与构筑台；筛选与详情；选取系统案例；从真实库存装配／拆解构筑卡并连接工具；校验输入输出类型与实体占用；显示缺料、待交付或通路未闭合的具体原因；至少一个有成本的协同算例。允许展示工具用简化参数，但必须标清范围与省略。

展示器自行选择轻量原生HTML/CSS/JS实现。不需要账户或联网。图形原创，不导入第三方截图和旧Demo源码。实验只限确定性规则算例与交互检查；不声称完整战斗实现或体验验证。玩家页面用自然语言，技术细节和检查记录留外部README。
