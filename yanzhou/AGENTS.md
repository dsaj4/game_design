# 言咒项目操作与路径映射

继承仓库根的资格门槛、Git保护和设计/代码隔离。Project ID仍为`game-002`，新工作区W为`yanzhou/`。本文件优先解释根手册的旧职责路径；不要在旧路径继续新写设计。

## 开始阅读

主系统任务先读README.md、CONTEXT.md、design/core-design.md、design/baseline.md、governance/questions.md及相关决策。仅涉及指定子目录时按任务缩小读取范围。进入探索时先读exploration/start.md与exploration/AGENTS.md，并按用户材料模式执行；不先套用上述主系统清单，不自动读取主系统或其他方向正文。

## 职责到实际路径

| 根手册旧职责路径 | 本项目实际路径 |
| --- | --- |
| game-design-workflow/core-concept.md | design/core-concept.md为版本入口；design/core-design.md为GDD浓缩摘要 |
| game-design-workflow/decision-log.md | governance/decision-log.md |
| game-design-workflow/gdd/current/ | design/；GDD.md保留0–18章 |
| 新GDD草案 | sources/gdd-drafts/GDD-YYYY-MM-DD-short-name.md；采纳后按变更更新design/ |
| game-design-workflow/idea-inbox/ | sources/inbox/ |
| game-design-workflow/idea-materials/ | sources/materials/ |
| game-design-workflow/idea-proposals/ | sources/proposals/ |
| game-design-workflow/evaluations/ | sources/evaluations/ |
| game-design-workflow/draft-changes/ | sources/draft-changes/ |
| docs/design-decisions-needed.md／当前问题 | governance/questions.md |
| docs/code-development-index.md | development/README.md |
| docs/test-handoff.md及test-reports/ | development/test-handoff.md及reports/ |
| docs/effect-registry/ | effects/ |
| docs/governance/ | governance/ |
| 研究问题、理论与案例 | 尚无项目研究树；需要时在research/按根职责建立，不凭目录补造材料 |
| game-002优化探索 | exploration/，Project ID另为game-002-optimization |

共享设计模板仍只从[根登记清单](../game-design-workflow/templates/README.md)选择，共享规则及Git规范仍在仓库根docs/。Markdown链接按真实文件位置解析。

## 设计及证据边界

- 主系统新想法先入sources/inbox；探索新想法按exploration/AGENTS直接写所属方向，Unknown保留；资格确认主动使用grill-with-docs，先查文档，一次一个关键问题。资格不等于采纳。
- GDD使用统一模板，审查相关素材；Raw不能直接进入GDD/Proposal/Evaluation。明确采纳的范围不重复索要许可。
- 改核心或规则先Draft Change并同步决策；G002-DOC-006/007为目录决定，G002-DOC-008为核心摘要与阅读规则决定，均不新增CORE玩法决定。
- design/是现行规则；sources/保留原日期决定；history/中的AGENTS和旧“当前”仅为历史材料，不覆盖本文件。
- 参数与系统职责按governance/document-contract.md；FX仅作稳定身份与追踪，不另维护竞争规则。
- 设计Accepted、Hypothesis/NotRun、实现进度分开记录。历史TH/CAL和Demo局部结果不得外推完整RC1或真人体验。
- 代码、技术结构、构建和运行细节放对应外部代码仓库；这里只维护开发索引与设计观察。没有具体测试任务授权时不自动启动玩法测试。
- 探索候选不得直接回写；需本地资格及目标项目Draft Change。独立肉鸽和旧项目不作为言咒默认背景。
- 原有未提交修改、删除、未跟踪资产保持不变，只暂存本任务文件。所有保护文件改动同轮提交推送，报告分支和提交。
