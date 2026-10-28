# 配方、槽位与查找：静态内容证据

2026-10-28。对象为用户指定的 `E:/Game/BOOK OF HOURS v2024.12.m.3/`；本机 `version.txt` 为 `2024.12.m.3`。本页由普通文件读取与 JSON 解析取得，**不是 REA Evidence，也不是实际运行记录**。适用清单 P1-5—8；不推断当前存档已拥有下列物品、房间已开放或玩家已经学会相关规则。

下文路径相对安装目录中的 `bh_Data/StreamingAssets/bhcontent/`。英文原版字段与 `loc_zh-hans` 的同 ID 覆盖分别核对；JSON 有大小写混用（`ID`／`id`、`Label`／`label`）、UTF-8 与 UTF-16 BOM 混用，不能靠只接受单一编码／大小写的检索声称完整覆盖。`aspecteditems.json` 的对象集中在极长单行，定位以对象 ID 和字段为准。

## 1. 最小可复核链：用启示之墨制作耀素

**静态结论：同一次制作可关联四类不同去向：技艺可复用、魂质疲劳、回忆转化、新产物生成。它没有要求额外实体原料。** 因而适合检验界面是否让玩家分清“可用条件”“加工代价”和“产物”；不能因为配方叫制作就假设必有一张材料卡被扣除。

| 角色 | 对象／来源定位 | 与本例相关的字段 |
| --- | --- | --- |
| 工作台 | `core/verbs/workstations_library_world.json:40`，`library.desk.reading.consider`；简中名“书桌：阅览室” | `category: Workstation`；`hints: [heart,lantern,moon,sky]`；`aspects: difficulty.prentice=5, difficulty.scholar=10, difficulty.keeper=15`；`ambits:true` |
| 魂质 | `core/elements/abilities.json:67`，`xpho`；“明识” | `ability:1, lantern:2, sky:1`；`xtriggers.fatiguing: zpho` |
| 初级技艺 | `core/elements/skills.json:34`，`s.inks.revelation`；“启示之墨” | `skill:1, lantern:2, moth:1`；配方另查此具名技艺标记；升级触发可逐级增加 `lantern`、`moth`、`skill` |
| 回忆 | `core/elements/aspecteditems.json`，`mem.sight`；“回忆：景象” | `unique:true`；`inherits:_memory`；`lantern:1` |
| 配方 | `core/recipes/crafting_4b_prentice.json:53`，`craft.inks.revelation_pigment.refulgin_lantern`；“制作：耀素” | `actionid:library.*`；`reqs:{ability:1,s.inks.revelation:1,lantern:5}`；`warmup:60`；`effects:{pigment.refulgin:1}`；`aspects:{fatiguing:1}`；`craftable:true` |
| 产物 | `core/elements/aspecteditems.json`，`pigment.refulgin`；“耀素” | `inherits:_material`；`pigment:1, lantern:2`；`audio:SmallRattly`；`scrutiny` 关联生成 `mem.revelation` 并转换回自身 ID；进一步的查看文本提示入门级灯配方可制作它 |

按这些内容字段相加，明识的灯2＋初级启示之墨的灯2＋回忆：景象的灯1＝灯5。另有天1和蛾1，但本配方不要求它们。此处是**数值对照推导**，尚未证明引擎实际如何汇总工作台、槽位和对象属性；最终须与 REA 程序集／实机证据合看。

该配方记录没有 `inherits`、`linked`、`alternative` 或显式额外阶段字段；不能把较高级的配方提示当成会自动接续的任务链。其 `StartDescription` 同时有氛围说明和括号内配方提示，提示“玻璃＋学者级灯”会得到另一类液体；这是一条后续发现线索。

### 去向配置与时点边界

| 初始对象 | 配置中可见的转化关系 | 本页能确认什么 | 仍不能确认什么 |
| --- | --- | --- | --- |
| `xpho` 明识 | 其 `fatiguing` → `zpho`；后者继承 `_ability.fatigued`，含 `ability:1,fatigued:1`；`zpho` 的灯／天以 `zlantern:2,zsky:1` 表示 | 存在正常／疲劳两组不同状态数据，而非简单把卡删掉 | 转化在开始、计时结束还是领取时发生；图形怎样提示；是否仍能拖回或另用 |
| `s.inks.revelation` | 该对象仅列 `skillingup` 的属性增长触发，没有列 `fatiguing` 转化 | 本记录没有把技艺定义成疲劳消耗品 | 父级／引擎是否还会处理它；真实占用和归还时点 |
| `mem.sight` | 继承 `_memory`；`core/elements/_prototypes.json:514` 定义 `fatiguing`／`fatiguing.memory` → `echo`；`core/elements/misc.json:37` 的 `echo` 有 `lifetime:1` | 回忆使用可关联转成短暂回声，不应按可复用技艺表达 | 转化触发时点、回声出现位置、消失时点及是否短暂可见 |
| `pigment.refulgin` | 配方 `effects` 给出数量1 | 本配方声明产生1份耀素 | 物件何时实例化、是否等领取才出现、落在哪个窗口／桌面／房间 |

