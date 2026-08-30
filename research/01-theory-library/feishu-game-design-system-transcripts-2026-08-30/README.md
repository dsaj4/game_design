# 飞书游戏设计系统课程逐字稿资料包

状态：`Research Input / Transcript Archive`

本资料包来自飞书多维表格“游戏设计系统课程”的“游戏设计系统课”视图。课程链接统一交给 BiliSum 转写，成功结果以 UTF-8 TXT 保存；这里保留原始逐字稿和来源追踪，不把课程内容直接写成项目设计结论。

## 来源与范围

- 飞书来源：[「哈基米游戏」在线课程表](https://gcnw76y7x5f3.feishu.cn/base/OP1jbJbGIaBmeisKLakcnwDZnMh?table=tblz6Wo5dnYavy7a&view=vewngI7Gfg)
- 表：`游戏设计系统课程`
- 视图：`游戏设计系统课`
- 飞书课程记录：237 条
- 去重后 B 站视频：235 个
- 成功逐字稿：233 份
- 失败：2 份
- 转写来源：224 份 B 站字幕，9 份 DashScope FunASR
- 逐字稿总字符数：1,343,661

## 文件结构

- [course-catalog.md](course-catalog.md)：237 条飞书记录、课程链接、时长、关键词和逐字稿状态。
- [manifest.json](manifest.json)：课程记录、飞书记录 ID、BiliSum 任务 ID、转写来源、文件路径、哈希和错误信息。
- [failed-items.md](failed-items.md)：无法由 BiliSum 读取的 2 个视频。
- `transcripts/`：按 BV 号命名的 TXT 逐字稿，一种视频只保存一份。

## 去重与数据质量

飞书视图中有两组记录共享 B 站 URL，因此 237 条记录对应 235 个唯一视频：

- `SJ-190_f` 与 `SJ-211_f` 都指向 `BV1kTKj6PEp9`，但课程标题不同，可能是来源表链接错配；两条记录暂时共享同一份逐字稿，并在 `manifest.json` 中保留原始标题。
- `SJ-1940_f` 与 `SJ-2069_f` 都指向 `BV1XkNT6sEVc`，标题含义一致，按正常重复记录处理。

## 使用边界

逐字稿只是研究输入，可能包含字幕断句、专名和语音识别错误。引用具体观点前应回看原视频并核对上下文。

本资料包不等同于 `research/02-theory-digests/` 的理论摘要，也不会直接改变 GDD、Proposal 或 `core-concept.md`。下一步应按当前设计问题选择少量相关课程，整理摘要，并回答“它如何改变本项目设计判断”。
