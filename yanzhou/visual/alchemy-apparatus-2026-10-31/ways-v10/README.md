# 炼金法器 · Ways源件与制作

2026-10-31 · game-002 / main · **AS-G002-036 / ALCHEMY-APPARATUS-10**。用户已选定当前Ways画风；共用画法、提示词约束和验收以[Ways统一美术基准](../../../system-design/presentation/art-direction.md)为准，本页保存两件源图、实际生成来源与法器边界。

**[查看统一基准板02](E:/Project/yanzhou-ui-prototypes/ways-art-baseline-2026-10-31/production-v02/index.html)**。新增已选完整卡面与适配卡图，当前法器源PNG保持原字节，没有重绘或像素处理；制作规格集中在统一基准。

| 原件 | 当前造型 | 实际规格 |
| --- | --- | --- |
| [平炼釜](refining-kettle-ways-v01.png) | 圆腹铜釜、赭黄厚口沿、蓝灰卷耳与低底；局部青绿旧色、正面留白 | 1536×1024 RGBA透明PNG |
| [白化曲颈瓶](albedo-retort-ways-v01.png) | 乳白梨腹、短厚弯颈、青绿口沿与低足；侧缘短线、正面留白 | 1174×1339 RGBA透明PNG |

题材来自[B01炼金设计](../../../sources/materials/M-2026-10-27-alchemy-batch-01.md)的平炼／白化方向，两个暂名仍是器物外形身份；没有由图片确定具体法器兼容、配方、供料接口、占格、D或获取。中央安静表面供后续铭文与生产反馈，不附带固定辅槽，也不延续旧悬浮拼接合同。

## 生成来源与检查

原生成输入固定1980877a30ff689db17200b06a6d00e0ebb2472f。用户指定Ways本地图集，实际查看器具总览及Copper Pot、Polished Distillation Cube、Albedo；三图按此顺序实际输入两次内置image_gen，仅作画法参考。第三方原图留在原提取目录，没有把底纹、浮叶、搅拌杆或管线作为运行素材。

准确提示词为[平炼釜](prompts/refining-kettle.txt)／[曲颈瓶](prompts/albedo-retort.txt)，输入角色和原输出路径沿[generation](generation.json)。两张PNG仍与工具原输出字节一致；参考图、来源清单和源图SHA沿[manifest](manifest.json)。这些是生成历史，当前共用画法按统一基准继续，不改写旧调用文字。

此前基准板01实际核对12图的分组、深浅背景、小尺寸和透明物件剪影，原记录与截图由manifest引用；02本轮检查沿统一基准，旧记录未覆写。原两件224／64／96／160px与三底检查仍保留原日期及范围，不假称本轮重跑引擎。风格SelectedByUser；具体资产细节、主游戏接入及玩家辨识仍独立验收。

## 旧稿与恢复

本轮清理前固定Git为db79ead8d155c6a6a1bdf012304589f34db81fdd，旧A—F及旧多版播放器按原路径取证；未入Git的PNG、参考裁图、旧代码和截图在[本机恢复包](E:/Project/yanzhou-art-archive/2026-10-31-ways-art-baseline/retired-apparatus-assets.zip)中。150文件逐项验证后，移出139个旧文件、其中51个PNG；当前两图、卡面10图、运行副本及ZIP指纹未改。整体指纹与验证记录沿manifest的cleanup，不另建去向表。

更早DM-G002-022与旧双护符的102文件恢复包仍位于[旧双护符恢复目录](E:/Project/yanzhou-art-assets/retired-artifacts-2026-10-31/)，设计输入固定37f30968e32d54f4e635a804f55388d3442c0dcc，两包原指纹沿manifest的priorRetiredDemo。其分件、绑定和历史浏览器证据不成为当前规则或工程能力。

归属game-002 / main；StyleBaselineSelected。ReadyForScope / PresentLocal限本机文件与视觉检查；没有制作铭文层、发光动画、绑定或接入引擎，未做玩法测试。第三方作者／公开复用许可Unknown，仅本机内部美术参考。
