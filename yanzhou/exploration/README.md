# 言咒探索方向

Project ID：`game-002-optimization`。目录修订：layout.2 / 2026-09-24。这里保存独立构思，与主系统现行规则隔离。

**一个方向一个文件夹，一份README存必要构思。** 先从下表选方向，打开即可阅读想法、玩家选择、与其登记基线的差异、未知项和来源。方向持续登记，既有编号保留且不复用。

[启动探索：选择阅读材料](start.md) · [核心设计](../design/core-design.md) · [方向对比与主系统吸收](comparison.md) · [整理前档案](../history/exploration-2026-09-24/README.md) · [主系统入口](../design/README.md)

方向Demo和制作/参考素材按[DA-1](../../docs/demo-asset-standard.md)在[统一目录](../../docs/registry/demo-assets.md)登记，原件与复用记录留所属方向或实现位置。查看其他方向资源仍须纳入本轮允许材料；不因目录可见自动扩读。

## 目录怎么用

```text
exploration/
├── README.md                         全部方向入口
├── comparison.md                     方向差异、背景与吸收范围
├── AGENTS.md                         简化存储与隔离约定
├── start.md                          启动方式、阅读模式和来源记录
├── DIR-001-battlefield-compiler/
│   └── README.md                      一个方向的必要构思
├── DIR-002-spell-expedition/
│   └── README.md
└── ...                               其余方向结构相同
```

新增方向先按[start.md](start.md)选阅读范围；未指定时仅用核心设计。使用下一未占用DIR编号与英文短名，先只建README，并在本页记录允许材料与实际阅读范围。正文写清“想做什么／玩家怎样选择／与现行设计的关系／还没想清什么／来源与状态”，未知就写Unknown。相关图片或确有必要的补充才放到同一方向文件夹，不预建空目录、不要求每个方向走一套流程文件。阶段和选择直接记在本页。

目录简化不改变资格：新构思默认Raw / Unqualified；需要正式提案或GDD时才完成资格并建立相应来源记录，详细规则见[AGENTS](AGENTS.md)。迁入当前主系统仍须目标项目复审、Draft Change和明确采纳。

## 启动时选择背景

| 你说 | 模型读取 |
| --- | --- |
| 只读核心设计 | 一份core-design.md，适合方向构思；新方向默认 |
| 读完整GDD | GDD及固定16份包内正文，不追读来源链接 |
| 读全量文档 | 当前主系统全部登记文本；历史、其他探索、外部代码分别选择 |
| 只读这些材料 | 精确文件／章节清单，不补读其他游戏正文 |
| 不读游戏背景 | 只从本轮输入形成新方向，不能宣称与当前系统兼容 |

例：“启动新方向：〈标题〉，只读核心设计，探索〈目标〉，不自行扩读。”完整边界、版本与记录方式见[start.md](start.md)。日常构思仍只用方向README，不增加流程树。

## 近期记录

此分组只反映最近新增的记录，不是新的推进、资格或采纳决定。编号永不复用。

| 方向 | 构思 | 状态 |
| --- | --- | --- |
| [DIR-028 时间轴深度构筑](DIR-028-timeline-depth/README.md) | 第8轮：时间产线核心升入TL-1，卡牌战场与新卡表重设计；兼容性审查、原始探索和UI候选各保留身份。 | 核心Qualified / Accepted；具体卡表Proposed；UI与早期构思Raw；FULL |
| [DIR-029 时间轴铺卡战斗](DIR-029-timeline-card-battle/README.md) | 自构法术，每杖按冷却生成一行牌，共享可折叠时间轴；默认并行、强力法术有独占格，同刻效果同时生效，敌方暗牌有线索。 | Raw Idea / Unqualified |
| [DIR-030 卡牌规则设计](DIR-030-card-rule-design/README.md) | 优先保留时间轴铺排，构句不作为核心；从有限时间容量发散十版简单规则，后续再收敛与评估。 | Raw Idea / Unqualified；CORE |
| [DIR-032 完整机制、卡牌试点与最小可玩链路](DIR-032-playable-mechanism-loop/README.md) | Q1–Q16确认，8配方与两战Demo已实现；生产、队列、维护、路由、奖励及携带形成完整试点链路，局部检查通过。 | Qualified试点；CUSTOM；真人体验NotRun |
| [DIR-033 炼金系统构筑与构句重设计](DIR-033-alchemy-system-redesign/README.md) | AGC-1分离设计、展示实现与独立审查；将构句重设计为真实卡牌装配、资源转化与行动协同的炼金系统，交付可操作展示册。 | 新卡义Raw候选；CUSTOM固定最新主系统＋DIR-031／032；Q1–Q3确认 |

## 其余待选与局部合格方向

