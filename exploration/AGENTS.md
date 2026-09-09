# 玩法探索区操作规则

继承根 AGENTS.md 的 Git 保护、素材资格、来源追踪和设计/代码隔离。管理决定见[WS-004](../docs/workspace-decisions.md)。本文件补充探索区路径，不修改 game-002 的玩法协议。

## 路由与读取范围

1. 先读本区 README、[项目注册表](registry/project-registry.md)，确定唯一 Project ID 和项目根 P。
2. 读 P/README.md、P/AGENTS.md 和 P/context/README.md。没有明确项目的请求沿根规则路由，不能自动加载两个探索项目。
3. 普通优化任务只使用已激活的 context pack；生成背景包的任务才按明确来源清单读取 game-002 的指定提交。来源链接不构成递归检索许可。
4. 独立肉鸽探索不能读取 game-002、优化项目背景包、旧项目归档或旧引擎的玩法数据来填补 Unknown。
5. 共享框架中的“本项目”“最终目标”和示例是框架作者的上下文，不自动成为任何游戏的设计决定。

## 路径映射

根流程中的游戏工作区路径，在本区按下表解释。不要为匹配根目录名而另建重复流程树。

| 根流程职责 | 探索项目内路径 |
| --- | --- |
| 原始输入 / idea-inbox | P/idea-inbox/ |
| 合格素材 / idea-materials | P/idea-materials/ |
| 提案 / idea-proposals | P/proposals/ |
| 评估 / evaluations | P/evaluations/ |
| GDD | P/gdd/ |
| 当前问题 | P/questions/ |
| 研究案例、来源判断、原型观察 | P/insights/，由项目 README 索引 |
| 模拟配置、结果索引 | P/simulations/ |
| 原型范围、外部实现与验证索引 | P/prototypes/ |
| 背景 / CONTEXT | P/context/README.md 与登记背景包 |
| 核心构思、玩法采纳记录 | 尚未建立；项目 README 记录当前阶段，不能虚构 Accepted 核心 |
| 回写 game-002 的拟修改 | 仅优化项目 P/draft-changes/ |

## 探索与资格

- Agent 可在已指定项目内记录来源、提出候选问题和原始想法；自行补出的设计必须标为 `Agent Proposal / Raw Idea / Unqualified`。
- 实验必须有明确候选、问题、范围和证据边界。候选测试记录保留 `Experimental / Unqualified`，不能作为已通过资格闸门的 Proposal、Evaluation 或 GDD 正文。需要正式评估时先补资格。
- 正式晋级仍使用 grill-with-docs 及根登记模板；已有来源能回答的先查文档，不能把猜测或分数当用户确认。
- game-002 的材料在背景包中保留来源资格和 Hypothesis 状态，不能直接算作优化项目已晋级的本地素材。优化差异须独立记录并确认关系。
- GDD 必须审查本项目 idea-materials 和相关 inbox；代码结构、构建及测试详情不进入 GDD。代码实现位于明确登记的外部仓库，P/prototypes 只作索引。
- 模拟不能证明真人可理解或好玩；结果可为未测、失败、待人工评议，禁止为了得分补造证据。

## 回写与登记

- 项目注册表是项目 ID、根路径、读取/写入边界的唯一登记入口。项目 README 提供导航，不另设冲突的注册表。
- 来源、框架和适配器按注册表追加版本；已生成背景包和历史运行不原地更新。
- 本项目只能写入 P。修改共享治理必须是明确的管理任务；优化结果回写 game-002 需来源、评估、目标项目复审和 Draft Change，不能直接覆盖其核心或决策记录。
- 新肉鸽项目不提供通往 game-002 的默认回写入口。旧实验仅是可评估的历史方法，不是默认代码依赖。
- 任何核心保护文档和注册表变更都按根 GitHub 规范提交推送；只暂存本任务文件，不处理无关未跟踪内容。
