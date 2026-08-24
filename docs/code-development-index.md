# 代码开发进度索引

最后更新：2026-08-24

本文档是代码开发状态的唯一仓库级入口。它记录“哪些设计已经实现、实现在哪里、验证到什么程度、与 GDD 有什么偏差”，但不定义玩法规则，也不替代各代码仓库内的 README、架构文档、Issue 或测试报告。

## ADR-DEV-001：隔离 GDD 与代码开发记录

| 字段 | 内容 |
| --- | --- |
| 状态 | `Accepted` |
| 日期 | 2026-08-24 |
| 决策来源 | 用户明确要求 |
| 被替代做法 | 在 `game-design-workflow/gdd/` 中维护客户端代码设计 GDD |

### 背景

`GDD-CLIENT-001` 同时记录了玩家规则、Godot 工程结构、脚本路径、数据契约和实现完成度，导致两种事实混在一起：

- GDD 应回答玩家做什么、规则如何运作、为什么采用这项设计，以及哪些设计仍待验证。
- 开发记录应回答代码在哪里、当前实现了什么、如何验证、阻塞项是什么，以及实现是否偏离 GDD。

如果实现状态反向成为 GDD 的设计依据，临时灰盒行为可能被误认成正式玩法决定。

### 决策

1. `game-design-workflow/gdd/` 只保存核心玩法设计与设计决策。
2. GDD 不记录引擎、类、模块、脚本路径、编程数据结构、API、序列化格式、构建命令、CI 或代码完成度。
3. 代码仓库、开发里程碑、实现状态、验证证据与设计偏差统一由本索引记录。
4. 详细技术架构和操作说明保留在对应代码仓库；本索引只建立可追踪链接。
5. 代码实现不能自动把 GDD 的 `Hypothesis` 提升为 `Confirmed`。设计状态仍通过 Proposal、Evaluation、Draft Change 和 Decision Log 决定。

### 取舍与后果

- 优点：设计事实和实现事实不再互相污染；程序可以明确看到实现偏差；GDD 更容易审阅。
- 代价：玩法规则变化和代码进度变化需要分别更新，并通过设计 ID 建立追踪。
- 风险：两边可能不同步。缓解方式是每次开发状态更新都填写“关联 GDD”和“偏差/阻塞”。
- 未采用：继续扩展“代码设计 GDD”。原因是它会让 GDD 同时承担设计合同、技术设计和项目管理三种职责。

## 文档边界

| 内容 | 记录位置 |
| --- | --- |
| 玩家处境、动作、反馈、取舍与体验目标 | `game-design-workflow/gdd/` |
| 胜负、资源、合成、抽牌、时序等玩法规则 | `game-design-workflow/gdd/` |
| 玩法假设、备选方案、采用理由与复审条件 | GDD 与 `game-design-workflow/decision-log.md` |
| 原型观察对设计判断的影响 | `research/06-prototype-insights/` |
| 代码仓库、引擎、模块、文件与数据格式 | 对应代码仓库文档；本索引只链接 |
| 已实现、开发中、阻塞、测试状态 | 本索引 |
| 构建、安装、运行、CI 和发布说明 | 对应代码仓库 |

## 状态定义

| 状态 | 含义 |
| --- | --- |
| `Planned` | 已有明确设计来源，尚未开始实现 |
| `In Progress` | 已开始实现，尚未达到验收条件 |
| `Implemented` | 代码路径已存在，可进入验证 |
| `Verified` | 已按列出的证据完成检查 |
| `Blocked` | 存在明确阻塞，不能继续 |
| `Parked` | 当前不推进，但保留实现和历史 |

`Implemented` 不等于玩法设计 `Confirmed`；前者描述代码事实，后者描述设计证据。

## 开发项目索引

