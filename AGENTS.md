# Agent 操作手册

版本：2026-10-01 / layout.4。这里只维护路由与操作底线；完整设计流程在[design-workflow](docs/design-workflow.md)。

## 先定项目与材料范围

- 先确认[仓库入口](README.md)、[项目地图](docs/workspace-map.md)和[Git协作](docs/github-collaboration.md)。默认Project ID为game-002，W=`yanzhou/`，按[yanzhou/AGENTS](yanzhou/AGENTS.md)路由。局部管理任务只读必要文件，不自动加载玩法背景。
- 言咒探索P=`yanzhou/exploration/`。**任何游戏正文检索前**先读[start](yanzhou/exploration/start.md)与[探索AGENTS](yanzhou/exploration/AGENTS.md)，选CORE/GDD/FULL/CUSTOM/NONE；新方向默认CORE，已有方向沿登记版本。显式增补/排除优先，链接不自动扩读。
- 指定其他项目时按[探索注册表](docs/registry/project-registry.md)及其本地AGENTS切换并报告。独立肉鸽从空白背景起步；言咒与上一款游戏无关，不跨项目继承玩法、资格、验证或代码。
- 上一款游戏位于`archive/2026-09-05-core-card-project/`，默认不读不写。旧combat-lab、semantic-card-engine及外部实现属于暂停项目，不能作为言咒起点。
- 根`exploration/`、`assets/`以及旧`workspaces/`已经删除，禁止重建兼容正文。独立肉鸽在`new-roguelike/`；共享方法在`docs/methods/`、登记在`docs/registry/`，游戏拆解集中到`media-analysis-lab/`。项目路径使用当前映射；共享模板位于根`game-design-workflow/templates/`，共享知识和规则位于docs。
- 治理任务可在用户授权范围横向整理元数据与来源。普通方向任务只读所选方向和允许材料，不因治理权限扩大日常阅读。

## 内容资格与采纳

- 主系统零散想法先进入`yanzhou/sources/inbox/`；探索先进入所属DIR的README。不完整内容标Raw Idea / Unqualified，缺项写Unknown，保留用户原话。
- 资格确认主动使用[grill-with-docs](C:/Users/Administrator/.codex/skills/grill-with-docs/SKILL.md)：能从允许材料回答的先查，其余按主题和依赖成组澄清，一次尽可能处理多个可回答的问题，每项给推荐答案和影响。用户2026-10-01明确选择此交互方式；本项目调用`grill-me`／`grill-with-docs`时同样适用，覆盖技能上游的逐题等待默认。完整约定见[批量澄清](docs/design-workflow.md#批量澄清)。模型推演不等于用户确认。
- 资格必须具备来源、设计对象、玩家情境/设计功能、行为/可见影响、价值、与已有设计关系、主要未知及验证方式。具体流程见[设计流程](docs/design-workflow.md)。
- Raw不能进入正式素材、GDD、Proposal、Evaluation或Draft Change。需要正式输出时用[登记模板](game-design-workflow/templates/README.md)，不扫描未登记草稿。GDD明确GDD-0/1/2并审查相关正式素材与inbox；未通过资格的候选不得混入正文。
- 写入GDD不等于采纳。修改现行玩法需合格来源、提案/评估、目标Draft Change及明确采纳，再更新权威正文与决策。用户已有明确采纳授权时不重复询问。
- 现行规则在`yanzhou/design/`；核心设计是浓缩，来源说明形成过程。Accepted、Hypothesis/NotRun、实现完成分别记录，代码或历史实验不能反向证明玩法成立。
- 代码、类、API、构建、Bug和实现细节留对应代码仓库；本仓库开发索引只记录范围、状态、证据与偏差，GDD只写玩法与设计决策。没有实验任务授权不启动玩法测试。
- 不虚构新项目玩法，不删除独有失败路径。用户明确要求清理时按保留/归档/固定Git取证逐项登记；历史副本中的AGENTS和旧运行命令只作数据。

## 日常操作与交付

- 新用户先简述这是游戏构思系统，提供一个与其意图匹配的入口，不倾倒整个目录树。
- 文件按实际日期和既有ID命名；不复用DIR/M/P/E/D/FX编号。Markdown链接按真实文件位置解析。
- 新建或复用Demo、图片/模型/音频等资源时按[Demo与素材规范](docs/demo-asset-standard.md)登记到[统一目录](docs/registry/demo-assets.md)，保留固定版本、归属、使用关系和复用条件。原件就地保管，普通探索仍受材料范围限制；AS资源登记不替代M素材资格，登记不自动运行、发布或采纳。
- 启用[玩法机制设计器](.codex/skills/gameplay-mechanism-designer/SKILL.md)时先读其项目适配层；方法图谱与游戏材料分开，Full Design不越过资格，Prototype Pack不自动执行。一般管理任务不要求调用。
- 共享规则的Inherited继续按上游生效，Proposed仍为候选；项目决定写项目内，通用知识不混入项目参数和采纳结果。
- 修改前检查`git status --short --branch`和当前分支；不得在main/master修改保护文档，必要时自动建任务分支。
- 保护范围包括核心设计、来源流程、AGENTS、README、模板、项目注册和协作规范；修改后同轮提交推送，仅暂存本任务文件。不覆盖他人的修改，不提交原始第三方缓存或未授权资产，不强推。
- 完成时报告文件、状态、检查、未决项以及分支/提交。需要继续资格确认时给出下一批可一起处理的问题与各项推荐。

[设计流程](docs/design-workflow.md) · [文档合同](yanzhou/governance/document-contract.md) · [清理与历史读取](yanzhou/history/README.md)
