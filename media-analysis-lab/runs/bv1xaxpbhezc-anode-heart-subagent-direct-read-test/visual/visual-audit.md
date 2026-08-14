# Anode Heart: Layer Null Visual Audit

This audit records which frames were actually opened and inspected with local image-viewing capability. Material-pack captions and BiliSum observations were treated as hints only; they were not copied into audited observations.

## Summary

- Audited frames with direct image reading: 15 / 28
- Not independently audited: 13
- Direct reader: Codex local image viewer plus manual visual inspection.
- Limitation: small pixel text and exact rule wording were recorded as OCR candidates, not high-confidence rules unless also supported by transcript text.
- Path friction: the scaffold inherited material-pack-relative `../source/...` paths, which are invalid from this separate output workspace; JSON paths were normalized to point back to the original run directory.

## Frame Audit

| ID | Image | Status | Direct read | Confidence | Visual evidence summary | Modules | Illustration |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V1 (I1) | `../bv1xaxpbhezc-anode-heart/source/frames/f0001.jpg` | audited | true | high | Card collection/library screen with a grid of locked and owned cards. The collection interface exposes cards as collectible assets with purchase/currency state and individual rule text. | module-1, module-4, module-6 | true |
| V2 (I2) | `../bv1xaxpbhezc-anode-heart/source/frames/f0002.jpg` | audited | true | high | Deckbuilding screen for a colorless deck: left deck list, right All Cards browser, category counters at the top. Deck composition is visible as typed counts, making unit/support ratio a deckbuilding constraint. | module-4, module-5 | false |
| V3 (I3) | `../bv1xaxpbhezc-anode-heart/source/frames/f0003.jpg` | audited | true | high | Evolution/DNA screen for Saplee with a hex-grid unlock tree. Longer-term growth can unlock starting energy and shard triggers, connecting deck archetype to economy. | module-4, module-5, module-6 | true |
| V4 (I4) | `../bv1xaxpbhezc-anode-heart/source/frames/f0004.jpg` | audited | true | high | Combat board with opposing units on the upper half, player units on the lower half, and a hand along the bottom. Combat is lane/row-like rather than a free board: units line up horizontally and resolve across a central divide. | module-3, module-4, module-8 | true |
| V5 (I5) | `../bv1xaxpbhezc-anode-heart/source/frames/f0005.jpg` | not-audited | false | low | Not independently inspected; do not treat caption as visual audit evidence. | module-5 | false |
| V6 (I6) | `../bv1xaxpbhezc-anode-heart/source/frames/f0006.jpg` | audited | true | medium | A modal/card-selection panel is open over combat, showing multiple selectable card slots on Page 1/1. Card effects can open choice panels during combat rather than only resolving instantly. | module-4, module-5 | false |
| V7 (I7) | `../bv1xaxpbhezc-anode-heart/source/frames/f0007.jpg` | audited | true | high | Shop popup with the title Choose a card to buy and three card choices. In-run shop uses shards or a similar currency to buy tactical card effects. | module-4, module-6 | true |
| V8 (I8) | `../bv1xaxpbhezc-anode-heart/source/frames/f0008.jpg` | audited | true | high | Player board has five units including a level 3 unit showing 10/10 and a front unit showing 11/4. The grass/native build can produce very large board stats compared with earlier low-stat frames. | module-3, module-4, module-8 | true |
| V9 (I9) | `../bv1xaxpbhezc-anode-heart/source/frames/f0009.jpg` | not-audited | false | low | Not independently inspected; do not treat caption as visual audit evidence. | module-4 | false |
| V10 (I10) | `../bv1xaxpbhezc-anode-heart/source/frames/f0010.jpg` | audited | true | high | Early combat frame with one enemy unit and one player unit on the board. Summoning a unit can apply a status effect immediately, so unit cards are not only stat bodies. | module-3, module-4 | true |
| V11 (I11) | `../bv1xaxpbhezc-anode-heart/source/frames/f0011.jpg` | not-audited | false | low | Not independently inspected; do not treat caption as visual audit evidence. | module-4 | false |
| V12 (I12) | `../bv1xaxpbhezc-anode-heart/source/frames/f0012.jpg` | not-audited | false | low | Not independently inspected; do not treat caption as visual audit evidence. | module-4 | false |
| V13 (I13) | `../bv1xaxpbhezc-anode-heart/source/frames/f0013.jpg` | audited | true | high | Combat board is divided by a horizontal striped line; enemy units above and player units below. The central line visually separates sides and likely marks combat resolution lanes/rows. | module-3, module-4 | false |
| V14 (I14) | `../bv1xaxpbhezc-anode-heart/source/frames/f0014.jpg` | audited | true | high | Hovered card Munching Saplee shows native / Plant / Tama tags and No Cost. Some cards convert HP gain triggers into native energy, connecting health growth to resource generation. | module-4, module-6 | false |
| V15 (I15) | `../bv1xaxpbhezc-anode-heart/source/frames/f0015.jpg` | audited | true | medium | Level 2 player unit is on the board, with two smaller 1/1 units beside it. Evolution or higher-level units coexist with base units on the same combat row. | module-4, module-5 | false |
| V16 (I16) | `../bv1xaxpbhezc-anode-heart/source/frames/f0016.jpg` | not-audited | false | low | Not independently inspected; do not treat caption as visual audit evidence. | module-4 | false |
| V17 (I17) | `../bv1xaxpbhezc-anode-heart/source/frames/f0017.jpg` | not-audited | false | low | Not independently inspected; do not treat caption as visual audit evidence. | module-5 | false |
| V18 (I18) | `../bv1xaxpbhezc-anode-heart/source/frames/f0018.jpg` | audited | true | medium | Combat frame with a greyed card moving or targeting on the right side, plus colored hit/feedback marks near a unit. High-level cards with large stats are part of the grass/native package. | module-4, module-5 | false |
| V19 (I19) | `../bv1xaxpbhezc-anode-heart/source/frames/f0019.jpg` | audited | true | high | Combat resolution frame shows floating -1 HP text over a top-side unit. Damage/healing feedback is communicated as floating text over units and separate resolution blocks. | module-3, module-4 | true |
| V20 (I20) | `../bv1xaxpbhezc-anode-heart/source/frames/f0020.jpg` | not-audited | false | low | Not independently inspected; do not treat caption as visual audit evidence. | module-4 | false |
| V21 (I21) | `../bv1xaxpbhezc-anode-heart/source/frames/f0021.jpg` | not-audited | false | low | Not independently inspected; do not treat caption as visual audit evidence. | module-4 | false |
| V22 (I22) | `../bv1xaxpbhezc-anode-heart/source/frames/f0022.jpg` | not-audited | false | low | Not independently inspected; do not treat caption as visual audit evidence. | module-4 | false |
| V23 (I23) | `../bv1xaxpbhezc-anode-heart/source/frames/f0023.jpg` | not-audited | false | low | Not independently inspected; do not treat caption as visual audit evidence. | module-4 | false |
| V24 (I24) | `../bv1xaxpbhezc-anode-heart/source/frames/f0024.jpg` | audited | true | high | Hovered card Porren shows native / Plant / Tama tags and No Cost. Some units refund cards on deletion, making death/removal part of resource flow. | module-3, module-4, module-8 | false |
| V25 (I25) | `../bv1xaxpbhezc-anode-heart/source/frames/f0025.jpg` | not-audited | false | low | Not independently inspected; do not treat caption as visual audit evidence. | module-4 | false |
| V26 (I26) | `../bv1xaxpbhezc-anode-heart/source/frames/f0026.jpg` | not-audited | false | low | Not independently inspected; do not treat caption as visual audit evidence. | module-4 | false |
| V27 (I27) | `../bv1xaxpbhezc-anode-heart/source/frames/f0027.jpg` | not-audited | false | low | Not independently inspected; do not treat caption as visual audit evidence. | module-4 | false |
| V28 (I28) | `../bv1xaxpbhezc-anode-heart/source/frames/f0028.jpg` | audited | true | high | Grass deckbuilding screen with deck counters: Apps 8, Tama 0, Patch 0, Virus 0 in the header. Deckbuilder enforces or warns around a 40-card minimum, filling missing slots with blanks. | module-4, module-5, module-8 | true |