| 方向 | 构思 | 状态 |
| --- | --- | --- |
| [DIR-001 战场编译器](DIR-001-battlefield-compiler/README.md) | 为句子选择Now、Commit、Echo时间姿态。 | Raw Idea / Unqualified |
| [DIR-002 法术远征](DIR-002-spell-expedition/README.md) | 将公开敌意、时间承诺与分叉远征连接。 | Raw Idea / Unqualified |
| [DIR-003 时间背包与循环调度](DIR-003-timeline-backpack/README.md) | 战前安排首次时点，各法术自动循环；实体独占与同刻覆盖。 | 局部Qualified / Hypothesis；部分吸收 |
| [DIR-004 敌方阶段窗口](DIR-004-enemy-phase-windows/README.md) | 公开窗口改变不同时刻的释放价值。 | Raw Idea / Unqualified |
| [DIR-005 有限调速](DIR-005-limited-cycle-tuning/README.md) | 战前以有限机会调整后续循环间隔。 | Raw Idea / Unqualified |
| [DIR-006 战后重组](DIR-006-postbattle-reconfiguration/README.md) | 奖励后替换实体词卡并局部重组下一场编排。 | Raw Idea / Unqualified |
| [DIR-007 空档蓄能](DIR-007-idle-reserve/README.md) | 主动留白积累有上限储备，供后续释放消耗。 | Raw Idea / Unqualified |
| [DIR-008 视觉施法音乐](DIR-008-spell-music/README.md) | 实际视觉释放触发法术独有音乐反馈。 | 局部Qualified / Hypothesis；未采纳 |
| [DIR-009 公开条件敌意](DIR-009-conditional-intent/README.md) | 公开条件使敌人按受影响状态执行不同攻击。 | Raw Idea / Unqualified |
| [DIR-010 封词借词](DIR-010-bound-enemy-word/README.md) | 封住敌方能力并临时取得对应词的组句用途。 | Raw Idea / Unqualified |
| [DIR-011 痕迹牵动敌方能力](DIR-011-scar-linked-enemy/README.md) | 改变战场痕迹，进而影响敌人的公开优势。 | Raw Idea / Unqualified |
| [DIR-012 两杖接句](DIR-012-sentence-handoff/README.md) | 让一次时点冲突转为有代价的两杖协作。 | Raw Idea / Unqualified |
| [DIR-013 冷却预算重排](DIR-013-rhythm-budget/README.md) | 保持相邻两次冷却总量，将节奏分成均分、短长或长短。 | Raw Idea / Unqualified |
| [DIR-014 有限候发](DIR-014-bounded-ready-window/README.md) | 释放资格保留一个有限等待窗口。 | Raw Idea / Unqualified |
| [DIR-015 法杖跟随](DIR-015-wand-follow-clock/README.md) | 先成功完成来源句，再启动跟随杖下一次冷却。 | Raw Idea / Unqualified |
| [DIR-016 未来投影](DIR-016-field-time-projection/README.md) | 战前选时间查看预计范围、对象变化与冲突反馈。 | Raw Idea / Unqualified |
| [DIR-017 待发法阵](DIR-017-pending-spell-circle/README.md) | 让已投入时间形成可交互的待发场上对象。 | Raw Idea / Unqualified |
| [DIR-018 巡行范围](DIR-018-patrol-cast-range/README.md) | 预设多个锚点，法术范围沿正常周期逐轮移动。 | Raw Idea / Unqualified |
| [DIR-019 知情远征](DIR-019-informed-expedition/README.md) | 将未来咒式目标、路线信息与特定成长机会连接。 | Raw Idea / Unqualified |
| [DIR-020 限额整备连续试炼](DIR-020-committed-trial/README.md) | 连续挑战中限制战间整备，使准备形成更长承诺。 | Raw Idea / Unqualified |
| [DIR-021 守点波次工坊](DIR-021-wave-workshop/README.md) | 固定战场的波次压力与工坊整备构成局内循环。 | Raw Idea / Unqualified |
| [DIR-022 工坊谜题巡回](DIR-022-puzzle-circuit/README.md) | 以离散构句谜题、巡回目标与知识掌握组织进度。 | Raw Idea / Unqualified |
| [DIR-023 双面战利品](DIR-023-dual-reward/README.md) | 成对选择下一场挑战和指定词卡奖励。 | Raw Idea / Unqualified |
| [DIR-024 借词布阵](DIR-024-borrow-word-formation/README.md) | 暂借一张火/冰名词换本场初始元素，该实体不能再入句，战后返还。 | Raw Idea / Unqualified |
| [DIR-025 咒式委托](DIR-025-spell-commission/README.md) | 普通胜利之外提供可选环境目标及奖励。 | Raw Idea / Unqualified |
| [DIR-026 自编遗迹](DIR-026-self-built-ruins/README.md) | 战前从合法地形模板选择初态并锁定。 | Raw Idea / Unqualified |
| [DIR-027 咒理试炼](DIR-027-spell-principle-trial/README.md) | 同一配置应对多种输入，通过解释和复盘形成知识成长。 | Raw Idea / Unqualified |

## 已搁置或结束

本次未发现足以将其余方向整体判为Parked/Rejected的明确决定，因此不以日期替代选择。后续明确搁置时在原README记原因，将同一条目移到本节；保留编号与来源，不复制新目录。旧流程、重复方向快照已按历史入口收束。

## 历史怎么查

旧背景包、原始表达、合格素材、研究、问题与运行记录统一存入[整理前档案](../history/exploration-2026-09-24/README.md)。方向页按需要链接具体来源；无需先穿过历史流程目录。历史中的待办和运行授权按原轮次理解。

已有方向沿自己的来源基准；新方向按启动模式选择材料，不默认套旧包。旧背景包保持原字节，不自动升级为RC1。普通方向讨论只读所选方向必要来源；对比任务才横向阅读。独立肉鸽项目继续位于仓库exploration/new-roguelike，不导入本区。

[时间轴跨方向资料导航](../governance/time-axis-review.md)登记本次CUSTOM横向审查；不改变各方向的既定阅读范围、资格与基线。
