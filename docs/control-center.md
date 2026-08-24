# 项目总控中心

最后更新：2026-08-24

这份文档是仓库的总控面板。它不替代 `game-design-workflow/` 和 `research/` 的正式流程，而是回答四个问题：

1. 当前项目已经确认了什么。
2. 现在最该推进什么。
3. 每类新内容应该落到哪里。
4. 作为总控 agent，如何持续保持状态、规范和工作区清晰。

## 当前项目快照

### 项目定位

这是一个游戏构思系统，不是游戏代码仓库。当前主线是一款围绕唯一核心卡展开构筑、探索、资源竞争、交易与回合制卡牌对战的 2D 系统型游戏。

### 当前正式状态

| 事项 | 状态 | 依据 |
| --- | --- | --- |
| 建立构思整理工作流 | Accepted | `game-design-workflow/decision-log.md` |
| “第一阶段先验证卡牌战斗，不引入资源系统” | Superseded | `game-design-workflow/decision-log.md` |
| 卡牌战斗系统细化 v2 | Accepted | `game-design-workflow/core-concept.md` |
| 整体系统构思优先，战斗改为关键解决层 | Accepted | `game-design-workflow/decision-log.md` |
| 关卡经营玩法 | 修改后再评估 | `game-design-workflow/evaluations/E-2026-05-29-level-operation.md` |
| 核心卡身份路线 | Active Research | `research/05-design-hypotheses/H-2026-05-31-core-card-identity-routes.md` |
| 字素合成战斗 GDD-002 | Evaluation（战斗机制主线） | `game-design-workflow/gdd/GDD-2026-08-22-glyph-synthesis-combat-system.md` |
| Godot 灰盒客户端 GDD-CLIENT-001 | Evaluation（代码设计合同） | `game-design-workflow/gdd/GDD-2026-08-24-godot-greybox-client.md`；实现：`../godot-demo/` |
| 成语组合战斗 GDD-001 | Parked（实现线） | `game-design-workflow/gdd/GDD-2026-08-21-card-battle-system.md` |
| 媒体拆解实验室 | Prototype Lab | `media-analysis-lab/README.md` |

## 当前总控判断

### 主线

当前唯一主线仍然是：

`唯一核心卡 + 通用辅助卡 + 激活费用 + 组合规则表 + 共享世界资源循环 + 回合制对战`

### 当前优先级

1. 先把整体系统闭环说清：战斗、资源、地图、掉落、交易和世界目标如何互相驱动。
2. 明确战斗在整体系统中的职责，避免它既被削弱成附属层，又重新吞掉所有优先级。
3. 围绕“核心卡如何同时成为战斗中心、世界身份和长期资产”推进研究、提案与评估。
4. 把新输入稳定分流到正确目录，避免聊天结论直接污染 `core-concept.md`；尤其不能让未达标想法绕过素材资格闸门。

### 当前活跃问题

- 共享世界中的主循环是什么，它如何稳定导向战斗、资源与成长判断。
- 资源系统最少需要几类资源，它们分别服务哪一段长期循环。
- 核心卡如何通过世界系统保持稀缺、身份感与长期目标。
- 战斗在整体系统中承担哪些不可替代的解决职责。
- 世界观框架应如何解释唯一核心卡、资源争夺与共享世界。

这些问题的正式入口仍以 [current-questions.md](/E:/Project/game/research/00-index-and-roadmap/current-questions.md) 为准。

## 工作区分工图

