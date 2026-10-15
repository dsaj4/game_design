# 第十三批：追加资源适配预览

2026-10-15 · game-002 · ImplementationIndex · DM-G002-011 / GODOT-DEMONCARDS-CANDIDATES-B13-01。用户明确要求「尝试全部适配接入」，见[原话与授权](../../sources/inbox/2026-10-15-demoncards-asset-integration.md)。范围为前序定向清单45对象，另复用19曲线与13时间轴；不扩成全部7,811原包。

已交付本机独立预览：[Windows入口](E:/Project/yanzhou-godot/build/development-batch-13/candidates-01/windows/Yanzhou.exe) · [操作说明](E:/Project/yanzhou-godot/docs/demoncards-candidates-preview-guide.md) · [188张实图及24份混音](E:/Project/yanzhou-godot/evidence/development-batch-13/captures/index.html)。桌面设置 → 系统页上方 → 资源检视；同目录 `Inspect-resources.cmd` 可独立打开。返回牌桌保持暂停。

## 实际使用关系

| 来源 | 本批使用 | 范围和偏差 |
| --- | --- | --- |
| AS-G002-027 / DEMONCARDS-CANDIDATES-01 | 13模型、17纹理及必要材质依赖可检视；主桌接书、书座、地板、柜体、烛体、硬币底几何6个模型ID | 托盘比例、晶体尖底与现宿主不适配，保留现成组件；晶体座、瓶、盖、卡包、小匣只检视，不新增玩法 |
| AS-G002-027 / DEMONCARDS-MOTION-01 | 19曲线＋13时间轴可播放／拖动；书表面、Candle组合、NS局部效果有Godot样例 | 原UE材质图、Blueprint和Niagara模块未完整移植；曲线不擅自改战斗时序。FuncCardBack原暗背用途仍Unknown |
| AS-G002-028 / demoncards-audio-v01 | 12音效可试听；9个接主桌既有翻牌、离场、筹码、详情和控制 | 3个瓶／饮用音只试听；主观音色未验收 |
| AS-G002-025/026及AS-G002-018—023 | 沿固定版本保留原桌／布／牌、作者字体和现有组件 | 新派生独立保存，旧B12源件、包和失败记录保留 |

源／派生／当前使用逐项见[45对象结果](E:/Project/yanzhou-godot/docs/coordination/demoncards-candidates-integration-v01.json)。技术变换、材质补缺、音频解码和具体调用留[实现报告](E:/Project/yanzhou-godot/docs/reviews/2026-10-15-demoncards-candidates-integration.md)，本索引不扩写实现规则。

## 固定版本与检查

运行代码 `e975de8bdbbe70591d4099c34b799e76c4bff1d7`，设计起点 `151a9a8bb8b100994607e37a66c5314886f66a22`；本批D交接／复核按文件SHA固定。两仓分支 `codex/2026-10-11-demo-control`；运行工程无remote，设计记录统一提交推送。源、构建、复制目录、实图和报告指纹统一见[交付证据](E:/Project/yanzhou-godot/docs/coordination/development-batch-13-evidence.json)。

- 源码及复制后的独立包均在1920×1080、1366×768检查：主桌每档80/80、检视每档87/87；包202文件／375,978,496字节逐项哈希一致。
- 每档检视59张PNG、12份真实引擎混音；音频全样本、静音和切换停止技术检查通过。检视和包内无引擎ERROR/WARNING；源码主桌每档保留1条模拟测试的重复鼠标进入警告。
- 原设计对接[D交接](../../visual/demoncards-candidates-2026-10-15/handoff-v01.md)及[独立复核v02](../../visual/demoncards-candidates-2026-10-15/design-review-v02.md)：指定16张静态图ValidatedForScope，无本范围新增阻塞；[v01问题记录](../../visual/demoncards-candidates-2026-10-15/design-review-v01.md)保留。主桌背景过亮、检视材质彩噪和768柜体净空问题的修正过程在工程报告中保留。

本机资源适配交付完成；未声称OS实体输入、长时性能、主观听感、最终用户美术接受或完整原系统还原通过。原第三方资源再分发条件Unknown，本轮未公开上传。玩法、资格及正式采纳状态不变；后续制作继续优先现成资源，真实缺口才新建／生成。
