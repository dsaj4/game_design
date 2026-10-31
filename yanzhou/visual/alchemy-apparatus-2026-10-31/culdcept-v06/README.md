# 炼金法器 · Culdcept器物画法变体

2026-10-31 · game-002 / main · **AS-G002-036 / ALCHEMY-APPARATUS-06**。

**[查看新版及三版切换](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/culdcept-v06/preview.html)**。C为本轮候选；[A·粗线简洁](../README.md)与[B·精线古朴](../antique-v05/README.md)继续保留，原件未覆盖。

用户要求借鉴Culdcept BEGINS重新生成，同时在提示词中保留现有简洁器形和细节量。本轮以B版对应器物为编辑目标，保持宽口双耳短足炼釜、梨腹弯颈曲颈瓶的基本形态和中央安静表面；主要变化是更明显的绘画笔触、成块的冷色暗部和克制暖高光。

| 新原件 | 实际规格 |
| --- | --- |
| [平炼釜](refining-kettle-culdcept-v01.png) | 1343×1171 RGBA透明PNG |
| [白化曲颈瓶](albedo-retort-culdcept-v01.png) | 1135×1386 RGBA透明PNG |

## 提示词的优先级

- **器形和细节量优先**：Image1为当前B版目标，锁定轮廓、视角、比例、部件数、孔洞和留白；前表面仍供独立铭文反馈。
- **参考只约束画法**：Image2／3分别为CounterShield、Tonfa独立主体，借其不透明手绘色面、带笔触的体积与冷暖关系；不借盾缘雕刻、兵器装饰或不规则深蓝衬底。
- **不补结构或装饰信息**：不增加花纹、铭文符号、雕饰、铆钉、接缝、裂纹、支架、附属器件或特效，也不变成带牌框／文字的完整卡面。

两份[准确提示词](prompts/refining-kettle.txt)逐件保存；[generation](generation.json)记录各输入角色、原生成路径与参考包。内置image_gen共两次，PNG逐字节复制，无程序图像编辑、裁切、抠图、改色或缩放。[manifest](manifest.json)固定尺寸、alpha、原件SHA和证据。

## 参考与检查

使用[AS-SH-005本机提取包](../../../../media-analysis-lab/runs/2026-10-30-culdcept-begins-art/README.md)@CULDCEPT-ART-2026-10-30-v01。实际查看整体风格板、主体板及CounterShield／Tonfa独立原图；两张独立主体实际进入image_gen，仅作本机画法参考。未复制其特征图案、文字、第三方运行图片或代码，未启动原游戏。

原04、05版共42个登记文件已按原SHA校验，保持原字节。浏览器已核A／B／C／三版切换、浅纸／深色／木色透明合成、剪影和224／64／96／160px样本；实际460×871视口无横向溢出。釜耳与弯颈在小图中仍可辨，结构与饰物数量未见增加；笔触表面比05更明显，接受仍待用户判断。[实际记录](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/culdcept-v06/browser-qa.json)及[当前画面](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/culdcept-v06/evidence/05-current-c.png)在独立外部目录。

ReadyForScope / PresentLocal限本机美术与文件检查，C风格PendingReview。CUSTOM输入固定于`764aa98f0a6b73f1fcc56f7cb49469fb779ef708`的既有两版及用户本轮要求，增补上述指定Culdcept本机图像参考；不扩读玩法、不改配方／法器配置、占格或接口，没有引擎与玩法测试。第三方原件保本机；新图与预览本机保管，说明／提示词／清单入Git，仅项目内部审阅。
