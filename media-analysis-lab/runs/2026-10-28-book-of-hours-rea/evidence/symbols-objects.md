# 符号、书籍身份与器物：静态内容核对

2026-10-28 · BOOK OF HOURS `2024.12.m.3` · 清单 P0-1—4 的数据层补证。

本稿由并行工作者以 PowerShell `ConvertFrom-Json` 读取安装目录中的发布内容和 Addressables 目录，未运行目标、未加载程序集、未观看截图。它是普通文件解析证据，**不具有 REA Evidence ID，也不证明界面实际显示、玩家理解或操作时点**。安装根为 `E:/Game/BOOK OF HOURS v2024.12.m.3/`，以下路径均相对该根；内容根缩写 `C = bh_Data/StreamingAssets/bhcontent/`，图像地址目录为 `bh_Data/StreamingAssets/aa/catalog.json` 的 `m_InternalIds`。引用对象ID和字段为主；压缩在一行的文件不以虚假的精细行号定位。

## 1. 符号不是一张图标对应一种万能数值

**静态观察：灯、铸、穹分别是稳定的主题键，但主题相同不等于功能相同。** 定义在 `C/core/elements/_aspects.json` 的 `lantern`（97行）、`forge`（68行）、`sky`（139行）；中文 `C/loc_zh-hans/elements/_aspects.json` 分别标为“灯”“铸”“穹”。它们的说明把世界观联想与较直白的准则概括并列，排序键统一在 `group1_primary.*`。

| 主题 | 对象中的强度 | 技能中的强度 | 工作台中的重用 | 可核对的图像地址 |
| --- | --- | --- | --- | --- |
| 灯 `lantern` | `mirrorscope` 透显镜：`lantern=1`、`boost.lantern=1`；`mem.revelation`：两项各为2 | `s.pyroglyphics`：`lantern=1`、`forge=2`；`s.purifications.exaltations`：`lantern=1`、`sky=2` | `library.workbench.gallery` 的 `hints`、魂质/技艺/回忆槽 `required` 都包含 `lantern` | `bhimages/aspects/lantern`；`bhimages/things/mirrorscope` |
| 铸 `forge` | `compasses.forge` 圆规：`forge=1`、`boost.forge=1`；`book.press` 亦有相同数值组 | `s.pyroglyphics`：`forge=2` | `library.workbench.gallery` 与 `library.telescope` 的同类槽都包含 `forge` | `bhimages/aspects/forge`；`bhimages/things/compasses.forge` |
| 穹 `sky` | `astrolabe.sky` 沉默男爵的星盘：`sky=1`、`boost.sky=1`；`mazarine.fife`：两项各为3 | `s.purifications.exaltations`：`sky=2`；`s.lockworks.clockworks`：`sky=1`、`knock=2` | `library.telescope` 的 `hints`、魂质/技艺/回忆槽 `required` 都包含 `sky` | `bhimages/aspects/sky`；`bhimages/comforts/astrolabe.sky` |

对象字段取自 `C/core/elements/aspecteditems.json`；技能取自 `C/core/elements/skills.json` 对应ID（`s.pyroglyphics` 14行、`s.purifications.exaltations` 334行、`s.lockworks.clockworks` 354行）；工作台取自 `C/core/verbs/workstations_library_world.json`（望远镜69行、风徊工作台70行）。这里证明的是**同一语义键跨数据域重用**；同一图像是否在以上每一处被渲染、图标和数字的实际位置，需结合引擎和截图。

### 相同主题下至少有四种角色

| 键/变体 | 已读的定义与用途 | 容易发生的推断错误 |
| --- | --- | --- |
| `lantern` | 普通灯强度，排序 `group1_primary.lantern` | 把所有带灯的数字都加总为当前投入 |
| `mystery.lantern` | 奥秘：灯；说明较难挑战需要较强技艺，排序为 `group2_challenges.lantern` | 书上的“奥秘：灯4”误当它提供灯4 |
| `mastery.lantern` | 已熟悉该文本的状态定义；图像地址另有 `bhimages/aspects/mastery.lantern` | 将阅读状态与可投入能力混为一项 |
| `zlantern` | 灯的疲劳态数值；定义明确指恢复后重新拥有的强度，排序 `group1_primary.zlantern` | 把未来恢复量当现在可用量 |

此外 `boost.lantern` 是 `isHidden=true` 的独立属性（185行），不能因为它数值与 `lantern` 相同就认定玩家面板显示两份或物品被消费两次。`forge`、`sky` 有对应 mystery、mastery、z 和 boost 家族。`catalog.json` 中 `bhimages/aspects/` 的确存在对应变体地址；**没有在本稿直接读过像素，因此不能声称变体靠颜色、底形或某种描边区分**。

