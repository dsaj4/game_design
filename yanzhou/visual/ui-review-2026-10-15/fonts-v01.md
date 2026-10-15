# 字体候选 v01

2026-10-15。AS-G002-024 / FONT-CANDIDATES-01。状态：本机文件与技术覆盖已核，用户选择待审；未安装系统字体、未改运行包。两个候选与现行黑体在审阅 HTML 的“字体同尺寸对照”中可直接比较。

| 角色候选 | 实际固定文件 | 一手来源 | 规格与用途建议 |
| --- | --- | --- | --- |
| 现行对照 | Noto Sans CJK SC Regular 2.004 | 既有 AS-G002-011 / FONT-ASSETS-01 | 正文、数值基线保持；本轮原文件哈希不变 |
| 宋体／印刷纸面感 | Noto Serif CJK SC Regular 2.003 | [官方发布](https://github.com/notofonts/noto-cjk/releases/tag/Serif2.003)；源提交 `9b0f1436e455d902de067a2501422e5dc71ad16b` | 简体中文语言版；适合先比较标题／牌名，也可独立比较正文。风格判断为制作建议 |
| 文楷／手写纸签感 | LXGW WenKai Regular 1.522 | [作者发布](https://github.com/lxgw/LxgwWenKai/releases/tag/v1.522) | 实际字体版本元数据 `Version 1.522; March 17, 2026`；先比较纸签及近观正文，未认定适合全游戏 |

下载文件是官方发布的原始 OTF／TTF，未改名、子集化或转格式。Noto Serif SHA-256 `2a2eae2628df83556c54018c41e20fa532c1b862c5256ae8b3f23feb918d12ca`；文楷 `39ad71264b588165b469e35e6afb162a378dacd1f95348160240ba9038ac3009`。原件就地位于 `E:/Project/yanzhou-godot/evidence/development-batch-11/ui-review-v01/fonts/`。文件大小、cmap数量、各许可哈希和精确下载URL在 `tools/ui-review-2026-10-15/data.json`，未把第三方原始二进制提交到设计库。

三种主字体分别用503个本轮真实捕获字、相关模板汉字、候选字及数字／标点／符号测试；本体均缺 `U+2731 ✱`，配现行 Noto Sans Symbols 2 2.008后均无缺字。此结论只覆盖该字集，不等于完整中文字库、其他语言、所有未来文案或Godot实际fallback已验。常驻20/18px、正文18px、标题24px同尺寸展示；字体改变后重算宽度和分页，不用缩字掩盖溢出。HTML中的混搭选项仅宋体标题＋黑体正文，不含额外未下载字重。

两份原许可均为 SIL OFL 1.1，随文件原样保存。固定版本原文：[Noto Serif许可](https://github.com/notofonts/noto-cjk/blob/9b0f1436e455d902de067a2501422e5dc71ad16b/Serif/LICENSE)、[文楷1.522许可](https://github.com/lxgw/LxgwWenKai/blob/v1.522/OFL.txt)。原文允许软件捆绑、嵌入及再分发，同时要求保留版权／许可、禁止单独售卖字体、遵守修改字体的保留名称条件。本轮仅使用未修改文件；未来子集化、改字形、转格式或公开分发需要按所用版本再次核条件。其他字重、罕见字形风格、字图内存与运行成本为未测，不以下载站“免费”代替许可。

浏览器同尺寸对照已实际目视，Godot中的字形、基线、行距、fallback、标题真实字重与两档重新捕获仍 NotRun；须在用户确定对应组件字体后继续。
