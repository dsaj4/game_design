# 言咒类似游戏的引擎使用调研

2026-10-11 · game-002 · 技术选型研究输入。用户要求先进行类似游戏的引擎使用调研；目标设备采用当前Windows电脑，正式引擎按Unity／Godot实测结果选择。

类似作品的公开资料支持继续比较Unity和Godot。Unity有《邪恶冥刻》的三维牌桌，以及《堆叠大陆》《密教模拟器》的卡牌生产与组合案例；Godot有《杀戮尖塔2》的规则开发经验、《背包乱斗》的装配后自动战斗，以及《恶魔轮盘》的三维桌面表现。**当前建议是保留两引擎进入P0，把Unity作为三维牌桌对照，把Godot的规则迭代和资产接入作为重点验证项。**这属于根据案例与本项目需求作出的判断，尚未冻结引擎、语言、版本或正式代码仓库。

## 对照范围

本项目输入为[开发计划](../production-plan.md)、[开发规范](../development-standard.md)、[资产接入清单](../asset-readiness.md)，以及设计提交`5c542e12c53a5ba3044b6e647e6c3950e9260bc5`中的[核心设计](../../design/core-design.md)。本次采用CUSTOM范围，没有扩读GDD分册、其他探索方向、旧项目或外部实现代码。

据此按四种具体需求选择参照：三维桌面物件与卡牌表现、配方与计时生产、构筑后自动运行、内容规则与恢复。下表的相似点和适用边界是本项目分析；引擎归属来自各行的一手资料。样本按相关性选择，不能用数量推断整个品类的市场占比或引擎优劣。

## 类似游戏与实际引擎

