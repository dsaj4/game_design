# 第01批 · 水、火、土、风、草

2026-10-30 · **AS-G002-039 / ALCHEMY-MATERIAL-CARDS-01**。本批5/32，成图PendingReview。[返回全量队列与制作入口](../README.md)。

![五张并列与手牌尺寸](E:/Project/yanzhou-art-assets/alchemy-material-cards-2026-10-30/batch-01/evidence/size-review.png)

**[取得本批完整资产包](E:/Project/yanzhou-art-assets/alchemy-material-cards-2026-10-30/batch-01.zip)** · [包内装载说明](E:/Project/yanzhou-art-assets/alchemy-material-cards-2026-10-30/batch-01/README.md) · [准确源件与校验](manifest.json)。包内有共用纸底1张、透明插画5张、原生合成成品5张、Godot组件与导入设置、完整提示词和检查记录。

| 卡面 | 构图与区别 | 本轮审阅点 |
| --- | --- | --- |
| [水](E:/Project/yanzhou-art-assets/alchemy-material-cards-2026-10-30/batch-01/cards/material-water/front-1024.png) | 蓝色S形流水、滴溅与水洼，灰石提供流向 | 灰石占比高于提示设想；与风同用流线，依赖水滴／波纹区分 |
| [火](E:/Project/yanzhou-art-assets/alchemy-material-cards-2026-10-30/batch-01/cards/material-fire/front-1024.png) | 叉放焦木、向上三角火焰与少量火星 | 色彩最饱和，是否需要再压低暖色由审阅判断 |
| [土](E:/Project/yanzhou-art-assets/alchemy-material-cards-2026-10-30/batch-01/cards/material-earth/front-1024.png) | 低厚土垄、松散颗粒与斜切沉积层 | 构图比其余更短宽；细层理缩小后不逐条可读 |
| [风](E:/Project/yanzhou-art-assets/alchemy-material-cards-2026-10-30/batch-01/cards/material-wind/front-1024.png) | 开放灰蓝气流托起羽毛与枯叶 | 气流带偏有实体感，需留意是否像丝带或水浪 |
| [草](E:/Project/yanzhou-art-assets/alchemy-material-cards-2026-10-30/batch-01/cards/material-herb/front-1024.png) | 绿色扇形茎叶、新芽、露水与少量细根 | 宽叶和细草叶共同建立植物生机，不指定真实植物物种 |

卡内均无名称、费用、数值、规则或类别图标；名称和序号只是审阅板的外部标签。图中物件、数量、露水和火星不产生卡效、产率、物种或新配方。

## 同样规格如何落地

五张独立内置image_gen生成，1024×1536 RGBA，原生成位置和SHA见manifest；本地[sources](sources/)与[prompts](prompts/)保留源文件／准确输入。共用纸框逐字节沿AS-G002-038固定版复用；原包不改。源画布不紧裁，原点(0,0)，pivot_uv=(0.5,0.5)；装配的插画rect_uv=(0.03,0.03,0.94,0.94)，等比缩放，纸底／圆角Shader及默认单图装载延续前版。主程序代码仅在外部美术交付工程，不进入设计规则正文。

## 实际检查与边界

已目视五张完整图及[深浅紫底透明板](E:/Project/yanzhou-art-assets/alchemy-material-cards-2026-10-30/batch-01/evidence/alpha-review.png)：无矩形纸底／明显纸色晕边。实际Godot4.7.2渲染280×420和155×229，材料主形可辨；细节降级与主观辨识仍供审阅，不当作玩家实验。

五张各自分层装配与原生成品字节相等；各100次纹理请求复用同一资源，普通Flat只请求5张成品，Layered共用一张纸底。11个PNG均沿同一无损、mipmap与straight alpha导入设置。干净目录不带.godot缓存重新导入并渲染，两张审阅图SHA一致；ZIP按锁定清单逐文件校验。记录在交付包evidence及[本批checks](checks.json)。

这是首批美术资产交付／审阅，不是主战斗工程接入、信息合同采纳、OS交互、全牌库性能或玩法测试。余下27种未生成，按用户每次5张的审阅节奏保留队列。复用范围为本项目本机制作与审阅；本批生成只引用本项目原创护盾源，运行包不含第三方图像／代码或字体文件。审阅板使用本机系统字体，不写入卡面。
