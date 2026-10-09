# 行动卡系统

Project ID：game-002。文档角色：Navigation。修订：2026-10-08 / action-framework.1。状态：既有规则 Accepted；新增行动／标记通用结构 Qualified，用户已确认；体验 NotRun。

本系统维护行动卡的效果描述、战斗行、倒计时、目标、支付与共同结算，包含标记子系统。通用框架保留原Qualified范围；CORE-057已采纳规则页TL-11的完整通用顺序与事件边界，具体卡池仍未发行。

| 文件 | 维护内容 |
| --- | --- |
| [rules.md](rules.md) | 行动对象、效果字段、标记接口及完整保留的既有 TL 结算规则 |
| [experience.md](experience.md) | 读懂时间、标记取舍与反馈的机制—行为—体验假设 |
| [design.md](design.md) | 定位、表达方向、未决接口及后续设计边界 |
| [examples.md](examples.md) | 独立存储逐拍、支付和标记关系示例；不产生新规则或默认参数 |

## 子系统与来源

[标记系统](mark-system/README.md)维护宿主、极性、叠层、支付、独立定时兑现与生命周期边界。两页分工：本页解决行动如何表达和执行，子页解决状态如何附着、积累与兑现。

以指定主材料为主要输入；已有确认、本轮 ACT-Q1／2、旧规则及差异见 [来源记录](../../../sources/inbox/2026-10-08-action-card-framework-review.md)与 [Qualified 素材](../../../sources/materials/M-2026-10-08-action-card-framework.md)。阶段 1—4 完成沿用户前提；原始候选不因阶段完成整体成为 CurrentSpec。

[行动内容合同](../../content/cards.md) · [法器](../artifact-system/README.md) · [敌人](../enemy-system/README.md) · [全部系统](../README.md)
