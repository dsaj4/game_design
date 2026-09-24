# 玩法探索区操作规则

继承根 AGENTS.md 的 Git 保护、素材资格、来源追踪和设计/代码隔离。管理决定见[WS-004](../docs/workspace-decisions.md)。本文件补充探索区路径，不修改 game-002 的玩法协议。

## 路由与读取范围

1. 先读本区 README、[项目注册表](registry/project-registry.md)，确定唯一 Project ID 和项目根 P。
2. 言咒优化先读P/AGENTS.md及[启动规范](../yanzhou/exploration/start.md)，按模式选择游戏材料；不自动读context。其他项目按其本地规则读P/README、P/AGENTS及背景入口。没有明确项目的请求沿根规则路由，不能自动加载两个探索项目。
3. 言咒新方向支持CORE/GDD/FULL/CUSTOM/NONE；未指定时CORE，已有方向沿其登记来源。仅明确生成包的任务才用历史生成流程；来源链接不构成递归检索许可。
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

## 2026-09-23方向目录约定

方向与历史记录的物理路径按各项目本地AGENTS映射。言咒现用DIR方向文件夹及READ-1阅读合同，旧directions和runs已归档；不恢复旧流程树。索引只作导航、关系与资格映射，不是正式素材或Proposal。用户指定当轮GDD时登记提交及明确范围，不能原地更新旧包。单方向只使用所选来源，跨方向比较须有相应任务范围；主系统玩法回写要求保持。

## layout.1物理路径

game-002-optimization的P已迁到yanzhou/exploration/，读取限制、资格和目标回写要求全部保持；本探索总目录仍管理独立new-roguelike和共享方法。先按注册表选择P，不因旧兼容入口自动使用过时目录。


## layout.2：言咒探索存储例外

game-002-optimization的P为yanzhou/exploration/。用户已要求按方向保存必要构思，因此上文流程路径、P/directions与runs映射不适用于该项目；以[项目AGENTS](../yanzhou/exploration/AGENTS.md)为准。构思、问题和状态直接留在DIR文件夹README，正式材料确有需要时同文件夹存放。旧背景与研究在yanzhou/history/exploration-2026-09-24，不恢复旧流程树。new-roguelike继续按其本地规则和原有路径执行。
