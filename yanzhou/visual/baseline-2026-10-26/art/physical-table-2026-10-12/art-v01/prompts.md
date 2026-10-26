> 2026-10-26归档附件。以下是原日期的来源／提示词记录；其中布局、当前状态、下一步和美术要求均不约束新基准。原字节及所有未保留文件按附件README的共同Git快照取证。

# PHYSICAL-CARD-ART-01 实际提示词

2026-10-12 · 内置 image_gen · AS-G002-013 · 所有调用 transparent_background=false。

结构输入为 DM-G002-012@PHYSICAL-CARD-HTML-04；风格源为 AS-G002-008@BATTLE-UI-ART-01。参考图作为图像输入，源件未改。下文完整保存生成和定向修正提示词；原始生成路径及输入关系见 manifest.json。

## 01 主桌面生成

```text
Use case: style-transfer / ui-mockup.
Create a new polished landscape 16:9 game art mockup for 言咒, by reworking the attached earlier tabletop artwork into the EXACT new composition below. The reference supplies ONLY dark carved walnut, forest-green worn leather, engraved antique brass, burgundy card backs, warm candlelight, realistic miniature materials, elegant slightly elevated near-top-down 3D camera (about 49 degree downward), blue crystal wand and brass ring wand design. Replace its obsolete card placement and token placement. This is a new version, not a duplicate of the old layout.

Scene: an elegant tactile occult strategy game tabletop viewed from the player's side, calm paused moment, all objects sharp and readable, contact shadows, abundant empty green surface. No characters or hands. No browser chrome. At very top center, a small red-and-brass enemy chess pawn; at bottom center a green hooded player chess pawn. Each pawn's status chips are ONLY to the viewer's RIGHT of that pawn. Immediately right: one heart-emblem life chip stack, then EMPTY shield-emblem brass saucer for zero shield; player also has an EMPTY diamond-emblem saucer for zero spell-count. To the LEFT of BOTH pawns is absolutely empty green felt, reserved for absent negative status. Do NOT copy the reference's chips on both sides. No numeric badges or ledger in the default view.

Center: two clean horizontal rows of exactly SEVEN narrow portrait card outlines each (7 enemy above, 7 player below), aligned to a thin engraved timeline separating rows. Timeline reads 0 1 2 3 4 5 6 left-to-right; the 0 medallion highlighted softly, not center 3. Only TWO actual cards on whole board: enemy row column 4 a burgundy BACK card with eye motif, small readable engraving "r4" and attack triangle, no face or damage value; enemy row column 6 a FACE-UP gold attack card with a restrained sword motif, readable "10" and "T6". All other enemy slots empty. All seven player slots empty. Narrow card proportions roughly 0.65 width/height. Small physical edge tags to far right "r8" interrupt symbol and "r12" attack triangle, no extra cards pretending to be in window.

Upper-left inside board: small brass sandclock with discreet engraving "16拍 · 5". The 5 means next shared fatigue, not health. Closed green book placed at outer upper left decorative corner, small crystal orb at outer upper right decorative corner. They are scenery only.
At far-left board edge: compact closed resource-drawer handle; do not show filled inventory.
Lower-left foreground: ONLY two functional wands, ring wand to left and blue crystal wand to its right, separated clearly and smaller than the whole board. Both idle, no countdown glow, no emitted card, no materials. They must not sit between the pawns and their positive chips.
At lower-right wood edge a few small brass physical playback controls (play, step, 1×, cog), tactile and minimal. No large text bars.
Tiny physical plaque below timeline may read "第0拍 · 暂停". No extra headings, no dense paragraphs, no stat boxes, no floating digital HUD. Emphasize visual clarity and craftsmanship, enough light on green tabletop, rich warm restrained fantasy atmosphere. Current state has player health30, enemy60, shield0 and counts0 but those numbers are hidden when not hovering; depict life stacks only as symbolic stacks, do not encode 30 or60 individual coins. Render as high-end game art concept, 16:9, full board within frame.
```

## 01 定向修正

```text
Use case: precise-object-edit. Edit this tabletop mockup with ONE targeted correction. Keep all camera, materials, lighting, board, pawns, all RIGHT-side chips, wands, drawer, visible front card10 atT6, edge tags and typography exactly as they are. Move the single burgundy face-down enemy card ONE slot to the RIGHT: it is currently above timeline medallion3; it must be centered exactly above medallion4, in the fifth slot counting from0. The slot above3 becomes empty outlined green felt. Change the tiny bottom engraving on this card to clearly readable "r4". Keep its eye-pattern BACK face, small attack triangle, do NOT reveal its front. Final enemy row slot0empty,1empty,2empty,3empty,4darkcard,5empty,6frontattack10. Final player row all7empty. Do not add any cards. No other changes. Preserve landscape16:9 and fullframe.
```

