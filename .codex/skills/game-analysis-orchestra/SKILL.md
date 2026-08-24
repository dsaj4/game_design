---
name: game-analysis-orchestra
description: Turn game screenshots, video notes, transcripts, and text materials into structured game analysis outlines and module-by-module design dossiers. Use when the user asks to generate a game breakdown, gameplay analysis, product case study, design dossier, or BiliSum-derived game analysis from a material pack, images, screenshots, notes, or transcripts.
---

# Game Analysis Orchestra

Use this skill to run the Phase 1 game-analysis workflow:

```text
material pack -> visual audit -> evidence map -> outline -> illustrated module-by-module dossier -> phase-1 check
```

Phase 1 is inspired by PaperOrchestra and AutoSurvey, but it only works from supplied local materials. Do not browse, download videos, run ASR, or change core game-design documents unless the user explicitly asks for a later workflow.

When screenshots or keyframes are available, run a visual audit before writing the outline. If the current agent has any direct image-reading capability, it must open and inspect the image files themselves; do not rely only on captions, filenames, BiliSum visual notes, or material-pack observations. Modern multimodal models can extract useful gameplay signals from game screenshots, but their observations must be treated as auditable evidence, not as final truth. Cross-check visual claims against transcript text, captions, and nearby frames.

## Inputs

Prefer a `materialpack.json` matching `assets/materialpack.schema.json`. If the user gives loose files instead, first create or update a material pack.

Minimum useful inputs:

- One project section with `game_name`, `slug`, `analysis_scope`, `status`, and `target_questions`.
- At least one text source or one image.
- Image entries should include captions, evidence tags, and observations.

## Workflow

1. Read `references/workflow.md`.
2. Validate the material pack:

```powershell
py -3 .codex/skills/game-analysis-orchestra/scripts/validate_material_pack.py --pack <materialpack.json>
```

3. If the pack contains images, read `references/visual-audit.md`, then generate a visual audit scaffold:

```powershell
py -3 .codex/skills/game-analysis-orchestra/scripts/scaffold_visual_audit.py --pack <materialpack.json> --out <workspace>
```

4. Fill `visual/visual-audit.json` and `visual/visual-audit.md` from direct image reading:
   - If the agent has a visual/image tool, open the actual image paths and inspect the pixels.
   - If the agent has no image-reading capability, keep frames as `status: not-audited`, add a limitation note, and continue from text/caption evidence only.
   - Never mark a frame `audited` by copying `caption`, `source_observations`, transcript text, or filename hints.
   - Extract only visible or strongly inferable information: UI layout, card text, costs, board state, feedback, affordances, and frame-to-frame state changes. Mark uncertainty and conflicts.
5. Validate the visual audit when it is filled:

```powershell
py -3 .codex/skills/game-analysis-orchestra/scripts/check_visual_audit.py --workspace <workspace>
```

6. Generate an outline scaffold:

```powershell
py -3 .codex/skills/game-analysis-orchestra/scripts/scaffold_outline.py --pack <materialpack.json> --visual-audit <workspace>/visual/visual-audit.json --out <workspace>
```

7. Read `references/outline-standard.md`, then edit `outline/outline.md` and `outline/outline.json` with actual claims, evidence, missing-information notes, visual evidence references, and diagram plans.
8. Read `references/module-writing.md`.
9. Generate a dossier scaffold:

```powershell
py -3 .codex/skills/game-analysis-orchestra/scripts/scaffold_dossier.py --pack <materialpack.json> --outline <workspace>/outline/outline.json --out <workspace>
```

10. Write the dossier module by module. Prioritize module 3, module 4, then module 2. If visual audit exists, include a “图文证据” section and use selected screenshots inside the relevant modules.
11. Run the Phase 1 check:

```powershell
py -3 .codex/skills/game-analysis-orchestra/scripts/check_phase1_outputs.py --workspace <workspace>
```

12. Report output files, visual-audit status, and the most important remaining gaps.

## Writing Rules

- Default to Simplified Chinese for all human-facing generated content: visual audit notes, outline claims, dossier prose, image captions, module conclusions, transfer hypotheses, and unknowns.
- Stable machine-readable ids may stay in ASCII, such as `module-3`, `V4`, `T1`, file paths, JSON keys, Mermaid syntax, and short structural aliases. Do not write the main dossier body in English unless the user explicitly asks for English.
- On Windows or mixed-encoding terminals, keep required Markdown headings bilingual or Chinese-first, for example `## 证据地图 / Evidence Map`, `## 模块3：核心玩法循环 / Module 3: Core Loop`. If Chinese heading text becomes corrupted, regenerate the heading instead of switching the whole document to English.
- Treat supplied materials as evidence, not as final conclusions.
- Distinguish facts, screenshot observations, visual-model observations, text-based inference, and author judgment.
- Do not invent commercial data, player metrics, release dates, or live-version facts.
- Keep all eight game-analysis modules in order, but write “materials insufficient” when evidence is thin.
- Always include a core loop diagram in module 3 and a system relation diagram in module 4.
- Always include “对本项目的转化” and “未确认信息”.
- Never use image OCR or UI interpretation as a high-confidence claim unless the visual audit marks it high confidence or text evidence confirms it.
- A frame marked `audited` must include direct-image-reading evidence in the visual audit. If direct reading did not happen, use `not-audited`.

## References

- `references/workflow.md`: Phase 1 procedure and source-project inspiration.
- `references/material-pack.md`: Material pack fields and evidence rules.
- `references/visual-audit.md`: Screenshot/keyframe visual extraction rules.
- `references/outline-standard.md`: Outline JSON/Markdown requirements.
- `references/module-writing.md`: Module-by-module writing standards.
- `references/source-inspirations.md`: PaperOrchestra and AutoSurvey mapping.

## Assets

- `assets/materialpack.schema.json`: Material pack schema.
- `assets/outline-template.md`: Human-readable outline template.
- `assets/dossier-template.md`: Game analysis dossier template.
