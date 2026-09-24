# 言咒探索区隔离规则

继承[共享探索规则](../../exploration/AGENTS.md)与根Git保护。这里不采用父目录主系统的默认读取清单。

Project ID：game-002-optimization；唯一P为yanzhou/exploration/optimization/。先读P/README、P/AGENTS及P/context/README，普通优化只按所选方向和活动包读取。用户明确指定RC1时记录固定提交和实际来源范围，不原地更新旧背景包。

本地路径继续使用idea-inbox、idea-materials、proposals、evaluations、gdd、questions、insights、simulations、prototypes、draft-changes、directions与runs。不要将其改指主系统sources/或design/。

回写需本地合格来源、提案/评估、差异以及目标game-002复审和Draft Change。主系统物理目录变为yanzhou/design等，权限仍分开；目录同属yanzhou不意味着可以互写。普通单方向任务不自动读取其他方向。独立new-roguelike留在仓库exploration/new-roguelike，禁止继承本项目背景。
