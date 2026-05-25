# 第一批学习材料清单

日期：2026-05-14

本清单用于启动“游戏理论学习 + 卡牌战斗设计调研”。材料按学习优先级排列，不要求一次读完。每条材料都需要后续转入 `02-theory-digests/`，再视情况转成 `05-design-hypotheses/`。

## A. 通用游戏设计框架

### MDA: Mechanics, Dynamics, Aesthetics

- 来源：https://aaai.org/papers/ws04-04-001-mda-a-formal-approach-to-game-design-and-game-research/
- 类型：论文/框架
- 优先级：高
- 学习目的：建立“规则如何生成玩家体验”的分析语言。
- 与本项目关系：用于拆解核心卡、辅助卡、组合规则、费用系统分别属于什么机制，又如何产生构筑身份、爆发感、控制感和公平感。
- 建议产出：`02-theory-digests/mda-for-card-battle-design.md`

### Game Design Workshop: A Playcentric Approach

- 来源：https://www.routledge.com/Game-Design-Workshop-A-Playcentric-Approach-to-Creating-Innovative-Games/Fullerton/p/book/9781032607009
- 官方样章：https://www.routledge.com/rsc/downloads/Game_Design_Workshop_Chapter_1.pdf
- 类型：书籍
- 优先级：高
- 学习目的：学习以玩家体验、原型、测试、迭代为中心的设计流程。
- 与本项目关系：帮助我们把“核心卡组合是否好玩”转成纸面测试和数字原型，而不是停留在设定讨论。
- 建议产出：`02-theory-digests/playcentric-design-and-prototype-loop.md`
- 原文保存：商业书籍不保存非授权全文；已保存 Routledge 官方页面和官方样章到 `raw-sources/metadata-only/` 与 `raw-sources/game-design-theory/`。

### Rules of Play: Game Design Fundamentals

- 来源：https://mitpress.mit.edu/9780262240451/rules-of-play/
- 类型：书籍
- 优先级：中高
- 学习目的：学习游戏作为规则系统、互动系统和意义系统的基础语言。
- 与本项目关系：帮助判断玩家选择是否清晰、是否有可感知反馈、规则是否能形成有意义的行动。
- 建议产出：`02-theory-digests/meaningful-play-and-card-combat.md`

### Characteristics of Games

- 来源：https://mitpress.mit.edu/9780262542692/characteristics-of-games/
- 类型：书籍
- 优先级：中高
- 学习目的：从玩家数、规则、运气/技巧、奖励/努力比等特征比较游戏。
- 与本项目关系：适合做卡牌游戏横向分析，尤其是运气、隐藏信息、构筑技巧和对战公平性。
- 建议产出：`02-theory-digests/game-characteristics-for-tcg-analysis.md`

## B. 卡牌/TCG 设计方法

### Mark Rosewater: Design 101

- 来源：https://magic.wizards.com/en/news/making-magic/design-101-2003-04-21-0
- 类型：设计文章
- 优先级：高
- 学习目的：识别新手卡牌设计常见错误，尤其是过度复杂、记忆负担、焦点分散。
- 与本项目关系：唯一核心卡很容易堆太多能力，必须用这类原则控制核心卡文本复杂度。
- 建议产出：`02-theory-digests/card-design-101-complexity.md`

### Mark Rosewater: Nuts & Bolts - Design Skeleton

- 来源：https://magic.wizards.com/en/news/making-magic/nuts-bolts-design-skeleton-2010-02-15
- 类型：设计文章
- 优先级：高
- 学习目的：学习如何用设计骨架管理卡池结构，而不是随意堆卡。
- 与本项目关系：第一版 10 张核心卡、24 张辅助卡、20-30 条组合规则，需要类似“骨架”来控制功能分布。
- 建议产出：`02-theory-digests/design-skeleton-for-core-card-prototype.md`

### Mark Rosewater: Nuts & Bolts - Filling in the Design Skeleton

