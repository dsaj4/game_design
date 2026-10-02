# 拆解技能迭代

当前正式安装：[game-analysis-orchestra](../../.codex/skills/game-analysis-orchestra/SKILL.md)。本区保存独立候选、历史校准与验证，不是运行安装目录。

2026-10-01迁入本地候选树`game-analysis-orchestra/`，共33份原文件逐字节保留，来自旧skill-iteration-workspace/game-analysis-orchestra-workbench。该子树继续Git忽略，不把未审查的本地候选随管理变更发布；其他机器缺少它属正常。

| 本地位置 | 用途／状态 |
| --- | --- |
| game-analysis-orchestra/game-analysis-orchestra/ | 19份技能候选文件；source-only，未晋级 |
| game-analysis-orchestra/iterations/ | 7份版本、评分与best-candidate记录 |
| game-analysis-orchestra/reports/ | 4份基线/人工校准；历史结果不改写 |
| game-analysis-orchestra/validation/ | 3份检查产物 |

已知历史结论：best candidate仍为iteration-001，明确Do not promote yet；旧基线质量与中文输出仍有未完成验证。没有证据证明近期仍在持续迭代，本次保留为可续用工作台，不声称已验证通过。

原报告中的旧绝对路径按迁移前日期解释；查本地候选时用上表新位置，运行材料仍在[既有runs](../runs/)。备份与逐文件SHA见[清理记录](../../docs/maintenance/2026-10-01-workspace-cleanup.md)。新实验记录明确输入、基准、候选、结果/失败和是否允许晋级；不重跑历史测试来改写旧结果。
