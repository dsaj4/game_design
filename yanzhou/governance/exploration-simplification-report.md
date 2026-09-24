# 探索结构简化记录

日期：2026-09-24。layout.2。管理决定G002-DOC-007；RC1 / doc.1不变。

## 结果

活动exploration从153份文件、optimization包装层及15类子目录，收束为27个方向文件夹和README、comparison、AGENTS三份入口文件，共30份Markdown。每个方向页直接包含来源中的实际构思，不再只是索引。时间背包和音乐另保留已有局部合格范围；其余不晋级。基线适配与主系统吸收并入comparison，避免另增一套导航。

151份旧optimization记录移到history/exploration-2026-09-24，保留研究、问题、运行、素材与固定包。旧AGENTS改为历史边界声明，旧入口增加档案标识；非冻结Markdown的相对链接按新位置重定位。原始字节可按[path map](exploration-path-map.json)内source_commit查询；固定背景包与JSON机器证据不改字节。归档不恢复旧脚本、运行预算或待办权限。

新增思路只需一个方向README，图片与必要支撑按需添加。正式资格与回写按项目AGENTS，日常构思不要求先建素材/提案/评估等流程文件。

## 验证

- 27/27方向都有具体构思、原Candidate ID、原资格状态和未决项；当前区共30份Markdown，无预建流程子目录。
- 151份旧记录均有档案落点；9份固定背景包文件逐字节SHA-256一致，JSON机器来源记录原样保留。
- 检查仓库现存文档链接，未新增缺失目标；当前改动中的章节链接一并修复。仓库原有缺失引用不纳入本次清理，固定包中无法独立解析的旧链接继续按来源提交取证。
- 既有942条修改/删除的存在状态及可读取文件哈希未变化；只暂存本任务文件，提交前检查暂存范围及git diff --check。

只做文档检查，不启动玩法测试，也不改变AUD-010。

## 路径衔接

layout.1的path-map.json记录上一轮迁移；本轮[exploration-path-map.json](exploration-path-map.json)衔接其探索路径。文件导航已更新为[当前文件清单](file-index.md)。旧机器manifest中的固定提交路径保持历史语境，不可当作当前工作树脚本配置。
