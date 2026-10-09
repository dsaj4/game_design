# 辅槽子系统

Project ID：game-002。文档角色：Navigation。修订：2026-10-08 / system-docs.1。范围：系统通用框架；沿用阶段 1—4 已完成的前提。

2026-10-08局部更新：[CORE-055 / commitment.1](../../../../sources/draft-changes/D-2026-10-08-batch-freeze-consumption-lock.md)已采纳本批D与开工标记冻结、完工扣除、打断释放及消费锁定相关接口；其余Qualified范围保持原状态；CORE-057已补通用总序、定时与支付承诺边界，具体上限／刷新／跨战等生命周期内容仍待定。

辅槽让玩家在本法器的生成节奏、行动量值与标记使用之间做配置取舍，同时保留可见成长。

| 文件 | 内容 | 状态 |
| --- | --- | --- |
| [rules.md：已确认规则与边界](rules.md) | 作用范围、允许修改项、支付底线、稀有度表达与既有接口 | 既有接口为 Accepted；AUG-Q2—5 为用户已确认的 Qualified 框架，尚非完整 CurrentSpec |
| [experience.md：玩家体验假设](experience.md) | 机制可能引起的行为、预期体验、观察与失败信号 | Hypothesis / NotRun |
| [design.md：设计定位与待定方案](design.md) | 已确认价值顺序、设计理由、表达方向、待补接口 | Q1 为已确认方向；具体落地建议与 Unknown 分列 |
| [examples.md](examples.md) | 独立情境、确定结果及未决边界；不新增规则或参数 | 说明性示例 / NotRun |

本目录是铭文系统下的辅槽子系统，不另分配 SYS 编号。槽位、实体、生产、队列和打造等共享规则仍由对应系统维护；本目录声明辅槽如何接入。放入 `rules.md` 表示它是规则性内容，不表示跳过资格、提案与采纳流程。

本次以已确认的 [通用框架素材](../../../../sources/materials/M-2026-10-08-augment-framework.md) 重写。原三份 `positioning.md`、`rules.md`、`examples.md` 已在本地逐字节备份；原输入身份与哈希见 [来源记录](../../../../sources/inbox/2026-10-08-augment-framework-review.md#文档拆分与原输入保全)。旧数值、线性三阶与被排除的效果不作为本版默认。

[铭文系统](../README.md) · [全部系统](../../README.md) · [分文件维护约定](../../../../governance/document-contract.md#系统文件夹与分文件职责) · [规则来源与用户原话](../../../../sources/inbox/2026-10-08-augment-framework-review.md#原始想法与触发来源)