| 区域 | 用途 | 进入条件 | 输出状态 |
| --- | --- | --- | --- |
| `game-design-workflow/idea-inbox/` | 原始想法隔离区 | 想法还不完整 | Raw Idea / Unqualified |
| `game-design-workflow/idea-materials/` | 正式想法素材库 | 已通过 `grill-with-docs` 资格确认 | Qualified GDD Material |
| `game-design-workflow/gdd/` | 统一模板形成的设计合同 | 已选择 GDD-0/1/2 并完成素材审查 | GDD |
| `game-design-workflow/idea-proposals/` | 整理玩法假设 | 已能说清玩家行为和乐趣 | Proposal |
| `game-design-workflow/evaluations/` | 判断值不值得推进 | Proposal 已成形 | Evaluation |
| `game-design-workflow/draft-changes/` | 准备改正式设定 | 已有提案和评估支撑 | Draft Change |
| `game-design-workflow/core-concept.md` | 正式核心构思 | 用户明确采纳 | Accepted |
| `research/01-04/` | 理论、案例、比较 | 外部知识输入 | Research |
| `research/05-design-hypotheses/` | 可验证假设 | 研究结论已能指导设计 | Research Hypothesis |
| `research/06-prototype-insights/` | 原型/纸面验证观察 | 已有测试或推演 | Prototype Insight |
| `media-analysis-lab/` | 视频/图文拆解实验区 | 验证新分析工作流 | Prototype Lab |
| `archive/` | 历史快照 | 需要保留上下文 | Archived |

## 总控 agent 操作规则

### 1. 先判断状态，再决定写哪里

每次接到输入时，优先判定它属于：

- Raw Idea / Unqualified
- Qualified GDD Material
- GDD
- Proposal
- Evaluation
- Draft Change
- Research
- Prototype Insight
- Accepted
- Parked
- Rejected

如果信息不够，只能落 `idea-inbox/` 并标记 `Raw Idea / Unqualified`；使用 [`grill-with-docs`](C:/Users/Administrator/.codex/skills/grill-with-docs/SKILL.md) 逐项澄清，通过后才可进入 `idea-materials/`、GDD 或 Proposal。

### 2. 正式内容和实验内容分开

- 会影响当前游戏主线判断的内容，走 `game-design-workflow/` 或 `research/`。
- 只是在验证分析方法、写作方法或工具链的内容，留在 `media-analysis-lab/`。
- 未经确认，不把实验区结论直接写进 `core-concept.md`。

### 3. 只维护一个主线焦点

总控 agent 应持续压缩焦点，避免同时推进多个大系统。当前只保留一个正式主线：

`唯一核心卡驱动的整体系统构思`

以下内容当前仍不直接进入正式主线：

- 详细数值平衡表
- 完整自动化动态平衡后台
- 真实 AI 生成核心卡的最终技术管线
- 完整剧情脚本或海量设定文本

### 4. 更新顺序固定

当一轮工作产生有效沉淀时，优先更新：

1. 对应流程文档本身。
2. 若影响正式方向，再更新 `decision-log.md` 或 `core-concept.md`。
3. 若影响项目全局判断，再回看这份总控文档是否需要同步。

## 维护节奏

### 每轮结束至少回答

- 本轮新增或更新了什么。
- 当前内容状态是什么。
- 它是否影响正式主线。
- 下一步最自然动作是什么。

### 每周或每个阶段建议回看

- `research/00-index-and-roadmap/current-questions.md`
- `research/00-index-and-roadmap/research-log.md`
- `game-design-workflow/decision-log.md`
- `docs/workspace-map.md`

如果发现“目录已经存在，但没人知道该往哪写”，优先补说明文档，而不是新增更多目录。

## 工作区清洁规则

- 新文档优先进入现有目录，不随手在根目录散落。
- 新流程先写明边界，再决定是否升级为正式目录。
- 模板、流程、正式结论、实验产物不要混放。
- `archive/` 只保留快照，不作为当前编辑入口。
- 如果一个目录持续承担独立职责，应至少有一个 `README.md` 说明用途与边界。

## 当前下一步建议

1. 先补一份“整体系统闭环提案”，把地图、资源、战斗、掉落、交易和世界目标串成一张因果图。
2. 把当前问题清单从战斗微观问题切到系统级问题，再决定哪个子系统先进入 Proposal。
3. 当有新的灵感、竞品或理论输入时，先按 [workspace-map.md](/E:/Project/game/docs/workspace-map.md) 分流，再决定是否升级状态。
