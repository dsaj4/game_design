# 项目总控中心

最后更新：2026-07-01

这份文档是仓库的总控面板。它不替代 `game-design-workflow/` 和 `research/` 的正式流程，而是回答四个问题：

1. 当前项目已经确认了什么。
2. 现在最该推进什么。
3. 每类新内容应该落到哪里。
4. 作为总控 agent，如何持续保持状态、规范和工作区清晰。

## 当前项目快照

### 项目定位

这是一个游戏构思系统，不是游戏代码仓库。当前主线是一款围绕唯一核心卡构筑组合的 2D 回合制卡牌对战游戏。

### 当前正式状态

| 事项 | 状态 | 依据 |
| --- | --- | --- |
| 建立构思整理工作流 | Accepted | `game-design-workflow/decision-log.md` |
| 第一阶段先验证卡牌战斗，不引入资源系统 | Accepted | `game-design-workflow/decision-log.md` |
| 卡牌战斗系统细化 v2 | Accepted | `game-design-workflow/core-concept.md` |
| 关卡经营玩法 | 修改后再评估 | `game-design-workflow/evaluations/E-2026-05-29-level-operation.md` |
| 核心卡身份路线 | Active Research | `research/05-design-hypotheses/H-2026-05-31-core-card-identity-routes.md` |
| 媒体拆解实验室 | Prototype Lab | `media-analysis-lab/README.md` |

## 当前总控判断

### 主线

当前唯一主线仍然是：

`唯一核心卡 + 通用辅助卡 + 激活费用 + 组合规则表 + 轮流回合制对战`

### 当前优先级

1. 继续细化第一阶段战斗原型所需的核心问题，不扩展资源、地图、掉落和完整交易市场。
2. 围绕“核心卡身份如何被玩家理解并反复调整构筑”推进研究、假设和提案。
3. 把新输入稳定分流到正确目录，避免聊天结论直接污染 `core-concept.md`。
4. 将实验性工作与正式研究流保持隔离，尤其是 `media-analysis-lab/`。

### 当前活跃问题

- 核心卡在战斗中的位置和表现形式是什么。
- 核心卡是否需要生命/耐久，还是只承担组合中心作用。
- 组合槽是否进入第一阶段原型。
- 防御/干扰响应窗口如何简化。
- 核心卡标签系统如何兼顾唯一性、可读性和动态平衡。

这些问题的正式入口仍以 [current-questions.md](/E:/Project/game/research/00-index-and-roadmap/current-questions.md) 为准。

## 工作区分工图

| 区域 | 用途 | 进入条件 | 输出状态 |
| --- | --- | --- | --- |
| `game-design-workflow/idea-inbox/` | 保存零散灵感 | 想法还不完整 | Idea |
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

- Idea
- Proposal
- Evaluation
- Draft Change
- Research
- Prototype Insight
- Accepted
- Parked
- Rejected

如果信息不够，不要卡住流程，先落 `idea-inbox/` 或研究目录。

### 2. 正式内容和实验内容分开

- 会影响当前游戏主线判断的内容，走 `game-design-workflow/` 或 `research/`。
- 只是在验证分析方法、写作方法或工具链的内容，留在 `media-analysis-lab/`。
- 未经确认，不把实验区结论直接写进 `core-concept.md`。

### 3. 只维护一个主线焦点

总控 agent 应持续压缩焦点，避免同时推进多个大系统。当前只保留一个正式主线：

`第一阶段卡牌战斗原型`

以下内容目前视为非主线：

- 关卡经营外层玩法
- 共享资源地图
- 野怪/Boss
- 核心卡掉落
- 完整交易市场
- 真实 AI 生成核心卡管线

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

1. 继续把“核心卡身份路线”从假设推进为更具体的原型提案或测试记录。
2. 针对第一阶段战斗原型，优先补齐核心卡位置、组合槽、响应窗口三项问题。
3. 当有新的灵感、竞品或理论输入时，先按 [workspace-map.md](/E:/Project/game/docs/workspace-map.md) 分流，再决定是否升级状态。