易混候选首先是“灯强度 / 灯奥秘 / 疲劳灯”，因为主题接近而职责不同。这是需要实机核对的设计风险；未记录真实玩家误读。月 `moon` / 蛾 `moth` 等不同图形是否近似，本稿未作视觉判断。

## 2. 一本书的身份链：锁匠的梦境

样本为 `t.thelocksmithsdreamalightthroughthekeyhole`，中译《锁匠的梦境：穿过锁孔之光》。原文条目在 `C/core/elements/tomes.json` 128—130行附近；中文文本覆盖在 `C/loc_zh-hans/elements/tomes.json`，ID位于2923行。

| 信息层 | 已确认字段 | 能说明什么 / 不能说明什么 |
| --- | --- | --- |
| 稳定身份 | 两种语言同ID；`unique=true`；`inherits="_book"` | 内容定义共用身份，唯一性是配置声明；不能仅此证明场景实体与详情预览共享同一运行实例 |
| 文本识别 | `Label` 是书名，`Desc` 是作者及卷次简介；中文覆盖相同字段 | 简介先让人知道“这是什么”；简介本身没有列出完整操作步骤 |
| 机制标签 | `mystery.lantern=4`，`period.nocturnal=1`，`cost.tally=1`，`r.purifications.exaltations=1`，`soph=4`，`codex=1` | 挑战、时代、内容关系与物理类别有分别的属性键；不能把 `cost.tally` 直接译成玩家实际支付价，亦不能把 `r.*` 当已学会的技能 |
| 承载形式 | `manifestationtype="Book"`，`audio="Book"` | 数据指定书籍表现类与音频类别；实际音效、外观和交互仍需运行核对 |
| 阅读前/中叙述 | `xexts["reading.lantern.intro"]` | 扩展讲解工匠梦境的共性；字段名支持阶段区分，但本稿没有观察出现时点 |
| 阅读叙述 | `xexts["reading.lantern"]` | 更深入地把林地、光与梦境联系起来；不能据字段名称断言只在完成后出现 |
| 结果钩子 | `xtriggers["mastering.lantern"]` 指向 `x.purifications.exaltations`，`morpheffect=spawn`、`level=1`；`reading.lantern` 指向 `mem.revelation`，同为 spawn、1 | 可以精确追查配置关系；不证明两者同时发生、实际取回位置或消耗时点 |

`_book` 定义在 `C/core/elements/_prototypes.json` 304行起。它声明 `manifestationtype=Book`、`readable=1`、`thing=1`、`unique=true` 和三个 `consider` 槽：魂质、可选技艺、可选回忆；魂质槽要求 `ability` 并排除 `fatigued`。这是样本本身没有展开的继承层。不能因本书条目不写 `slots` 就说它没有操作槽。

同文件另有 `_book.unc`（295行起），带 `uncatalogued=1` 和不同魂质槽限制。这证明“未编目书籍”有独立原型；本稿未建立本样本从某个未编目对象变来的映射，不把它拼成真实操作链。

### 图像地址能建立候选对应，不能替代同物验证

目录中同时存在以下地址：

- `bhimages/books/t.thelocksmithsdreamalightthroughthekeyhole` 与末尾 `_` 版本。
- `bhimages/books/loc_zh-hans/t.thelocksmithsdreamalightthroughthekeyhole` 与末尾 `_` 版本。
- `loc_ru` 中亦有相同ID的一对地址。

本稿未看到这些纹理，**不把无后缀/下划线后缀直接命名为封面/书脊**。本书JSON也没有单独的颜色、封面、字体或 `icon` 字段；不能从书名或准则推测它的封皮颜色。实际身份链仍须由同对象在架上、选中、详情、投入后四处截图及引擎身份关系建立。

## 3. 信息分层的数据证据与操作缺口

样本把 `Label`、`Desc`、`aspects`、`slots`、`xexts`、`xtriggers` 分开，这提供了**内容分层的结构条件**。`_aspects.json` 的准则说明常将意象性描述与方括号中的较直白概括并置；`memory`（1519行）的说明明确提及制作、升级技艺以及一般回忆在黎明消失的规则。与仅有氛围的透显镜简介相比，操作信息并非都藏在同一种散文里。

但这不等于信息在界面上已经分得好。未知包括：常驻显示哪些属性，悬停新增什么，是否必须层层打开才能解释 `mystery`，长文如何收起，玩家能否从规则问题顺利找到答案，以及中文字号和装饰字体可读性。

