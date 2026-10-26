> 2026-10-26归档附件。以下是原日期的来源／提示词记录；其中布局、当前状态、下一步和美术要求均不约束新基准。原字节及所有未保留文件按附件README的共同Git快照取证。

# 主桌少文字UI效果图 v01

2026-10-17 · game-002 / main · AS-G002-029 · 视觉候选 / Unqualified · Hypothesis / NotRun。

本图按用户“交给设计agent在目前真实截图下用生图模型生成一个效果图”的明确请求制作。它是少文字方案的静态表现示意，不表示Q1—Q3已获确认，不构成玩法采纳、引擎实现或玩家理解效果的验证。设计agent负责提示词、内置模型生成及视觉检查；协调者负责独立复核、资源目录登记和版本提交。

## 输入与固定输出

- 设计输入：[主桌少文字与图形时间方案](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/sources/inbox/2026-10-17-minimal-battle-ui.md)，固定设计输入提交 `71c7950`；本轮只制作真实截图基础上的效果图。
- 唯一编辑底图：[B13完工暂停截图](E:/Project/yanzhou-godot/evidence/development-batch-13/package-main-01/1920x1080/09-completion-paused.png)，1920×1080；SHA-256 `d974b54753390760fc862ebdcce50d2d5ae0291939a854e60d104f098b444a2b`。
- 采用工具：内置 `image_gen`，编辑意图 `precise-object-edit`，`transparent_background: false`。两次调用均引用以上同一个真实底图；未调用外部API、CLI或栅格合成工具。
- 最终本机项目文件：[minimal-battle-ui-art-v01.png](E:/Project/yanzhou-godot/evidence/ui-concepts/2026-10-17-minimal/minimal-battle-ui-art-v01.png)。
- 最终生成原件：[exec-282a4bc6-ad95-46d3-8a30-d465c81940f1.png](C:/Users/Administrator/.codex/generated_images/01a14cfb-73e7-7c03-a394-bf5354165043/exec-282a4bc6-ad95-46d3-8a30-d465c81940f1.png)，保留在默认生成目录。
- 最终尺寸：1672×941；保持与底图接近的16:9画幅，未作后期缩放、拉伸或裁切。
- 最终项目副本SHA-256：`d478521339be289d3a5f404a171cfd0ebc95993e1a9de4bc1ad5f660bbab54d5`。
- 首版原件仅作制作记录：[exec-f5a883b7-c596-4fc1-8045-50ed1549f78b.png](C:/Users/Administrator/.codex/generated_images/01a14cfb-73e7-7c03-a394-bf5354165043/exec-f5a883b7-c596-4fc1-8045-50ed1549f78b.png)。首版的右环近四分格且窗外提示缺类别，因此进行一次定向修订；最终采用第二次输出，不将首版作为项目消费入口。
- PNG留在外部实现仓库的gitignored evidence路径，本设计仓库只维护制作说明与资源登记；文件存在不表示允许发布或接入游戏。

## 画面中的准确状态

| 对象 | 底图事实与效果图表达 | 检查 |
| --- | --- | --- |
| 当前时间／状态 | 刻度0—6；当前2有包围标识；暂停双竖线与完工阶段齿轮；1×保留 | 视觉通过 |
| 玩家生命／护甲 | 心形30、盾形0 | 视觉通过 |
| 敌方生命／护甲 | 心形60、盾形0 | 视觉通过 |
| 施法次数 | 总量、可用、锁定各为0；使用标记／手／锁图形；此图形语法为未采纳候选 | 三个0保留；图形首次理解未验证 |
| 容量 | 五格：一实心、一虚线预留、三空；待复用0不占格 | 视觉通过 |
| 守护法器 | 刚完工后无在制批次；原实物保留，旁边为空轨盾形环 | 无已填进度 |
| 施法法器 | 当前普通批次三分格，右侧与下侧两段已填，左上段空；旁边未来用途仍为普通火焰图形 | 未出现强化／新批次 |
| 玩家实牌 | 仅一张护盾，+4，位于刻度3下方 | 视觉通过；预测使用虚线边框 |
| 敌公开牌 | 攻击10，位于刻度6上方，保留锁定图形 | 视觉通过 |
| 敌暗牌 | 位于揭示刻度4，背面；程序位置2、攻击类别、眼形标识 | 未显示量、目标、延迟或生效时间 |
| 窗外提示 | 8带打断类别，12带攻击类别，均有方向／眼形标识 | 视觉通过 |
| 疲劳 | 沙漏旁端点16、两个心形与−5 | 视觉通过；没有攻击图形 |
| 真实场景 | 桌、红垫、书、沙漏、双方棋子、两件原法器、烛台、筹码及控制物件保留位置与镜头 | 构图保持；生成重采样不等于逐像素保留 |

