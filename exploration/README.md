# 玩法探索区

状态：`Skeleton Ready`。创建日期：2026-09-09。

本区已按用户确认建立最小目录、项目注册表和背景包生成规则。尚无已生成背景包、探索提案、评判结果、模拟运行或 GDD 正文。建区属于管理决定，不是玩法采纳。

| 工作区 | 用途 | 当前状态 |
| --- | --- | --- |
| [game-002 优化](game-002-optimization/README.md) | 读取锁定版本的 game-002 背景，探索优化 | Core Design Context Active；baseline-2026-09-09-001 |
| [独立肉鸽探索](new-roguelike/README.md) | 从本项目空白起点探索可行玩法 | Ready for Raw Exploration |

默认正式工作区仍是 `workspaces/game-002/`。进入探索任务时先明确 Project ID，按[项目注册表](registry/project-registry.md)路由；两个探索项目不得互相扫描或写入。

## 入口

- [探索区 Agent 规则](AGENTS.md)
- [项目注册表](registry/project-registry.md)：项目路径、背景权限、写入范围和当前背景包。
- [框架注册表](registry/framework-registry.md)：已登记候选、版本和文件摘要。
- [来源注册表](registry/source-registry.md)：共享来源与受限的 game-002 来源集合。
- [适配器注册表](registry/adapter-registry.md)：可参考的现有能力及尚未接入的部分。
- [背景包生成规则](game-002-optimization/context/pack-generation-rules.md)
- [架构与落地范围](../docs/architecture/game-exploration-framework.md)

## 共享能力

| 模块 | 本轮已建立 | 尚未实现 |
| --- | --- | --- |
| [媒体分析](shared/media-analysis/README.md) | 单文件分析流程：素材、核心循环、系统关系、设计启发与自检 | 新的媒体分析任务与可选工具接入 |
| [设计评判框架](shared/evaluation-frameworks/README.md) | v0.1 五层设计链、有效策略与可理解涌现评估 | 量化校准和机器评分器 |
| [模拟契约](shared/simulation-contracts/README.md) | 输入、运行清单、原始结果、汇总和失败状态的文件契约 | 可执行 Schema、统一运行器 |
| [原型契约](shared/prototype-contracts/README.md) | 原型范围、试玩 session、规则/体验验收和代码仓库边界 | 新可玩原型和自动验收器 |
| [GDD 标准](shared/gdd-standards/README.md) | 共享正式模板入口和资格要求 | 探索 GDD 正文 |
| [研究方法](shared/research-methods/README.md) | 问题、来源卡、证据、研究报告和假设的文件契约 | 新研究结论 |

各项目以 `idea-inbox -> 资格确认 -> idea-materials -> proposals/GDD -> evaluations` 推进。候选试验可保留 Experimental 状态，不能借模拟通过跳过资格确认或用户采纳。
