# 来源注册表

更新日期：2026-09-09。来源登记不等于内容资格、背景包生成或玩法采纳。

| Source ID | 类型与位置 | 允许使用方 | 当前状态 | 固定版本/摘要 |
| --- | --- | --- | --- | --- |
| SRC-G002-CONTEXT-V2 | [game-002 核心设计背景包](../../yanzhou/history/exploration-2026-09-24/context/baseline-2026-09-09-001/context-pack.md) | 仅 game-002-optimization 优化任务 | Frozen / Historical Core Design Only | pack `baseline-2026-09-09-001`；source commit `d0c36b9d464680a484f83b234db081b97124b701`；逐文件摘要见 manifest |
| SRC-EMERGENT-V01 | 用户提供的涌现式策略框架 | 两个探索项目均可按问题选择 | Registered / Proposed | [框架登记锚点](framework-registry.md) |
| SRC-SH-CARD-FACE-20261029 | [七款游戏官方卡面与卡外说明材料](../../media-analysis-lab/runs/2026-10-29-card-face-display/README.md#素材与证据)；Steam／官方媒体包／开发文章 | 公共视觉研究；项目转化另行记录 | Research / LimitedEvidence；2026-10-29静态目视 | CARD-FACE-RESEARCH-01；E1—E7的URL、标题、观察与局限沿报告，原件／获取日期／SHA沿manifest；第三方原始图像与HTML仅本机保管，不授权公开分发或项目规则采纳 |

新外部媒体按上表与各分析包登记。媒体分析方法的可用入口在[适配器注册表](adapter-registry.md)，方法入口不能当成已有媒体证据。

后续媒体来源至少登记 source ID、URL/本地位置、标题、获取时间、内容摘要、所属项目、引用片段、许可/本地保存边界及观察与推断的区别。抓取失败保留失败状态，不编造正文。

背景包生成成功后新增独立来源行，包含目标项目、pack ID、source commit、manifest 路径、逐项哈希和验证结果。未通过检查的包不激活；旧包不覆盖。指向 inbox、外部代码或归档的链接仅保留来源指针，不自动扩展读取范围。
