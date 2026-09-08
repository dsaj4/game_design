# ADR-0002：建立隔离的玩法探索区与双项目工作区

## Status

`Proposed`

## Context

当前仓库已经有 `workspaces/game-002/`，用于当前游戏设计与开发索引；另有共享研究、媒体分析原型、旧项目冻结实验和 GDD 模板。用户希望新增一个尚未建立的玩法探索区，承载：

- 基于 game-002 背景的优化探索；
- 与 game-002 独立的新肉鸽游戏探索；
- 外部媒体游戏分析；
- 设计评判框架，例如 `emergent_strategy_game_framework_v0.1.md`；
- 数值模拟和原型测试；
- GDD 标准与写作工作区。

现有目录中的实验代码和媒体分析产物职责不同，不能通过复制一份 GDD 或把两个旧引擎合并来解决。game-002 的正式设计还受素材资格、Proposal、Evaluation、Draft Change 和用户采纳流程保护。

## Decision

采用文件型模块化单体，在仓库根新增规划中的 `exploration/`，内部划分 `shared/`、`game-002-optimization/` 和 `new-roguelike/`。

- `workspaces/game-002/` 继续是当前游戏的正式工作区和开发索引，不迁入探索区。
- `game-002-optimization` 通过带来源、版本、Git commit 和 SHA-256 的 context pack 读取 game-002 背景；探索结果必须经过 Draft Change 才能回写。
- `new-roguelike` 从空白 context 开始，不继承 game-002 的玩法、代码、数值、测试或排期。
- `shared/` 只保存媒体分析协议、评判框架、模拟/原型契约、GDD 标准入口和研究方法；项目结论保存于各项目目录。
- 采用 Markdown + JSON + 可重复 CLI/脚本和文件注册表。暂不引入数据库、API、消息总线、微服务或前后端服务。
- 评判框架、运行契约和 GDD 模板独立版本化。`emergent-strategy-game-framework@v0.1` 登记为 `Proposed / Candidate`，不能单独证明“好玩”。
- `media-analysis-lab/`、`combat-lab/`、`semantic-card-engine/` 先通过引用或 legacy adapter 接入；不在本 ADR 中移动、删除或改写。

完整目录、数据流、状态闸门、NFR、失败模式和迁移顺序见[玩法探索区项目框架](../architecture/game-exploration-framework.md)。

## Consequences

### Positive

- game-002 正式设计和新探索不会互相污染。
- 实验结果具备输入、版本、种子、框架和代码提交的追溯关系。
- 现有媒体分析工作流、GDD 模板和旧模拟器可以渐进复用，不必一次性重构。
- 文件型方案适合当前 Git + Markdown 工作方式，可离线审阅和复盘。
- 失败的模拟、人工评审和未采纳候选能够保留，不会被误当成正式玩法。

### Negative

- 需要维护 project/framework/schema/adapter 注册表和版本号。
- context pack 会产生快照维护成本，并可能暂时落后于 game-002 最新状态。
- 不同实验器需要实现统一契约或保留适配层，初期会有少量格式转换工作。
- Markdown/JSON 文件在大规模查询和并发编辑时不如数据库方便。

### Neutral

- 玩法探索区建立后仍然不是游戏代码仓库；实现继续登记到对应代码仓库和 game-002 开发索引。
- `emergent_strategy_game_framework_v0.1.md` 当前仍可留在根目录作为用户候选输入，正式注册/迁移另需执行步骤。

## Alternatives Considered

### 直接扩充 `workspaces/game-002/`

拒绝：会把优化探索与正式设计混在同一资格链中，也无法为独立的新肉鸽项目提供清晰边界。

### 每个探索项目复制整套共享模板和工具

拒绝：复制会产生模板漂移、框架版本不明和修复不同步。共享方法应有唯一来源，项目只保存自己的实例和结果。

### 把 combat-lab 与 semantic-card-engine 合并成统一引擎

拒绝：两者来自已暂停旧项目，抽象边界、数据模型和实验目的不同。先用 legacy adapter 验证共同契约，只有重复需求形成证据后再抽象。

### 一开始采用数据库/服务化/微服务

拒绝：当前材料以文件为主、规模和协作负载未达到该复杂度；会增加运行、备份和调试成本，不能直接提高设计判断质量。

## References

- [玩法探索区项目框架](../architecture/game-exploration-framework.md)
- [当前工作区地图](../workspace-map.md)
- [涌现式策略游戏设计框架 v0.1](../../emergent_strategy_game_framework_v0.1.md)（当前根目录候选，未登记为 Accepted）
- [GDD 写作模板索引](../../game-design-workflow/templates/README.md)
- [媒体分析实验室](../../media-analysis-lab/README.md)