## 02 悬浮近观生成

```text
Use case: style-transfer / ui-mockup.
Create a landscape16:9 art direction contact sheet of FOUR independent game CLOSE-UP screens in a clean2x2 editorial arrangement. Use supplied tabletop image for exact material and prop design: forest-green worn leather, dark walnut, fine antique brass, warm candlelight, rich yet readable 3D miniatures. Four quadrants are four DIFFERENT moments, NOT four UI panels inside a game. Only very thin editorial separators between images. At top small title "言咒 · 悬浮近观" and subtitle "不同情境". Each quadrant fills its area with the same softly blurred tabletop scene; foreground objects float cleanly against that scene, with generous air between them. ABSOLUTELY NO rectangular background panels, dialog cards, banner backgrounds, filled stat boxes, opaque circular backplates, or data-table interface. Objects and discreet serif gold text directly over the blurred scene. Small floating brass × at top-right of each scene, no header/footer bar.

UPPER LEFT scene, label "01 法器 · 第1拍": large brass ring wand floating at left (same ring wand prop as reference). A fine detached circular countdown arc completely surrounds the wand. One exactly HALF-CIRCLE gold illuminated arc and one dark half indicate one of two beats elapsed; static, no movement trails. Small clear text by ring "剩余1拍". Right of wand: a small EMPTY floating brass material socket, with readable "无需材料". No material item or output card visible in default state. Beneath the empty socket tiny upward chevron and "上划查看产物". Small detached text "完工2拍" beneath wand. The countdown surrounds the entire wand, not just its circular tip. No extra currencies or options.

UPPER RIGHT scene, label "02 棋子 · 第0拍": a LARGE green hooded player chess pawn on left. All positive state objects ONLY to its right: floating gold-rimmed red heart-chip stack with exact readable "生命30"; next an EMPTY shield-emblem saucer with exact "护盾0". Farther below/right a small independent brass sandclock and discreet labels "16拍" and "各5". In this state-focused close-up only, exact values visible. A tiny clear graphic sequence shield→heart indicates damage order. No chips to pawn's left, no negative effects. No stats panel. Pawn and chips must look like physical objects, not line-icon UI.

LOWER LEFT scene, label "03 暗牌 · 第0拍": large narrow burgundy card BACK floating vertically at left, engraved antique gold eye motif, like reference enemy r4 card. No front illustration visible, no reveal motion. To its right, independent small brass medallion marked "2", engraving "程序2"; a small sandclock with "r4"; and attack triangle with "攻击". Only these public facts, no damage amount, no useT. Three spatially spaced floating objects/text, no rows of boxed stats and no rectangular information area.

LOWER RIGHT scene, label "04 资源 · 空态": three SMALL separate empty brass rings/sockets hovering at different shallow depths over blurred tabletop, no common rectangular backing. All visibly empty, no stones, no resource coins, no outputcards. Compact gold text directly in negative space "无需材料" and "材料0". An optional small brass drawer-handle prop at far left makes source clear, but NO large drawer panel or tray fills background. Socket count is just visual organization, not three-item capacity.

High-quality semi-realistic 3D game art mockup; strong legibility and physical material consistency. Minimal Chinese copy exactly as above. Do not add other text, full game HUD, ordinary interface cards, invented mechanics, cards as resource materials, labels over objects. Warm restrained lighting, dark but clear backgrounds.
```

## 02 定向修正

```text
Use case: precise-object-edit. Make ONE tiny correction to this 2x2 contact sheet and preserve every other pixel-level composition and all text, colors, materials, objects and positions. In the UPPER RIGHT quadrant, between the heart-life chip stack on the left and the empty shield saucer on the right, the small gold triangular arrow currently points RIGHT. Reverse ONLY this arrow so it points LEFT: from the shield toward the heart, meaning ordinary damage meets shield first then life. Keep the two chip positions exactly unchanged: life30 then shield0, both to pawn's RIGHT. Do not change any numbers. Do not add panels. All other three quadrants remain unchanged.
```

## 03 守护牌过程生成

