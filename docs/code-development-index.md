# 代码开发进度索引

最后更新：2026-08-29

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
| Godot 统一情境 Demo | [fantacy-breakdown-godot-demo](https://github.com/Winterwhite11/fantacy-breakdown-godot-demo) | [GDD-BATTLE-003](../game-design-workflow/gdd/GDD-2026-08-29-battle-system-003-unified-glyph-action-events.md) | 统一情境最小验证原型 V0.1 | 2026-08-29，Godot 4.7.1、53 项自动检查与双状态截图 | `Verified` |
| 战斗系统 003 确定性模拟器 | 本仓库 [`combat-lab/`](../combat-lab/README.md) | [GDD-BATTLE-003](../game-design-workflow/gdd/GDD-2026-08-29-battle-system-003-unified-glyph-action-events.md) | 首期合成表与 PvE 胜率基线 | 2026-08-29，34 项测试与 30,000 局主基线 | `Verified` |
| 语义卡牌生成引擎实验 | 本仓库 [`semantic-card-engine/`](../semantic-card-engine/README.md) | [概念合成世界模型 Raw Idea](../game-design-workflow/idea-inbox/2026-08-29-semantic-composition-world-model.md) | 确定性语义推演 MVP | 2026-08-29，9 项测试、CLI 与 UTF-8 输出检查 | `Verified` |
| 成语组合模拟器 | 本仓库历史 `combat-lab/` | `GDD-BATTLE-001` | 旧战斗对照证据 | 2026-08-22 归档判断 | `Parked` |

## 语义卡牌生成引擎实验

### 项目边界

- 项目入口：[独立引擎 README](../semantic-card-engine/README.md)
- 设计来源：[概念合成世界模型原始想法](../game-design-workflow/idea-inbox/2026-08-29-semantic-composition-world-model.md)
- 当前只验证“概念 + 动作 + 核心镜片”能否编译成确定、可审计的卡牌 IR；没有接入真实 AI、Godot 或正式卡池。
- 设计来源仍是 `Raw Idea / Unqualified`。技术实现通过不代表玩法可行性、GDD 资格或正式采纳已经确认。

### 当前开发里程碑

| 里程碑 | 范围 | 状态 | 证据 | 下一步 |
| --- | --- | --- | --- | --- |
| `SEMANTIC-CARD-MVP-001` | 声明式概念目录、单调前向推演、核心镜片、预算守恒、规范化 IR 与内容哈希 | `Verified` | 9 项 pytest；`validate`/`generate` CLI；Python 编译检查 | 与 `combat-lab` 和 Godot 的效果字段统一为共享 IR |

### 已知技术边界

| 项目 | 当前实现 | 处理要求 |
| --- | --- | --- |
| AI 参与 | 当前完全不调用模型 | 先证明确定性规则层成立，再让模型只生成结构化候选 |
| 效果能力 | 只允许 `damage`、`shield`、`heal`、`cancel_intent` | 新操作码必须显式扩展执行器和测试，不接受模型任意发明字段 |
| 数值与平衡 | 概念强度直接形成临时预算 | 接入正式内容前增加价值预算扫描和批量战斗验证 |
| 客户端接入 | 输出独立 `card-ir-v0` JSON | 先解决 Godot 单效果字段与 `combat-lab` 多效果列表的差异 |
| 生成时机 | 尚未决定 | 继续确认内容生产期、核心卡诞生时或其他非战斗窗口 |

## 战斗系统 003 确定性模拟器

### 当前开发里程碑

| 里程碑 | 范围 | 状态 | 证据 | 下一步 |
| --- | --- | --- | --- | --- |
| `BATTLE003-SIM-001` | 003 回合、两类卡、永久合成、核心特有表、公开意图与 PvE 条件胜率 | `Verified` | [`v2 胜率基线`](../combat-lab/reports/2026-08-29-v2-battle003-baseline.md)，34 项自动测试 | 扫描能量、抽牌和护盾生命周期 |
| `BATTLE003-CONTEXT-001` | 确定性“卡牌 + 目标 + 状态”结算 | `Implemented` | 单一煤矿情境样例与自动测试 | 串联验证由 Godot Demo 承担；不混入当前胜率基线 |
| `BATTLE003-HUMAN-001` | 投影穷举、行动卡理解与永久消耗体验 | `Planned` | Godot Demo V0.1 与 GDD-BATTLE-003 H-001—H-005 | 招募首轮 5 名玩家并记录原始观察 |

### 实现边界与偏差

| 项目 | GDD 侧 | 当前模拟侧 | 处理要求 |
| --- | --- | --- | --- |
| 数值状态 | 能量、抽牌、血量和内容量仍为 `Unknown/Hypothesis` | 使用 4 能量、5 抽牌、30 玩家血量和首期临时卡表 | 仅作为 `v2` 条件，不反向确认 GDD |
| 遭遇范围 | 最小原型还要求 2 个事件、3 个环境对象、特殊状态敌人、分解与补充 | 当前胜率只模拟 1 名普通敌人；一个情境样例只验证确定性映射 | 完成串联前不得标记完整 GDD 原型验收 |
| 决策模型 | 玩家可在己方窗口自由交错出牌与合成 | AI 先按启发式连续合成，再枚举能量合法的字素出牌组合 | 报告为策略条件胜率，不宣称最优或真人胜率 |
| 终止条件 | 战斗以一方血量归零结束 | 另设 30 回合模拟保险，触及时记作超时 | 超时只用于暴露僵局，不写回 GDD 胜负规则 |

## Godot 统一情境 Demo

### 项目入口

- 仓库：https://github.com/Winterwhite11/fantacy-breakdown-godot-demo
- 快速开始：仓库 `README.md`
- 玩家操作与验收：仓库 `docs/USAGE.md`
- 真人测试记录：仓库 `docs/TESTING.md`
- 技术架构与扩展方式：仓库 `docs/ARCHITECTURE.md`
- 设计来源：[GDD-BATTLE-003](../game-design-workflow/gdd/GDD-2026-08-29-battle-system-003-unified-glyph-action-events.md)
- 当前实现分支：`codex/2026-08-29-gdd-battle-003-demo`
- 当前本地提交：`d3ce346 Build GDD-BATTLE-003 playable validation demo`
- 远端同步：`Blocked`；2026-08-29 当前 GitHub 凭据 `dsaj4` 向 `Winterwhite11/fantacy-breakdown-godot-demo` 推送时返回 `403`

### 当前开发里程碑

| 里程碑 | 范围 | 状态 | 证据 | 下一步 |
| --- | --- | --- | --- | --- |
| `B003-DEMO-V0.1` | 5 基础字素、3 行动卡、两张核心卡、两事件、3 环境对象、特殊状态战斗、分解与补充的完整路线 | `Verified` | 本地提交 `d3ce346`；固定首手可自动走完全流程 | 取得仓库推送权限并发布远端分支 |
| `B003-RULES-001` | 永久合成、行动复用、核心特有候选、上限替代、逐层分解、事件生命周期与回合边界 | `Verified` | Godot 4.7.1 headless，53 项规则与集成检查通过 | 将首轮真人观察与自动规则证据分开记录 |
| `B003-UI-001` | 单页统一情境、相关性层级、双产物并列投影与测试指标 | `Verified` | 1440×900 与 1280×720 真实渲染；普通态和双候选合成态无重叠 | 用 5 名目标玩家验证信息密度与投影穷举 |
| `B003-HUMAN-001` | H-001—H-005 真人体验测试 | `Planned` | 仓库 `docs/TESTING.md` 已建立记录协议 | 完成首轮 5 名目标玩家测试 |
| `B002-GRAYBOX-HISTORY` | 旧地图、地图永久合成与战斗瞬时合成 | `Parked` | GDD-BATTLE-002 历史实现仍留在仓库但不再作为启动入口 | 只作历史对照，不回写当前规则 |

### 当前实现范围

| 能力 | 实现状态 | 设计状态 | 备注 |
| --- | --- | --- | --- |
| 字素卡付费直接打出；行动卡按目标相关性免费且同回合复用 | `Verified` | `Confirmed rules / untested experience` | 自动检查覆盖相关与不相关目标、弃牌和复用 |
| 所有真实合成永久化；字素消耗，行动卡保留，产物立即入手 | `Verified` | `Confirmed rules / untested experience` | 已覆盖纯行动禁止、取消无变化、一般/特有候选与记录归属 |
| 一般配方与当前核心特有配方并列选择 | `Verified` | `Confirmed rules / scale Unknown` | 豪杰与王权使用共享材料语义，界面同时呈现两个候选 |
| 两个普通事件、三个有限环境对象和固定收益层级 | `Verified` | `Confirmed rules / readability Hypothesis` | 事件一次提交，对象处理后耗尽，奖励永久进入手牌和牌组 |
| 公开下一行动、主动护盾、特殊晶壳状态与打断更新 | `Verified` | `Confirmed rules / values Unknown` | 敌方行为为灰盒替代物，不代表最终敌人内容 |
| 一层分解与无需基础字素的补充路径 | `Verified` | `Confirmed rules / frequency Unknown` | 逐层回退保留中间祖先，不复制行动卡 |
| 旧 7×5 地图与双轨合成 | `Parked` | GDD-BATTLE-002 历史证据 | 文件仍保留，但主入口不再暴露旧规则 |

### 已知设计偏差

| 偏差 | GDD 侧 | 当前代码侧 | 处理要求 |
| --- | --- | --- | --- |
| 数值 | 能量、抽牌、血量、敌方伤害和同名上限仍为 `Unknown` | 使用 4 能量、5 抽牌、30 玩家 HP、18 敌方 HP；仅为水刃制造首测上限/替代分支 | 只作为 V0.1 条件，后续扫描相邻参数，不反向确认 GDD |
| 内容规模 | GDD 只规定最小原型下限 | 当前使用引导式固定路线和小型人工卡池 | 先完成 H-001—H-005，不据此推断正式内容量 |
| 地图与失败回滚 | GDD 将地图生成排除，并把探索失败后的永久变化列为 `Unknown` | 主入口使用统一单页；战败可重开，本轮不裁决永久变化是否应回滚 | 串联正式地图前回到整体系统 GDD 决策 |
| 投影测试 | 合成投影可无限试选，需测量穷举 | 当前记录投影次数、取消次数和决策时长，不限制试选 | 真人测试后判断是否需要调整信息或试选约束 |
| 远端交付 | 代码仓库应有可拉取分支/提交 | 本地提交完整，当前账号无目标仓库写权限 | 由仓库所有者授权或提供可写远端后推送 `d3ce346` |

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
