# GDD Toolkit项目适配

game-project-1 / 2026-10-02。此安装为上游v2.3.0的**项目方法适配版**。来源与原文件哈希见../source-lock.json；根CLI、安装器和插件配置未安装。当前可执行工作流以SKILL.md与本文为准，上游参考文件只供选择性方法阅读。

## 输入与方法边界

遵守[根手册](../../../../AGENTS.md)、目标项目AGENTS及[设计流程](../../../../docs/design-workflow.md)。普通探索先选择材料与固定版本，旧方向不自动换基线。主系统当前规则按目标design定位；管理任务不自动读玩法。代码审查仅在明确代码/GDD对照任务中读取指定外部仓库及版本，不把“新会话”当作扫描代码授权。

“设计支柱”可引用已明确的核心目标和约束；没有时写Unknown或给待确认候选，不要求重造一份pillars.md或重新确认已有决定。Pairwise只检查任务涉及的已知接口；扩大到全部系统须在允许材料内并说明覆盖成本。不强迫每对系统存在交互，No interaction可作为有依据的结论；未读不等于无交互。

MDA对玩家行为与体验的推断保持Hypothesis，原模板的5–15秒循环、复杂度点数、示例参数都是方法示例，不是言咒设定。当前已采纳参数仍是对应版本的规格，不因上游说“数值均为占位”而降格或改动。

## 输出映射（不创建.design-context）

| 上游角色 | 本项目实际维护处 |
| --- | --- |
| GDD与systems | 主系统design唯一正文；新GDD草案按sources/gdd-drafts；探索按本地AGENTS |
| design-log / pillars | 既有governance/decision-log与已采纳核心目标；新建议留inbox/方向README |
| tensions / open-questions | 主系统governance/questions及已有冲突记录；方向问题留本方向 |
| brainstorming / rejected-ideas | sources/inbox或方向README；保持原话、状态与失败路径 |
| mda-analyses / design-reviews / pairwise | 优先嵌入所属方向或已有审查；正式Evaluation按资格与登记模板 |
| code-change-queue / code-audits | development索引只记范围、偏差与证据；技术细节及代码任务留外部实现仓库 |

上表按目标项目AGENTS映射，独立肉鸽不继承言咒内容。没有必要输出时不为“每轮日志”新增文件。不得创建第二套GDD、Obsidian vault、影子问题清单或自动日程。

## 原参考的使用限制

- `references/flowcharts.md`中的自动发现、扫描代码、写.design-context、按代码删改GDD等箭头在本项目不执行；仅在用户需要比较方法时读取。
- `assets/obsidian-vault-layout.md`和`references/templates/project-context.md`保留为上游参考，不用于建目录或初始化项目。
- 上游GDD-skeleton、system-design等不是本项目登记模板。正式输出只用[根模板](../../../../game-design-workflow/templates/README.md)；技术章节不复制进GDD。
- failure-modes中的绝对化建议作为审查线索，不能把“无原型”“缺乏矩阵”机械写成资格失败或自行修改已采纳设计。指出具体影响和证据。
- PASS/BLOCK是审查意见，不是Accepted/Rejected；不使用投票取代用户采纳。Raw的新玩法分析保留Raw，只有资格完整才进入正式素材及后续流程。
- 缺口按项目批量澄清规则处理。报告引用来源版本与覆盖范围，给实际冲突/边界及下一步；不得声称仅看文档就验证玩法，亦不自动运行实验。
