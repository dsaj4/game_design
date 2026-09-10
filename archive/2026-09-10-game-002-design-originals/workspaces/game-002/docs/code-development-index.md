# game-002 代码开发进度

最后更新：2026-09-09

当前设计基线：`Core Concept v0.5 / Stable Design Baseline`。现有代码和实验只验证旧的战中牌库流程与测试数据，不代表当前自走棋式自动战斗已经实现或验证；不得把实验状态写回核心设计。

用户于2026-09-07指定 `E:/Project/game-002-glyph-timeline` 的测试接口和18张样例，要求导入既有测试数据并尝试动词、名词分堆。本次登记这个独立样片的实现与验证事实；不继承旧游戏代码或测试，不将双牌库试验自动写成正式玩法。
技术细节、提取审阅单与实验数据留在对应代码仓库。此前“无代码仓库”的记录属于建区时快照，不代表此样片当前不存在。

| 项目/里程碑 | 设计来源 | 代码仓库 | 状态 | 证据 | 偏差/阻塞 | 下一步 |
| --- | --- | --- | --- | --- | --- | --- |
| 18张校准测试数据载入 | [已确认数值框架](../game-design-workflow/idea-materials/M-2026-09-07-core-numerical-framework-v01.md)、[测试六词卡表](../game-design-workflow/idea-inbox/2026-09-07-simple-spell-starter-deck.md)及用户本轮指定接口 | E:/Project/game-002-glyph-timeline | Verified / Experimental | [接口与可导入样例](E:/Project/game-002-glyph-timeline/docs/test-data.md)；[验收记录](E:/Project/game-002-glyph-timeline/docs/verification.md) | 固定起手与demo洗牌不同于离线模型，不承诺复现原38T轨迹；力量和词义仍为测试假设 | 使用测试面板比较同参数下的供牌 |
| 动名双牌库对照 | 用户明确要求尝试两类抽取卡组；具体交替、空类与预览规则是本次实验裁定 | E:/Project/game-002-glyph-timeline | Verified / Experimental | [1536场实际引擎对照](E:/Project/game-002-glyph-timeline/docs/dual-deck-experiment.md)、[本地提取记录](E:/Project/game-002-glyph-timeline/design-supplements/records/F-2026-09-07-dual-deck-experiment.md)；79项规则与42项桌面/手机回归通过 | 正式单牌库基线未修改；提取v1尚未批准玩法入箱，无整局或玩家平衡证据 | 按等总供给结果评议词性稳定与语义配对；需要时再明确后续实验变体 |

代码分支：`codex/dual-deck-experiment`；提交：`804400d2dab8a7159e4fe3ceaddd3f68262f41f5`。该代码仓库未配置远端，本次为本地提交，没有伪称推送。开发服务：[http://127.0.0.1:5183](http://127.0.0.1:5183)，测试数据面板可分别选单牌库、双牌库样例并载入重开。

状态：Planned / In Progress / Implemented / Verified / Blocked / Parked。
实现状态不能替代玩法确认。
