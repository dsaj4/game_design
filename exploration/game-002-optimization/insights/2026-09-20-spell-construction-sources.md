# 本轮法术构筑探索：来源与边界

- 日期：2026-09-20
- Project ID：`game-002-optimization`；目标游戏：`game-002`
- 状态：`Research / Provisional`
- 起始提交：`97a1bfc9774845d3e63f3bc5bba29e14ba8a8e16`
- 活动包：`baseline-2026-09-09-001`，来源提交`d0c36b9d464680a484f83b234db081b97124b701`，本轮未改动或重新激活背景包。

## 授权与读取范围

用户明确进入exploration，目标game-002，禁止阅读其他探索方向，并指定全游戏GDD，要求完善语义引擎、词条锻造、几何构型后分析。按注册表路由到`exploration/game-002-optimization/`。

显式指定GDD作为本轮补充来源；其主页明确关联Wiki属于GDD正文。本轮仅补读构句／配置和战斗／状态两页中与三候选直接相关的规则，没有沿来源链接加载旧inbox、决策链、其他玩法方向或代码。

根及本项目README、AGENTS、运行手册和注册表仅用于路由、隔离和写入规则；其中已有历史方向的导航摘要不可避免可见，未展开对应正文，亦未作为本轮创意依据。run-control只检索运行结构和预算字段，旧运行正文保留。

## 设计来源清单

路径均相对仓库根。Git blob定位固定版本；SHA-256为本轮独立工作树的完整文件字节摘要，可能包含本地换行约定，不与Git对象ID混用。

| 来源 | Git blob | SHA-256 |
| --- | --- | --- |
| workspaces/game-002/game-design-workflow/gdd/GDD-2026-09-14-yanzhou-full-game.md | ec73f57ed12cb2b95f09f4fd2a1ac409ee4314f9 | 8bcea638dbb4a72194100ae0189cfb6dbb871acfdf118e2fd508330ac2d170c6 |
| workspaces/game-002/game-design-workflow/gdd/yanzhou-rc1/02-grammar-and-configuration.md | 8197ed5395ce97a345c097f73ab10dda9ab3f520 | 5dd54a0966ffdec1d7f40c99cc36e9c94274caf877f832494d9cfb8e533bf243 |
| workspaces/game-002/game-design-workflow/gdd/yanzhou-rc1/03-combat-and-status.md | 1607cbe8a6cc603f3970e8a835b5a526d0141e4c | 96b73e32242fe2ac8e30e2255933def77ebf37b804313fa4817c458d38f65ada |
| exploration/game-002-optimization/context/baseline-2026-09-09-001/context-pack.md | eaef75fb8740f254ab05e010ba579de20ab8ab67 | 90895b2085e01b63e119488a6835206f3a24d9523436034ab7c809f8078dffbb |

重点读取位置：GDD产品合同、不变量、系统依赖、成长和证据状态；02的WG01、SG01、CG01、修饰词、镶嵌与效果组边界；03的核心闭环、RC02／04／06、BR03／05／06、GR02／03／05／07及阶段次序。没有声称本轮重新审计全卡池数值或全部遭遇。

## 版本差异处理

旧包描述核心尚未开始以及手牌／补牌等早期设计。用户指定RC1已明确战外完整库存构句、循环法杖、共享槽与完整一局。涉及本轮机制判断时采用RC1；旧包只保留其登记身份与历史边界，不导入旧手牌循环或数值。

RC1规则Accepted不等于体验已测。本轮所有新卡名、空间容量、记忆限制、锻造渠道建议和示例数值均为Agent推荐假设。用户要求“完善构思”授权草拟，不能据此将自行补完内容写成已通过素材资格。

## 方法与模板

- [原始想法登记模板](../../../game-design-workflow/templates/idea-template.md)：保留原话、触发、体验假设、资格字段和状态。
- [共享评判框架](../../shared/evaluation-frameworks/README.md)：版本v1.0，底层参考框架v0.1；使用有效选择、因果链、可理解涌现和伪涌现检查。没有校准分数或运行ER。
- 评估模板只用于确认正式Evaluation门槛，本轮未套用为已晋级文档。
- grill-with-docs：能从GDD回答的先查，用户需决定的内容一次提出一个关键问题；所有补充方案先留inbox。

## 输出与执行事实

- 三份原始记录：SC-A-v01、SC-B-v01、SC-C-v01。
- 一份[综合构思分析](2026-09-20-spell-construction-analysis.md)、本来源记录、一份[当前问题](../questions/Q-20260920-spell-construction.md)，并更新本项目导航与run-control。
- 未读取其他方向正文；未启动外部产品研究、玩法模拟、可玩原型、真人试玩或全卡池复测。
- 未创建本地合格素材、正式Proposal／Evaluation／GDD／Draft Change，未修改目标game-002设计。
- 原工作区有大量无关未提交改动。本轮在独立工作树与独立分支完成，只提交本任务文件。
