# 现行版本清单

更新：2026-10-05。Project ID：game-002。文档角色：BaselineManifest。

| 层 | 当前身份 | 边界 |
| --- | --- | --- |
| 产品设计 | GDD-G002-FULL-001 / 2.1 / TL-1 + INS-1 / processing.2 | 已确认核心结构进入正式系统，见G002-CORE-037–052；CORE-041的配置入口由INS-1替代 |
| 文档成熟度 | GDD-0，概念与核心结构版 | 卡表、完整时序和参数尚未闭合，不能沿用旧GDD-2的制作就绪结论 |
| 核心摘要 | Core Concept v0.10 / CORE-SUM-5 | 只浓缩本版已采纳规则 |
| 新卡表 | 重新设计；通用边界局部采纳，旧候选池已退役 | 旧53实体不是新版可用池；当前没有已采纳的新发行池 |
| 空间 | 卡牌行是主战场 | 旧2×5、邻近、锚点、满位回退及三种范围均不作为TL-1默认规则 |
| 费用与干涉 | 每战固定费用，暂不设计成长 | 具体能力、数值、时长、回充等延期 |
| 证据 | Hypothesis / NotRun | 未运行新玩法、平衡或真人测试 |
| 视觉与实现 | 原版本分别保存 | 旧暗面Demo、旧翻牌演示、布局可视化均不是TL-1规则实现 |

## 来源与替代

本轮比较输入固定为 `d6e54af395518401fb4d8466b2302a1271da557a`。新结构来自DIR-028已确认内容及本轮INT-01–13答复；[正式素材、提案、评估与差异](../sources/draft-changes/D-2026-10-01-timeline-production-core.md)记录精确范围。

[旧RC1完整目录](https://github.com/dsaj4/game_design/tree/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design)及[旧术语](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/CONTEXT.md)按固定提交保留，不创建第二份当前规格。旧CORE-001–036、53实体、12遭遇、数值、源材料及失败证据保持当时含义；只按新版明确保留的条款使用，不能填补新版Unknown。

新卡表重新设计不等于删除原始资料。探索其他方向的固定背景也不随此次主系统切换自动更新。

[现行正文](README.md) · [当前问题](../governance/questions.md) · [逐文件兼容性审查](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/compatibility-audit-2026-10-01.md)

兼容补全以TL-1提交`ed013948f6c5379fc984413ffd08ae8e7ce0f0c9`为输入，按[CORE-048](../sources/draft-changes/D-2026-10-01-compatible-rules-reuse.md)明确复用TL-26–37；不改变上轮RC1固定取证版本。原参数继续不默认继承，只有本轮明示的结构常量进入参数表。

## INS-1局部替代（2026-10-04）

复审输入为提交`a4a7aea8500970ef3504a62e576fc99f08c566db`；[DIR-036素材与P/E](../sources/materials/M-2026-10-04-artifact-inscription-core.md)只确认用户已明确的结构，通过[CORE-049采纳D](../sources/draft-changes/D-2026-10-04-artifact-inscription-core.md)回写。原方向R1–R3仍使用其登记CORE版本，本轮主系统复审范围独立登记，未刷新原输入。

TL-38–45采用法器、有限名词／动词核心空缺、必填核心、预设挂接可选辅槽、辅槽新增／解锁打造、材料类别绑定、行动类别与独立卡效及核心契合方向。替代TL-20入口、自由修饰挂接和法器直接交付资源卡路径；不改变实体占用、材料托管、有限队列、效果目标、实际顺延、每战固定干涉费用与保存边界。

材料／卡效、契合形式、打造成本与持久范围、高阶材料来源仍Unknown；后续新卡表需按铭刻接口设计与审查。仍GDD-0 / Hypothesis / NotRun，无新发行实体、实验或实现证据。

## routing.1局部澄清（2026-10-04）

输入为`b0754e5c08273201f4b04639a371ff2da16cafe6`及本轮用户四项说明、供料调时答复。[CORE-050](../sources/draft-changes/D-2026-10-04-routing-response-clarification.md)明确所有敌方行动牌正延迟、攻防／运转功能取舍、未来供料优先级可临时调整，以及供料间接调整未来开工。CORE-044的固定分料顺序局部细化为默认顺序；维护优先、托管边界和战前争入行顺序保留。

付费调牌序只保留inbox候选；额外调时与具体干涉能力待定，未确定新的卡效、配方或数值。主版本仍GDD 2.1 / TL-1 + INS-1，GDD-0 / Hypothesis / NotRun。

## processing.1局部替代（2026-10-05）

输入提交`cb5bea76595d3a7bff057a15332f5148effa84c2`及用户“仅设处理时间……”和S1-Q6–8“本批全部按推荐”。[CORE-051／M→E→D](../sources/draft-changes/D-2026-10-05-single-processing-time.md)采纳：仅处理耗时D且正整数≥1，取消J、R、独立周期／冷却及首次起点S；开工托管完整材料并预留本批所需队列容量，无位不开工，处理完成立即入行。容量Q同时计已入行牌与有效预留。

替代旧完工后留在法器等位的机制；同拍实际入行处理保留战前法器序。当轮开工预留争用、具体排位和打断释放时点仍Unknown，S1-Q1最早翻开与S1-Q5临时供料恢复未被该批确认；后续决定见processing.2。该轮主版本仍2.1、GDD-0，核心摘要v0.9／CORE-SUM-4，未新增卡池、实验或实现证据。

## processing.2接口补全（2026-10-05）

输入提交`0c511dd7f8c1e2dda84a65e2b540a2517456771d`及用户“下一批全部按推荐”。[CORE-052／M→E→D](../sources/draft-changes/D-2026-10-05-production-queue-interfaces.md)采纳S1-Q9／10／11／1／5：预留只占容量，实际入行排队；开工按有效供料优先级同时检查材料与容量，不足者本次跳过；中断结清释放预留，容量与退料最早下拍复用；入行最早下拍翻开；单份临时供料在指定结束拍分料前恢复基础方案，新替旧且不恢复旧临时方案。

保留CORE-051唯一D、无冷却、无完工等待与有限队列；不把最早下拍翻开解释成下拍保证生效。完整同拍顺序、正常离队容量复用、多牌批次、到期与新操作受理先后以及内容数值仍Unknown。主版本GDD 2.1／GDD-0不变；核心v0.10／CORE-SUM-5，全部新验收预期NotRun，无新发行实体、实验或实现证据。
