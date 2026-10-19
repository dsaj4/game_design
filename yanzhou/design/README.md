# 言咒主系统

2026-10-18导航核对 · GDD 2.6 / GDD-0。当前先完善首场核心玩法，再进入2D表现方向；规则本身没有因整理改变。先看[开发期间设计变化与复盘](../governance/development-review-2026-10-18.md)及[当前问题](../governance/questions.md#开发前先看)，开发时使用[规范](../development/development-standard.md)与[阶段计划](../development/production-plan.md)。

**从[GDD](GDD.md)看整体，再按系统查 rules；[EX-001](examples/simple-spell.md)保留原回归，[EX-002](examples/complete-battle.md)给出独立完整单战。** 当前未决事项只在[问题登记](../governance/questions.md)维护。

| 需要什么 | 入口 |
| --- | --- |
| 简短理解游戏 | [核心设计](core-design.md) |
| 整体循环与开发阅读顺序 | [GDD](GDD.md) |
| 六系统及两子系统 | [系统目录](systems/README.md) |
| 路线、经济、交互与保存 | [公共流程](common/README.md) |
| 首批物件与具体情境 | [Examples](examples/README.md) |
| 物件字段与内容状态 | [卡牌](content/cards.md) · [法器](content/wands.md) · [遭遇](content/enemies-encounters.md) |
| 常量与数值使用方式 | [参数](parameters.md) |
| 行为验收预期 | [验收](validation.md) |
| 版本、资格与来源 | [基准](baseline.md) · [来源审查](source-review.md) |

每个系统保留五个文件：README导航；rules规定行为；design解释设计；experience列体验目标与失败信号；examples解释情境。全套共用TL-11结算顺序，规则不在示例或UI说明中另写一套。

完整系统仍有待决项；EX-001提供首批配置，EX-002仅增加本场完整战斗参数。案例值不是全游戏默认值。新增验收预期和体验观察未执行，旧局部工程证据沿其原版本。

<!-- 旧章节链接保留；历史正文见 baseline 固定版本。 -->
<a id="言咒现行设计"></a>