## Audited Frame Notes

### V1 / I1

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0001.jpg`
- Confidence: high
- Visible elements: Card collection/library screen with a grid of locked and owned cards. | Top bar shows Page 9/31, a Bitcrush button, and 488 Bits currency. | Right-side detail panel for Saplee shows level, native Plant Tama tag, HP/BP, bonus text, and a revive-trigger effect.
- OCR candidates: Page: 9/31 | 488 Bits | Saplee (LV. 1) | On Revive: +1 HP to this Tama
- Gameplay observations: The collection interface exposes cards as collectible assets with purchase/currency state and individual rule text. | Card identity combines element/type tags, HP/BP stats, bonus growth, and triggered effects.
- UI affordances: Page arrows for browsing card pages. | Close button and Bitcrush action in the library header.
- State changes: none visible from this single frame
- Dossier caption: Card library UI shows collectible cards, Bits currency, and per-card rules rather than only battle state.

### V2 / I2

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0002.jpg`
- Confidence: high
- Visible elements: Deckbuilding screen for a colorless deck: left deck list, right All Cards browser, category counters at the top. | Top counters read Apps: 22, Patch: 3, Tama: 15, Virus: 0; deck area says 40 Cards. | Bottom card detail panel describes Toy Heart as a neutral App that selects one Tama and grants HP with a future HP bonus penalty.
- OCR candidates: 40 Cards | Apps: 22 | Patch: 3 | Tama: 15 | Virus: 0 | Toy Heart [neutral App]
- Gameplay observations: Deck composition is visible as typed counts, making unit/support ratio a deckbuilding constraint. | The deckbuilder separates current deck from the global card pool and supports sorting/import/export.
- UI affordances: Sort, Import, Export buttons. | Test button is present but appears disabled or inactive.
- State changes: none visible from this single frame
- Dossier caption: Deckbuilding view makes card-type ratios and deck size visible before combat.

