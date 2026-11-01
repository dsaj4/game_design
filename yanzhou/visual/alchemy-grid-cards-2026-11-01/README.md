# 五件配套卡图 · 统一尺寸

2026-11-01 · game-002 / main · **AS-G002-041 / CARD-ART-03**。

**[打开物品与卡图配套审阅板](E:/Project/yanzhou-ui-prototypes/alchemy-grid-cards-2026-11-01/index.html)**。

![五张同尺寸卡图与对应物品](E:/Project/yanzhou-ui-prototypes/alchemy-grid-cards-2026-11-01/evidence/cards-pairing-review.png)

五张卡图均为 **1174×1340像素、不透明RGB PNG**。画布、比例和显示框统一，与物品的一格／两格及横竖方向无关。画面中的长瓶、紧凑木炭、横向黏土、竖长羽毛与细长疗伤草分别对应[新版透明物品03](../alchemy-grid-items-2026-11-01/README.md)。图稿不含格线、卡框、名称或效果文字。

| 内容ID／名称 | 物品展示占格 | 同尺寸卡图原件 |
| --- | --- | --- |
| alchemy.water · 清泉水 | 1×2 | [water-card-v01.png](E:/Project/yanzhou-art-assets/alchemy-grid-cards-2026-11-01/sources/water-card-v01.png) |
| alchemy.fire · 燃烧木炭 | 1×1 | [fire-card-v02.png](E:/Project/yanzhou-art-assets/alchemy-grid-cards-2026-11-01/sources/fire-card-v02.png) |
| alchemy.earth · 黏土团 | 2×1 | [earth-card-v01.png](E:/Project/yanzhou-art-assets/alchemy-grid-cards-2026-11-01/sources/earth-card-v01.png) |
| alchemy.air · 风息羽毛 | 1×2 | [wind-card-v01.png](E:/Project/yanzhou-art-assets/alchemy-grid-cards-2026-11-01/sources/wind-card-v01.png) |
| alchemy.herb · 疗伤草 | 1×2 | [herb-card-v01.png](E:/Project/yanzhou-art-assets/alchemy-grid-cards-2026-11-01/sources/herb-card-v01.png) |

疗伤草卡图仍是生长场景，因此不带采收物品上的红绳；四片细长绿叶、红芽与细长茎保持同一身份。这是既有表面职责的延续。

## 生成与验收

CUSTOM视觉续作，输入固定 **5f4644d38a2d7a6d1b6e088547562f20940b18c8**。直接输入为AS-G002-041@CARD-FRAME-02对应旧卡图（编辑目标、场景／画法及尺寸参考）和AS-G002-040@ALCHEMY-ITEM-PILOT-03对应新物品（最新轮廓、比例与身份）。五张旧卡图和现有模板均实际目视并核对manifest／提示词；本轮未新增第三方输入。

使用内置image_gen共6次。木炭首张实际为1174×1339，比统一要求少一行，未选作交付；随后再次使用image_gen输出1174×1340版本。其他四张各一次。最终五张尺寸全部相同，原PNG按生成字节保存，没有程序拉伸、裁图、抠色或尺寸归一化。原输出、参考角色、SHA、实际尺寸和[完整提示词](prompts/)见[manifest](manifest.json)。

实际检查：

- 5／5最终文件尺寸严格为1174×1340，均为RGB；持久副本与生成原输出SHA一致。
- 目视五对卡图／物品：新版形状与身份一致，卡图边界完整；共同画布未跟随物品长宽变化。
- [统一图窗检查](E:/Project/yanzhou-ui-prototypes/alchemy-grid-cards-2026-11-01/evidence/card-window-review.png)：使用02原1003×1568模板及原图窗坐标(33,34,938,1077)，插画等比contain；另看155×229宿主和96×150缩图。五件主体完整，无挤压或主体裁切。源插画全画幅装入图窗，微小比例差由统一底色补齐。
- 审阅图由本机静态渲染并目视，不是浏览器／游戏截图。HTML仅完成路径与脚本语法检查；沿本会话file协议访问限制，未重试浏览器绕行。
- 旧卡图、新透明物品及模板原件SHA保持。卡图和物品均未更新内容库关联、未接入游戏，未运行玩家辨识测试。

**ReadyForScope / PresentLocal**仅限上述卡图制作与静态配套／图窗检查。模板、名称板与字体没有升级；审阅模板名称区留空，不将本轮宣称为完整整卡生产验收。原02源包和ZIP保留，03延续AS-G002-041的插画用途，不另分配ID。范围仅项目内部制作／审阅，未随包附第三方原图或字体。