## 保留情况与已知偏差

1. 模型保留原画面的物件配置、视点、光照方向和主要相对位置，未生成新战斗场景或平面仪表盘。全图经过模型重生成，细小纹理、边缘、字形及局部几何会与底图不同；不能当作原引擎像素截图。
2. 输出1672×941，低于1920×1080底图，约16:9；此文件未作人为补边或伸缩。
3. 护盾牌用虚线外沿表达预测，未严格做成候选中的独立“虚线底签”。当前指针仍采用原截图包围2的形式，并非新建固定中央指针；符合本轮保留真实构图的范围。
4. 守护空闲环是贴近原法器的UI徽记，施法环旁小圆签表示未来普通用途；小圆签不表示第三个加工批次。是否会被误认为新物件或额外进度环，需后续画面评审。
5. 疲劳两个心形并列表达双方；没有明显宿主连线。施法三量用图形区分，其首次可读性未检验。
6. 环进度、时间位置与暂停表现仅检查单张静态画面；没有验证旋转、单步、回看、减动效、键盘操作、近观、极端数值、768p或真人理解。未改代码、未启动游戏或玩法实验。

## 完整最终提示词

以下为第二次调用传入的完整提示词；唯一引用图片为上文真实底图。生成输出保留原件，本机项目PNG为逐字节复制。

