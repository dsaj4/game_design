# 言咒本轮视觉基准

2026-10-31法器现有两版：[A·粗线简洁](alchemy-apparatus-2026-10-31/README.md)，AS-G002-036@ALCHEMY-APPARATUS-04，用户要求保留；[B·精线古朴及两版切换](alchemy-apparatus-2026-10-31/antique-v05/README.md)，同AS@05，以更细腻的轮廓、旧色与克制明暗营造神秘感，器形、留白与细节量延续。两件仍为B01平炼釜／白化曲颈瓶外形候选，B待审阅；A原图／播放器与23个登记文件保持原SHA。小尺寸、三背景及切换已核，具体占形／接口与工程未定未验；此前旧双护符清理沿04记录。

2026-10-28 · game-002。用户暂定桌面风格以 **v03** 为基准，卡牌设计重点参考独立符号板；已沿新设计制作 **v06底部扇形持牌示意**。后续视觉工作从本页进入。

2026-10-28的[四版卡面历史候选](card-artifact-design-2026-10-28/README.md)，AS-G002-035，保留A—D四张卡板和原提示词。其旧法器、比例图与双护符设计已清理；不覆盖后续卡面选择。

2026-10-29卡面转入[展示优先的七游戏横向研究](../../media-analysis-lab/runs/2026-10-29-card-face-display/README.md)：用户偏向效果说明外置、正面简洁且有独特主体图。已记录[项目意图与未决项](../sources/inbox/2026-10-29-display-first-card-face.md)，暂不沿前轮固定效果区续画；本轮仅研究，未改现行合同或工程，也不影响上方法器制作。

同日按后续要求已制作[两条路线、六种卡面风格探索](card-face-exploration-2026-10-29/README.md)，AS-G002-037：象形咒印三版与物象寓言三版，共六板18个主题演绎。卡内无效果说明，定位字在板外；本轮重在灵感差异，用户选型PendingReview，尚未锁定正式信息宿主或接入工程。

2026-10-31物品／卡面当前为[五件具体物品与场景卡面试点](alchemy-item-pilot-2026-10-31/README.md)，AS-G002-040@ALCHEMY-ITEM-PILOT-01：清泉水、燃烧木炭、黏土团、风息羽毛、疗伤草，各有独立透明物品图和不透明竖版场景插画。参考本机Backpack Battles的粗轮廓与材质分区，继承护盾画法但重做物件题材／构图；无人物、卡内效果文字或数值。小尺寸及alpha合成检查已完成，接受PendingReview，未确定占格或接入主游戏。原[元素／法师三版](alchemy-material-cards-2026-10-30/README.md)保留历史，不再作为本轮续画模板。

当前功能入口为[Godot完整首场与卡牌交互动效](../development/card-motion-2026-10-29.md)：EX-004完整单战及悬停、拿起、选用、落槽、取消归位、生产入手和当前列使用动画已接入；卡面、法器和法术声画保持占位。恶魔牌／本地尖塔2只作动作结构参考，没有第三方运行素材进入包；上方炼金法器新稿仍未接入。原[首轮HTML示意](first-battle-handflow-2026-10-28/README.md)继续保留独立身份与局部浏览器证据。

美术沿[十件逐件imagegen源件v02](tabletop-components-2026-10-28/imagegen-v02/README.md)；先完成[静态引擎v01](engine-scene-2026-10-28/README.md)，现继续用于同工程完整首场。原图、独立文字层与最下方扇形持牌保留；旧混合制作包及同期美术候选均不混入运行版本。

| 用途 | 当前选定输入 | 适用范围 |
| --- | --- | --- |
| 桌面风格基准与本轮更新 | [v06示意与v03风格来源](../exploration/DIR-042-herbal-engraving-style/README.md)，AS-G002-032@HERBAL-ENGRAVING-06 | v03纸本秘术、暖木／米白／灰绿与双法器身份；v06沿现行规则将手牌放最下方，补铭刻／边注，具体造型与排布待审阅 |
| 卡牌设计重点参考 | [卡牌符号设计板](../exploration/DIR-042-herbal-engraving-style/card-symbols-2026-10-28/README.md)，AS-G002-033@CARD-SYMBOLS-V05-01 | 实色图案区、大轮廓主体、六类符号及主题色关系；保留v05来源身份 |

![v06底部扇形持牌示意](../exploration/DIR-042-herbal-engraving-style/scene-v06.png)

v06显示EX-004第一轮生产结束、尚未布牌的静态状态：底部五张护盾与一张普攻，两组计数6／0，上方己方五列为空。已撤去旧库存卡堆、容量和整理点，分开法器本批／下批信息，并补充铜环铭刻、核心词片、书页法阵和朱砂边注。图像由内置image_gen三步编辑完成，[准确提示词及检查边界](../exploration/DIR-042-herbal-engraving-style/README.md#2026-10-28-底部持牌与语言细节更新)保留；本机PNG未上传。

## 怎样继续

桌面沿v03风格及本轮v06继续审阅，卡牌主体符号优先用独立设计板。v06已示意实色主体图、纸本卡框与独立效果区的组合；原符号板未改像素。纹样集中在器物、书页与边缘，保持读数与牌面区域安静；生成文字仍须人工排字，正式切片及小尺寸未验收。

位置、组件职责和交互继续查[现行文字合同](baseline-2026-10-26/README.md)。v03源于旧规则：图中的三资源堆、单一手牌堆、手牌容量和整理点只属于原画面，不恢复为当前规则；两组持牌、手动布牌、立即回收与列间窗口仍沿CORE-067。当前合同中的未决展示项继续保留。

## 本轮收束与恢复

其他整场稿v01／v02／v04／v05、暗酒红对象与皮肤、早期写实桌面／组件板、旧风格图和旧HTML退出活动工作区，不再列为平行候选。可继续使用的经验已合入场景说明和文字合同；Book of Hours的[分析报告](../../media-analysis-lab/runs/2026-10-28-book-of-hours-rea/README.md)与研究清单保留为研究依据。

清理前固定提交为 `ddf6ebfe7b3121cbb71d1257c229206a86321a1e`。[旧视觉文件](https://github.com/dsaj4/game_design/tree/ddf6ebfe7b3121cbb71d1257c229206a86321a1e/yanzhou/visual/baseline-2026-10-26)及[旧方向记录／提示词](https://github.com/dsaj4/game_design/tree/ddf6ebfe7b3121cbb71d1257c229206a86321a1e/yanzhou/exploration/DIR-042-herbal-engraving-style)按固定Git取证。四张未入Git的退出整场PNG已逐字节复制至 `E:/Project/yanzhou-art-archive/2026-10-28-v03-selection/`，与原manifest逐图核对SHA-256后才移出工作区；该处保留原manifest，不发布图像。当前选定PNG继续本机保管。

v06、首轮HTML、静态引擎及当前完整首场分别保留范围与版本。EX-004关键状态已有实际实现与限定检查，真实材料／回收等完整持牌合同、正式卡面小尺寸辨识、用户接受与真人体验仍待后续；PRE2D-Q01保持Open。未改GDD或开展平衡实验，资源身份及历史关系沿[统一AS／DM目录](../../docs/registry/demo-assets.md)。