### V3 / I3

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0003.jpg`
- Confidence: high
- Visible elements: Evolution/DNA screen for Saplee with a hex-grid unlock tree. | Header shows Unlock Evo. with a shard-like cost of 1 and Unlocked: 2/26. | Text says the selected setup starts with 1 native Energy and gains 1 Shard when a Tama gains HP.
- OCR candidates: Unlock Evo. | Unlocked: 2/26 | DNA: Saplee | Start with 1 native Energy. Gain 1 Shard whenever your Tama gain HP.
- Gameplay observations: Longer-term growth can unlock starting energy and shard triggers, connecting deck archetype to economy. | The tree layout suggests multiple passive/evolution nodes rather than a single linear upgrade.
- UI affordances: Arrow navigation in the unlock panel. | Unlock cost indicator near the top-left button.
- State changes: none visible from this single frame
- Dossier caption: Evolution/DNA screen links archetype identity to starting energy and shard income.

### V4 / I4

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0004.jpg`
- Confidence: high
- Visible elements: Combat board with opposing units on the upper half, player units on the lower half, and a hand along the bottom. | Left side has a Pass button and stacked icons/counters; bottom center has Shop and resource bars. | Right edge shows a blue turn/action badge with the number 3 and a deck/card count area.
- OCR candidates: Pass | Shop | HP 11 | BP 3
- Gameplay observations: Combat is lane/row-like rather than a free board: units line up horizontally and resolve across a central divide. | The player manages hand cards, board slots, HP/BP totals, shop access, and pass timing in one combat screen.
- UI affordances: Pass button remains available during the player decision state. | Hand cards are selectable at the bottom.
- State changes: Compared with earlier sparse board frames, this frame shows a developed mid-combat board with six player units.
- Dossier caption: Mid-combat frame shows the main loop surface: hand, board, pass/shop controls, resources, and opposing units.

