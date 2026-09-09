# game-002 优化探索

Project ID：`game-002-optimization`。状态：`Active / Core Design Context Active`。

任务是基于锁定版本的 game-002 核心设计背景探索优化。当前活动包为 `baseline-2026-09-09-001`；已有一份 `Raw Idea / Unqualified` 施法优化候选，尚无合格素材、正式提案、评估或 GDD。

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
