# 当前设计基准

2026-11-04 · **GDD 3.9 / GDD-0 · CORE-076 table-axis.2**。[R1—R6采纳D](../sources/draft-changes/D-2026-11-04-column-scheduling.md)统一列时序、整体确认、同器续批、费用合并与零材料指令；空间沿CORE-075。[首战与内容库迁移](../sources/draft-changes/D-2026-11-04-first-battle-table-axis-migration.md)已完成：CONTENT-LIBRARY-08、first-distillation.3、EX-005与首战包已同步。四通用包、展示合同及其他旧表述清理仍待完成；主游戏与体验NotRun。

| 项目 | 当前范围 |
| --- | --- |
| 核心 | [GDD](GDD.md)唯一连续正文；三权限统一卡牌，材料为用途 |
| 背包 | [TL-46](systems/backpack-system/rules.md)：跨战与生产共用网格、备用配置占格、分阶段装载、散装核心1格／兼容嵌入额外0格；首战几何已定，其他几何与交易细则待补 |
| 核心与辅助 | 核心战前可逆装配；CORE-075辅助覆盖圈替代单器连接，同效叠加与批次继承保持；相关旧表述仍待清理，不属于本轮R1—R6增量 |
| 生产与排程 | 固定用途，工序行手动排料／零材料指令；c至c+D−1占用、c+D可用，同器下列续批；本列整体确认，非法或费用不足保留草稿、不推进、不部分冻结 |
| 使用与结算 | 两组持牌、免费布置、立即回收；每回合5个时间列，确认冻结后战斗，未终局才列末到货／补给；序幕无敌牌、不计疲劳 |
| 当前具体内容 | [内容库](../content-library/README.md)69项alchemy、35配方、3构筑；八器本体沿CORE-074，P／两炉心沿CORE-075；首战新增一小炉与序幕后已同步，其他配置／携带／取得继续按原资格 |
| 案例 | [EX-005](examples/first-battle-alchemy.md)已按CORE-076重算指定手动路线、两胜一败与重装；EX-003独立条件机制例；EX-001／002固定旧输入；EX-004继续退役 |
| 未迁移扩展 | 定时、期限、维护等保持原资格，新时序未闭合，不因内容清理启用 |
| 展示与实现 | 首战布局／内容及专用包已同步，四通用包与展示合同待同步；完整实现、玩法与体验NotRun，旧证据不外推 |

## 状态与适用域

Accepted、Qualified、实现与体验证据分别记录。CORE-072只采纳明确字段；原61项之外新增炼金咒定义，不恢复退役身份。CORE-071替代CORE-066的原首战内容，并删除敌人储备、关系小样与两件独立造型的内容库身份；通用规则和原独立历史证据保持其适用域。新内容缺失写Unknown，炼金候选不自动成为首战输入。

[验收](validation.md)保留通用规则情境和既有ID；退役内容的数值路线撤下，不作为当前通过条件。已完成静态几何与指定路线算术检查；未运行主游戏、引擎恢复或玩家测试。

## 版本与来源

本次列时序沿[CORE-076](../sources/draft-changes/D-2026-11-04-column-scheduling.md)，空间沿CORE-075；此前范围／解封规则沿[CORE-074](../sources/draft-changes/D-2026-11-02-feeding-ranges.md)，首战原冻结沿[CORE-073](../sources/draft-changes/D-2026-11-01-alchemy-first-battle.md)，原限定内容沿[CORE-072](../sources/draft-changes/D-2026-11-01-alchemy-executable-content.md)；通用规则和各历史来源继续按其范围。

启动任务仍一次固定整个设计仓库提交，包与细则共用。实现证据只在[开发入口](../development/README.md)，未决见[questions](../governance/questions.md)，来源见[source-review](source-review.md)。

<a id="2026-10-08系统框架重建与审查"></a>
<a id="commitment1批次冻结与消费锁定2026-10-08"></a>
<a id="enemy1敌情合同与卡面种类2026-10-05"></a>
<a id="guidance-alignment1设计与体验集成2026-10-11"></a>
<a id="ins-1局部替代2026-10-04"></a>
<a id="processing1局部替代2026-10-05"></a>
<a id="processing2接口补全2026-10-05"></a>
<a id="resource1资源设计与通用边界2026-10-09"></a>
<a id="routing1局部澄清2026-10-04"></a>
<a id="time-formula1耗时公式2026-10-08"></a>
<a id="timing1共同拍序与阶段一完成2026-10-05"></a>
<a id="timing2同拍结算2026-10-08"></a>
<a id="来源与替代"></a>
<a id="现行版本清单"></a>
