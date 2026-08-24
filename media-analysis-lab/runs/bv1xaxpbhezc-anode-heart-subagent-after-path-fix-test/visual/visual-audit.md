# Anode Heart: Layer Null Visual Audit

This audit was performed from direct local image reads using the actual JPG files under the source run. The material pack captions were not treated as visual evidence because they are BiliSum/provider-none anchors and appear mojibake in this console.

## Summary

- Frames in pack: 28
- Directly audited frames: 8
- Not audited frames: 20
- Direct image reading worked from `source_path_absolute` even though this output workspace is a different sibling run directory.
- Dossier illustration candidates: V4, V10, V13, V14, V15, V19, V23, V25

## Frame Audit

| ID | Image | Status | Direct read | Confidence | Visible/gameplay notes | Modules | Illustration |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V1 | `../source/frames/f0001.jpg` | not-audited | false | low | Not independently inspected. | module-1, module-4 | false |
| V2 | `../source/frames/f0002.jpg` | not-audited | false | low | Not independently inspected. | module-4, module-5 | false |
| V3 | `../source/frames/f0003.jpg` | not-audited | false | low | Not independently inspected. | module-4, module-5 | false |
| V4 | `../source/frames/f0004.jpg` | audited | true | medium | Grid battle board with deployed units, hand, Pass, HP/BP, shop, and deck/discard counters; supports the main combat decision surface. | module-2, module-3, module-4, module-8 | true |
| V5 | `../source/frames/f0005.jpg` | not-audited | false | low | Not independently inspected. | module-2, module-5, module-8 | false |
| V6 | `../source/frames/f0006.jpg` | not-audited | false | low | Not independently inspected. | module-4, module-5 | false |
| V7 | `../source/frames/f0007.jpg` | not-audited | false | low | Not independently inspected. | module-3, module-4, module-5 | false |
| V8 | `../source/frames/f0008.jpg` | not-audited | false | low | Not independently inspected. | module-4, module-5, module-8 | false |
| V9 | `../source/frames/f0009.jpg` | not-audited | false | low | Not independently inspected. | module-3, module-5 | false |
| V10 | `../source/frames/f0010.jpg` | audited | true | medium | Tooltip for Pawee exposes tags, no cost, On Summon Dazed effect, and stat fields while board and hand stay visible. | module-3, module-4, module-6 | true |
| V11 | `../source/frames/f0011.jpg` | not-audited | false | low | Not independently inspected. | module-3, module-4 | false |
| V12 | `../source/frames/f0012.jpg` | not-audited | false | low | Not independently inspected. | module-4, module-6 | false |
| V13 | `../source/frames/f0013.jpg` | audited | true | medium | Near-full board and battle HUD show capacity pressure alongside shop/resource, HP/BP, and deck state. | module-3, module-4, module-6 | true |
| V14 | `../source/frames/f0014.jpg` | audited | true | medium | Tooltip for Munching Saplee links tag choice, HP growth, bonus growth, and native energy generation. | module-3, module-4, module-6 | true |
| V15 | `../source/frames/f0015.jpg` | audited | true | medium | Level-2 unit with higher visible stats supports the existence of a growth/evolution layer, but exact prerequisites need text evidence. | module-4, module-5, module-6 | true |
| V16 | `../source/frames/f0016.jpg` | not-audited | false | low | Not independently inspected. | module-4, module-5, module-6 | false |
| V17 | `../source/frames/f0017.jpg` | not-audited | false | low | Not independently inspected. | module-5, module-8 | false |
| V18 | `../source/frames/f0018.jpg` | not-audited | false | low | Not independently inspected. | module-4, module-5, module-6 | false |
| V19 | `../source/frames/f0019.jpg` | audited | true | medium | Wide grass board, visible HP feedback, and high-stat hand/deployed units support recovery/growth board pressure. | module-3, module-4, module-5, module-6 | true |
| V20 | `../source/frames/f0020.jpg` | not-audited | false | low | Not independently inspected. | module-3, module-4 | false |
| V21 | `../source/frames/f0021.jpg` | not-audited | false | low | Not independently inspected. | module-3, module-4 | false |
| V22 | `../source/frames/f0022.jpg` | not-audited | false | low | Not independently inspected. | module-3, module-4, module-6 | false |
| V23 | `../source/frames/f0023.jpg` | audited | true | medium | Bear tooltip exposes typed native cost, BLOCK/spillover wording, On Summon draw, and HP/BP fields. | module-3, module-4, module-6 | true |
| V24 | `../source/frames/f0024.jpg` | not-audited | false | low | Not independently inspected. | module-3, module-4, module-8 | false |
| V25 | `../source/frames/f0025.jpg` | audited | true | medium | Explicit response prompt says to play a card in response or pass, showing counterplay timing and availability constraints. | module-3, module-4, module-8 | true |
| V26 | `../source/frames/f0026.jpg` | not-audited | false | low | Not independently inspected. | module-3, module-4, module-8 | false |
| V27 | `../source/frames/f0027.jpg` | not-audited | false | low | Not independently inspected. | module-3, module-4, module-8 | false |
| V28 | `../source/frames/f0028.jpg` | not-audited | false | low | Not independently inspected. | module-3, module-4, module-6 | false |

## Audit Notes

- OCR was used only as candidate evidence. Exact rules are cited from text sources unless the frame text is clear enough and marked medium confidence.
- No audited observation was copied from the material-pack captions.
- The path fix is visible in the scaffolded `source_path_absolute` fields: those absolute paths opened correctly from a different output workspace.
