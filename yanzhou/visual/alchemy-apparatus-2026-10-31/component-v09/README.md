# 炼金法器 · 单组件参考版

2026-10-31 · game-002 / main · **AS-G002-036 / ALCHEMY-APPARATUS-09**。

**[查看F版与六版切换](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/component-v09/preview.html)**。前五版原件及原预览保留，本轮继续提供两件法器的美术候选。

用户补充两张单组件截图，要求按其样式再做一版。F直接借鉴灰蓝外壳、黑色轮廓、折角硬边色面、厚框与旧铜边圈；器形分别采用炉体折烟囱、球腹斜颈。部件只保留主要构造，不加雕刻、文字或背景法阵。中央暗色圆面保持空白、无亮球，供后续独立铭文与生产亮光叠加。

| 新原件 | 造型 | 实际规格 |
| --- | --- | --- |
| [平炼釜·炉式候选](refining-kettle-component-v01.png) | 厚框炉体、低底座、折烟囱尖帽，旧铜边圈与暗色工作面；少量锈红炉口 | 1098×1433 RGBA透明PNG |
| [白化曲颈瓶·球腹候选](albedo-retort-component-v01.png) | 球腹斜长颈、小底足，灰蓝壳体、旧铜边圈及少量暗紫口沿 | 1246×1263 RGBA透明PNG |

## 输入与生成

两张用户附件已逐字节就地保管：[小炉组件](references/compact-furnace.png)240×467、[球腹斜颈组件](references/orb-retort.png)159×224。二者按此顺序实际输入两次内置image_gen，均为风格及器形语言参考；没有以旧A—E图像为编辑目标。本轮采用重新设计的独立器物，不重建两侧完整嵌合体。

游戏来源沿用户此前《幸存者的炼金术》的说明；原作者与分发许可Unknown，仅供本机内部美术参考。没有复制截图背景、法阵或UI作为运行素材。

准确提示词为[平炼釜](prompts/refining-kettle.txt)与[曲颈瓶](prompts/albedo-retort.txt)，输入角色与原输出路径沿[generation](generation.json)。生成PNG从工具原输出逐字节复制，无程序图像编辑、裁切、抠图、改色或缩放。预览只缩放定位完整图像，不含两张参考截图。[manifest](manifest.json)固定原件、参考、提示词与预览证据的SHA。

## 检查与边界

前五版100个登记文件（含08版参考图）按原SHA验证未变。实际浏览器677×871视口已核A—F切换、六版对照、F的浅纸／深色／暖灰木色透明合成、剪影及224／64／96／160px样本，无横向溢出。两件主体轮廓与中央暗面仍可区分；64px下尖顶和瓶颈细节较小。[检查记录](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/component-v09/browser-qa.json)及[当前画面](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/component-v09/evidence/05-current-f.png)保存在独立预览目录。

ReadyForScope / PresentLocal仅限本机美术、源图一致性与预览检查；F造型与风格接受PendingReview。CUSTOM输入为`ba0290088276fa0fd4de204de8c00f139197b436`的既有五版美术与用户本轮要求，增补这两张附件；不扩大玩法材料范围。炉式／球腹是形态候选，不定义占格、接口、配方或核心兼容；本轮未制作拆件、铭文图层、发光动画或绑定，未接入背包／引擎或进行玩法测试。PNG本机保管，说明／提示词／清单入Git；后续项目复用沿此固定版本与来源限制。
