# 现行版本清单

更新：2026-10-04。Project ID：game-002。文档角色：BaselineManifest。

| 层 | 当前身份 | 边界 |
| --- | --- | --- |
| 产品设计 | GDD-G002-FULL-001 / 2.1 / TL-1 + INS-1 法器铭刻与时间产线 | 已确认核心结构进入正式系统，见G002-CORE-037–049；CORE-041的配置入口由INS-1替代 |
| 文档成熟度 | GDD-0，概念与核心结构版 | 卡表、完整时序和参数尚未闭合，不能沿用旧GDD-2的制作就绪结论 |
| 核心摘要 | Core Concept v0.8 / CORE-SUM-3 | 只浓缩本版已采纳规则 |
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
