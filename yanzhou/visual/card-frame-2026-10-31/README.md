# 卡片边框 · Ways参考首版

当前制作采用[完整卡面基准02](complete-v02/README.md)：深褐薄边、上部卡图窗与下部独立名称板；同一模板五件试配，中文名称真实排字。02已由用户选入[统一美术基准](../../system-design/presentation/art-direction.md)，下文01金色窄框及原包仅保留历史生成与检查用途；文中的PendingReview按01当时状态解释，不作为后续制作入口。

2026-10-31 · game-002 / main · **AS-G002-041 / CARD-FRAME-01**。FrameCandidate / PendingReview。用户明确此前五幅画面作为**卡图**，本轮开始独立卡片边框设计；一张通用透明框配现有五张卡图，原卡图字节保持。本版是边框候选，不把框色或卷角定义为稀有度、费用、状态或玩法标记。

![卡框与五张卡图的小尺寸对照](E:/Project/yanzhou-art-assets/card-frame-2026-10-31/evidence/frame-review.png)

## 本版设计

深褐圆角外沿，暖赭金框带，米白内线；左上与右下各一处小卷角，侧边只有少量顺边短线。图案集中在窄框，中央为透明窗口；不另设效果栏、题签、费用徽章或文字。无色彩变体、背面、悬停／选中状态，本轮只做一种正面框体。

卡框是一张独立1024×1536 RGBA原图，中央及外角为透明。卡图另行装入内窗，不烘进框文件。实际透明窗口的中心横／纵截面为x80、y91、864×1357；现有2:3卡图等比contain放入，内窗比例差以少量暖底补齐，不裁切或拉伸卡图。整体仍按2:3等比缩放，不承诺任意比例拉伸或九宫格。

## Ways借鉴与来源

CUSTOM视觉续作，设计仓库输入固定 **1d88eda9cdcb6da731ef964942f23a660ba7fcfc**。沿[统一美术画法](../../system-design/presentation/art-direction.md)，不加载或改动玩法。用户指定[Ways本地图册](E:/Game/Ways%20of%20Alchemy-analysis/2026-10-31/index.html)；读取art_manifest并查看frame、card_bg、card_stack_frame、back、description_frame、card_background和card_process_completed_bg等导出图。

实际生成输入仅为card_stack_frame与back两图，分别借深褐圆角／细内线及平涂赭金／角部线条；不复制背面的锁、链、太阳图案或完整布局，也不把源游戏的下部文字分区带入本版。这里只核对静态资源，不声称确认源游戏完整装配或状态逻辑。输入路径、角色、SHA和原图字节沿[manifest](manifest.json)。

内置image_gen生成1次，准确请求见[提示词](prompts/frame-v01.txt)。原输出复制到本目录sources/和交付包，保留原RGBA及PNG字节；未裁切、抠色或程序绘改。图像生成预览里透明像素的RGB不作为底色，实际合成以alpha为准。

## 交付与检查

[透明框原件](E:/Project/yanzhou-art-assets/card-frame-2026-10-31/frames/frame-v01.png) · [完整审阅包](E:/Project/yanzhou-art-assets/card-frame-2026-10-31.zip)。包内为新框、独立框体控件、五张AS-G002-040@02卡图的原字节副本、提示词与Godot审阅工程；卡图副本只供自包含预览，不另发行素材身份。程序在仓库外，图片／ZIP本机保管；文档、提示词与清单入Git。

独立Godot4.7.2实际显示：空框、清泉水／木炭大图及五张155×229宿主；另核[深／浅／紫底的透明窗口](E:/Project/yanzhou-art-assets/card-frame-2026-10-31/evidence/frame-alpha-review.png)。框体中心与外角alpha为0，100次请求同一框纹理；六张运行PNG使用无损及mipmap，原卡图SHA未变。检查范围见[checks](checks.json)。

第一张审阅板因系统窗口限高截断底排，已调整审阅窗口和排布并重新渲染，当前板完整；没有更改框或卡图像素。当前套图与暖底比例待用户审阅，尚未接入主工程、做交互／状态或玩家辨识测试。原卡图包与统一画法不因候选框生成而重新定版。