```text
Use case: style-transfer / ui-mockup.
Create a polished landscape16:9 FOUR-FRAME visual storyboard for the 言咒 tabletop strategy game. The input image is a style/material/prop reference only: dark carved walnut, forest-green leather, antique brass, warm candlelight, burgundy card backs, green hooded player pawn, ring wand. Render actual tactile game objects in semi-realistic 3D. Four separate frames arranged2x2 with thin quiet editorial separators, not four gameplay windows. Every frame is a close cropped view of the SAME player's lower board region; do not show full enemy board. Header text outside scenes "言咒 · 守护牌的一次生效". The process is automatic, no hand, no mouse pointer, no play button, no drag instruction.

Track ONE consistent narrow portrait face-up card: ivory parchment, fine brass frame, emerald shield emblem, exact small title "简易护盾", large readable "4", tiny identity "G02" at bottom. It is produced already face up; NEVER show this player card burgundy back and NEVER show flipping. No random other card graphics. These are four moments of ONE card, not four simultaneously existing cards.

FRAME1 upperleft label "01 · 2拍完工入列": a physical brass ring wand lies at left, from its ring a soft brief gold light guides one finished face-up shield card toward a single faint target outline on green tabletop. Depict only ONE solid card, not two copies. A restrained curved editorial arrow indicates wand→queue direction. Small directly overlaid words below scene "入行2 · 最早3". No material item; this artifact needs no materials.

FRAME2 upperright label "02 · 2拍正面待效": the SAME G02 shield4 card resting calmly fully face-up in its player queue slot, aligned to a timeline medallion marked "3"; current beat text is2 and expected use is3. Keep slight perspective and narrow card proportions. No flight trails, no flash, no damage yet. Small direct caption "预计3拍". No disguised card back. This is waiting, not use.

FRAME3 lowerleft label "03 · 3拍使用": the SAME fully face-up card floats slightly raised at left, brief narrow GOLD ribbon connects shield emblem to a green hooded player pawn at center-right. A subtle physical curved shield shimmer embraces the pawn, readable temporary "+4" near its right-hand shield chips. All positive chips to pawn's RIGHT: life stack remains unchanged, shield pile newly present; count saucer remains EMPTY at this substep. No enemy target, no offensive bolt. The effect is brief and local, avoid giant energy dome, fireworks or screenwash. Small direct caption "先获得护盾".

FRAME4 lowerright label "04 · 3拍记次后离场": same pawn stationary, to its RIGHT are three physically separated objects left-to-right heart life stack, shield token stack, a SINGLE diamond-emblem spell-count chip freshly landed into its own small saucer. Small local restrained glint around the new diamond chip and temporary "+1". The SAME G02 used card at far LEFT has just slid away out of queue and is dissolving into a FEW faint motes, leaving the local traced queue slot clearly empty. Its last faint remnant must retain face-up shield design, no turning backside. No new replacement copy. Bottom editorial caption "生命30 · 护盾4 · 次数1". This caption is storyboard annotation, not a permanent gameplay stats panel. It records AFTER shield then count. No circular lock icon, counts are not locked.

Keep the four labels and captions crisp Chinese gold/ivory text laid directly over negative space, NO boxed labels, opaque detail panels, dialogs, HUD table or footerbar. Enough open space so source, waiting card, target and chip change are easy to read. Storyboard motion strokes belong only to active event frames1,3,4; frame2 perfectly static. This shows intended motion snapshots, not a paused board playing an effect. Do not put r-reveal or T-enemy-use annotations anywhere in this player-card chain. Consistent card artwork and props across allframes.
```

## 03 定向修正

```text
Use case: precise-object-edit. Correct timing and token continuity of this four-frame shield-card storyboard while preserving all style, typography, framing, art and layout.
UPPER LEFT and UPPER RIGHT occur at current beat2: highlight the timeline medallion "2" instead of "3" in BOTH top frames. Medallion3 must be ordinary non-highlighted brass. In upper-left frame the curved trajectory must finish pointing into the slot directly above medallion3, not slot4; shorten the arrow so its endpoint lies inside slot3, keep a SINGLE moving face-up card. In upper-right the waiting shield card stays above medallion3.
LOWER LEFT frame has current beat3, highlight3. To the green pawn's right, show exactly THREE separate physical positive state objects from left to right: RED HEART LIFE STACK unchanged; SHIELD stack receiving "+4"; EMPTY DIAMOND-emblem saucer with no coin. Currently the illustration accidentally omits heart pile and mislabels empty saucer; fix this row, move pawn a little left if needed for space. Keep shield effect local and the "+4" adjacent ONLY to shield pile. No count +1 yet here.
LOWER RIGHT stays unchanged: life30, shield4, diamond count1 +1, departing face-up G02 card, currentbeat3.
Do not change the card, labels, caption, text values, use sequence, or add new cards. No panels.
```
