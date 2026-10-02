# 根目录整理记录

2026-10-01。状态：Accepted / Workspace Administration。决定WS-005。用户要求清理、重建仍有用途的技能工作台、独立肉鸽迁出并删除原exploration、保留并集中游戏拆解到media-analysis-lab。

## 处理

- 独立肉鸽移到new-roguelike，按design/sources/exploration/governance/development职责组织；原CONTEXT和运行控制信息保留，Unknown、空白背景及未执行状态不变；删除9个空流程占位，按需要创建实际目录。
- 原exploration的4份注册、共享方法和运行规则迁入docs；媒体分析/GDD转化方法迁入media-analysis-lab。旧总入口/AGENTS退役，由根与项目规则接管，不留兼容目录。
- 原assets的4份文件迁到media-analysis-lab/references/writing-examples。现有media-analysis-lab/runs、examples及全部真实输入/失败记录不改字节；既有已删除研究案例用固定Git链接索引。
- 33份技能候选/实验材料迁到media-analysis-lab/skill-iteration并保持本地忽略；根skill-iteration-workspace重建为跟踪入口。正式技能仍在.codex/skills，候选未晋级；只补充正式技能的项目存储路由。
- 缓存与误生成的%SystemDrive%目录退出工作树，7个空根流程子目录退出工作树；archive中仅清除剩余缓存的2026-08-22目录，其余独有历史保留。
- 收尾939项任务开始前已缺失的跟踪路径：research 886、combat-lab 28、semantic-card-engine 24、旧框架1。它们本轮没有再次删除磁盘正文；按本次明确清理授权提交退役，Git历史不重写。
- 模板/共享规则按目标项目AGENTS解析路径；修复移动后的链接。Inherited/Proposed不改级别，项目规则不变。

## 取证与恢复

固定基准：`d18ea22222c6271405927e369452d04e1c8a6fd0`。逐项去向、原SHA、原Git blob与退役路径见[处理清单](2026-10-01-workspace-cleanup.json)。用`git show <提交>:<原路径>`读取，权限仍按当轮材料范围，旧AGENTS与命令只作历史数据。

仓库外备份：`E:/Project/game-agent-maintenance/2026-10-01-root-layout/backup`。所有迁移源在移动前核对SHA；本地候选未发布。原未跟踪DOCX和未登记模板保留原位，不提交。批量递归删除被自动审批拦截（仅返回blocked by policy），改用非破坏性的Move-Item，将退役目录与缓存存到同级retired恢复区；项目中不留旧目录。缓存无设计证据；独有失败和原始输入没有按“重复”删除。

## 检查

提交前执行活动Markdown链接检查、移动/冻结文件SHA核对、运行技能结构校验、Git差异检查；不运行游戏实验或重新评价历史拆解质量。文档检查不证明玩法或完整拆解流程通过。

检查结果：378份活动Markdown、5120处本地链接通过；557份应保持原字节的文件SHA一致（含全部言咒文件、既有拆解运行/示例及本地候选）。正式拆解技能结构校验通过；33份本地候选继续被Git忽略，原未跟踪DOCX和模板SHA未变。32份缓存文件已逐字节保存于retired恢复区。
