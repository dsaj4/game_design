# 历史与来源取证

Project ID：game-002。文档角色：HistoricalNavigation。2026-09-30 / layout.3。

清理基准提交：`d44ecd04840b434b171d26f601bafbd87c311c92`。历史的“当前”、未决项、操作口令与资格仅按其原日期有效。现行规则读[design](../design/README.md)，不要恢复整套旧目录来开展新工作。

## 本地保留

- [已完成的P/E/D记录](accepted-design-records/README.md)：六组已采纳设计的18份过程资料；原始输入和正式素材继续在sources。
- [探索原始构思](exploration-2026-09-24/idea-inbox/)、[局部合格素材](exploration-2026-09-24/idea-materials/)、[研究](exploration-2026-09-24/insights/)、[运行记录](exploration-2026-09-24/runs/)与[旧问题](exploration-2026-09-24/questions/)。保留独有内容，不重新解释为当前待办。
- [冻结背景包](exploration-2026-09-24/context/baseline-2026-09-09-001/context-pack.md)及manifest原字节不改。历史包的相对路径按原提交解释；本地旧路径已移除时用该提交读取，不自行改写SHA或扩展材料范围。

## 已退出工作树的快照

| 资料 | 固定版本入口 |
| --- | --- |
| 整理前GDD、核心和FX全文 | [原快照](https://github.com/dsaj4/game_design/tree/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization) |
| 旧审查 | [审查记录](https://github.com/dsaj4/game_design/tree/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/audits) |
| 重复方向页与旧登记 | [方向快照](https://github.com/dsaj4/game_design/tree/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/exploration-2026-09-24/directions) |
| layout.1与layout.2迁移映射 | [第一次映射](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/governance/path-map.json) · [第二次映射](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/governance/exploration-path-map.json) |
| 时间轴详细定位、哈希和覆盖快照 | [原审查附件](https://github.com/dsaj4/game_design/tree/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/governance/time-axis-review) |
| 旧兼容目录 | [workspaces](https://github.com/dsaj4/game_design/tree/d44ecd04840b434b171d26f601bafbd87c311c92/workspaces) · [optimization](https://github.com/dsaj4/game_design/tree/d44ecd04840b434b171d26f601bafbd87c311c92/exploration/game-002-optimization) |

无需联网或恢复文件也可用`git show <提交>:<原路径>`读取；目录用`git ls-tree -r <提交> -- <目录>`查找。用户仍需授权相应历史范围，Git取证不绕过READ-1。

保留的旧探索历史正文按上述清理基准提交或文件自身更早来源解释。其本地副本字节冻结，相对链接可能指向已退役快照；沿固定提交查看即可保留完整引用语境。活动文档的链接已经改到现用位置或固定版本，不以失效本地兼容页作为入口。

[本轮处理清单](../governance/cleanup-map.json) · [清理报告](../governance/cleanup-report.md)
