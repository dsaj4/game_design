# 炼金法器 · 精线古朴变体

2026-10-31 · game-002 / main · **AS-G002-036 / ALCHEMY-APPARATUS-05**。

**[打开两版切换与小尺寸对照](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/antique-v05/preview.html)**。A为用户要求保留的[04版粗线简洁方案](../README.md)，B为本轮精线古朴候选，待用户审阅；两版并存。

## 画法调整

仍然只画平炼釜与白化曲颈瓶。外轮廓改用较细、略有粗细变化的褐墨线，弧线与边缘更收敛；铜色降低艳度，釜腹保持沉静靛黑，曲颈瓶用旧象牙白与灰绿。通过大面明暗、较窄的边缘反光和深色器口营造古朴神秘感。

器形、孔洞、中央安静表面和零件数量延续04版。没有增加铭文符号、花纹、雕饰、铆钉、裂纹或场景道具；不靠额外装饰表达神秘。新图仍可另叠加铭文反馈，不在PNG里烘焙文字或发光。

| 原件 | 实际规格 |
| --- | --- |
| [平炼釜 · 精线古朴](refining-kettle-antique-v01.png) | 1343×1171 RGBA透明PNG |
| [白化曲颈瓶 · 精线古朴](albedo-retort-antique-v01.png) | 1135×1386 RGBA透明PNG |

两次内置image_gen分别以04版对应原图为编辑输入，生成后逐字节复制到本目录，未程序裁切、抠图、缩放或改色。[准确提示词](prompts/refining-kettle.txt)同目录有两份；[generation](generation.json)记录输入与工具原件，[manifest](manifest.json)固定尺寸、alpha、SHA及预览证据。

## 保留与检查

04版两张PNG、原提示词、说明、清单及播放器共23个已登记文件通过原SHA核对，全部保持原字节。新图、新播放器和新证据位于独立子目录；本轮没有覆盖04版或再次清理旧文件。

实际IAB检查了A／B／两版对照切换、木色／浅纸／深色alpha合成、剪影和224／64／96／160px样本，当前460×1362视口无横向溢出。细线版64px仍可区分双耳宽釜与弯颈瓶，轮廓比A更柔和；这是agent目视判断，实际背包底色与玩家辨识待验。[浏览器记录](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/antique-v05/browser-qa.json)及[当前画面](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/antique-v05/evidence/06-current-new.png)保存在外部目录。

ReadyForScope / PresentLocal限原件一致性与本机视觉审阅；B风格接受PendingReview。沿04版内容边界，不改法器身份、配方、占格、接口、兼容或数值，没有引擎与玩法测试。

CUSTOM输入为`863ec9e3972a0f2f195da6ad9818872c8b336652`下的04版两图／既有美术约束及本轮用户要求；只做画法变体，不增读其他设计或未提交稿。第三方图像本轮没有重新输入，原图与预览本机保管，说明／提示词／清单入Git，仅项目内部审阅。
