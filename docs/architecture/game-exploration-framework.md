# 独立项目与共享方法架构

2026-10-01 / layout.4，依据[WS-005](../workspace-decisions.md)。现行路径以[地图](../workspace-map.md)、[项目登记](../registry/project-registry.md)及本地AGENTS为准。

```text
game/
  yanzhou/                 默认正式游戏；自己的design、sources与探索方向
  new-roguelike/            独立游戏；自己的空白背景与按方向探索
  media-analysis-lab/      公共拆解方法、参考、证据、报告和技能试验
  docs/registry/           项目、来源、框架和适配器身份
  docs/methods/            通用研究、评估、模拟与原型契约
  game-design-workflow/templates/  唯一登记模板
  skill-iteration-workspace/       技能试验入口
  .codex/skills/            项目运行技能
```

## 项目边界

- W为选定游戏根。现行规则在design，来源与正式过程在sources，管理在governance，实现证据在development，候选在exploration/DIR目录。按需建文件，不预建多套空流程树。
- 言咒方向按READ-1默认CORE，肉鸽按READ-NR-1默认NONE；续作沿原登记来源和固定版本。共享方法、技能或链接不扩大游戏材料权限。
- 原始方向先在README保存构思、证据、Unknown和状态。Qualified、Accepted、实验完成分别记录；跨项目转化需目标资格/复审和Draft Change，不能直接覆盖规则。
- 外部游戏拆解集中在media-analysis-lab，项目内只留转化和采纳；运行技能保留标准安装位置，候选副本不自动运行或晋级。
- 普通构思不强制背景包、run-control或模拟；明确实验任务才按[运行流程](../exploration-workflow.md)和[方法契约](../methods/README.md)执行。没有因本次迁移实现自动生成器、模拟运行器或统一适配器。

## 旧方案取证

原2026-09-09架构中根exploration、重复流程树、默认背景包与迁入媒体实验室的候选不再是现行目录指令。其独有设计、失败边界及未实现提案完整保留在[迁移前版本](https://github.com/dsaj4/game_design/blob/d18ea22222c6271405927e369452d04e1c8a6fd0/docs/architecture/game-exploration-framework.md)，不据此重建旧目录或声称能力已实现。

[原建区ADR](../adr/0002-game-exploration-workspaces.md)作为历史决定保留，WS-005覆盖其物理布局，资格和证据隔离仍适用。
