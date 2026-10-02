# 言咒实现与资产索引

> 2026-10-01版本范围：当前设计已切换TL-1；以下既有实现和局部检查仍对应原输入。本轮只迁移设计文档，不修改外部代码、不执行玩法测试。

文档角色：ImplementationIndex。更新：2026-10-02。旧主系统与DIR-029条目保留原日期和交付结论；本次新增DIR-032独立TL-1试点，范围及证据见新增节。

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

## DIR-029翻牌演示：本轮实现与证据

- 设计来源：[方向第13–19轮](../exploration/DIR-029-timeline-card-battle/README.md)、已确认的固定棋子与左移、v9单行牌桌候选，以及2026-09-30用户“尝试制作一个简单demo，展示翻牌的效果”的直接授权。未将候选布局或临时动画时长升级为Accepted。
- 交付范围：敌方翻面、己方同刻共同掀起、共同时间牌列左移、固定棋子局部点压、法杖来源高亮；播放／暂停／继续／重播仅为演示控制。代码和技术说明位于本任务持久可视化目录，设计仓库仅记录索引。
- 局部检查已通过：[浏览器结果](C:/Users/Administrator/.codex/visualizations/2026/09/24/01a0d1f2-4d90-7db2-8527-684c3085e2ee/verification.json)。涵盖同刻同步、暂停续播、重复重播取消旧动画、牌组居中、棋子基座固定、敌牌揭示后保留、来源高亮、375/320窄窗口及减少动态效果偏好；未观察到浏览器异常。已目视检查桌面和窄窗口截图。
- 边界：静态四刻样例，不计算伤害／胜负，不实现构句、独占格、多敌人或真实冷却。牌面采用文字与装饰替代最终插画。无真人体验、平衡或主系统RC1通过结论。下一步由用户体验翻牌与停顿节奏，再决定是否调整。

## 旧RC1 Demo缺口（原版本）

本节以下仍是旧RC1及原TL-1后续工作的历史索引；DIR-032的新试点不覆盖这些旧结论。

已有34词／19可换件、三种杖、四杖起点、2×5战斗、19节点／12遭遇及保存流程。尚缺复杂条件／数量比较、精确实例与来源筛选编辑、拖动、独立敌人／完整环境形态美术、音频、实体桌面与长袋及完整路线表现。不是原生引擎EXE。

16项局部检查和固定seed42烟测已记录；烟测在C5L第76刻失败，第6战与首领未到达。720单场／20整局和真人U01–08未完成；[测试交接](test-handoff.md)维护运行身份。

## 后续工作

后续实现须以[TL-1当前规则](../design/README.md)重新界定范围；现有Demo不具备材料产线、动态队列、倒计时干预与新保存合同。先解决使预期不唯一的设计问题，再另行授权原型和测试。不得把旧Demo修补状态直接标为TL-1完成。

[全部历史版本、资产和交付证据](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization/docs/code-development-index.md)。

## DIR-032 两战机制试点：DM-G002-004

2026-10-02。归属game-002-optimization / DIR-032，保持探索身份；[方向与来源](../exploration/DIR-032-playable-mechanism-loop/README.md)、[完整试点机制](../exploration/DIR-032-playable-mechanism-loop/P-2026-10-02-playable-loop-demo.md)、[资源登记](../../docs/registry/demo-assets.md#dm-g002-004)。

- 已实现：八条声明配方、真实词卡占用、六杖编排、材料托管与三阶段生产、有限队列、敌牌揭示／截止、免费未来路由、维护／休眠／增幅、疲劳、两战终局、整包词卡奖励、独立资源携带、暂停和本地恢复。
- 入口：[Demo](E:/Project/yanzhou-tl1-demo/demo.html)、[运行／操作说明](E:/Project/yanzhou-tl1-demo/README.md)。独立实现，不以旧RC1代码为起点。
- 固定版本：外部Git `afc6e4e0454bb3e306a49899022c340faabb5941`，DIR032-0.1；[文件指纹](E:/Project/yanzhou-tl1-demo/manifest.json)。本机可访问，代码已本地提交，未创建远端仓库。
- 局部证据：22项规则检查通过，6组同初始库存固定输入都完成两战；实际浏览器核对完整流程、临时路由承诺隔离、刷新保持已知敌情与暂停、真实奖励词卡、自动暂停与战终清理。完整结果和保留失败见[验证记录](E:/Project/yanzhou-tl1-demo/evidence/verification.md)。
- 偏差／覆盖：只提供八条声明配方的编辑，不是任意自然语言解释；无付费干涉能力、商店／完整路线、复杂修饰／复合行动、完整发行池。主系统GDD仍保持原采纳状态。可复制JSON导出已核对，内置浏览器下载事件未核验。
- 证据身份：ReadyForScope；固定输入可达性与程序检查不证明真人理解、趣味或平衡。当前增幅示例较直接辉核慢，下一步先观察选择价值与因果可读性，再扩卡。

## DIR-032 效果语言与UI样稿：DM-G002-005

2026-10-02。归属game-002-optimization / DIR-032；[表达层候选](../exploration/DIR-032-playable-mechanism-loop/UI-2026-10-02-effect-language.md)、[统一登记](../../docs/registry/demo-assets.md#dm-g002-005)。

- 交付：[独立交互展示稿](E:/Project/yanzhou-tl1-demo/ui-language/index.html)，外部Git 22950acae3bbe805432a7bd4449364c9c33bc016，EL-01；[运行和检查说明](E:/Project/yanzhou-tl1-demo/ui-language/README.md)。
- 范围：八条配方、战前展开／战中折叠、四关键词定义、法杖投入与时间、词卡／资源数量、辉核休眠／托管／增幅、封止截止、行满和临时路由的可见表达。
- 局部检查：实际浏览器点击和卡面文字核对、两张截图、语法解析通过，捕获错误日志为空。记录中保留定位失败及AX检查误差的处理；未做真人理解、跨浏览器或窄屏验证。
- 边界：示例状态不代表真实战斗结果；不接入DM-G002-004存档和引擎。原manifest的8个文件哈希不变，本轮未重跑玩法测试。Q17已确认，新增用词／布局仍Raw候选，主系统未回写。
