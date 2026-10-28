# DIR-042 纸本秘术工坊

2026-10-26建立，2026-10-28更新 · game-002-optimization。状态：Raw Idea / Unqualified；当前主稿v04，待用户审阅。

**[查看主稿 v04：字印工坊](scene-v04.png)** · [本轮完整提示词](scene-v04-prompt.txt) · [文件与SHA-256](manifest.json)

2026-10-28新增：[Book of Hours 深度分析清单](book-of-hours-analysis-checklist-2026-10-28.md)。按符号、实体／卡牌、信息分层、器物美术及生产／持牌操作确定取材重点；研究由用户后续执行，借鉴建议待取证与选择。

![言咒：纸本秘术与铭文工坊，纯文字生成v04](scene-v04.png)

## 本轮意图与阅读范围

用户要求重新编写提示词、从零生成，不基于原图编辑；参考Potion Craft的纸本秘术气质，融入言咒的咒文、语言与铭文，并依据新设计更新布局。具体外观及两组持牌的排布仍是候选，不等于用户已采纳完整展示合同。

- 模式：CUSTOM续作增补。共同版本为 `f8849ed93c159ecee6baceddb5cfa52cde4084cf`，对应GDD 3.0 / CORE-067。以下五份文件完整已读：`yanzhou/design/GDD.md`、`yanzhou/CONTEXT.md`、`yanzhou/design/baseline.md`、`yanzhou/design/examples/round-first-battle.md`、`yanzhou/visual/baseline-2026-10-26/README.md`。
- 增补依据：本轮明确要求加入言咒背景并按新设计更新布局；只取核心、术语、首场与视觉文字合同，没有读取系统细则、其他方向正文、历史设计或外部实现仓库。
- 操作规则沿根／项目／探索AGENTS、READ-1、轻量记录、Git协作与DA-1。未运行HTML、引擎或玩法测试。
- 美术外部参照沿2026-10-26已核实的[官方商店介绍](https://store.steampowered.com/app/1210320/Potion_Craft_Alchemist_Simulator/)：中世纪手稿与医学书籍。此次不新增产品拆解，没有导入Potion Craft图像文件。
- 旧图及旧提示词是本方向已知历史，但本轮没有将v01—v03、基准预览或任何其他图片传给生成工具。工具调用仅含新提示词及非透明背景参数，未传 `referenced_image_paths` 或 `num_last_images_to_include`。

## 本版：字印工坊

本轮用“可装配的实体语言”连接画面与玩法。词块来自当前已装配铭文；印章、字轨、压模、咒文滚轮及书页字形是外观建议，不另增配方、法器能力、世界观设定或铭文实体。

| 对象 | 本版设计与依据 |
| --- | --- |
| 整体画法 | 延续纸本秘术的棕墨细线、版画排线、薄涂设色与哑光纸／陶／铜／木；用印刷与铭刻感连接中文字形，不使用草木主题 |
| 守护护符 | 矮宽陶木护印压模；本体嵌入“庇护”核心与“迅速”辅槽词块。词与槽的归属沿EX-004§3，不把装饰字当成额外库存 |
| 施法护符 | 铜制咒文滚轮与木架，嵌入“打击”；用排列字轨和断句表现器具。当前强化批次与未来集中兑现分开标注 |
| 卡面与暗牌 | 护盾主体、攻击主体与效果栏分开；背面使用方印式字形。敌暗牌只显示攻击／打断类别和即时／延时，不泄露未公开名称或量值 |
| 背景陈设 | 左侧摊开暗句手稿及书写工具，周边少量书册；作为平面语言／铭刻气氛，不成为新的资源堆、供料或可点击系统 |
| 颜色 | 米白纸、灰绿织物、温木与铜色，辅以灰蓝防护及朱红印记；本版未校准为正式UI色彩规范 |

### 新布局及对现行设计的映射

- 上半区保留敌上我下、两行各五列。主稿己方前四位已布护盾，第五位留空，表现手动选择上牌；不把产出自动塞入战斗行。
- 宽工作台置于左下至中部，保留双法器及III／IV两个空预留。铭文直接附在所属法器上。
- 右下改为展开的持牌区，当前四张均可逐张辨识；两个索引签分别为“可战斗4”和“不可战斗0”，切组只换查看内容，不另建库存。
- 原左侧三资源堆与右下默认手牌堆退出本稿；没有手牌容量分母、H3或整理点。卡上“用后移除”符合首场全部产物均不可回收，不借本例假造回收／合成内容。
- 右上只承载敌我生命、玩家护甲与施法次数；上缘显示回合、阶段、生产拍，底缘保留本窗口的单步／确认结算。
- 依据：GDD§3、TL-08、§7；EX-004§2—6；当前视觉基准的范围表及手牌／布牌条目。两组持牌的最终排布在现行设计中仍待闭合，本图是首次候选表达，不是新权威基准。

### 画面情境

采用EX-004第二轮最终整理的一处可达中间状态：第一轮已改未来用途为兑现；t10生产结束，敌138／144，玩家60／60、8甲、5／10施法次数。己方行先布G6、G8、G5、G7，末位暂空；手中仍为B9、A6、G9、G10，即强化打击、简易攻击、两张简易护盾。两组数量为4／0，没有虚构材料卡。

敌行是公开爆裂试剂14＋三张攻击即时暗牌＋一张打断延时暗牌；完整敌表不泄露到背面。守护当前10→11批次为0／1，施法9→12批次为1／3；这些是按EX-004静态推导的画面输入，不是运行证据。

## 实际检查与未决项

2026-10-27已目视v04并核验规格与原件哈希。成图可见两行五位、四张已布牌与一个空位、四张持牌、4／0组标签、双法器与两处空预留；旧资源堆、手牌堆、容量及整理点未出现。主要生命／护甲／施法次数和批次数字与提示词相符。

- 实际规格：1672×941 PNG、RGB无透明。请求1920×1080，实际返回尺寸以文件为准；复制原件未缩放、拼贴或后期改字。
- 对手手部没有清楚画出，未完整继承原文字基准的对侧手部存在；法器高度差也比旧方向弱。不能把本稿当作所有结构项都已通过。
- 篆印、背景文字及个别铭文字形仍有生成变形；字轨是视觉纹样，不登记新词义。正式组件需要人工排字，敌方打断符号也须统一准确字形。
- 本次只检查静态成图；持牌切换、选择／拖放、详情、列间窗口、各倍率可读性与命中区均未验证。超多持牌浏览、卡牌查找和回收动效不由这张四牌情境解决。
- 风格接受与具体布局仍待审阅；未修改主GDD、当前视觉基准或实现，未执行玩法／真人实验。

## 历史版本与保留经验

v01—v03以 `13b9b3a0510e875bc4986ce52d9ded27e9fe9044` 的旧视觉输入为背景，具体阅读及外部交接来源沿[固定旧方向记录](https://github.com/dsaj4/game_design/blob/b4f716544fcf71c6a33ddc2b30dfc843babe1914/yanzhou/exploration/DIR-042-herbal-engraving-style/README.md)取证。该记录中的三资源堆、单一手牌堆与旧整理点不作为CORE-067依据。

- [v01](scene-v01.png)：统一手稿画法，但木纹、纸斑及草本陈设偏密，注意力分散。
- [v02](scene-v02.png)：减少大面纹理与散落植物，保留清楚轮廓；低噪声表面经验仍适用。
- [v03](scene-v03.png)：按用户要求将草木换为法阵、书籍和炼金器具，但仍是旧图的局部修订。手部与法器接近牌位、缺少生产／未来用途等原偏差保留在旧记录，不写成新版通过。
- v04：新提示词纯文字生成；切换到当前CORE-067与实体语言主题。旧图及原提示词不覆盖、不删除，保留比较和取证。

## 2026-10-27 外部美术参照初筛

用户希望寻找与Potion Craft相邻的2D中世纪、炼金、法术和神秘题材作品。本次只作面向DIR-042的参照筛选：检索开发商／发行商官方介绍、Steam商店页，并通过Steam公开appdetails接口定位截图，在浏览器目视下列12款各一张官方截图。没有下载原始美术、购买或运行游戏，也没有据此采纳玩法、字体、资产或世界观。言咒背景仍沿本页原CUSTOM五文件与固定版本，新增输入只有本轮公开参考研究。

下表“借鉴与优先级”是模型依据官方画面和介绍的判断；题材相近、视觉相近与交互可借鉴分别说明。A优先看，B针对单项看，C补充观察。

| 优先级／作品与官方入口 | 已核实的题材／表现 | 对言咒可借鉴什么及边界 |
| --- | --- | --- |
| A · [Pentiment](https://www.obsidian.net/games/pentiment) | 16世纪历史叙事，官方明确参考彩饰手稿及木刻印刷；二维线描、平涂与书卷式界面 | 线条粗细、颜料色块、少量排线、文字与场景统一。适合修正过度做旧的纸纹；魔法较弱，主要取画法 |
| A · [Inkulinati](https://store.steampowered.com/app/957960/Inkulinati/) | 中世纪边饰手稿，活墨绘出战斗单位；纸面战场配手部演出 | 咒文／印记如何变成可见行动，纸面、实体手与操作反馈的层级。角色及纸面为2D画法，手部等有立体演出；滑稽动物气质单独取舍 |
| A · [Scriptorium: Master of Manuscripts](https://store.steampowered.com/app/3119540/Scriptorium_Master_of_Manuscripts/) | 中世纪手稿工坊，组合图像、装饰字与羊皮纸制作书页；官方注明可创作塔罗等内容 | 抄写／铭刻工坊的工具与页边、初始大字、边框和图文组织；是文字工坊参照，魔法规则较弱。立体书册外壳与2D插画需分开理解 |
| A · [Strange Antiquities](https://store.steampowered.com/app/2885870/) | 神秘古董店，以图鉴观察、辨认并管理秘术物件；官方画面有护符、钟摆、雕像、玻璃器与柜台 | 减少草木后怎样仍有充实的施法环境；用器物剪影、材质与局部符号区分法器。偏近代古董店气质，具较强明暗体积感，非药典版画同画法 |
| A · [BOOK OF HOURS](https://store.steampowered.com/app/1028310/BOOK_OF_HOURS/) | 神秘书库与制作，卡牌、书籍、技能／仪式图标；背景属1930年代的秘密历史 | 稳定的符号家族、书籍与知识卡的识别、叙事文本和机制标签的层级；适合铭文／词义／用途的信息组织。密集多窗布局仍需针对五列与工作台另选 |
| B · [Astrologaster](https://store.steampowered.com/app/742520/Astrologaster/) | 莎士比亚时期伦敦，以占星诊断为题材；官方截图为纸偶／立体书舞台 | 纸片角色和书页的材质一致性、星象符号、蓝金设色及纸本转场。偏文艺复兴与舞台叙事，非俯视牌桌 |
| B · [Cultist Simulator](https://store.steampowered.com/app/718670/Cultist_Simulator/) | 1920年代秘密历史与神秘仪式，卡牌代表知识、工具、人物与行动 | 简洁符号承载抽象知识，书籍／仪式／行为的图标区分与查看层级；对实体词义的卡牌化有启发。纯界面密度较高，写实器物参照较少 |
| B · [7 Days to End with You](https://playism.com/en/game/7daystoendwithyou/) | 2D像素语言解读叙事，通过上下文推测陌生词义；官方画面用未知字形及词条呈现 | 铭文字形与可解释含义的对应、词组切分和查阅。适合“语言感”，画法与中世纪纸本距离较大，不据此新增解谜语言规则 |
| B · [The Cosmic Wheel Sisterhood](https://store.steampowered.com/app/1340480/The_Cosmic_Wheel_Sisterhood/) | 像素巫术叙事、占卜与自制塔罗式卡牌，宇宙女巫题材 | 卡面象征物组合、卡牌身份与巫术环境的统一；配色和符号叙事可单取。非中世纪／版画质感 |
| B · [Wytchwood](https://store.steampowered.com/app/729000/Wytchwood/) | 黑暗童话绘本，收集魔法材料、制作咒术；2D手绘元素与2.5D场景感 | 法术器物的夸张轮廓、图鉴式识别与颜色区分。更偏野外／草木，适合取法术物件设计，整体场景不是本轮低草木桌面方向 |
| B · [WitchHand](https://store.steampowered.com/app/2420880/WitchHand/) | 卡牌式女巫聚落与生产，炼金研究、法术、建筑和资源通过卡牌组织 | 生产进度与归属关系、卡面轮廓和类别色的快速识别。画法鲜艳卡通、聚落感强，和药典纸本距离较大 |
| C · [Amlebic](https://store.steampowered.com/app/4719460/) | 商店自述手绘炼金构筑、羊皮纸／铁胆墨／刻纹器皿；截图为炼金圆阵与元素手牌 | 圆阵、元素符号与持牌的纸面组合，可作补充观察。目视界面较模板化，不优先作为整体美术质量标杆；商店披露部分视觉资产使用生成式AI，未实玩核验 |

### 建议优先转化的参照关系

1. 画法与纸面层级：Potion Craft＋Pentiment，观察干净底色、物体排线与文字留白，而不是继续增加旧纸斑点。
2. 法器与工作环境：Strange Antiquities＋Scriptorium，观察护符、手稿、钟摆、刻纹、铜与玻璃的物件关系；具体选用哪些道具仍待设计选择。
3. 言咒自身的语言身份：BOOK OF HOURS＋7 Days to End with You，参考符号家族和字形／词义的关联；铭文实体及语义权限仍按现行言咒材料。
4. 施法呈现：Inkulinati，参考书写／印记进入行动的连贯表现。以上均为视觉研究建议，不是新增机制或采纳结论。

### 已目视的官方截图索引

以下只保存远端来源链接，未下载或打包第三方原图。链接来自对应Steam appdetails接口的screenshots字段；官网文字和画面只证明本次公开展示，不能代替实玩、手感、全部界面状态或项目适配验证。

- [Pentiment：书卷界面与线描设色](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1205520/ss_115917c4fe73896ec794b7e8e1795db02f33a11b.1920x1080.jpg?t=1759874806)
- [Inkulinati：纸上角色与手部施法演出](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/957960/ss_cc5a4634d9528e4b9506bba58c05ea25897884c5.1920x1080.jpg?t=1789478311)
- [Scriptorium：书页、工具与插画组合](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3119540/41da659b3c6e83ca4f43588ba7647c922b601e17/ss_41da659b3c6e83ca4f43588ba7647c922b601e17.1920x1080.jpg?t=1793099148)
- [Strange Antiquities：护符与器物陈设](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2885870/97e01678e90e067e1442528b7b70b195f7e7ce6e/ss_97e01678e90e067e1442528b7b70b195f7e7ce6e.1920x1080.jpg?t=1778730364)
- [BOOK OF HOURS：书籍卡与符号家族](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1028310/ss_bc1d3a08eb54377ae3e78bae6d64efb9ff91b166.1920x1080.jpg?t=1762944591)
- [Astrologaster：纸偶与立体书式舞台](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/742520/ss_6fd67e02f53d88f29eac55b323db7318f20a9c47.1920x1080.jpg?t=1759644602)
- [Cultist Simulator：卡牌、仪式及属性符号](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/718670/ss_5206dd7f298f61caac7ef81018ae05c32060b242.1920x1080.jpg?t=1761059623)
- [7 Days to End with You：陌生字形与语境](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1859280/ss_edcbdf4320bc1d2145acb6e0e0873d355905a443.1920x1080.jpg?t=1787026710)
- [The Cosmic Wheel Sisterhood：像素巫术环境](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1340480/ss_0a4b74eb8dcd857d4ea1ba745240346a6bafb628.1920x1080.jpg?t=1765878706)
- [Wytchwood：手绘童话场景](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/729000/ss_b5c706abacf932c95851ab3c74ef5555f2151215.1920x1080.jpg?t=1705693631)
- [WitchHand：生产卡牌与进度](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2420880/ss_7ab5ad5307ea2e89c5a8d3a3b67c0773db2eea4a.1920x1080.jpg?t=1726250594)
- [Amlebic：炼金圆阵与元素牌](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4719460/782056f78061e5150f47929c7bb371caaf1beaf8/ss_782056f78061e5150f47929c7bb371caaf1beaf8.1920x1080.jpg?t=1786610451)

## AS-G002-032 纸本秘术工坊场景候选包

| 字段 | 内容 |
| --- | --- |
| 归属／维护位置 | game-002-optimization / DIR-042；本README |
| 用途／类型 | 静态美术与新布局候选审阅；图片、提示词；非Demo或运行截图 |
| 主入口 | `scene-v04.png`；准确提示词 `scene-v04-prompt.txt`；历史图及提示词由manifest列明 |
| 固定版本 | `HERBAL-ENGRAVING-03`；[manifest](manifest.json)固定四图规格、SHA-256及工具原件。原02版沿上述旧方向固定提交的同路径manifest取证；PNG本机保存，本轮只提交文档及提示词 |
| 设计来源 | 当前五份允许材料与共同提交见本页阅读范围；历史图沿各自原输入，不将旧规则升级为现行 |
| 生命周期／访问 | ReadyForScope / PresentLocal；2026-10-27，仅静态成图、文件与哈希检查；设计Raw / Unqualified |
| 制作与复用 | 设计agent使用内置image_gen；v04是text-to-image，没有参考图／编辑底图。项目内部概念参考，公开分发与正式采用条件仍待核 |
| 关系 | v04在本包内续作，图像像素不derived-from旧图；按CORE-067及当前视觉文字合同重构。v01—v03的图像编辑关系见历史manifest，不覆盖 |

提示词：[v01](scene-v01-prompt.txt)、[v02](scene-v02-prompt.txt)、[v03](scene-v03-prompt.txt)、[v04](scene-v04-prompt.txt)。工具原件位置见manifest。未用于当前HTML、正式系统或其他方向；下一步按用户审阅结果继续具体外观与布局。
