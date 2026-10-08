# 敌人系统

Project ID：game-002。文档角色：Navigation。修订：2026-10-08 / enemy-framework.1。设计基准：GDD 2.1 / GDD-0，TL-1 + INS-1 / processing.2 + timing.1 + enemy.1。

本系统范围：敌方固定程序、遭遇输入与内容约束、应对窗口、敌情信息和表现方向。沿现有五文件整理；不新增敌人发行池或战斗能力。

| 文件 | 维护内容 | 当前状态 |
| --- | --- | --- |
| [rules.md](rules.md) | TL-16、遭遇字段、首版限制、信息与跨系统接口 | 继承 Accepted；标记仅作 Qualified 接口引用，未决处为 Unknown |
| [experience.md](experience.md) | 敌情如何影响选择、观察任务与失败信号 | Hypothesis / NotRun |
| [design.md](design.md) | 压力定位、选择代价、秘仪与炼金方向及待定依赖 | 已确认方向保留；具体表现和完整内容仍待定 |
| [examples.md](examples.md) | 揭示、取消、锁定、停供、终局和种类辨识的六组情境 | 已采纳规则的 Derived 说明；无运行证据 |

## 系统边界

| 本系统维护 | 相邻权威负责 |
| --- | --- |
| 敌方程序与遭遇合同 | [行动卡](../action-card-system/rules.md)：揭示锁定、取消、共同拍序、伤害、中断、落空与终局 |
| 应对窗口对玩家生产的要求 | [法器](../artifact-system/rules.md)：供料调整、处理耗时、容量、入行及返工；[资源](../resource-system/rules.md)：材料可用拍与维护 |
| 敌人作为标记宿主的接口引用 | [标记](../action-card-system/mark-system/rules.md)：宿主、极性、叠层、定时登记和未决排序；仍为 Qualified |
| 敌情信息的分阶段衔接 | [局内路线](../../common/run-route/rules.md)：出发前摘要；[交互与保存](../../common/interaction-save/rules.md)：信息可达性与恢复 |
| 敌人通用设计与内容准入约束 | [敌人与遭遇内容](../../content/enemies-encounters.md)：绿狮、万溶之液、雷比斯等候选及具体程序；数值 Illustrative |

## 来源与状态

- 已采纳来源：[阶段二 Qualified 素材](../../../sources/materials/M-2026-10-05-stage-two-enemy-pressure.md) → [限定评估](../../../sources/evaluations/E-2026-10-05-stage-two-enemy-pressure.md) → [CORE-054](../../../sources/draft-changes/D-2026-10-05-stage-two-enemy-pressure.md)。不重新询问阶二 Q01—24。
- 标记接口：[行动／标记局部素材](../../../sources/materials/M-2026-10-08-action-card-framework.md)。宿主范围已确认，不代表具体敌牌、延迟修改或新触发事件已经采纳。
- 本轮固定输入 `a23c75d74187f45f04b50376658be0274049f3f8`；实际覆盖、未提交原件哈希和取舍见 [敌人来源审查](../../../sources/inbox/2026-10-08-enemy-framework-review.md)。文档整理记 [DOC-016](../../../governance/decision-log.md#g002-doc-016)。
- 首批敌人仍为候选；完整遭遇参数与复杂结算未冻结。文档阶段完成、玩法采纳、体验验证和实现状态分别判断；本轮仅静态整理，未开展玩法实验。

## 相邻文档

[敌人与遭遇内容](../../content/enemies-encounters.md) · [局内路线](../../common/run-route/README.md)

[全部系统](../README.md) · [文档职责](../../../governance/document-contract.md#系统文件夹与分文件职责)
