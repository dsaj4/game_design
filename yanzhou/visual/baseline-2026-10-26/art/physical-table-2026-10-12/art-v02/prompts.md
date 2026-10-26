> 2026-10-26归档附件。以下是原日期的来源／提示词记录；其中布局、当前状态、下一步和美术要求均不约束新基准。原字节及所有未保留文件按附件README的共同Git快照取证。

# PHYSICAL-CARD-ART-02 实际提示词

2026-10-12 · AS-G002-013 · 内置 image_gen · transparent_background=false。

编辑输入为 art-v01/03-shield-sequence.png；旧版不覆盖。最终修正输入为首轮生成图；原始输出路径与输入SHA-256见manifest.json。

## 按用户两点修订

```text
Use case: precise-object-edit.
Edit this existing 2x2 storyboard with exactly the user's simplification: production is wand lights up THEN card appears directly in its queue position; use is card lights up WHILE the target pawn gets a local effect. NO traveling energy, NO physical card flight, NO arrows or connecting trails.

Preserve overall 16:9 composition, all four frames, green leather and carved walnut tabletop, antique brass, warm light, the same green player pawn, same narrow face-up ivory G02 shield card showing 简易护盾 / 4 / G02, right-side life/shield/count chips, all Chinese labels and numbers, the second and fourth frames unchanged.

UPPER LEFT frame 01 (2拍完工入列): REMOVE ENTIRE curved gold arrow and ALL connecting spark trail from wand to card. Wand ring lights up locally with a restrained warm glow around its ring only. The card now APPEARS IN PLACE directly in the slot above timeline medallion3, exactly matching the resting card position in upper-right frame. Show a single card, aligned to the board slot, partly translucent at its lower edge with a very few local appearance motes, fading into existence at that place. It must NOT be suspended between the wand and slot, NOT angled in flight, NOT moving from wand to slot. Current beat2 stays highlighted. A tiny direct caption may read "法器亮起 → 卡牌浮现" but no arrow drawn in scene. Existing bottom "入行2 · 最早3" stays. Wand local glow and card local materialization are spatially separate with dark green EMPTY space between them.

LOWER LEFT frame03 (3拍使用): REMOVE ENTIRE gold ribbon/beam that currently goes from card to pawn. Put the single G02 card back into its own queue slot above timeline medallion3, stationary and face-up, with a restrained warm rim light and brighter shield emblem. Card DOES NOT rise toward pawn, fly away, or move in this use step. The green pawn simultaneously has the existing local shield shimmer around it. Card glow and pawn shield glow are TWO SEPARATE effects with EMPTY space between, NO connection. Current3 remains highlighted. Right-side life remains same; shield+4; diamond empty. Existing bottom caption "先获得护盾" stays. No outbound beam, lightning, dotted path, arrow, comet, or string of particles between them.

UPPER RIGHT and LOWER RIGHT stay exactly as reference (waiting at2, then count+1 and departing card at3). Invariants: first card appears at3 during currentbeat2; no changed game timing; effect is shield+4 then count+1; final life30 shield4 count1. No new panels, no UI boxes, no hands, no extra cards. This is a targeted simplification of visual action, not redesign of setting or mechanics.
```

## 定向校正浮现刻位

```text
Use case: precise-object-edit. ONE POSITION CORRECTION in upper-left frame only. Keep all four frames and every other object, caption, lighting, materials, no-beam design exactly unchanged.
In upper-left frame, the newly materializing shield card is incorrectly sitting above timeline "4" at the rightmost slot. Move that single card approximately one full slot-width LEFT into the outlined slot directly ABOVE MEDALLION "3" (the empty slot immediately left of its current location). Align its center with the 3 medallion, not with4. The rightmost slot above4 must now be EMPTY. Preserve currentbeat2 glow. Retain local wand glow, local materializing card glow and transparent lower edge. NO arrow, flight trail, ribbon, lightbeam or connection. Leave upper-right, lower-left and lower-right frames unchanged.
```
