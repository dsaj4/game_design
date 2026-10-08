# 法器系统

Project ID：game-002。文档角色：Navigation。修订：2026-10-08 / artifact-framework.1。设计基准：GDD 2.1 / TL-1 + INS-1 / processing.2 + timing.1 + enemy.1；框架成熟度 GDD-0。证据：Hypothesis / NotRun。

本系统范围：法器本体、处理流程、供料编排、容量预留、打断返工与契合接口。

| 文件 | 维护内容与状态 |
| --- | --- |
| [rules.md](rules.md) | TL-03—07／38／45 为 Inherited / Accepted；辅槽及标记接口引用既有 QualifiedFramework，未升级为完整采纳 |
| [experience.md](experience.md) | 自动运行、瓶颈识别、应对窗口及成长归因的假设与观察方式；均 NotRun |
| [design.md](design.md) | 法器定位、既有取舍、契合方向与未决接口；整理建议和已确认方向分开 |
| [examples.md](examples.md) | 开工、预留、排队、打断、改线、标记与终局情境；说明性推导，不是发行参数或运行结果 |

## 系统边界

| 本系统负责 | 相邻系统负责 | 入口 |
| --- | --- | --- |
| 接受合法配置，决定能否开工与何时完成 | 铭文实体、暗句补全、兼容、装配与打造 | [铭文规则](../inscription-system/rules.md) |
| 托管本批材料并承担有限容量承诺 | 材料来源、可用时点、维护及数量合同 | [资源规则](../resource-system/rules.md) |
| 完工提交行动卡，区分完工与生效 | 普通队列、目标、行动支付、敌牌倒计时与终局 | [行动规则](../action-card-system/rules.md) |
| 接收本法器的时间及行动量值修饰 | 辅槽权限、实际标记状态、读取与支付 | [辅槽](../inscription-system/augment-system/rules.md)、[标记](../action-card-system/mark-system/rules.md) |
| 维护法器与核心铭文的契合接口 | 具体法器、配方、D、批次张数与参数 | [法器内容合同](../../content/wands.md)、[参数](../../parameters.md) |

## 本轮范围与来源

依据用户“阅读此交接文档，整理法器系统相关内容”，沿现有五文件框架归位。固定输入为 `71e7a0a18709e19e85ea171feb10b2ba2b432097`；已提交来源与本地 Raw 输入分别登记在 [法器整理来源记录](../../../sources/inbox/2026-10-08-artifact-framework-review.md)。

本轮复用 [辅槽 Qualified 素材](../../../sources/materials/M-2026-10-08-augment-framework.md)和 [行动／标记 Qualified 素材](../../../sources/materials/M-2026-10-08-action-card-framework.md)中已确认的接口，不新建另一套资格或玩法决定。阶段 1—4 完成沿既有前提；具体卡池、法器发行、局外成长、原型及玩法实验不在本轮范围。

旧输入中的减料、多产、虚拟材料和压缩预留例不进入本框架；处置与未读范围见来源记录。文档整理记为 [G002-DOC-015](../../../governance/decision-log.md#g002-doc-015)，不改变 CORE 采纳。

## 相邻文档

[铭文装配](../inscription-system/README.md) · [法器内容](../../content/wands.md)

[全部系统](../README.md) · [文档职责](../../../governance/document-contract.md#系统文件夹与分文件职责)
