# 言咒游戏规则入口

2026-11-02 · 阅读版8 · GDD 3.7／CORE-074。这里维护核心行为、精确细则、参数、内容合同与验收预期。先完整阅读[唯一核心正文](GDD.md)；设计目标、预期体验和具体方案集中在平级的[系统设计手册](../system-design/handbook.md)，团队工作方法查[规范层](../standards/README.md)。

| 现在要做什么 | 下一步 |
| --- | --- |
| 实现一个已定行为 | 从[任务设计包](../development/task-pack.md)开始，按行为选择必要条款 |
| 查某项规则 | [行为与规则索引](../governance/rule-index.md)，定位后只读相关章节 |
| 人工审校 | 让agent按[场景审阅规范](../standards/design-review.md)讲解，配合任务包图示 |
| 查具体物件／数值 | [具体内容库](../content-library/README.md)、[案例](examples/README.md)、[内容合同](content/cards.md)、[参数](parameters.md) |
| 检查结果应怎样 | [按行为归组的验收预期](validation.md)，不当成执行报告 |
| 查系统结构 | [系统目录](systems/README.md)与[公共流程](common/README.md) |
| 查状态、未决或来源 | 按需读[基准](baseline.md)、[问题](../governance/questions.md)、[来源索引](source-review.md) |

规则与规则情境留本目录，共用背包现行细则在[TL-46](systems/backpack-system/rules.md)，CORE-074已定范围不占格、八器本体及资源组解封；CORE-073／074冻结首战网格与装载；通用扩包和其他配置仍待设计。理由、体验和当前工作稿移至system-design；不再为未设计系统预建五个空页。细则保留确定行为与必要边界；任务包是带引用的派生视图，不能独立改规则。日常开发不加载全部来源、验收或设计理由。

复杂细则已按当前内容与条件扩展区分；周期、维护、开工标记冻结和附属反应不作为首场默认需求。审阅指出锁定／冻结／支付需优先简化后，首场说明收束为“实有、锁定、可消费与生效付款”；扩展仍在对应权威页按需读取。

完整GDD范围由[READ-1](../exploration/start.md#gdd包固定文件清单)固定，读取核心不能冒充全量。CORE-071已淘汰原EX-004及其他非alchemy内容；新[完整首战规格](../content-library/first-battle.md)已由CORE-073冻结，实施与体验NotRun。EX-003只覆盖局部条件，EX-001／002保留旧连续拍固定范围，均不发行当前物件或替代新首战输入。

<a id="言咒现行设计"></a>
