# 目录与文件放置

Project ID：game-002。修订：progressive-reading.1 / 2026-10-23。规则版本见baseline；本次仅调整读取、分文件与派生交接职责。

| 位置 | 内容与维护责任 |
| --- | --- |
| README.md | 五个日常入口；不复制库存、进度或规则正文 |
| design/ | 唯一核心GDD、按需细则、内容、参数、验收；core-design仅留旧引用导航 |
| design/systems/各系统/ | 六个主系统：法器、铭文、行动卡、敌人、资源、局外成长；辅槽归铭文、标记归行动卡；按规则、理由、体验、示例实际内容拆分；局外成长只保留README |
| design/common/ | 既有局内路线、局内经济、交互与保存的公共流程／合同；不计作额外主系统，不混入未开发的局外成长 |
| sources/ | 意图摘要、合格素材与尚需追踪的P/E/D；已完成的指定记录见history |
| exploration/ | 一个DIR一个README，附件按需；DIR-001–036已退役，后续编号按探索入口继续分配，不擅自改历史资格 |
| effects/catalog.md | 137个稳定FX身份、当前应用与固定历史来源；旧条目全文和参数按原版本取证 |
| governance/ | 问题、决策、规范与专题；文件索引按现存文件维护，迁移旧快照按Git查 |
| development/ | 外部实现索引、派生任务包、场景审阅规范和证据入口 |
| visual/与research/ | 表现来源、项目研究；不拥有规则采纳权 |
| history/accepted-design-records/ | 已完成指定P/E/D记录，编号及原采纳范围保留 |
| history/exploration-2026-09-24/ | 仍有独有价值的原始构思、资格、研究、运行记录与冻结背景 |
| history/README.md | 固定Git历史入口；已删除快照无需恢复到工作树即可读取 |

`workspaces/`及`exploration/game-002-optimization/`完全退役；不留跳转文件。原迁移映射与被删快照保存在清理基准提交，现用映射为cleanup-map.json。来源提交中的旧路径按原提交解释，不能全局替换历史manifest字段。

新文件用稳定职责名或日期/ID。来源与历史不复制现行规格；结束的批次只归档，不批量生成空流程树。共享模板留根game-design-workflow/templates，独立肉鸽和旧游戏留自身项目。

新增或迁移后核对文件索引的职责入口，并检查活动文档本地路径与锚点。原`tools/docs.py`已于2026-10-18按用户要求提交退役，不能把该命令列为现用工具；原校验逻辑可从固定Git版本取证。历史冻结正文按固定提交解析，不当作现用导航。删除清单及恢复版本见[清理报告](cleanup-report.md#2026-10-18未提交内容分批整理)。
