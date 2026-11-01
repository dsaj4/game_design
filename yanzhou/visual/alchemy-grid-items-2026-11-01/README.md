# 五件物品占格重绘

2026-11-01 · game-002 / main · **AS-G002-040 / ALCHEMY-ITEM-PILOT-03**。

后续配套已完成：[五张统一1174×1340卡图03](../alchemy-grid-cards-2026-11-01/README.md)。卡图尺寸不随物品占格变化；下文保留本次物品批次的实际检查范围。

**[打开五件格子审阅板](E:/Project/yanzhou-ui-prototypes/alchemy-grid-items-2026-11-01/index.html)**：相同格子尺寸显示五件新图，可切换深浅／紫底、格线、剪影，并按住按钮对照旧图。

![五件按占格重绘的透明物品](E:/Project/yanzhou-ui-prototypes/alchemy-grid-items-2026-11-01/evidence/grid-review.png)

本轮按用户要求，先重做现有五种样例，使物品比例对应内容库已写的格子数。交接文档中“接着画生铁块等五种材料”只是后续建议，本轮未执行。沿用已选WAYS-ART-BASELINE-02画法，保留水线／炭裂隙／浅捏痕／灰蓝羽尖／四叶红芽与红结等辨识特征。网格只在审阅图中绘制，PNG内没有格线、文字、卡框或背景。

## 五个原件

| 内容ID／名称 | 展示占格 | 原PNG尺寸 | 原件 |
| --- | --- | --- | --- |
| alchemy.water · 清泉水 | 1×2，竖向两格 | 887×1774 | [water-v02.png](E:/Project/yanzhou-art-assets/alchemy-grid-items-2026-11-01/sources/water-v02.png) |
| alchemy.fire · 燃烧木炭 | 1×1，单格 | 1254×1254 | [fire-v01.png](E:/Project/yanzhou-art-assets/alchemy-grid-items-2026-11-01/sources/fire-v01.png) |
| alchemy.earth · 黏土团 | 2×1，横向两格 | 1774×887 | [earth-v01.png](E:/Project/yanzhou-art-assets/alchemy-grid-items-2026-11-01/sources/earth-v01.png) |
| alchemy.air · 风息羽毛 | 1×2，竖向两格 | 887×1774 | [wind-v01.png](E:/Project/yanzhou-art-assets/alchemy-grid-items-2026-11-01/sources/wind-v01.png) |
| alchemy.herb · 疗伤草 | 1×2，竖向两格 | 887×1774 | [herb-v01.png](E:/Project/yanzhou-art-assets/alchemy-grid-items-2026-11-01/sources/herb-v01.png) |

内容库四件两格物品的body均为`[[0,0],[0,1]]`。黏土采用已列允许旋转的90°展示；其余保持0°。画布比例与展示占形严格一致；宿主用完整源画布等比contain，中心锚点，不需要压扁、裁主体或程序抠色。每格像素大小由宿主确定，源图像素不定义游戏格子尺度。

这是按既有候选几何制作的视觉资产；内容库原身份／命名／几何资格不变，图稿完成不等于玩法采纳。

## 输入与生成

CUSTOM视觉生产。共同输入固定 **f349e954a211885d45cd9e6aae4f605205a97bac**，读取内容库中五项的正文、shape与art，以及美术基准、原物品包manifest／提示词、完整卡面职责和资产规范。工作期间并行交付后HEAD为`26ce1bb90198f3b94b5ddb5a4d5103bf8e5c191a`；实际复核五个目标条目与输入快照完全一致。

直接图像输入均为[AS-G002-040@02](../alchemy-item-pilot-2026-10-31/ways-v02/README.md)对应原创透明物品，逐张目视，角色为编辑目标＋身份／画法参考；本轮未打开或送入第三方图集。实际调用内置image_gen共6次，准确输入、原输出路径、RGBA／alpha范围、SHA与占格来源见[manifest](manifest.json)，完整[提示词集](prompts/)已保存。

清泉水第一次已成竖长瓶，但实际输出画布为1024×1536，因此只保留为未选中过程稿；第二次重构为严格1:2的887×1774。其余四件各一次。请求像素与实际像素的差异如实保留，未改写成要求尺寸。

最终五件和过程稿原PNG字节完整复制到`E:/Project/yanzhou-art-assets/alchemy-grid-items-2026-11-01/sources/`。审阅HTML、静态合成程序和证据在外部UI原型目录；审阅合成等比缩放，不修改美术源件。旧五件原图的SHA仍与源manifest一致。

## 实际检查与边界

- 五件全部通过原生成输出与持久原件SHA一致、真实RGBA透明、画布与格子比例相符、可见轮廓未碰画布边缘检查。
- 已目视[同格审阅图](E:/Project/yanzhou-ui-prototypes/alchemy-grid-items-2026-11-01/evidence/grid-review.png)：每格128px，另看最长边152px／64px。水瓶、木炭、黏土、羽毛、疗伤草均完整，关键身份可辨；这是静态目视判断，未做玩家辨识实验。
- 已目视[浅／深／紫底检查](E:/Project/yanzhou-ui-prototypes/alchemy-grid-items-2026-11-01/evidence/alpha-review.png)：每格112px及64px缩图；未见明显白边、背景块或外发光。原alpha保持，不将接近不透明的像素伪报为255。
- HTML源路径和嵌入脚本已做静态检查。浏览器工具拒绝本机file协议，未绕过限制、未执行浏览器UI验收；两张证据是本机静态渲染图，不是浏览器截图。
- 本轮只重画占格用的五件独立物品。旧场景卡图、通用模板和整卡未改；旧圆瓶卡图尚未与新长瓶重新配套。没有整卡组装，因此不宣称图窗、字体或155×229整卡宿主已验收。
- 内容库catalog及其派生展板保持原样；接入所需稳定ID、图片路径、用途、SHA和源AS均在本批manifest。未接入主游戏、未启动玩法测试。

ReadyForScope仅限上述透明图稿和静态审阅；PresentLocal。使用范围沿项目内部制作与审阅，未随包交付第三方原图或字体，公开分发权限未另行评估。该版本延续AS-G002-040的同五件物品身份，不重新分配资产ID，也不覆盖02风格基准和历史源包。
