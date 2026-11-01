# 炼金法器 · Ways of Alchemy暖色手绘版

2026-10-31 · game-002 / main · **AS-G002-036 / ALCHEMY-APPARATUS-10**。

**[查看G版与七版切换](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/ways-v10/preview.html)**。前六版原件及原预览保持；本轮继续制作平炼釜／白化曲颈瓶的美术候选。

用户指定[本地Ways of Alchemy图集](<E:/Game/Ways of Alchemy-analysis/2026-10-31/index.html>)作为风格来源。G采用深褐粗描边、圆润手绘轮廓、暖铜与青绿配色、沿器物弧面分布的横向短线。短线集中在口沿、侧缘与底足，中央材质面保持大块留白；器形回到圆腹铜釜与青白曲颈瓶，不把上版炉体／圆形暗盘作为本轮轮廓约束。

| 原件 | 造型 | 实际规格 |
| --- | --- | --- |
| [平炼釜](refining-kettle-ways-v01.png) | 圆腹铜釜、赭黄厚口沿、蓝灰卷耳与低平底；局部青绿旧色，正面留白 | 1536×1024 RGBA透明PNG |
| [白化曲颈瓶](albedo-retort-ways-v01.png) | 乳白梨腹、短厚弯颈、青绿口沿与低足；侧缘短线，正面留白 | 1174×1339 RGBA透明PNG |

## 实际参考与生成

已查看指定目录的器具总览，并逐张查看Copper Pot、Polished Distillation Cube、Albedo原图。三图按此顺序实际输入两次内置image_gen，均仅作画法参考；第三方原件留在原提取目录，无复制、裁切或抠图。

- [Copper Pot](<E:/Game/Ways of Alchemy-analysis/2026-10-31/images/sprites/defaultlocalgroup/Copper pot__1571776474073694157.png>)：暖铜色、深褐线与椭圆口沿。
- [Polished Distillation Cube](<E:/Game/Ways of Alchemy-analysis/2026-10-31/images/sprites/defaultlocalgroup/Polished Distillation Cube__243529624046421214.png>)：金属的手绘色面与横向短线。
- [Albedo](<E:/Game/Ways of Alchemy-analysis/2026-10-31/images/sprites/defaultlocalgroup/Albedo__4997806272049595607.png>)：粗轮廓、乳白／青绿配色与圆润瓶形。

没有采用原图底纹、药液纹样、浮叶、搅拌杆或管线作为运行素材。准确提示词见[平炼釜](prompts/refining-kettle.txt)／[曲颈瓶](prompts/albedo-retort.txt)，输入角色与原生成路径沿[generation](generation.json)。新PNG从工具输出逐字节复制，无程序图像编辑、改色或缩放；预览只缩放定位完整图像。[manifest](manifest.json)固定新原件、实际参考图、外部图集／来源清单快照和预览证据，参考图SHA另与原提取art_manifest逐项核对。

## 检查与范围

前六版121个登记文件按原SHA验证未变。实际浏览器1280×720视口已核A—G切换、七版对照、G的浅纸／深色／暖灰木色透明合成、剪影及224／64／96／160px样本，无横向溢出。64px下短线收成纹理，主体轮廓与正面留白仍清楚。[检查记录](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/ways-v10/browser-qa.json)与[当前画面](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/ways-v10/evidence/05-current-g.png)保存于独立预览目录。

ReadyForScope / PresentLocal仅限本机美术、文件一致性和预览检查；G造型及风格接受PendingReview。CUSTOM输入固定于`1980877a30ff689db17200b06a6d00e0ebb2472f`的既有六版美术及用户本轮要求，增补指定Ways of Alchemy图集中的实际参考图；参考用途仅为美术，不采纳其配方或规则。未制作铭文、拆件、发光动画或绑定，未接入背包／引擎或进行玩法测试。原图与预览本机保管，说明／提示词／清单入Git；第三方作者／许可Unknown，仅供项目内部美术审阅，后续复用沿本固定版本与来源限制。
