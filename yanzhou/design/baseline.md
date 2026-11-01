# 当前设计基准

2026-11-01 · **GDD 3.4 / GDD-0 · CORE-071 alchemy-only.1**。用户已明确淘汰38项非alchemy内容，原EX-004案例与首战包撤下，完整首战套组、敌表与初态待设计。依据[CORE-071采纳D](../sources/draft-changes/D-2026-11-01-alchemy-only-content.md)。

| 项目 | 当前范围 |
| --- | --- |
| 核心 | [GDD](GDD.md)唯一连续正文；三权限统一卡牌，材料为用途 |
| 背包 | [TL-46](systems/backpack-system/rules.md)：跨战与生产共用网格、备用配置占格、分阶段装载、散装核心1格／兼容嵌入额外0格；几何与交易细则待补 |
| 核心与辅助 | 核心战前可逆装配；辅助独立占格单器连接，同效可叠加，批次／成品继承，战中固定 |
| 生产与供料 | 固定用途、专属待料、齐备吸收、默认自动补料；空间与时点沿CORE-068／069／070 |
| 使用与结算 | 两组持牌、免费布牌、列间停顿、立即回收；5生产拍／5列，敌后续、疲劳、终局与恢复规则保持 |
| 当前具体内容 | [内容库](../content-library/README.md)仅保留61项alchemy、35配方、3构筑，原值与逐项资格保留；未采纳完整首战 |
| 案例 | [EX-003](examples/round-hand.md)仅保留独立条件机制例；EX-001／002为旧连续拍固定输入；EX-004退役，不供新实现使用 |
| 未迁移扩展 | 定时、期限、维护等保持原资格，新时序未闭合，不因内容清理启用 |
| 展示与实现 | 旧工程及HTML按原固定版本保留；完整新内容与背包布局未闭合，执行和体验NotRun |

## 状态与适用域

Accepted、Qualified、实现与体验证据分别记录。CORE-071替代CORE-066的原首战内容，并删除敌人储备、关系小样与两件独立造型的内容库身份；通用规则和原独立历史证据保持其适用域。新内容缺失写Unknown，炼金候选不自动成为首战输入。

[验收](validation.md)保留通用规则情境和既有ID；退役内容的数值路线撤下，不作为当前通过条件。未运行新的程序模拟、引擎或玩家测试。

## 版本与来源

本次内容退役沿[CORE-071](../sources/draft-changes/D-2026-11-01-alchemy-only-content.md)；空间、装配、供料和统一卡牌分别沿[CORE-070](../sources/draft-changes/D-2026-11-01-shared-backpack.md)、[069](../sources/draft-changes/D-2026-10-31-spatial-auxiliaries.md)、[068](../sources/draft-changes/D-2026-10-31-backpack-production.md)、[067](../sources/draft-changes/D-2026-10-27-unified-card-model.md)。历史记录保留原日期／范围，后续替代不改写当时采纳事实。

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