### V6 / I6

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0006.jpg`
- Confidence: medium
- Visible elements: A modal/card-selection panel is open over combat, showing multiple selectable card slots on Page 1/1. | Left card detail panel describes a native App named nutrient and a health-draining effect from one Tama. | Bottom hand includes green cards and a level 3 card with 10/10 visible stats.
- OCR candidates: Page: 1/1 | nutrient [native App] | Sap 1 HP from 1 Tama | Lv3 | 10/10
- Gameplay observations: Card effects can open choice panels during combat rather than only resolving instantly. | Grass/native package visibly includes HP manipulation and high-level units.
- UI affordances: Cancel button on the selection panel. | Page arrows on the modal.
- State changes: none visible from this single frame
- Dossier caption: Selection modal illustrates in-combat card targeting and grass/native HP manipulation.

### V7 / I7

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0007.jpg`
- Confidence: high
- Visible elements: Shop popup with the title Choose a card to buy and three card choices. | Each option has a shard-like cost below it: 3, 4, and 5. | Highlighted card text says Turbodrive shuffles hand into deck and draws 3 cards.
- OCR candidates: Choose a card to buy. | Turbodrive. Shuffle your hand into the deck. Draw 3 cards. | 3 | 4 | 5
- Gameplay observations: In-run shop uses shards or a similar currency to buy tactical card effects. | Draw/filtering is purchasable mid-run, tying economy directly to draw consistency.
- UI affordances: Close button in shop popup. | Card choices are presented as clickable purchase options.
- State changes: none visible from this single frame
- Dossier caption: Shop frame proves an in-combat/in-run economy surface with purchasable draw effects.

### V8 / I8

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0008.jpg`
- Confidence: high
- Visible elements: Player board has five units including a level 3 unit showing 10/10 and a front unit showing 11/4. | Bottom stats show Shop, shard/resource count, HP 25, and BP 3. | Text box says Your Turn; opponent side has two remaining units.
- OCR candidates: Your Turn. | Lv3 | 10/10 | HP 25 | BP 3
- Gameplay observations: The grass/native build can produce very large board stats compared with earlier low-stat frames. | Turn loop returns to player after board development, preserving hand/board/shop decisions.
- UI affordances: Pass button and hand cards remain available on the player turn.
- State changes: Compared with V4, player HP and board stats are much higher, showing progression inside the match.
- Dossier caption: Late combat frame shows board-growth payoff and player-turn return path.

### V10 / I10

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0010.jpg`
- Confidence: high
- Visible elements: Early combat frame with one enemy unit and one player unit on the board. | Hovered hand card Pawee displays tags neutral / mouse / Tama and No Cost. | Tooltip text states On Summon: inflict Dazed on 1 Tama and cannot attack this round.
- OCR candidates: Pawee | neutral mouse Tama | No Cost. | On Summon: Inflict Dazed on 1 Tama.
- Gameplay observations: Summoning a unit can apply a status effect immediately, so unit cards are not only stat bodies. | Card hover/selection exposes rule text before commitment.
- UI affordances: Pass button on left; hand card tooltip triggered from bottom hand.
- State changes: none visible from this single frame
- Dossier caption: Early combat decision frame shows hand selection, summon text, status effect, and board placement.

### V13 / I13

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0013.jpg`
- Confidence: high
- Visible elements: Combat board is divided by a horizontal striped line; enemy units above and player units below. | Player has six units across the bottom row, suggesting the visible board capacity is capped at six units. | Bottom resource/status area shows Shop, HP, BP, and hand/deck indicators.
- OCR candidates: Shop | HP 15 | BP 3
- Gameplay observations: The central line visually separates sides and likely marks combat resolution lanes/rows. | The six-unit row makes board capacity a tactical limit.
- UI affordances: Pass button available during the state. | Hand cards remain visible under the board.
- State changes: Player board is full or near full, unlike sparse early combat frames.
- Dossier caption: Fuller board frame supports board-capacity and lane-resolution analysis.

### V14 / I14

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0014.jpg`
- Confidence: high
- Visible elements: Hovered card Munching Saplee shows native / Plant / Tama tags and No Cost. | Card text includes On Trigger, selecting one Tama, HP gain, HP bonus gain, and then gaining native Energy. | Top and bottom bars show separate colored energy/resource counters.
- OCR candidates: Munching Saplee | native Plant Tama | No Cost. | Then: Gain 1 native Energy.
- Gameplay observations: Some cards convert HP gain triggers into native energy, connecting health growth to resource generation. | The UI distinguishes generic and native/element-specific resource pools.
- UI affordances: Hover panel gives detailed timing text and bonus/stat preview.
- State changes: none visible from this single frame
- Dossier caption: Card tooltip shows energy generation tied to trigger timing and HP growth.

