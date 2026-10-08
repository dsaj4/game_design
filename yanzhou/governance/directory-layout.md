# 目录与文件放置

Project ID：game-002。修订：system-docs.2 / 2026-10-08。规则基准仍为TL-1 + INS-1 / GDD 2.1（GDD-0）；本次更新系统文件夹与分文件职责。

| 位置 | 内容与维护责任 |
| --- | --- |
| README.md | 五个日常入口；不复制库存、进度或规则正文 |
| design/ | 唯一现行GDD、系统分册、内容、参数、验收；core-design仅浓缩 |
| design/systems/各系统/ | 六个主系统：法器、铭文、行动卡、敌人、资源、局外成长；辅槽归铭文、标记归行动卡；各目录五文件分工（README、rules、experience、design、examples） |
| design/common/ | 既有局内路线、局内经济、交互与保存的公共流程／合同；不计作额外主系统，不混入未开发的局外成长 |
| sources/ | 原始表达、合格素材与尚需追踪的P/E/D；已完成的指定记录见history |
| exploration/ | 一个DIR一个README，附件按需；DIR-001–036已退役，新方向从DIR-037继续，不擅自改历史资格 |
| effects/catalog.md | 137个稳定FX身份、当前应用与固定历史来源；旧条目全文和参数按原版本取证 |
| governance/ | 问题、决策、规范与专题；文件索引按现存文件维护，迁移旧快照按Git查 |
| development/ | 外部实现索引、交接输入和实际验证证据 |
| visual/与research/ | 表现来源、项目研究；不拥有规则采纳权 |
| history/accepted-design-records/ | 已完成指定P/E/D记录，编号及原采纳范围保留 |
| history/exploration-2026-09-24/ | 仍有独有价值的原始构思、资格、研究、运行记录与冻结背景 |
| history/README.md | 固定Git历史入口；已删除快照无需恢复到工作树即可读取 |

`workspaces/`及`exploration/game-002-optimization/`完全退役；不留跳转文件。原迁移映射与被删快照保存在清理基准提交，现用映射为cleanup-map.json。来源提交中的旧路径按原提交解释，不能全局替换历史manifest字段。

新文件用稳定职责名或日期/ID。来源与历史不复制现行规格；结束的批次只归档，不批量生成空流程树。共享模板留根game-design-workflow/templates，独立肉鸽和旧游戏留自身项目。

新增或迁移后更新文件索引，并检查活动文档本地路径与锚点。原`tools/docs.py`目前为用户既有未提交删除，不能把该命令列为现用工具；本轮临时检查使用固定Git中的校验逻辑，不恢复其工作树文件。历史冻结正文按固定提交解析，不当作现用导航。具体范围与已知历史缺口见清理报告。
