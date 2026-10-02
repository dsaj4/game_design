# 游戏拆解与媒体分析

2026-10-01统一入口。状态：Research / Prototype Lab。游戏视频、截图、文本拆解的方法、参考样例、材料包、分析产物和拆解技能试验集中在本目录；观察和研究不等于任何游戏的正式规则。

| 位置 | 用途 |
| --- | --- |
| [methods/project-analysis](methods/project-analysis.md) | 从媒体证据到玩法分析的方法 |
| [methods/gdd-transfer](methods/gdd-transfer.md) | 拆解启发进入目标项目GDD的资格边界 |
| [references/writing-examples](references/writing-examples/README.md) | 原根assets中的结构标准与两份DOCX参考样例 |
| [schemas](schemas/material-pack.schema.json)、[templates](templates/game-analysis-dossier-template.md)、[prompts](prompts/game-analysis-dossier.md) | 原型材料包与写作结构 |
| [examples](examples/core-card-duel/materialpack.json) | 保留的旧项目格式样例，仅作方法参考 |
| [runs](runs/) | 既有真实输入、截图、分析稿、检查和失败记录；路径与字节不改 |
| [skill-iteration](skill-iteration/README.md) | 拆解技能候选、人工校准与质量迭代入口 |
| [正式拆解技能](../.codex/skills/game-analysis-orchestra/SKILL.md) | 保留在Codex识别的安装位置；本目录不维护第二套运行安装 |

新拆解按`runs/<来源或任务slug>/`集中保存输入清单、证据、分析稿与检查；相同材料的修订追加版本，不复制整套根目录。第三方原始缓存和未授权资产默认不发布；现有引用和失败证据保留。外部事实、图像观察、推断和作者判断分别标注，材料不足写Unknown。

对言咒或肉鸽的设计转化留目标项目sources或方向README，并引用这里的报告版本；不把项目资格、参数或采纳决定迁到公共拆解区。已退出工作树的研究案例只在[历史案例索引](references/historical-cases.md)登记固定Git位置，不恢复旧research兼容树。

## 原型工具

现有工具与格式保留，架构见[architecture](architecture.md)，验收见[acceptance](acceptance.md)。拆解原型不自动联网、下载、运行ASR或改写游戏核心。

```powershell
python media-analysis-lab/tools/build_analysis_packet.py --pack media-analysis-lab/examples/core-card-duel/materialpack.json --out <仓库外临时输出目录> --check
```

该工具生成分析任务包、草稿和质量检查；这不等于正式技能完整流程通过。既有runs仍按原日期与原验证范围解释。