因此完整状态链目前应写作：**选择工作台及对象 → 满足条件的配方预告 → 开始行为（待观察）→ 60的配置计时 → fatiguing／effects处理（实际时序待观察）→ 结果去向和领取（待观察）**。这里的 `60` 是数据字段值，不能只凭它写成现实60秒。

## 2. 合法、数值不足、类型不符：同一工作台的三个对照

“槽位能接纳”与“配方已成立”是两个问题。本例的Soul／Skill／Memory槽分别有 `essential` 类型门槛，以及同组 `required` 属性列表。字段列出多个属性时到底按任一、全部或其他规则匹配，须由引擎／运行证据确认，不能只看单词 required 猜定。

| 候选对照 | 预判及静态依据 | 待采集的实际反馈 |
| --- | --- | --- |
| 满足配方 | 明识进Soul、启示之墨进Skill、回忆：景象进Memory；每项有相应类型，灯合计5，具名技艺和魂质均在 | 是否能放入、是否出现“制作：耀素”、是否有可执行开始按钮、点开始前能否撤回 |
| 类型都对但灯不足 | 相同明识＋初级启示之墨，暂不放回忆：景象；灯合计4，未达到配方灯5要求 | 是否展示差值、只显示泛提示或仍能开始另一配方；不能预写“按钮必定灰掉” |
| 有灯却不是魂质 | 耀素本身有灯2、继承 `_material`，但没有 `ability:1`；尝试放入Soul槽 | 是否拒绝、回弹、解释缺少魂质类型、是否仅变色；资源的同一灯符号不意味着所有槽都接受它 |

数值不足有配套文字证据：`core/recipes/z_fallthrough_hints.json:244` 的 `prentice.lantern.hint` 为 `hintonly:true`，同时要求有技能和能力、灯至少1及灯相对其他力量占优；其提示用自己的话概括为：入门需5，学者需10及合适原料，秘授需15及特定原料。这是**内容作者准备的引导分支**，不是已经观察它会在本例触发。

另有一种容易被误认为数值不足的失败：`prentice.lantern.noskillmatch.hint`（同文件:221）在灯达到5且有技能／能力时，提示可能没有适合当前技艺的配方。也有 `skill.missing.skill.hint`（:628）和 `skill.missing.ability.hint`（:635）。这些记录支持将“缺类型／缺量／所选技艺不支持”分成不同反馈意图；优先级、覆盖条件和UI成效须实机核对。

### 阅读桌槽位的确切配置

- `a / Soul`：`essential:{ability:1}`；`required:{heart:1,lantern:1,moon:1,sky:1}`。
- `s / Skill`：`essential:{skill:1}`；相同四种属性列表。
- `m / Memory`：`essential:{memory:1}`；相同四种属性列表。
- `i1 / Papers`：`required:{readable:1,blank:1}`；`forbidden:{record.phonograph:1,film:1}`。这在数据层区分纸面书写／阅读与唱片／影片；不能当作已观察拒绝动画。
- `i2 / With`：`required:{ink:1,tool:1}`；`forbidden:{fatigued:1}`。

### 高级对照：为什么不能只看总力量

`core/recipes/crafting_3_scholar.json` 中的 `craft.scholar.inks.revelation_glass_ichor.vitreous_lantern` 要求 `ability:1,s.inks.revelation:1,glass:1,lantern:10`，输出 `ichor.vitreous:1`、`warmup:90`、`fatiguing:1`。它展示配方门槛还包含原料类型，和初级耀素配方仅需要总灯5有结构差异。该对象未显式列输入 `effects:-1`；不能因此说玻璃必定保留，因为原料还可能通过 `fatiguing` 的触发映射变化。

## 3. 收藏查找：内容确实提供了哪些手段

`core/elements/tips_hints.json` 明确留下了下列说明。它们是 shipped-content 的提示语证据，仍需运行证据证明在该界面的真实覆盖、视口范围和反馈方式。

