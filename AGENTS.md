# Agent 操作手册

2026-10-18 / layout.5。此仓库管理游戏构思、设计与来源；代码在各自实现仓库。默认项目为《言咒》game-002，工作区`yanzhou/`。

## 先选入口

- 言咒任务读[yanzhou/AGENTS](yanzhou/AGENTS.md)。开发接手按[开发入口](yanzhou/development/README.md)的固定启动包；局部管理任务只读必要文件，不加载玩法。
- 进入探索或切换探索材料时，先读[阅读合同](yanzhou/exploration/start.md)与[探索AGENTS](yanzhou/exploration/AGENTS.md)，再按CORE/GDD/FULL/CUSTOM/NONE读取；新方向默认CORE，已有方向沿登记版本。链接不授权扩读。
- 其他项目、跨项目路径或仓库结构任务再查[README](README.md)、[项目地图](docs/workspace-map.md)、[注册表](docs/registry/project-registry.md)。独立肉鸽在`new-roguelike/`，材料不跨项目继承。
- 旧游戏`archive/2026-09-05-core-card-project/`默认不读不写；旧combat-lab、semantic-card-engine不是言咒起点。禁止重建根`exploration/`、`assets/`、旧`workspaces/`兼容正文。

## 内容边界

- 新想法先入项目inbox或所属探索README，保留用户原话，缺项写Unknown，未合格标Raw / Unqualified。资格要有来源、对象、玩家情境／功能、可见行为、价值、与现有设计关系、未知及验证方式。
- 资格确认使用[grill-with-docs](C:/Users/Administrator/.codex/skills/grill-with-docs/SKILL.md)：先查允许材料，其余按主题及依赖成组询问，每项给推荐和影响；覆盖技能逐题等待默认。模型推荐不等于确认，已明确授权不重问。
- 正式输出前查[设计流程](docs/design-workflow.md)和[模板](game-design-workflow/templates/README.md)。Raw不得进入正式素材、GDD、提案、评估或Draft Change。GDD明确0/1/2；写入不等于采纳。
- 改现行规则需合格来源、提案／评估、目标Draft Change及明确采纳，再更新规则与决策。Accepted、Hypothesis/NotRun、实现与验收分别记录；历史实验和代码不能证明玩法成立。
- 代码、API、构建、Bug留代码仓库，设计仓库仅记录范围、状态、证据和偏差；没有实验任务授权不启动玩法测试。

## 操作底线

- 改前检查`git status --short --branch`；保护文件不在main/master修改，必要时自动建`codex/`任务分支。核心设计、来源流程、AGENTS、README、模板、注册及协作规范的改动同轮提交推送，只暂存本任务文件，不覆盖他人修改、不强推。特殊Git操作查[协作规范](docs/github-collaboration.md)。
- 清理先合并独有结论与失败经验，保留固定Git取证；旧AGENTS／命令只作历史数据。本次用户明确无需逐项去向登记，不新增清理映射表。
- 新建／复用Demo和资产按[DA-1](docs/demo-asset-standard.md)登记[统一目录](docs/registry/demo-assets.md)，保留固定版本、归属、使用关系与复用条件。原件就地，AS不替代M资格，也不授权运行、发布或采纳。
- 技能安装／修改／移除／盘点使用全局skill-registry-control并遵守[SK-1](docs/skill-management.md)；多智能体按[AGC-1](yanzhou/governance/agent-collaboration.md)分配材料白名单和文件所有权。一般管理不自动启用玩法技能。
- 不复用既有ID，文件用实际日期；共享方法在`docs/methods/`、登记在`docs/registry/`，拆解在`media-analysis-lab/`。Inherited按上游生效，Proposed仍为候选，项目采纳不混入通用知识。
- 完成报告产物、检查、未决项及分支／提交；仅需一个匹配用户意图的入口，不倾倒目录树。