| 游戏 | 已确认的引擎或框架 | 对言咒最有用的相似点 | 适用边界与一手依据 |
| --- | --- | --- | --- |
| 邪恶冥刻 Inscryption | Unity；维护招聘明确要求C# | 三维桌面、实体卡牌、物件选择和氛围表现，是当前视觉路线的主要参照 | 开发者[访谈](https://www.gamedeveloper.com/design/how-game-jam-sacrifices-became-inscryption)确认Unity；[工作室招聘](https://www.danielmullinsgames.com/work-disabled)确认Unity／C#维护要求。不能据此推定本项目的材质、规则或性能已通过。 |
| 堆叠大陆 Stacklands | Unity | 卡牌组合、资源生产、配方取得和自动战斗，适合对照生产结果怎样变成可读物件 | 主设计师兼程序员在[IGF访谈](https://www.gamedeveloper.com/business/how-stacklands-uses-simplicity-to-create-a-compelling-card-based-village-builder)直接确认Unity。其卡牌堆叠方式不等于本项目的有限行动队列和逐拍顺序。 |
| 密教模拟器 Cultist Simulator | Unity | 卡牌作为资源与操作对象，多项活动和组合关系集中在桌面上 | [Unity官方作品介绍](https://unity.com/blog/games-made-with-unity-horror)列出本作；[开发商商店介绍](https://store.steampowered.com/app/718670/Cultist_Simulator/)说明组合卡牌、制作和资源用途。不能把叙事活动的运行方式当作本项目攻防时序。 |
| 杀戮尖塔2 Slay the Spire 2 | Godot；开发团队确认C#，并维护自有MegaDot分支 | 大量卡牌与状态规则、内容维护、自动检查和频繁构建 | [Mega Crit官方AMA](https://www.reddit.com/r/Games/comments/1rdqanv/hi_reddit_were_mega_crit_the_developers_of_slay/)说明技术经历；[Godot官方展示](https://godotengine.org/showcase/)列出本作。团队对Godot的推荐明确面向2D；不能直接外推三维牌桌或原版Godot的全部能力。 |
| 背包乱斗 Backpack Battles | Godot | 装配／购买后自动战斗，物件关系影响效果，运行过程需读得懂 | [开发者Demo页](https://playwithfurcifer.itch.io/backpack-battles)标明Made with Godot，介绍背包构筑和自动战斗；[Godot官方回顾](https://godotengine.org/article/2024-cherry-picks/)收录本作。二维背包界面不能证明当前GLB的表现和运行成本。 |
| 恶魔轮盘 Buckshot Roulette | Godot | 三维桌面、有限物件、回合操作与反馈，为Godot提供比纯二维卡牌更接近的视觉参照 | [Godot官方开发者访谈](https://godotengine.org/article/godot-showcase-buckshot-roulette/)介绍本作与作者的Godot经历。其物件数量和卡牌规则复杂度与本项目不同。 |
| Dancing Duelists | Godot；Casey Yano的评估文章讨论C#流程 | 构筑后按序自动运行；以范围有限的小游戏评估引擎 | [Mega Crit发布页](https://megacrit.itch.io/dancing-duelists)明确是三周Godot评估项目；[创始人评估文章](https://caseyyano.com/on-evaluating-godot-b35ea86e8cf4)说明流程和裁剪。团队规模、已有技术能力及范围不同，三周不能作为言咒工期。 |
| Luck be a Landlord | Godot；当时桌面版使用含Steamworks集成的定制构建 | 构筑后多种效果自动兑现，适合对照效果反馈和内容增加 | [开发者日志](https://blog.trampolinetales.com/dans-devlog-april-2023/)直接说明Godot及移植困难。它没有当前三维牌桌；定制构建和平台集成也会产生维护成本。 |
| 小丑牌 Balatro | LÖVE／Love2D框架 | 卡牌反馈、效果叠加和信息密度；说明这类规则并不依赖大型三维引擎 | [原开发发布帖](https://www.reddit.com/r/love2d/comments/13xsim2/finally_submitted_the_steam_build_for_my_game/)标题声明使用Love2D，作者回复链接到本作Steam页。卡牌的透视与着色效果不能等同已完成三维资产工作流。 |
| 杀戮尖塔 Slay the Spire | libGDX框架 | 卡牌规则、状态组合与局内内容，提供框架路线的对照 | [libGDX官方展示](https://libgdx.com/showcase/)直接列出本作。该归属只针对初代；续作采用Godot，不能混写成同一技术栈。 |
| 循环英雄 Loop Hero | GameMaker | 间接战斗、玩家调整构筑与循环成长，适合对照自动过程的可读性 | [GameMaker官方对移植团队的访谈](https://gamemaker.io/en/blog/pc-to-mobile-loop-hero)确认原作使用GameMaker。移植仍涉及输入、界面和性能适配，不能以跨平台支持替代实际验收。 |

资料确认的是上述作品在所述开发阶段使用的技术。除明确列出的C#及定制分支信息外，具体引擎小版本、渲染管线和包版本没有在本表确认；不按产品画面反推，不把旧案例使用的版本选为新工程默认值。全部网页核对日期为2026-10-11，资料自身的发表时间保留原页。

## 开发经验对选型的影响

### 三维牌桌需要实际导入对照

《邪恶冥刻》使Unity成为与现有桌面表现直接相关的参照。《恶魔轮盘》则说明Godot也有三维桌面作品，不能只用Godot的二维案例判断它的适用范围。两者的案例都没有测过本项目资产，因此目前无法据此确定材质修复耗时、点击遮挡、重导入稳定性或帧时间。

本项目已有Blender v02／GLB。Godot官方[推荐glTF 2.0，支持GLB](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html)；Unity的官方[glTFast编辑器导入](https://docs.unity3d.com/Packages/com.unity.cloud.gltfast@6.15/manual/ImportEditor.html)支持GLB。两边都有可检查的接入路径；格式支持本身不能决定实际材质一致性。资产清单记录的1103个mesh条目也不能直接当成绘制调用数或性能结果。

### 规则逻辑与表现分开能降低返工

Mega Crit团队在官方AMA中说明：他们先把内容从Unity的Scriptable Objects转为C#类，配合自动检查，并将内容逻辑与渲染／输入分开；后来切换Godot时，大量规则代码得以保留，输入和表现仍需要改造。团队还维护了自有MegaDot分支，并经历等待引擎修复或自行补功能的情况。[团队原答复](https://www.reddit.com/r/Games/comments/1rdqanv/hi_reddit_were_mega_crit_the_developers_of_slay/)

对言咒的推论是：无论最终选哪个引擎，都应沿[现有开发规范](../development-standard.md)独立核对逐拍结算、支付、队列与恢复。C#值得作为P0共同规则实现的候选，以便对照结果和保留代码；正式语言仍在选型时确定。若试用Godot／C#，需采用其[.NET版编辑器](https://docs.godotengine.org/en/stable/tutorials/scripting/c_sharp/index.html)。这一建议不要求照搬Mega Crit的内容架构或维护引擎分支。

### 构建速度与平台接入都应计入成本

Casey Yano在2023年评估中肯定Godot的迭代与构建流程，同时指出纹理图集、字体等问题。这是当时的项目经验，不能直接作为2026年版本的测量结论。[原评估](https://caseyyano.com/on-evaluating-godot-b35ea86e8cf4)

《Luck be a Landlord》开发者记录过Steamworks定制构建影响Android导出的问题；《Loop Hero》移植团队也说明输入、可读性和平台服务需要单独处理。对本项目而言，先验收Windows离线构建与保存恢复；以后新增平台时重新检查对应工作，不从其他作品的跨平台发行推定一键完成。[开发者日志](https://blog.trampolinetales.com/dans-devlog-april-2023/) · [移植团队访谈](https://gamemaker.io/en/blog/pc-to-mobile-loop-hero)

## Unity和Godot的当前比较依据

| 本项目问题 | Unity的已有依据 | Godot的已有依据 | P0需要取得的证据 |
| --- | --- | --- | --- |
| 三维牌桌能否接近现有视觉 | Inscryption的同类表现；官方glTFast路径 | Buckshot Roulette的桌面表现；原生GLB导入路径 | 同一相机与视口的对照图、材质差异及修复时间 |
| 卡牌生产与自动运行能否清楚呈现 | Stacklands、Cultist Simulator提供相关形态 | Backpack Battles、Dancing Duelists提供自动战斗形态 | EX-001真实推进及未来用途操作，不能只播预制动画 |
| 复杂规则能否持续检查 | 同样可以执行独立规则检查；本项目尚无结果 | Mega Crit公开了C#与自动检查经验；本项目尚无结果 | 相同输入的事件账目、关键失败例和故障定位过程 |
| 保存和独立包是否可靠 | 案例使用不代表本项目恢复正确 | 案例使用不代表本项目恢复正确 | 退出后恢复、可控写入失败、清洁目录离线启动 |
| 日后改资产会不会丢交互绑定 | 当前GLB重导入尚未检查 | 当前GLB重导入尚未检查 | 修改一个组件后重导入，核对点击、材质与对象关系 |
| 工具和许可条件能否满足 | Personal资格及实际订阅条件待项目核对 | MIT许可；分发引擎须保留相应版权与许可说明 | 固定工具／包版本、实际安装与接手成本及使用条件 |

Unity在2023年的Runtime Fee事件属于历史选型背景。官方已于2024年9月宣布取消该费用；当前[定价说明](https://unity.com/products/pricing-updates)确认它不适用于任何版本的Unity游戏。不能据此继续计算“按安装量收费”。[Personal页面](https://unity.com/products/unity-personal)仍列财务资格条件；本项目是否满足尚未核对。Godot采用[MIT许可](https://godotengine.org/license/)，开源许可也不等于插件接入、平台移植或维护没有工作量。

LÖVE、libGDX和GameMaker的案例可以用来学习效果反馈与规则组织。本项目已经采用三维源场景、相机、实体物件和GLB作为开发输入，在当前范围下继续集中比较Unity／Godot更直接；本轮不增加第三套实现路线。Noita的[自研引擎介绍](https://nollagames.com/fallingeverything/)与[开发者技术演讲](https://www.gdcvault.com/play/1025695/Exploring-the-Tech-and-Design)主要涉及像素物理与可破坏世界，无法为当前逐拍牌桌需求提供同等直接的选型依据。

## 调研结论与下一步

同类作品已提供足够依据进入原定P0，无需因“某个引擎是否做得了卡牌游戏”继续扩大案例调查。Unity的重点是三维牌桌接入与相关交互的实现成本；Godot的重点是在同样视觉目标下能否取得更低的迭代、构建与维护成本。哪一边更省力仍由同机实测决定。

按[开发计划的六项同题任务](../production-plan.md#两边完全相同的任务)执行时，优先查明固定GLB的实际导入差异与EX-001的可核对结算，再完成中文物件交互、恢复及写入失败、Windows独立包、重导入与接手复现。硬门槛和原评分权重保持原计划；本次不预填评分，不把案例数量换算为引擎得分。

状态：类似游戏引擎调研完成；P0引擎实测NotRun。尚未安装引擎、创建新版实现工程、修改资产或运行玩法实验。引擎／语言／渲染／准确版本及正式仓库仍待P0结论确定；本报告不形成玩法素材资格或采纳决定。
