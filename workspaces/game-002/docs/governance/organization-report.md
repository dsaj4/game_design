# 言咒全量整理交付

Project ID：game-002。文档角色：OrganizationReport。日期：2026-09-23。管理状态：Accepted / Documentation；本次未新增玩法采纳、素材资格或玩法测试结果。

## 已落地结构

- [现行正文](../../game-design-workflow/gdd/current/README.md)：RC1 / doc.1，保留GDD的0–18章，拆分7系统及内容、参数、验证、来源分册。
- [统一规范](document-contract.md)、[规则定位](rule-index.md)、[ID登记](id-registry.md)、[矛盾登记](conflict-register.md)：明确唯一维护位置、状态维度和变更约定。
- [27探索方向](../../../../exploration/game-002-optimization/directions/README.md)及[横向对比](../../../../exploration/game-002-optimization/directions/comparison.md)：拆分10份原始记录中的独立候选，保存原ID及背景；[部分吸收记录](../../../../exploration/game-002-optimization/directions/baseline-and-absorption.md)区分已有采纳、功能重合和未采纳增量。
- [134效果追踪](../effect-registry/README.md)：稳定FX身份链接现行实体与规则，完整历次语义和旧参数独立留存。
- [开发索引](../code-development-index.md)、[测试交接](../test-handoff.md)、[视觉入口](../visual/README.md)、[历史](../history/README.md)：设计与实现、局部证据分别阅读。

## 实际范围与保留

本轮466份文件：新增265份、修改201份，其中188份为整理前历史快照。完整改动与保留来源见[inventory.md](inventory.md)／[inventory.json](inventory.json)。历史副本仅新增识别说明并重定位相对链接，原字节SHA及起点提交`87ef6d1b7e2ba5812a3d62216a439a9c254393b0`可追溯原文。

既有未提交删除、两份素材的删行、未跟踪视觉产物、调试文件和无关归档均未修改、恢复或暂存。独立new-roguelike仍为空白背景；只在共享导航保留项目入口。本次比较授权不替代未来单方向任务的读取限制。

## 静态核验

| 检查 | 结果与范围 |
| --- | --- |
| 本轮文档本地路径及Markdown章节链接 | 已核对9281处；当前文档错误0；历史遗留2处，均为同一张本轮前已删除的参考图 |
| 结构与实体 | 7系统；53实体／55可链接ID；134个FX入口；GDD 0–18章完整 |
| 探索来源 | 27方向均有来源、背景、资格、差异和验证建议；10份原始输入哈希保持 |
| 文件保护 | 本轮开始时的全部未提交变更逐路径哈希／缺失状态一致 |
| 文本格式 | UTF-8严格读取、无替换字符、代码围栏成对；Git暂存区空白检查通过 |
| 玩法验证 | 本轮NotRun；旧Demo、TH、CAL仅保留原输入范围和结果 |

历史缺图未恢复，因为该删除属于进入任务前的工作树变更。未把其原引用改成其他图片。历史目录与FX章节兼容入口保留；冻结研究应使用原提交／哈希，不以旧链接跳转后的当前内容替换原输入。

## 仍需处理

AUD-010仍Open：新开始法术和已有持续过程在同刻读写同一元素的总排序需要澄清，不能以开始槽优先级代替。原26组选择Closed不是所有组合无歧义的证明。下一步先补这项规则的准确裁决，再冻结实现／验证输入；本次未自行选择排序方案。

后续新增方向按索引规范登记，按问题选择独立验证，不将多个替代主循环一次叠加。正式规则变化仍走Draft Change及决策记录。