```text
Use case: precise-object-edit.
Asset type: one polished in-game UI concept image edited directly on the supplied real game screenshot.
Input image: Image 1 is the ONLY EDIT TARGET, not loose inspiration. Edit its existing small UI labels and graphical carriers. Preserve the original 16:9 frame, camera, perspective and every scene object.

Primary request:
Turn this exact screenshot into a restrained, minimal-text battle UI. Make the existing timeline positions carry event timing, and use small brass segmented progress rings bound to the TWO EXISTING artifacts to carry production progress. The result must unmistakably still be the supplied real game screenshot, with the same objects in the same places, not a new illustration, new scene, dashboard, or redesigned tabletop.

LOCKED SCENE / KEEP UNCHANGED:
The original low-poly / pixel-textured 3D render, dark background, warm lighting, wooden tabletop, red cloth and gold border, book at top left, fatigue hourglass, upper brown enemy figurine, lower green player figurine, upper right green glass object, both candles, counters, brass tokens, existing left magnifier-like guardian artifact and right spear-like spell artifact, all bottom and side physical controls, all exact object positions and sizes. Do not beautify or relight the scene, replace models, add another artifact, add extra cards, crop, tilt or zoom. Keep the broad empty red felt spaces. All interface additions should be quiet ivory/brass/green, with the same in-scene perspective as the existing plaques.

THE EXACT PAUSED GAME STATE, do not invent a new state:
Timeline visible tick numbers: 0, 1, 2, 3, 4, 5, 6. Keep these digits in their original positions. The current tick is 2, marked clearly by the original brass enclosing ring at x~833 y~458. It is paused in completion phase. On the upper-right original status plaque, remove the sentence and use a clear PAUSE glyph plus a small completion-phase gear glyph. Keep 1× by the bottom controls. The actual bottom play, single-step and settings physical controls all stay where they are.

Card layout, strongly preserve:
1) The one player shield card stays at x~960 y~530 directly below timeline tick 3. Keep its short Chinese title "护盾", shield pictogram and "+4". Delete "预计3" and all time text. Give it a subtle dotted/outlined little prediction base tab, to distinguish a forecast placement from a guaranteed result. Do not add any other player card.
2) The face-down enemy card stays at x~1080 y~391 directly above timeline tick 4. It reveals at 4. Keep the card back. Use only a tiny eye/reveal corner pictogram, program sequence digit "2", and attack-category corner symbol. Remove "r4" and other time text. It MUST remain face down and MUST NOT reveal any effect amount, delay, resolution tick, target, card name or hidden content.
3) The face-up enemy attack card stays at x~1320 y~390 directly above timeline tick 6. Keep short title "攻击", attack/fire pictogram, and "10". Remove "T6" and other time text. A small locked-target pictogram may remain; do not alter its value or move the card.
4) At the right offscreen edge, retain two understated future reveal hints: arrow/eye with digit "8" and interrupt-category symbol, then arrow/eye with digit "12" and attack-category symbol. Replace the existing "r8" and "r12". For 8 the category symbol MUST be a clear interruption/cancel glyph (a circle crossed by a diagonal slash), after the digit 8. For 12 the category symbol MUST be an attack/flame glyph, after the digit 12. Both rows must be distinct: right-pointing arrow + eye + 8 + crossed-circle; right-pointing arrow + eye + 12 + flame. These are reveal hints only, not face-up cards and not extra cards on the timeline.

Capacity:
Replace the original lower-left Q plaque at x~407 y~590 with ONE compact independent brass rack of EXACTLY FIVE equally sized clearly countable horizontal slots in that original plaque area: first slot filled ivory (one real card), second slot outlined/dashed or hatched (one reserved production space), last three slots empty (three available spaces). No sixth slot. No occupied recycling slot. No Q, no numerator/denominator, no "实", "预", "待", no explanation legend. Keep this rack separate from the timeline.

Artifact progress:
The actual left magnifier-like guardian artifact has JUST finished a batch and currently has NO active batch. Its old tiny dash label becomes a small quiet EMPTY idle ring nearby, attached visually to the same artifact without covering or redrawing it. The idle ring is a thin unfilled brass track with a subtle shield center; no filled progress and no spinning arrow that implies an active batch.
The actual right spear-like spell artifact has an active NORMAL spell batch of total duration THREE logical units, TWO completed and ONE remaining. Replace ONLY the old "D3·余1" label near x~1460 y~710 with a refined small brass circular ring, about 75–90 px diameter, next to and visually bound to the existing spear, not covering it. The ring is split into EXACTLY THREE equal 120-degree arc chambers, like three slices of a pie around a hollow center. There are ONLY THREE radial joins, precisely at 12 o’clock, 4 o’clock and 8 o’clock. The first arc from 12 to 4 clockwise is filled ivory/gold. The second arc from 4 to 8 clockwise is filled ivory/gold. The final arc from 8 to 12 clockwise is EMPTY dark. Thus the filled arc is one continuous TWO-THIRDS circumference with just a single internal join at 4 o’clock; the empty region is the one-third on the UPPER LEFT. Put a small fixed pointer at 8 o’clock, the end of the second completed arc, and a small start notch at 12. NEVER quarter the circle, NEVER use four arcs, and do not put a divider at 3, 6 or 9 o’clock. Center shows the normal attack production pictogram. A separate tiny normal-attack future-use pointer can be attached next to it. Current and future uses are BOTH normal. Do not show an empowered spell, 18, 5 cost, a full circle, a new batch or a generic percentage. There should be only TWO rings in total, one idle at the left artifact and this active 2-of-3 ring at the right artifact.

Vitals and counters:
On the upper enemy plaque, show clean HEART pictogram + "60" and SHIELD pictogram + "0", no words and no square placeholder glyph.
On the lower player plaque, show HEART + "30" and SHIELD + "0".
On the existing lower-right spell-counter plaque, replace the long Chinese text with three compact unambiguous glyph-number pairs in the original plaque area: spell-marker icon + "0", open-hand/available icon + "0", lock icon + "0". All three accurate zeros must remain. Do not add balances.
On the small plaque next to the top-left fatigue hourglass, replace "16拍·双方5" with a miniature public tick endpoint "16" and TWO linked heart-loss pictograms with the single clearly associated amount "−5", communicating both sides lose 5 life. No attack/fire symbol, no sentence.

Typography / finish:
Use the existing warm paper and engraved brass visual language. Keep large digits crisp and readable. The only Chinese words needed on the whole tabletop are the short card names "护盾" and "攻击"; remove all timing words and technical abbreviations from labels. Keep tick digits 0–6, future hint digits 8 and 12, fatigue endpoint 16, exact vitals/counters and effect amounts. No long legends, explanatory panels, side-by-side comparisons, annotations, arrows to commentary, outside review UI, title, watermark, English labels or new HUD. Image should be a clean exact-state concept render of the existing gameplay screen.
Recheck before finishing: same scene and same three cards; current2; shield+4 at3; dark program2 reveal at4; public attack10 at6; five capacity slots filled/dashed/empty/empty/empty; left artifact idle; right artifact 2-of-3 normal; enemy60/0, player30/0; three spell counters0; fatigue16 and both life−5; paused and1×.
FINAL CRITICAL VISUAL CHECK: Spell progress circle is a three-sector ring with joins only at clock positions12,4,8, exactly two gold sectors and one dark sector. The two offscreen hint rows each retain its category glyph, crossed-circle for8 and flame for12. Preserve all original screenshot scenery as closely as possible; no visual redesign of the table itself.
```

