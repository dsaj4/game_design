# 炼金法器 · 黑线漫画版

2026-10-31 · game-002 / main · **AS-G002-036 / ALCHEMY-APPARATUS-08**。

**[查看E版与五版切换](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/survivor-v08/preview.html)**。沿平炼釜／白化曲颈瓶两件继续制作风格候选，前四版原件与原预览保留。

本轮按用户提供的《幸存者的炼金术》高清截图，参考左右嵌合装置中**单个小装置**的画法：黑色粗轮廓、较细结构线、硬边明暗、灰蓝金属与锈红／橄榄色，以及略带折角的夸张器形。每张仍是一件简洁独立法器；不照搬大型嵌合体、角色、场景或UI。延续非拟真、少装饰和正面铭文留白。

| 新原件 | 造型 | 实际规格 |
| --- | --- | --- |
| [平炼釜](refining-kettle-survivor-v01.png) | 锈红宽腹、灰蓝厚口沿与短底座，折角双耳；前腹保持大块空白 | 1536×1024 RGBA透明PNG |
| [白化曲颈瓶](albedo-retort-survivor-v01.png) | 米白梨腹、夸张折颈与斜向开口，灰蓝嘴沿和小底足，橄榄灰硬边暗部 | 1312×1199 RGBA透明PNG |

## 来源与生成

[高清参考图](references/survivor-alchemist-hd.png)为用户提供，2561×1441，原临时附件已逐字节保存到本包。游戏名称沿用户说明；原作者与分发许可Unknown，仅供本机内部风格审阅。该图作为**唯一图像输入**实际进入两次内置image_gen，角色仅为画法参考，重点看两侧小装置；没有把旧A—D图片作为编辑目标，也没有输入此前的低清裁图。

两份准确提示词为[平炼釜](prompts/refining-kettle.txt)与[曲颈瓶](prompts/albedo-retort.txt)，调用关系和原生成路径见[generation](generation.json)。两张完整新图从工具输出逐字节复制，无程序图像编辑、裁切、抠图、改色或缩放。预览只缩放定位完整源图，不包含参考截图。[manifest](manifest.json)固定新原件、参考图、原生成文件、提示词与预览证据的SHA。

## 检查与范围

前四版80个登记文件按原SHA验证未变。实际浏览器677×871视口已核A／B／C／D／E／五版对照，无横向溢出；E另核浅纸／深色／暖灰木色透明合成、剪影与224／64／96／160px样本。64px下釜耳边缘较小，主体轮廓仍可辨；未观察到新增铭文、雕饰或附属设备。[检查记录](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/survivor-v08/browser-qa.json)及[当前画面](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/survivor-v08/evidence/05-current-e.png)保存于独立预览目录。

ReadyForScope / PresentLocal限本机美术与文件检查，E造型及风格接受PendingReview。CUSTOM输入固定于`0565c52ef8dfa09f2ac282eda8c20279c1c72002`的现有四版与用户本轮要求，增补本轮高清附件；不改占格、供料、核心兼容或配方规则。当前为完整静态主体，未接入动画、绑定、背包或引擎，未做玩法测试。PNG本机保管，说明／提示词／清单入Git；后续项目复用沿此固定版本与来源限制。
