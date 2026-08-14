# Subagent Direct Image Reading Test Notes

Status: Partial success / needs work

## Scope

- Skill: `E:\Project\game\.codex\skills\game-analysis-orchestra`
- Material pack: `E:\Project\game\media-analysis-lab\runs\bv1xaxpbhezc-anode-heart\inputs\materialpack.json`
- Output workspace: `E:\Project\game\media-analysis-lab\runs\bv1xaxpbhezc-anode-heart-subagent-direct-read-test`

## Result

The subagent successfully tested the direct-image-reading part of the skill:

- 15 frames were marked `audited`.
- All audited frames set `direct_image_read: true`.
- 13 frames remained `not-audited`.
- `check_visual_audit.py` passed 8 / 8.

The full Phase 1 workflow did not complete:

- `outline/outline.json` and `outline/outline.md` are scaffold outputs.
- No dossier was generated.
- `check_phase1_outputs.py` was not run.

## Useful Finding

The visual audit produced genuinely new visual observations beyond BiliSum captions, including UI text, card details, resource counters, deckbuilding counters, board layout, and combat feedback.

## Friction Found

When a material pack from one run is used to write outputs into a different run directory, image paths such as `../source/frames/f0001.jpg` are ambiguous. The skill scripts were updated after this test to preserve `source_path_absolute` in visual-audit and outline evidence, and to convert image embeds relative to the generated dossier.
