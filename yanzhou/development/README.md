# 言咒实现与资产索引

> 2026-10-04版本范围：当前为GDD 2.1 / TL-1 + INS-1，尚无对应完整实现或体验验证证据。以下既有实现与局部检查只对应原输入；本次审查不修改外部代码、不执行玩法测试。

文档角色：ImplementationIndex。更新：2026-10-04。旧主系统与探索试点保留原日期和交付结论；DIR-029／032／033等已退役，不再是当前实现任务。

## Demo与素材登记（DA-1 / 2026-10-01）

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
