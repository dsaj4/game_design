# 言咒 · Yanzhou

Project ID：game-002。当前设计：**GDD 2.1 / TL-1 + INS-1 / processing.2 + timing.1 + enemy.1 + commitment.1，GDD-0**。规则采纳基准2026-10-08；系统框架整理2026-10-08。核心结构、主辅槽铭刻、单一处理、生产／队列接口、阶段一共同拍序与阶段二敌情合同已采纳；发行内容、完整时序与数值待设计，体验Hypothesis / NotRun。现有探索方向已退役。

| 我想做什么 | 入口 |
| --- | --- |
| 了解游戏 | [核心设计](design/core-design.md) |
| 查询正式规则 | [GDD与系统导航](design/README.md) |
| 设计新卡表 | [内容合同与当前缺口](design/content/cards.md) |
| 查看铭刻采纳范围 | [DIR-036局部采纳](sources/draft-changes/D-2026-10-04-artifact-inscription-core.md) |
| 处理当前问题 | [问题清单](governance/questions.md) |
| 查看实现与验证 | [开发索引](development/README.md) |

[探索方向](exploration/README.md) · [阅读范围](exploration/start.md) · [术语](CONTEXT.md) · [来源](sources/README.md) · [决策与规范](governance/README.md) · [效果身份](effects/README.md) · [视觉](visual/README.md) · [历史取证](history/README.md) · [文件索引](governance/file-index.md) · [Agent规则](AGENTS.md)。

阶段一文档交付已完成：[共同规则、预算与配套情境](sources/inbox/2026-10-05-stage-one-closure.md)。示例数值不等于发行参数，阶段完成不等于运行验证。

阶段二首批文档交付已完成：[敌人压力、卡面种类与候选](sources/inbox/2026-10-05-stage-two-enemy-pressure.md)，按CORE-054采纳。该记录保留当轮进度，不再作为当前阶段待办。

当前工作是系统框架重建后的接口核对。沿用户“阶段1—4设计完成”的前提，六系统及公共流程已分文件整理；辅槽、行动／标记的新增通用结构为 Qualified，既有 TL 条款保持 Accepted，局外成长尚未开发。阶段交付、正式内容登记与运行验证分别记录，不重启旧阶段，也不把候选自动当作发行池。

[2026-10-08主系统审查与清理](governance/main-system-review-2026-10-08.md) · [当前未决接口与下一批建议](governance/questions.md#重建后接口核对2026-10-08)

当前局部采纳：[CORE-055 / commitment.1](sources/draft-changes/D-2026-10-08-batch-freeze-consumption-lock.md)，开工冻结D与应付标记、完工扣除、打断释放下拍可用；消费前预警和玩家指定数量锁定。其他Qualified框架不整包升级，完整总序与生命周期仍待补齐，NotRun。