| 内容定位 | 说明意图（概括） | 对查找的意义／限制 |
| --- | --- | --- |
| `tip.slot`:22 | 点槽位，高亮可放对象；悬停某属性，高亮拥有该属性的对象 | 从任务槽反向找候选、从属性找对象；这和按名字检索不同。高亮是否遍及远处房间／被遮挡卡片，Unknown |
| `tip.workstationhints`:80 | 工作台窗口顶部图标提示相关力量 | 进入工作台时先缩小语义范围；不表示给出了完整配方或最佳决策 |
| `tip.send`:106 | Shift-click发到最近工作台；Ctrl-click发到最近动词 | 减少拖拽距离；“最近”的判定及多个窗口并存时的错投风险，待实际操作 |
| `tip.journal`:112 | 日志放错书架可能难找，即使不能误毁 | 游戏自身提示承认空间记忆仍有找回代价；这不能当成本轮玩家真的漏找过的证据 |

`core/settings/settings.json` 另有按 memories／abilities／skills／misc 分开的 `AutoSortOverlap_*`，各值标签对应不重叠、25、50；另有 `GridSnapLevel`（0—4、默认2）和 `AutosortEarlierCardsOnTop`（布尔，默认0）。配置能证明作者提供按类组织／压叠／前后顺序的选项，不能证明当前存档选值、重叠比例的像素解释或大收藏时的效率。

本页限定在上述 settings、tips 和已读工作台内容；没有从中确认按名称输入的全局搜索框、跨房间书目目录、同名多份物品的数量表达或“刚得到”的独立筛选。因此 P1-7 的三类真实任务（按已知名称、按条件、按新获得）**仍需实机案例**。不能把高亮存在直接写成“大量卡牌检索已解决”，也不能据这个范围声称整个游戏没有搜索功能。

## 4. 多任务与窗口：已完成不必靠记忆位置

`core/elements/tips_hints.json:120` 的 `tip.completedworkstations` 明确说明 Backspace 可轮转到配方已完成的工作台。它提供“完成集合”导向的回访入口，可与当前任务窗口分开讨论；尚未证明会弹通知、自动夺取焦点或在地图外可见。

可见性设置的配置范围：`ScreenCanvasSizeSlider` 为75—110、默认100；`FontSize` 为12—36、默认19。它们是可配置范围，不是本次实际分辨率或UI缩放。地图总览、近看工作台和多窗遮挡仍须截图；静态选项不足以评定舒适／迷失。

## 5. 面向言咒的候选用途与代价

以下仅沿 DIR-042 既定CUSTOM摘要及清单提出，状态 Raw / Unqualified，不改变言咒的生产时序或现行规则。

1. **同符号不等于同权限。** 耀素有灯，但不能据此当成Soul。言咒可将“这个对象是什么”与“这次操作接受什么”分别表达；代价是必须给玩家看得懂的拒绝原因，不能只靠同色或同字暗示。
2. **把类型错、数量差、配方不支持分开。** 这三类内容提示背后需要不同解决动作；候选下一步是先写言咒已有动作的错误情境与一句可执行提示，不新增自动决策。
3. **投入的代价需要按对象说明。** 技艺占用、魂质变疲劳、回忆耗去、新物生成属于不同关系；它可启发言咒区分可复用对象与材料，但这里的 `fatiguing` 不是可直接复制的消费时序。
4. **从槽位反查候选可能比常驻全筛选更轻。** 只有实机验证高亮的覆盖范围、遮挡和错误理解后，才能判断是否足够支撑双组持牌；单看四张牌不足以决定大收藏布局。
5. **不宜直接迁移“最近窗口自动接收”。** Shift／Ctrl快捷发送可减少拖拽，但言咒同屏有双法器、持牌与战斗行；“最近”可能和玩家认定的当前目标不同。候选是明确选中目标之后再显示可发送处，是否增加快捷键另行决定。

## 6. 清单状态与仍需补证

| 项目 | 本页覆盖 | 状态 |
| --- | --- | --- |
| P1-5 合法／不足／类型错 | 具体对象、槽条件、配方和hint分支已定位；UI动作及拒绝样式未观察 | 部分回答 |
| P1-6 制作及唯一对象去向 | 配方与继承触发链已定位；开始／完成／领取的实际时点与位置未知 | 部分回答 |
| P1-7 大量收藏查找 | 任务槽／属性高亮、分类叠放配置、日志漏放提示已定位；真实找回和数量表达未观察 | 部分回答 |
| P1-8 多任务与注意力 | 完成工作台轮转、字体／缩放配置已定位；多窗遮挡与舒适／迷失画面对照未观察 | 部分回答 |

本页不宣称全部技能／全部配方已读，不对 `_legacy*`、DLC工作流、隐藏分支或未读引擎行为作排除结论。配置存在不能代替实际操作，也不能推断玩家已经理解或喜爱这些表达。
