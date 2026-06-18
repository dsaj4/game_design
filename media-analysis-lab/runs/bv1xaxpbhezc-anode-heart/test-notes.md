# BiliSum Real Material Test Notes

Status: Phase 1 real test complete

## Input

- Source: BiliSum task `8ebfffe6b2ea4128ad7ff1de05e425e2`
- Video: `BV1xAXPBHEzc`
- Game: `Anode Heart: Layer Null`
- Text sources: 4
- Image sources: 28 frames

## Outputs

- `inputs/materialpack.json`
- `outline/outline.json`
- `outline/outline.md`
- `drafts/bv1xaxpbhezc-anode-heart-dossier.md`
- `checks/phase1-check.md`

## Result

`check_phase1_outputs.py` passed 9 / 9.

The generated dossier is a real Chinese game-analysis draft, not only a scaffold. It covers:

- Core positioning.
- Player experience.
- Core loop.
- System architecture.
- Content progression.
- Resource/economy loop.
- Narrative and visual packaging limits.
- Strengths, risks, and transfer hypotheses for the current unique-core-card project.

## Pipeline Findings

1. Material-pack paths are resolved relative to the pack file location. Because this run stores the pack under `inputs/`, references to source files must use `../source/...`.
2. PowerShell pipeline input can corrupt Chinese string literals passed into inline Python on this machine. For future scripts, either read Chinese text from UTF-8 files or keep generated control fields in ASCII/English.
3. BiliSum visual evidence had `provider=none`; frames are useful timestamped evidence, but not OCR-grade visual interpretation.

## Next Suggested Step

Run a Phase 2 review pass on the dossier using the existing `research/08-analysis-quality-system/review-rubric.md`, then decide which weak modules should be revised first.
