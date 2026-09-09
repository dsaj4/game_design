# game-002 优化探索

Project ID：`game-002-optimization`。状态：`Active / Skeleton Ready / Awaiting Context Pack`。

任务是基于锁定版本的 game-002 背景探索优化。当前仅建立目录和规则，尚未生成背景包，也没有新玩法、提案、评估、实验或 GDD。

先读[本项目约束](AGENTS.md)、[背景入口](context/README.md)和[项目注册表](../registry/project-registry.md)。本项目不能直接修改 game-002；优化候选在本地独立资格确认，再决定是否提出回写请求。

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

当前管理依据：[WS-004](../../docs/workspace-decisions.md)。没有玩法 Accepted 决定。下一步按[生成规则](context/pack-generation-rules.md)生成首个背景包，然后选一个优化问题；不把建区当作背景导入已完成。
