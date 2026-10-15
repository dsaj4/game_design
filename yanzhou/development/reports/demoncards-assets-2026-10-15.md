# 恶魔牌原资源接入记录

2026-10-15 · game-002 · ImplementationIndex。用户要求“列出清单进行接入”，沿十九组件版继续本机预览。既有「言咒设计对接」负责设计，总控完成集成与核验；未新增玩法或平衡结论。

| 输入 | 实际接入范围 |
| --- | --- |
| AS-G002-025 / DEMONCARDS-ORIGINAL-01 | 原桌、布、卡三模型；木纹、红布、暖纸三纹理。另两张辅助图仅保留来源，未入运行包。原游戏暗背未证实，保留当前登记背面 |
| AS-G002-026 / demoncards-fonts-v01 | 作者全濑体1.11、狮尾B2宋朝SC Regular/Bold；短标题、正文与常驻精确读数分别分配，原OFL随包 |
| 现有组件与规则 | 保留当前其他组件、卡文、真实公开状态、窄槽、触发／使用／详情／移动及暂停取消约定 |

[逐项清单](E:/Project/yanzhou-godot/docs/coordination/2026-10-15-demoncards-asset-integration.md) · [实际集成与检查](E:/Project/yanzhou-godot/docs/reviews/2026-10-15-demoncards-asset-integration.md) · [真实画面](E:/Project/yanzhou-godot/evidence/development-batch-12/captures/index.html) · [设计交接](../../visual/demoncards-assets-2026-10-15/design-handoff-v01.md)。

代码固定 `8d22262dfa4a3cf9cdc96cae5f9994f27608cafe`。源码修正轮及独立复制包两档各72项通过；原包/副本200文件364,033,411字节指纹一致，旧7案例及跨进程恢复相等通过；原预检Q叠行、首轮模型格式失败、第二轮“功能通过而文字／墨绘视觉失败”分别保留，未用后续结果覆盖。新包另存 `E:/Project/yanzhou-godot/build/development-batch-12/original-assets-01/windows/`，设计限定复核以独立D报告为准，原/包68PNG中64全同、4张各差1或5个字边像素，文本与几何数据相同；完整证据见集成报告。

原第三方模型／纹理就地保管，本批资源仅本机预览，未公开上传。OS输入、正式性能及用户最终美术接受未验；不将局部工程核验升级为完整美术或玩法接受。第九／十批原包、源件及当时结论保留。

[设计D v02限定复核](../../visual/demoncards-assets-2026-10-15/design-review-v02.md)：实际两档10幅，LimitedForScope，无新增本批阻断；三项原视觉问题在对应画面关闭。768句号独行／短语跨页保留为非阻断排版残差；其余58幅未由D人工复核。
