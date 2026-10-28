# 全imagegen版接入说明

AS-G002-034 / TABLETOP-COMPONENTS-02 · 2026-10-28。

本包exports/中只有10张完整源PNG，每件各由一次内置image_gen调用产生；导出与生成原件字节一致。没有旧版直裁片、拼接底板或30个九片／三片导出。完整原画布及alpha留白保留，没有裁边、抠色、归一化alpha、锐化或放大。

- wood-background为不透明底层；felt-mat和workbench-base为独立透明层。
- confirm、tab-active、tab-idle、header为无字底板。名称、组数量和其他读数使用字体另排。
- chip-heart、chip-armor、chip-spell是三类有限短叠外形；准确总数另排，物理层数不表示上限。

manifest记录原生画布和contentBoundsAlpha16（[x,y,width,height]，源左上为0，右下界不包含）。内容框只是定位元数据，未应用于源PNG。预览可按该框展示物件；正式工程如需裁边、压缩、mipmap或切片，另存工程派生，不覆盖这些生成原件。

新版单件轮廓和比例会与v01有差别，不能沿用v01的固定边距、命中区或认为选中／未选中已严格同形。先按目标显示尺寸核对，再决定界面伸缩办法。生成图的柔影和部分半透明像素原样保留；不要把预览黑底或棋盘格当作背景再抠色。

preview-components与preview-alpha只是实际PNG的并排／底色检查，不是新的资产源或真实游戏截图。正式导入、触区、分辨率预算与用户美术接受尚未验收；法器、卡牌继续后置。此包不带玩法、字体、第三方素材或公开发布授权。
