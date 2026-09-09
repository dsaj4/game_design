# game-002 优化探索

Project ID：`game-002-optimization`。状态：`Active / Core Design Context Active`。

任务是基于锁定版本的 game-002 核心设计背景探索优化。当前活动包为 `baseline-2026-09-09-001`。本次时间背包探索之前，已有两份 `Raw Idea / Unqualified` 候选（战场编译器、法术远征肉鸽），当时尚无合格素材、正式提案、评估或 GDD；前一轮匹配研究推荐先验证“公开敌意的法术远征 + 时间承诺战斗 + 词卡流派构筑”。

2026-09-09 用户另行提出[纵向时间背包与循环法术](idea-inbox/2026-09-09-timeline-backpack-spells.md)，当前讨论切换至该候选 `C-timeline-backpack-v01`；连同上述历史候选，现有三份 inbox 记录。本轮仅对照活动背景包，不读取其他探索方向正文。TB1–TB4 已独立晋级[战前编排与循环调度](idea-materials/M-2026-09-09-timeline-backpack-scheduling.md)，状态 `Qualified GDD Material / Hypothesis`：战前编排、战中自动循环、实体词卡独占、同刻覆盖和命中打断只损失本次释放且周期不变。其他状态效果与改进建议保持 `Raw Idea / Unqualified`，后续问题见[验证问题](questions/Q-20260909-timeline-backpack.md)。尚无本候选的正式提案、评估、GDD 或实际验证。上段研究推荐保留为历史上下文，不作为本轮选择依据。

本轮后续范围按 SC1 调整：用户要求先不涉及具体卡片效果。TB5 已补齐有限首次启动窗口与各法术独立循环整场的关系；TB6 已确认以编入战斗的词卡总张数限制容量，法术数量自然受其约束；TB7 已确认默认公开敌方整场攻击安排。本轮七项机制决定与一项范围调整已记录，下一轮建议用抽象法术验证周期冲突与危险刻规划。

先读[本项目约束](AGENTS.md)、[背景入口](context/README.md)和[项目注册表](../registry/project-registry.md)。本项目不能直接修改 game-002；优化候选在本地独立资格确认，再决定是否提出回写请求。

每轮从[运行控制](run-control.md)开始；它记录活动问题、预算、候选版本、停止条件和人工闸门。共享执行顺序见[Agent 运行手册](../agent-runbook.md)。

| 位置 | 用途 |
| --- | --- |
| [context](context/README.md) | 背景包来源、生成规则、当前包与适用边界 |
| [questions](questions/) | 优化问题、需要补入的背景和验证优先级 |
| [idea-inbox](idea-inbox/) | 用户原始输入与 agent 候选，Raw Idea / Unqualified |
| [idea-materials](idea-materials/) | 经本项目资格确认的素材，不能直接复制来源资格 |
| [proposals](proposals/) | 来自合格素材的优化提案 |
| [evaluations](evaluations/) | 提案评估、框架版本与证据限制 |
| [simulations](simulations/) | 候选实验计划、运行配置/结果索引，禁止虚报完成 |
| [prototypes](prototypes/) | 原型范围、外部实现仓库和验证索引 |
| [gdd](gdd/) | 使用共享正式模板的探索 GDD |
| [insights](insights/) | 外部产品分析、模拟/试玩观察，区分事实与推断 |
| [draft-changes](draft-changes/) | 拟回写 game-002 的差异及依据，不是目标已采纳记录 |

当前管理依据：[WS-004](../../docs/workspace-decisions.md)。没有玩法 Accepted 决定。背景包已激活；下一步按[Agent 运行手册](../agent-runbook.md)选择一个优化问题并开始首轮受控探索，不把背景包激活当作玩法采纳。

## 本轮研究入口

- [纵向时间背包机制相似度研究](insights/2026-09-09-timeline-backpack-similarity-review.md)：已核对 `Moment to Moment`、`Rogue Voltage`、《The Bazaar》、`Order Automatica` 及多个邻近案例。结论为 `Research / Needs Human Review`；`Moment to Moment` 对“离散时间轴上对齐敌我行动”构成高重合风险，尚未发现第二个同构案例。该研究不改变局部合格素材的 `Hypothesis` 状态。
