# game-002 代码开发进度

日期：2026-09-11。设计依据：[Core Concept v0.6](../game-design-workflow/core-concept.md)。

| 里程碑 | 设计来源 | 状态与证据 | 阻塞与下一步 |
| --- | --- | --- | --- |
| 战前配置与完整自动战斗 | 当前核心及[正式素材](../game-design-workflow/idea-materials/README.md) | Planned；尚无符合当前全流程的实现验收证据 | [接口范围](design-decisions-needed.md)已确认；先建立当前规则所需参数，再登记实现与验证 |
| 时间、覆盖、打断与终止验证 | 当前核心及[攻防候选v0.1](../game-design-workflow/idea-materials/M-2026-09-11-simple-spell-parameter-candidates.md) | Limited Verified：TH-2026-09-11-001/r2的726组逐事件差分与10项规则边界通过；[报告](test-reports/TH-2026-09-11-001-r2-run-01.md) | 仅两句攻防、固定单敌；其他词义和完整流程未验收 |
| 超时疲劳 | [G002-CORE-014与FAT-C候选](../game-design-workflow/idea-materials/M-2026-09-11-overtime-fatigue.md) | Design Only；方向已采纳，本轮没有实现或验证证据 | 先按TH-2026-09-11-002/r2独立审查执行候选；TH-001实现不含疲劳，不能沿用其Pass |
| 词义、数值与路线验证 | 当前合格素材及[数值重设计任务](numerical-redesign.md) | Planned；候选参数不等于已平衡 | 重新建立输入并完成资格确认，再验证完整规则关系 |

可用实现资源目录为 E:/Project/game-002-glyph-timeline；本次未检查或修改该目录，不能据目录存在推定当前设计已实现。[实现记录快照](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/docs/code-development-index.md)保留已登记的提交、测试范围及原始证据。

## 关联demo数值测试注册

按用户2026-09-11指定的「时序施法原型」任务，另登记`E:/Project/yanzhou-pixel-lab`为本轮可玩数值测试实现；不替换上述资源身份，不视为完整v0.6实现。

| 项目 | 当前记录 |
| --- | --- |
| 设计与参数 | 固定提交1d4bb7faff715f787cba31794829fc8c6527a1c1；Candidate v0.1，未Accepted |
| 实现提交 | 8347088f5e56d46bdc39793cfeb2b59ef01dba33；分支codex/test-agent-candidate-v01，本地已提交，无远端 |
| 测试协作 | [固定交接](test-handoff.md)，TH-2026-09-11-001 / r2，Codex测试agent任务01a08e19-0acb-7cb2-a022-1f54ec6c308d |
| 可玩入口 | [本地demo](http://127.0.0.1:5199/)；根目录已有启动言咒.cmd |
| 已覆盖 | 四种攻防配置、8/10/12刻敌人节奏、六张实体卡、两根法杖、单敌、时间编排、自动战斗、记录导出入口；页面共用引擎726组与独立模型一致，构建与包装检查通过 |
| 实现边界 | 原v0.5视觉资产复用，旧火焰/雷电/回响与金币参数不参与本包；每次重试还原输入生命。范围恒定许可、无跨战成长；浏览器交互和玩家体验未验收 |
| 技术细节与证据 | [代码仓库测试维护说明](E:/Project/yanzhou-pixel-lab/docs/numerical-testing.md)、[实现哈希与事件清单](E:/Project/yanzhou-pixel-lab/docs/test-evidence/TH-2026-09-11-001-r2-run-01/verification.json) |
| 下一步 | 当前先审查数值框架与疲劳候选；后续实现疲劳须登记新设计／实现版本并独立验证。T01/T02玩家可读性测试仍未执行 |

技术细节与测试结果写在对应代码仓库；本索引只记录里程碑、证据、阻塞和下一步。代码完成度不能提升核心或素材的证据状态。