静态可构造的具体核对任务是：看到书的“灯奥秘4”后，玩家能否找到一个实际提供灯强度的魂质/技艺/回忆；再检查回忆灯2与书的奥秘4是否被误当两张相同功能的“灯卡”。这是待执行任务，不能记录成已观察到的成功或失败。

## 4. 器物、家具和工作台的不同承载方式

三个小物有具体的物性命名与音频/表现原型关系，但不都使用同一表现类：

| 对象 | 类型与属性证据 | 图像/预制体地址证据 | 视觉上仍待核对 |
| --- | --- | --- | --- |
| 透显镜 `mirrorscope` | `inherits="_"`，`tool=1`、灯与boost各1；`_` 原型为 `ManifestationType=Thing`（`_prototypes.json` 4行起） | `bhimages/things/mirrorscope` | 镜片/支架剪影、材质、缩小时可辨性 |
| 圆规 `compasses.forge` | 同属 `_`，`tool=1`、铸与boost各1 | `bhimages/things/compasses.forge` | 两脚开合是否是主识别线索，细尖是否在小尺寸丢失 |
| 星盘 `astrolabe.sky` | `inherits="_comfort"`，`tool=1`、穹与boost各1；`_comfort` 为 `Comfort`，有 comfort/considerable 与查看槽（346行起） | `bhimages/comforts/astrolabe.sky`、`bhimages/comforts/named/astrolabe.sky` | 环形结构、底座、named版本的用途 |
| 望远镜 `library.telescope` | 独立 verb；`category=Workstation`、`ambits=true`、`audio=Telescope`；五个槽含魂质/技艺/回忆及两个追加槽；5/10/15三个难度属性 | `bhimages/fitments/library.telescope`、`library.telescope2`；`bhimages/verbs/library.telescope`；`prefabs/workstations/library.telescope` | 场景体量与窗口图像怎样对应，选中/禁用反馈是否独立于美术本体 |

**推断：**相同主题属性允许工具、记忆、技能和工作台关联，而 `Thing / Comfort / Book / Workstation` 分开处理承载方式；因此没有必要让所有功能对象都画成同一种牌。**限定：**这只是一条可供视觉与交互核对的结构判断，本稿没有证明其体量层级、描边粗细、颜色数量或场景噪声效果。

## 5. 面向言咒的候选用途（Raw / Unqualified）

仅沿 DIR-042 已记录的背景版本 `f8849ed93c159ecee6baceddb5cfa52cde4084cf` 与该方向摘要讨论，不宣称读过本轮未授权的系统细则。

1. **把语义主题和功能角色拆开。** “庇护/打击”等文字可保留语义，需求、当前提供值、未来恢复值分别采用有明确职责的附加表示；代价是必须建立少量可学习的角色标记，避免出现很多只换颜色的近似符号。最小核对：同一主题同时出现于器物、持牌和槽条件时，让阅读者分别指出哪里是需求、哪里是能力、哪里暂不可用。
2. **同一对象多种表示用共同身份承接。** 书籍数据的同ID、多地址、独立文本层可参考，但图像本身不能承担唯一库存的保证。实体铭文与详情说明应核对是否存在两份可拖动感；最小核对：从详情返回后，能否指出唯一实物位置与占用状态。
3. **简述与完整说明分层，同时保留操作入口。** 可参考短名、对象简介、明确条件和扩展阅读各有职责的结构；代价是正文很容易只留下氛围而把必要规则藏进详情。最小核对：先只看主桌判断下一步，再允许详情，记录为解决一个规则疑问必须经过几层。
4. **器物类型分工不等于每类另建库存。** 工具、家具、书籍和工作台可以保留不同体量与轮廓，同时共享语义标签；代价是需更明确地表达哪些是可移动对象、哪些只是场景入口。最小核对：在静态画面标出可操作物、装饰物和只读图。

不适合直接迁移的是按13种主题再派生多组状态图标的规模。单是主准则与疲劳准则就在同一排序组形成26条定义，还另有奥秘、掌握、阅读等变体；这是内容目录规模的事实，不能作为言咒也需要同样数量的依据。

## 未完成取证

- 尚未直接看过本稿列出的任何图像像素；没有颜色、形状、线条、缩放质量的实证判断。
- 没有同一本书在场景与详情的实机前后图；没有占用/移动/复制误判的观察。
- 没有一次符号正确预测、真实误读、点错或漏看的操作证据。
- 没有依据普通 `required` 多键写法擅自判定它们是全部满足或任一满足；该逻辑交由引擎解析或实机核对。
- 没有把 `spawn`、`unique`、`boost` 或文本阶段名当作实际生效时点。制作状态、扣除、归还与结果位置须另用状态链证据。
