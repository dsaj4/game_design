# 飞书游戏设计系统课程逐字稿资料包

状态：`Research Input / Transcript Archive`

本资料包来自飞书多维表格“游戏设计系统课程”的“游戏设计系统课”视图。课程链接统一交给 BiliSum 转写；多分集视频先通过 B 站公开页面接口展开，再以 `?p=N` 逐集提交。这里保留原始逐字稿和来源追踪，不把课程内容直接写成项目设计结论。

## 来源与范围

- 飞书来源：[“哈基米游戏”在线课程表](https://gcnw76y7x5f3.feishu.cn/base/OP1jbJbGIaBmeisKLakcnwDZnMh?table=tblz6Wo5dnYavy7a&view=vewngI7Gfg)
- 表：`游戏设计系统课程`
- 视图：`游戏设计系统课`
- 飞书课程记录：237 条
- 去重后 B 站视频：235 个
- B 站分集总数：753 P
- 完整课程：233 个
- 不完整或失败课程：2 个
- 成功逐字稿分集：749 P
- 转写来源：224 份 bilibili-subtitle，525 份 dashscope_funasr
- 逐字稿总字符数：2499340

## 文件结构

- [course-catalog.md](course-catalog.md)：237 条飞书记录、课程链接、时长、关键词和逐字稿状态。
- [manifest.json](manifest.json)：课程记录、分集、BiliSum 任务 ID、转写来源、文件路径、哈希和错误信息。
- [multipart-inventory.json](multipart-inventory.json)：从 B 站公开接口读取的分集结构与 CID。
- [multipart-repair-state.json](multipart-repair-state.json)：逐分集修复任务的断点状态。
- [failed-items.md](failed-items.md)：仍无法完成或不完整的课程。
- `transcripts/<BV>.txt`：课程合并逐字稿。
- `transcripts/<BV>/pNNN.txt`：多分集课程的单集逐字稿。
- [repair-multipart-transcripts.ps1](repair-multipart-transcripts.ps1)：可重复执行、可断点续跑的修复脚本。

## 多分集处理

BiliSum 1.19.1 的单 URL 转写接口不会自动遍历 B 站分 P。修复脚本先读取 `data.pages`，再把每个 `https://www.bilibili.com/video/<BV>?p=<N>` 作为独立任务提交。已有第 1 P 会复用，避免重复转写。

## 使用边界

逐字稿只是研究输入，可能包含字幕断句、专名和语音识别错误。引用具体观点前应回看原视频并核对上下文。

本资料包不等同于 `research/02-theory-digests/` 的理论摘要，也不会直接改变 GDD、Proposal 或 `core-concept.md`。下一步应按当前设计问题选择少量相关课程，整理摘要，并回答“它如何改变本项目设计判断”。
