# 来源注册表

更新日期：2026-09-09。来源登记不等于内容资格、背景包生成或玩法采纳。

| Source ID | 类型与位置 | 允许使用方 | 当前状态 | 固定版本/摘要 |
| --- | --- | --- | --- | --- |
| SRC-G002-CONTEXT-V1 | [game-002 背景来源配置](../game-002-optimization/context/generation-profile.json) | 仅 game-002-optimization 的背景包生成任务 | Configured / Not Generated | 生成时固定 source commit；逐文件摘要尚未生成 |
| SRC-EMERGENT-V01 | 用户提供的涌现式策略框架 | 两个探索项目均可按问题选择 | Registered / Proposed | [框架登记锚点](framework-registry.md) |

当前未登记新的外部媒体、context pack 或跨项目设计引用。媒体分析方法的可用入口在[适配器注册表](adapter-registry.md)，方法入口不能当成已有媒体证据。

后续媒体来源至少登记 source ID、URL/本地位置、标题、获取时间、内容摘要、所属项目、引用片段、许可/本地保存边界及观察与推断的区别。抓取失败保留失败状态，不编造正文。

背景包生成成功后新增独立来源行，包含目标项目、pack ID、source commit、manifest 路径、逐项哈希和验证结果。未通过检查的包不激活；旧包不覆盖。指向 inbox、外部代码或归档的链接仅保留来源指针，不自动扩展读取范围。