### V15 / I15

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0015.jpg`
- Confidence: medium
- Visible elements: Level 2 player unit is on the board, with two smaller 1/1 units beside it. | Player hand includes two pink unit cards and one 3/2 unit card. | Top-right deck/count indicator and bottom Shop/HP/BP bars remain visible.
- OCR candidates: Lv2 | HP 6 | BP 3
- Gameplay observations: Evolution or higher-level units coexist with base units on the same combat row. | The frame supports the existence of level states, but not the full evolution prerequisite by itself.
- UI affordances: Pass remains available; hand cards can still be played or held.
- State changes: none visible from this single frame
- Dossier caption: A level 2 unit on board visually supports the evolution/level layer, with exact prerequisites requiring text confirmation.

### V18 / I18

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0018.jpg`
- Confidence: medium
- Visible elements: Combat frame with a greyed card moving or targeting on the right side, plus colored hit/feedback marks near a unit. | Bottom hand includes a level 3 card whose large 10/10 stat line is visible. | Board contains several green-bordered native/plant units with varied stats.
- OCR candidates: Lv3 | 10/10
- Gameplay observations: High-level cards with large stats are part of the grass/native package. | Visual feedback indicates an action or effect resolving, but exact cause requires transcript support.
- UI affordances: The right-side ghosted card/arrow suggests targeting, movement, or resolution feedback.
- State changes: none visible from this single frame
- Dossier caption: High-level grass/native card and combat feedback support the growth-route discussion, with causal details uncertain.

### V19 / I19

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0019.jpg`
- Confidence: high
- Visible elements: Combat resolution frame shows floating -1 HP text over a top-side unit. | Left side displays blocks of numbered damage or resolution tiles, including 2, 3, 4, 2, 3 and a lower row 2, 1. | Player board has six units, with bottom stats showing HP 13 and BP 3.
- OCR candidates: -1 HP | HP 13 | BP 3
- Gameplay observations: Damage/healing feedback is communicated as floating text over units and separate resolution blocks. | Resolution appears stepwise/ordered, with visible damage blocks on the left.
- UI affordances: Pass button is dark/disabled during resolution, implying player input is locked while effects resolve.
- State changes: Compared with decision frames, this one appears to be an automatic resolution state.
- Dossier caption: Resolution frame shows floating HP feedback and ordered damage blocks while input is disabled.

### V24 / I24

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0024.jpg`
- Confidence: high
- Visible elements: Hovered card Porren shows native / Plant / Tama tags and No Cost. | Card text reads On Delete: Draw 1 card. | Player hand contains several non-unit cards/cards with App-like icons while only one player unit is on board.
- OCR candidates: Porren | On Delete: Draw 1 card. | No Cost.
- Gameplay observations: Some units refund cards on deletion, making death/removal part of resource flow. | The frame visually supports draw variance concerns: hand composition can be non-unit-heavy while board presence is thin.
- UI affordances: Hover detail panel and Pass button support inspection before action.
- State changes: none visible from this single frame
- Dossier caption: Draw-on-delete card and thin board state support the deck-consistency risk discussion.

### V28 / I28

- Path: `../bv1xaxpbhezc-anode-heart/source/frames/f0028.jpg`
- Confidence: high
- Visible elements: Grass deckbuilding screen with deck counters: Apps 8, Tama 0, Patch 0, Virus 0 in the header. | Warning text says the deck contains less than 40 cards and will be filled out with Blanks in game. | Right panel shows Page 1/5 card pool filtered to native Element, and selected Tanukee costs 2 native Energy and draws 1 card on summon.
- OCR candidates: Apps: 8 | Tama: 0 | Patch: 0 | Virus: 0 | Your deck contains less than 40 cards! | Tanukee ... Cost: 2 native Energy. On Summon: Draw 1 Card.
- Gameplay observations: Deckbuilder enforces or warns around a 40-card minimum, filling missing slots with blanks. | Card pool filtering by element/type supports archetype-specific rebuilding after failures.
- UI affordances: Sort, Import, Export, Test controls; card-pool page arrows and filter label.
- State changes: This frame contrasts with V2 by showing grass/native filtering and an incomplete deck warning.
- Dossier caption: Grass deckbuilder frame shows minimum-deck warning, typed counts, and elemental card-pool filtering.
