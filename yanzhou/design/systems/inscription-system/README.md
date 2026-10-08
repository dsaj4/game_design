# 铭文系统

Project ID：game-002。文档角色：Navigation。修订：2026-10-08 / inscription-framework.1。成熟度：GDD-0 通用框架；继承结构 Accepted，辅槽新增约束 Qualified，体验 Hypothesis / NotRun。

本系统范围：铭文实体、核心装配、兼容与挂接，包含辅槽子系统。

| 文件 | 维护内容 | 状态 |
| --- | --- | --- |
| [rules.md](rules.md) | 核心与辅槽装配、实体占用、兼容、批次承诺及打造；引用相邻权限 | 既有 TL 为 Accepted；辅槽新增权限只作 Qualified 引用 |
| [experience.md](experience.md) | 兼容理解、实体分配、变化归因与可选修饰的观察方式 | Hypothesis / NotRun |
| [design.md](design.md) | 定位、选择及代价、表达建议、未决内容与处理顺序 | 已确认结构与建议分列 |
| [examples.md](examples.md) | 合法性、缺料、重复占用、挂接、失效、打造的边界情境 | Derived / NotRun；不新增发行实体或默认参数 |

## 系统边界

| 本系统维护 | 相邻系统维护 | 入口 |
| --- | --- | --- |
| 铭文实体、词义、合法组合、主辅槽及预设挂接 | 法器本体、处理耗时、材料托管、预留、打断与契合 | [法器](../artifact-system/README.md) |
| 装配形成的配置及效果绑定约束 | 行动种类、独立卡效、队列、实际目标与终局 | [行动卡](../action-card-system/README.md) |
| 修饰如何接入合法配置 | 实有标记、宿主、生命周期与定时兑现 | [标记](../action-card-system/mark-system/README.md) |
| 辅槽新增／解锁的结构边界 | 材料供给和数量合同、局内获取与经济、允许操作与保存 | [资源](../resource-system/README.md)、[经济](../../common/run-economy/README.md)、[交互](../../common/interaction-save/README.md) |

本轮仅整理通用结构；具体铭文、法器、行动、稀有度预算和打造价格仍由后续内容设计提供。沿用阶段 1—4 完成前提，不据此提高规则采纳或体验证据状态。

## 子系统

[辅槽系统](augment-system/README.md)：归属于铭文系统，权限、体验假设与设计独立分文件。

## 来源与核对

[核心铭刻素材](../../../sources/materials/M-2026-10-04-artifact-inscription-core.md)及 [CORE-049 采纳](../../../sources/draft-changes/D-2026-10-04-artifact-inscription-core.md)支持继承结构；[辅槽素材](../../../sources/materials/M-2026-10-08-augment-framework.md)保存 AUG-Q1—5 确认，状态不随目录整理改变。

本轮固定输入、局部原件覆盖与排除项见 [来源记录](../../../sources/inbox/2026-10-08-inscription-framework-review.md)。规则验收引用 [INS-V01–09](../../validation.md#ins-1铭刻验收预期ins-v0109)，统一问题仍见 [INS-Q01–07](../../../governance/questions.md#ins-1未决项)。没有运行玩法实验。

## 相邻文档

[法器系统](../artifact-system/README.md) · [局内获取与经济](../../common/run-economy/README.md)

[全部系统](../README.md) · [文档职责](../../../governance/document-contract.md#系统文件夹与分文件职责)
