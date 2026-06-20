# Subagent After Path Fix Test Notes

Status: Historical PASS; after Chinese-output gate, Phase 1 check is NEEDS WORK

## Scope

- Skill: `E:\Project\game\.codex\skills\game-analysis-orchestra`
- Material pack: `E:\Project\game\media-analysis-lab\runs\bv1xaxpbhezc-anode-heart\inputs\materialpack.json`
- Output workspace: `E:\Project\game\media-analysis-lab\runs\bv1xaxpbhezc-anode-heart-subagent-after-path-fix-test`

## Result

The repaired workflow completed end to end:

- `check_visual_audit.py`: PASS, 8 / 8 checks.
- Original `check_phase1_outputs.py`: PASS, 10 / 10 checks.
- After adding the Simplified Chinese body requirement, `check_phase1_outputs.py`: NEEDS WORK, 10 / 11 checks.
- Audited frames: 8 / 28.
- All audited frames have `direct_image_read: true`.
- The dossier contains 6 embedded images.
- All embedded image paths resolve from the generated `drafts/` directory back to the original source frames.

## Key Finding

The path fix worked. `source_path_absolute` preserved the original frame location when the material pack and output workspace lived in different run directories, and dossier-relative image embeds resolved correctly.

## Remaining Friction

- Some source text or generated headings can still show mojibake in Windows console paths or mixed-encoding flows.
- The skill now recommends stable ASCII headings for required structure while allowing Chinese prose under those headings.
- Visual audit quality is useful but still partial: only selected frames were directly read in this validation run.
- This run's dossier used too much English prose. It is kept as an after-fix historical workflow test, but it no longer satisfies the current Chinese-output requirement.