| 项目 | 仓库 | 关联设计 | 当前阶段 | 最近验证 | 状态 |
| --- | --- | --- | --- | --- | --- |
| Godot 灰盒客户端 | [fantacy-breakdown-godot-demo](https://github.com/Winterwhite11/fantacy-breakdown-godot-demo) | [GDD-BATTLE-002](../game-design-workflow/gdd/GDD-2026-08-22-glyph-synthesis-combat-system.md) | 地图与字素战斗灰盒 | 2026-08-24 文档与仓库检查 | `Implemented` |
| 成语组合模拟器 | 本仓库历史 `combat-lab/` | `GDD-BATTLE-001` | 旧战斗对照证据 | 2026-08-22 归档判断 | `Parked` |

## Godot 灰盒客户端

### 项目入口

- 仓库：https://github.com/Winterwhite11/fantacy-breakdown-godot-demo
- 快速开始：仓库 `README.md`
- 玩家操作与验收：仓库 `docs/USAGE.md`
- 技术架构与扩展方式：仓库 `docs/ARCHITECTURE.md`
- 设计来源：[GDD-BATTLE-002](../game-design-workflow/gdd/GDD-2026-08-22-glyph-synthesis-combat-system.md)

### 当前开发里程碑

| 里程碑 | 范围 | 状态 | 证据 | 下一步 |
| --- | --- | --- | --- | --- |
| `GRAYBOX-CLIENT-001` | 地图进入战斗并返回的可运行闭环 | `Implemented` | Godot 仓库与使用说明 | 按验收清单完成实际试玩记录 |
| `BATTLE-SYNTH-001` | 首测基础字、字词打出与两材料合成 | `Implemented` | `data/cards.json`、战斗场景 | 对齐 GDD 费用与合成生命周期 |
| `MAP-SYNTH-001` | 地图永久 2→1 合成 | `Implemented` | 使用说明中的永久合成流程 | 验证长期构筑价值 |
| `BATTLE-PILE-001` | 回合开始洗牌、当回合不即时洗回 | `Implemented` | `PileController` 与使用说明 | 记录至少一轮人工验收证据 |
| `CORE-GLYPH-001` | 本源字解释器与铭文耐性 | `Planned` | GDD-BATTLE-002 | 先确认玩法规则与首测模板 |
| `SYNERGY-201-208` | 处理层与元素协同 | `Planned` | card-table 与 GDD-BATTLE-002 | 确定首批协同范围 |

### 当前实现范围

| 能力 | 实现状态 | 设计状态 | 备注 |
| --- | --- | --- | --- |
| 7×5 网格、单格移动、墙体与战斗格 | `Implemented` | 灰盒范围 | 地图尺寸和输入方式不是正式核心规则 |
| 战斗胜利清除格子、失败重开 | `Implemented` | `Hypothesis` | 需由地图 GDD 决定长期结果 |
| 基础字直接打出 | `Implemented` | `Hypothesis` | 首测子集 |
| 蒸汽、酸、水刃、土墙、高压蒸汽 | `Implemented` | `Hypothesis` | 当前只支持两材料逐步合成 |
| 地图永久合成与战斗瞬时合成 | `Implemented` | `Hypothesis` | 玩法规则已迁入 GDD-BATTLE-002，尚未正式采纳 |
| 回合开始才洗弃牌堆 | `Implemented` | `Hypothesis` | 玩法规则已迁入 GDD-BATTLE-002 |
| 简单 AI 攻防轮换 | `Implemented` | 灰盒替代物 | 不代表最终敌人设计 |
| 本源字解释器 | `Planned` | `Hypothesis` | 未实现 |
| 铭文耐性强制校验 | `Planned` | `Hypothesis` | 未实现 |
| 处理协同 201–208 | `Planned` | `Hypothesis` | 未实现 |

### 已知设计偏差

| 偏差 | GDD 侧 | 当前代码侧 | 处理要求 |
| --- | --- | --- | --- |
| 回合能量 | 共享 4 点为 `Hypothesis` | 当前灰盒使用 3 点 | 不以代码反改 GDD；下一轮原型对比后决策 |
| 合成层数 | GDD 允许更高层字词并受耐性限制 | 当前仅两材料逐步合成 | 先验证两步合成可读性，再决定三材料 UI |
| 本源字 | GDD 将其视为身份解释规则 | 当前未实现 | 进入下一里程碑前先完成设计确认 |
| 协同表 | GDD 定义 201–208 方向 | 当前只做首测字词结果 | 选择最小协同子集后再排期 |

## 更新协议

每次代码相关工作完成后，只更新本索引中受影响的项目，并至少记录：

1. 代码仓库与提交、PR 或 Release。
2. 关联的 GDD、规则 ID 或设计决策。
3. 状态从什么变成什么。
4. 使用了什么验证证据。
5. 是否出现与 GDD 不一致的行为。
6. 下一步和明确阻塞项。

禁止事项：

- 不把类名、函数名、脚本路径或引擎架构写回 GDD。
- 不因为代码已经实现，就把玩法假设标记为 `Confirmed` 或写入 `core-concept.md`。
- 不在本索引复制完整技术说明；详细内容留在代码仓库。
- 不静默接受实现偏差；偏差必须同时标明 GDD 侧与代码侧状态。

## 迁移记录

| 日期 | 变更 | 结果 |
| --- | --- | --- |
| 2026-08-24 | PR #3 新增 `GDD-CLIENT-001`，记录 Godot 灰盒代码设计 | 后续判定为职责混合 |
| 2026-08-24 | 将 `GDD-CLIENT-001` 迁出 GDD，建立本索引 | GDD 与代码开发进度正式隔离 |
