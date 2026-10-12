# 言咒实现与资产索引

> 当前阶段：2026-10-12 第六批Windows包 **GODOT-EX002-0.4** 限定技术验收通过；固定运行源码9c50458a56a38f0c6ebd001d9e6a3ef34382adaa，设计输入abe8869。完整单战／恢复／播放／界面、固定字体与基础音画设置，新增失焦暂停、公开卡面和运行材质样板；唯一工程为[E:/Project/yanzhou-godot](E:/Project/yanzhou-godot/README.md)。设计CORE-060—062及EX-002，视觉Blender v02；旧0.1／0.2／0.3包保留，正式音画质量与真人体验未完成。

> 当前调度（2026-10-12）：**第六批完成，下一批DQ-12／44预算确认按DOC-024暂停，专门设计对接进行第06轮**；[唯一问题登记](../governance/questions.md#performance-round06)。R7失焦／最小化停、返回仍停及状态／草稿保留已完成限定工程验证，无需再问。346项核心、复制包旧案例7次／完整界面12次／失焦2次运行通过；两档各32项UI、31项表现、19项卡面、53项失焦检查，失焦每档25次自有窗口OS操作；[第六批报告](E:/Project/yanzhou-godot/docs/reviews/2026-10-12-batch-06-integration.md)、[包证据](E:/Project/yanzhou-godot/docs/coordination/development-batch-06-release-evidence.json)。每项证据仅证明其技术范围，不等于成品或真人验收。

## 当前开发入口

| 需要什么 | 唯一入口 |
| --- | --- |
| 阶段目标、引擎评估与下一任务 | [正式开发计划](production-plan.md) |
| 基础逻辑之后：画面、资产、动作、UI与完整单战 | [成品 Demo HTML 任务表](demo-quality-taskboard.html)（52项必做＋4项后续；含依赖、产物和验收） |
| 开发总控、并行分工与首版保全 | [2026-10-11 总控首轮](reports/demo-control-2026-10-11.md) · [实现仓库当前调度](E:/Project/yanzhou-godot/README.md) |
| 类似游戏使用的引擎与选型依据 | [2026-10-11引擎调研](reports/similar-game-engine-research-2026-10-11.md) |
| Godot首版、实际检查与边界 | [本轮交付](reports/godot-start-2026-10-11.md) · [代码／构建入口](E:/Project/yanzhou-godot/README.md) |
| Godot第二批工程集成与新证据 | [GODOT-EX001-0.2报告](E:/Project/yanzhou-godot/docs/reviews/2026-10-11-batch-02-integration.md) · [新Windows包](E:/Project/yanzhou-godot/build/development-batch-02/windows/Yanzhou.exe) · [四状态对照板](E:/Project/yanzhou-godot/evidence/development-batch-02/captures/index.html) |
| 当前完整单战包与技术证据 | [GODOT-EX002-0.4 Windows包](E:/Project/yanzhou-godot/build/development-batch-06/windows-02/Yanzhou.exe) · [第六批报告](E:/Project/yanzhou-godot/docs/reviews/2026-10-12-batch-06-integration.md) · [固定包证据](E:/Project/yanzhou-godot/docs/coordination/development-batch-06-release-evidence.json) |
| 工作方式、质量与交付要求 | [开发规范](development-standard.md) |
| 当前资产、接入差异及核验 | [开发输入与资产](asset-readiness.md) |
| 玩法与首批内容 | [主系统](../design/README.md) · [EX-001原回归](../design/examples/simple-spell.md) · [EX-002完整单战](../design/examples/complete-battle.md) |
| 设计待决与验证入口 | [集中问题](../governance/questions.md) · [测试交接](test-handoff.md) |

准备轮核验5包75文件与原哈希一致，随后完成11款类似游戏的引擎资料调研。用户先授权当前Windows电脑实测，最终直接选定Godot，替代双引擎比较流程。本轮[DM-G002-011](../../docs/registry/demo-assets.md#dm-g002-011)实装EX-001 0—14拍并进行规则／交互／恢复等技术检查；这些不是完整117项验收或真人体验／平衡实验。后续逐阶段回填实际版本与结果，以下保留各原日期交付说明。

文档角色：ImplementationIndex。更新：2026-10-11。旧主系统与探索试点保留原日期和交付结论；DIR-029／032／033等已退役，不再是当前实现任务。

## 2026-10-11 Blender 战斗桌面建模首版

当前迭代为[AS-G002-010 / BATTLE-3D-02](../visual/battle-ui-2026-10-11/model-v02.md)：按用户要求增加近大远小的透视，收窄卡牌与空位框；源工程、GLB、组件与检查图另存v02。v01及其原始检查保留；不新增玩法实现或测试结论。

[AS-G002-010 / BATTLE-3D-01](../visual/battle-ui-2026-10-11/model-v01.md)：依据 HTML v10、已选效果图与19张组件参考，新建可编辑 Blender 总场景、独立组件库、GLB及主图/灰模/斜侧图/六件近景。外部制作入口、固定文件清单和实际检查见交付页。已检查原生重开、纹理打包、GLB回导、布局与接触面；静态几何与材质首版完成，雕刻细节和实时材质/性能仍待后续制作。无战斗规则实现、完整UI交互或玩法测试；本次模型未自动视为已采纳美术。

## 2026-10-11 HTML战斗结构示意

[DM-G002-010 / BATTLE-UI-HTML-10](../visual/battle-ui-2026-10-11/v10-outline.md)：三格抽屉向桌内展开，两主体与时间轴中点对齐桌面中心线，刻位左右对称。保留前沿四法器本体、桌上物件及空位，未恢复已删面板。单文件离线可看，原件和证据在链接中的本机持久目录。Edge检查1920／1366／736宽度、抽屉方向、主体及时间轴居中、刻位对称、物件边界、空位、面板删除和HTTP／离线显示；1366预览已目视检查。仅轮廓展示完成，无交互或3D模型；玩法与体验NotRun。[v09及其原检查](../visual/battle-ui-2026-10-11/v09-outline.md)完整保留。

## Demo与素材登记（DA-1 / 2026-10-01）

2026-10-12第六批素材复用：0.4包固定运行源码9c50458，直接复用AS-G002-009原版牌背／火焰／护盾三图；AS-G002-010原GLB叠加运行材质／灯光代码小样，源件未改，不新分配模型ID。两者使用关系见[统一目录](../../docs/registry/demo-assets.md#as-g002-009)。包和副本各195文件、238,983,705字节，指纹一致，来源说明和字体原许可随包；运行卡面与生命布局问题已修，仍保留材质细节／完整动作和成品质量缺口。

2026-10-12第五批素材接入：[AS-G002-011@FONT-ASSETS-01](../../docs/registry/demo-assets.md#as-g002-011)固定Noto中文／符号已随0.3包运行，禁系统回退及两份OFL原字节随包检查通过；[AS-G002-012@SYNTH-AUDIO-01](../../docs/registry/demo-assets.md#as-g002-012)原创程序合成声音样板已接入非暂停新揭示，暂停清理与实际引擎混音检查通过，听感未审。胜败音有资源但依CORE-061无可听运行触发。两者由固定运行源码9cf9b64使用，包及复制目录各195文件、232,308,612字节，逐文件指纹一致；登记不提升成品状态。

2026-10-11新增[AS-G002-008 战斗效果图 v01](../visual/battle-ui-2026-10-11/art-v01.md)：基于HTML v10结构的独立生成概念图，已目视核对构图及检查图像文件；用户已选为效果示意图初版。同日交付[AS-G002-009 组件隔离设计 v01](../visual/battle-ui-2026-10-11/components-v01/README.md)，含18张透明组件及1张环境图；已检查图像与透明通道并核对本机总览显示。无运行实现或3D工程。HTML v10原件未改，玩法验证状态不变。

按[统一规范](../../docs/demo-asset-standard.md)管理；[全项目目录](../../docs/registry/demo-assets.md)负责发现入口，本页继续维护实现范围和原证据。本次仅登记，未运行或升级旧Demo。

- [DM-G002-001 暗面Demo](../../docs/registry/demo-assets.md#dm-g002-001)：视觉参照[AS-G002-001](../../docs/registry/demo-assets.md#as-g002-001)；完整代码版本和复用条件待补，旧RC1身份保留。
- [DM-G002-002 DIR-029翻牌演示](../../docs/registry/demo-assets.md#dm-g002-002)：以[AS-G002-002 v9](../../docs/registry/demo-assets.md#as-g002-002)为视觉参照，使用文字/装饰占位，并非导入该PNG；源码/预览指纹见目录。
- [AS-G002-003 Godot/Blender实验集合](../../docs/registry/demo-assets.md#as-g002-003)及[DM-G002-003 E1 R2小样](../../docs/registry/demo-assets.md#dm-g002-003)：2026-10-01用户通知恢复后，README、主要资产说明及工程入口均已确认存在。外部固定提交`1dd488c507a73933e5f16e9d3829e451b5e37937`；工作树另有未提交Blender修改，详见统一目录恢复记录。本轮未运行小样或重验美术。

| 项目 | 记录中的版本与用途 | 完成边界／入口 |
| --- | --- | --- |
| 暗面Demo | v0.1；codex/dark-demo；cf7b98d | [README](E:/Project/yanzhou-dark-demo/README.md)；05视觉下的独立可玩流程，完整RC1验收未完成 |
| Godot／Blender资产实验 | 独立美术及技术实验；AS-G002-003 / DM-G002-003，按各报告版本 | [已恢复的仓库入口](E:/Project/game-002-godogen-lab/README.md)；原生资产、视觉探索与E1 R2分别保留范围；旧RC1来源不代表TL-1实现，本轮仅核对登记 |
| 其他历史Demo与迭代 | 原版本分别保留 | 见历史开发记录，不按最近修改日期自动替代 |
| DIR-029时间轴翻牌 | v0.1；2026-09-30；局部动效原型 | [实现说明及验证入口](C:/Users/Administrator/.codex/visualizations/2026/09/24/01a0d1f2-4d90-7db2-8527-684c3085e2ee/timeline-flip-demo-notes.txt)；四刻翻牌、固定棋子、牌列左移，不含战斗结算 |

## 旧RC1 Demo缺口（原版本）

本节以下仍是旧RC1及原TL-1后续工作的历史索引；原DIR-032试点不覆盖这些旧结论。

已有34词／19可换件、三种杖、四杖起点、2×5战斗、19节点／12遭遇及保存流程。尚缺复杂条件／数量比较、精确实例与来源筛选编辑、拖动、独立敌人／完整环境形态美术、音频、实体桌面与长袋及完整路线表现。不是原生引擎EXE。

16项局部检查和固定seed42烟测已记录；烟测在C5L第76刻失败，第6战与首领未到达。720单场／20整局和真人U01–08未完成；[测试交接](test-handoff.md)维护运行身份。

## 后续工作

后续实现须以[TL-1 + INS-1当前规则](../design/README.md)重新界定范围；旧RC1 Demo不能据此视为具备新版产线与铭刻；后续局部TL-1试点仅按原覆盖记录解释，也未完成INS-1验证。先解决使预期不唯一的设计问题，再另行授权原型和测试。不得把旧Demo修补状态直接标为TL-1完成。

[全部历史版本、资产和交付证据](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/code-development-index.md)。

## 2026-10-04探索实现退役

DIR-001–036已按用户决定删除，相关试点、UI稿和展示册不再作为当前实现任务。DM-G002-002、004–008以及AS-G002-002、004标为Archived，原版本、检查范围和失败记录继续按[统一目录](../../docs/registry/demo-assets.md)与[固定开发记录](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/development/README.md)取证。

本轮删除本仓库方向内文件，没有删除外部实现仓库或持久演示目录，没有重新运行Demo或玩法测试，也不把旧试点规则自动采纳到INS-1。新实现须重新明确现行设计范围和输入；未提交内容的恢复入口见[清理报告](../governance/cleanup-report.md#2026-10-04探索方向退役)。