## 首次调用提示词记录

首次调用同样使用唯一真实底图；以下为完整输入，保留以便区分最终修订的来源。

```text
Use case: precise-object-edit.
Asset type: one polished in-game UI concept image edited directly on the supplied real game screenshot.
Input image: Image 1 is the ONLY EDIT TARGET, not loose inspiration. Edit its existing small UI labels and graphical carriers. Preserve the original 16:9 frame, camera, perspective and every scene object.

Primary request:
Turn this exact screenshot into a restrained, minimal-text battle UI. Make the existing timeline positions carry event timing, and use small brass segmented progress rings bound to the TWO EXISTING artifacts to carry production progress. The result must unmistakably still be the supplied real game screenshot, with the same objects in the same places, not a new illustration, new scene, dashboard, or redesigned tabletop.

LOCKED SCENE / KEEP UNCHANGED:
The original low-poly / pixel-textured 3D render, dark background, warm lighting, wooden tabletop, red cloth and gold border, book at top left, fatigue hourglass, upper brown enemy figurine, lower green player figurine, upper right green glass object, both candles, counters, brass tokens, existing left magnifier-like guardian artifact and right spear-like spell artifact, all bottom and side physical controls, all exact object positions and sizes. Do not beautify or relight the scene, replace models, add another artifact, add extra cards, crop, tilt or zoom. Keep the broad empty red felt spaces. All interface additions should be quiet ivory/brass/green, with the same in-scene perspective as the existing plaques.

THE EXACT PAUSED GAME STATE, do not invent a new state:
Timeline visible tick numbers: 0, 1, 2, 3, 4, 5, 6. Keep these digits in their original positions. The current tick is 2, marked clearly by the original brass enclosing ring at x~833 y~458. It is paused in completion phase. On the upper-right original status plaque, remove the sentence and use a clear PAUSE glyph plus a small completion-phase gear glyph. Keep 1× by the bottom controls. The actual bottom play, single-step and settings physical controls all stay where they are.

Card layout, strongly preserve:
1) The one player shield card stays at x~960 y~530 directly below timeline tick 3. Keep its short Chinese title "护盾", shield pictogram and "+4". Delete "预计3" and all time text. Give it a subtle dotted/outlined little prediction base tab, to distinguish a forecast placement from a guaranteed result. Do not add any other player card.
2) The face-down enemy card stays at x~1080 y~391 directly above timeline tick 4. It reveals at 4. Keep the card back. Use only a tiny eye/reveal corner pictogram, program sequence digit "2", and attack-category corner symbol. Remove "r4" and other time text. It MUST remain face down and MUST NOT reveal any effect amount, delay, resolution tick, target, card name or hidden content.
3) The face-up enemy attack card stays at x~1320 y~390 directly above timeline tick 6. Keep short title "攻击", attack/fire pictogram, and "10". Remove "T6" and other time text. A small locked-target pictogram may remain; do not alter its value or move the card.
4) At the right offscreen edge, retain two understated future reveal hints: arrow/eye with digit "8" and interrupt-category symbol, then arrow/eye with digit "12" and attack-category symbol. Replace the existing "r8" and "r12". These are reveal hints only, not face-up cards and not extra cards on the timeline.

Capacity:
Replace the original lower-left Q plaque at x~407 y~590 with ONE compact independent brass rack of EXACTLY FIVE equally sized clearly countable horizontal slots in that original plaque area: first slot filled ivory (one real card), second slot outlined/dashed or hatched (one reserved production space), last three slots empty (three available spaces). No sixth slot. No occupied recycling slot. No Q, no numerator/denominator, no "实", "预", "待", no explanation legend. Keep this rack separate from the timeline.

Artifact progress:
The actual left magnifier-like guardian artifact has JUST finished a batch and currently has NO active batch. Its old tiny dash label becomes a small quiet EMPTY idle ring nearby, attached visually to the same artifact without covering or redrawing it. The idle ring is a thin unfilled brass track with a subtle shield center; no filled progress and no spinning arrow that implies an active batch.
The actual right spear-like spell artifact has an active NORMAL spell batch of total duration THREE logical units, TWO completed and ONE remaining. Replace ONLY the old "D3·余1" label near x~1460 y~710 with a refined small brass circular ring, about 75–90 px diameter, next to and visually bound to the existing spear, not covering it. The ring has EXACTLY THREE broad separated arcs: TWO filled ivory/gold arcs and ONE empty dark arc, clear top start notch, clockwise pointer at the end of the second completed arc. Center shows the normal attack production pictogram. A separate tiny normal-attack future-use pointer can be attached next to it. Current and future uses are BOTH normal. Do not show an empowered spell, 18, 5 cost, a full circle, a new batch or a generic percentage. There should be only TWO rings in total, one idle at the left artifact and this active 2-of-3 ring at the right artifact.

Vitals and counters:
On the upper enemy plaque, show clean HEART pictogram + "60" and SHIELD pictogram + "0", no words and no square placeholder glyph.
On the lower player plaque, show HEART + "30" and SHIELD + "0".
On the existing lower-right spell-counter plaque, replace the long Chinese text with three compact unambiguous glyph-number pairs in the original plaque area: spell-marker icon + "0", open-hand/available icon + "0", lock icon + "0". All three accurate zeros must remain. Do not add balances.
On the small plaque next to the top-left fatigue hourglass, replace "16拍·双方5" with a miniature public tick endpoint "16" and TWO linked heart-loss pictograms with the single clearly associated amount "−5", communicating both sides lose 5 life. No attack/fire symbol, no sentence.

Typography / finish:
Use the existing warm paper and engraved brass visual language. Keep large digits crisp and readable. The only Chinese words needed on the whole tabletop are the short card names "护盾" and "攻击"; remove all timing words and technical abbreviations from labels. Keep tick digits 0–6, future hint digits 8 and 12, fatigue endpoint 16, exact vitals/counters and effect amounts. No long legends, explanatory panels, side-by-side comparisons, annotations, arrows to commentary, outside review UI, title, watermark, English labels or new HUD. Image should be a clean exact-state concept render of the existing gameplay screen.
Recheck before finishing: same scene and same three cards; current2; shield+4 at3; dark program2 reveal at4; public attack10 at6; five capacity slots filled/dashed/empty/empty/empty; left artifact idle; right artifact 2-of-3 normal; enemy60/0, player30/0; three spell counters0; fatigue16 and both life−5; paused and1×.
```