- 来源：https://magic.wizards.com/en/news/making-magic/nuts-bolts-filling-design-skeleton-2011-02-28
- 类型：设计文章
- 优先级：高
- 学习目的：学习从普通、受限、最难设计的位置开始填充卡池。
- 与本项目关系：可指导先设计通用辅助卡与核心标签，而不是一开始追求花哨核心卡。
- 建议产出：并入 `design-skeleton-for-core-card-prototype.md`

### Mark Rosewater: Nuts & Bolts - Iteration

- 来源：https://magic.wizards.com/en/news/making-magic/nuts-bolts-iteration-2014-03-03
- 类型：设计文章
- 优先级：高
- 学习目的：学习如何记录每张卡是否有效、是否被玩到、是否应替换。
- 与本项目关系：适合建立卡牌原型测试表，追踪核心卡、辅助卡和组合规则的表现。
- 建议产出：`06-prototype-insights/card-playtest-tracking-method.md`

### Mark Rosewater: Twenty Years, Twenty Lessons

- 来源：
  - https://magic.wizards.com/en/news/making-magic/twenty-years-twenty-lessons-part-1-2016-05-30
  - https://magic.wizards.com/en/news/making-magic/twenty-years-twenty-lessons-part-2-2016-06-06
  - https://magic.wizards.com/en/news/making-magic/twenty-years-twenty-lessons-part-3-2016-06-13
- 类型：GDC 演讲整理/设计文章
- 优先级：中高
- 学习目的：吸收长期运营卡牌游戏的设计经验。
- 与本项目关系：尤其适合思考“玩家会抵抗变化”“知道目标玩家”“限制带来创造”等问题。
- 建议产出：`02-theory-digests/twenty-lessons-for-unique-core-card-game.md`

## C. 卡牌对战关键概念

### Richard Garfield: Lost in the Shuffle - Luck and Games

- 来源：https://magic.wizards.com/en/news/feature/lost-shuffle-luck-and-games-2010-11-29
- 类型：设计文章
- 优先级：高
- 学习目的：理解卡牌游戏中的运气、技巧、随机性和玩家感知。
- 与本项目关系：唯一核心卡 + 抽牌 + 组合规则会产生大量随机性，需要判断哪些随机性让游戏更有趣，哪些会破坏公平感。
- 建议产出：`02-theory-digests/luck-skill-and-core-card-combat.md`

### Magic Level One: Card Advantage

- 来源：https://magic.wizards.com/en/news/feature/basics-card-advantage-2015-07-13
- 类型：策略概念文章
- 优先级：中高
- 学习目的：理解手牌、资源交换和长期优势。
- 与本项目关系：调度辅助卡、抽牌、弃牌、检索、限制组合都需要用卡差视角分析。
- 建议产出：`02-theory-digests/card-advantage-tempo-and-combo.md`

### Magic Level One: Tempo & Card Advantage

- 来源：https://magic.wizards.com/en/news/feature/tempo-card-advantage-delicate-balance-2014-11-17
- 类型：策略概念文章
- 优先级：中高
- 学习目的：理解节奏与资源优势的取舍。
- 与本项目关系：费用系统、组合爆发、防御响应都和节奏密切相关。
- 建议产出：并入 `card-advantage-tempo-and-combo.md`

### Hearthstone Design Lessons: Iterate Fast

- 来源：https://www.gamedeveloper.com/design/-iterate-fast-and-other-design-lessons-learned-from-i-hearthstone-i-
- 类型：开发经验文章
- 优先级：中
- 学习目的：学习数字卡牌游戏如何快速迭代、降低复杂度、强化读牌体验。
- 与本项目关系：可用于判断第一阶段原型是否应该用更短局、更少响应、更强 UI 反馈。
- 建议产出：`02-theory-digests/digital-card-game-iteration-and-readability.md`

## D. 后续待搜集方向

- 卡牌游戏响应窗口和连锁复杂度。
- 数字卡牌 UI 如何表达可用行动、费用、响应。
- 生成式卡牌/程序化卡牌设计的风险。
- TCG 动态平衡、禁限、轮换与玩家信任。
- 小丑牌、杀戮尖塔等组合构筑游戏的设计文章或开发访谈。
