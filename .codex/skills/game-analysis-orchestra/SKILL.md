---
name: game-analysis-orchestra
description: Turn game screenshots, video notes, transcripts, and text materials into structured game analysis outlines and module-by-module design dossiers. Use when the user asks to generate a game breakdown, gameplay analysis, product case study, design dossier, or BiliSum-derived game analysis from a material pack, images, screenshots, notes, or transcripts.
---

# Game Analysis Orchestra

Use this skill to run the Phase 1 game-analysis workflow:

```text
material pack -> evidence map -> outline -> module-by-module dossier -> phase-1 check
```

Phase 1 is inspired by PaperOrchestra and AutoSurvey, but it only works from supplied local materials. Do not browse, download videos, run ASR, or change core game-design documents unless the user explicitly asks for a later workflow.

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

3. Generate an outline scaffold:

```powershell
py -3 .codex/skills/game-analysis-orchestra/scripts/scaffold_outline.py --pack <materialpack.json> --out <workspace>
```

4. Read `references/outline-standard.md`, then edit `outline/outline.md` and `outline/outline.json` with actual claims, evidence, missing-information notes, and diagram plans.
5. Read `references/module-writing.md`.
6. Generate a dossier scaffold:

```powershell
py -3 .codex/skills/game-analysis-orchestra/scripts/scaffold_dossier.py --pack <materialpack.json> --outline <workspace>/outline/outline.json --out <workspace>
```

7. Write the dossier module by module. Prioritize module 3, module 4, then module 2.
8. Run the Phase 1 check:

```powershell
py -3 .codex/skills/game-analysis-orchestra/scripts/check_phase1_outputs.py --workspace <workspace>
```

9. Report output files, status, and the most important remaining gaps.

## Writing Rules

- Treat supplied materials as evidence, not as final conclusions.
- Distinguish facts, screenshot observations, text-based inference, and author judgment.
- Do not invent commercial data, player metrics, release dates, or live-version facts.
- Keep all eight game-analysis modules in order, but write “materials insufficient” when evidence is thin.
- Always include a core loop diagram in module 3 and a system relation diagram in module 4.
- Always include “对本项目的转化” and “未确认信息”.

## References

- `references/workflow.md`: Phase 1 procedure and source-project inspiration.
- `references/material-pack.md`: Material pack fields and evidence rules.
- `references/outline-standard.md`: Outline JSON/Markdown requirements.
- `references/module-writing.md`: Module-by-module writing standards.
- `references/source-inspirations.md`: PaperOrchestra and AutoSurvey mapping.

## Assets

- `assets/materialpack.schema.json`: Material pack schema.
- `assets/outline-template.md`: Human-readable outline template.
- `assets/dossier-template.md`: Game analysis dossier template.
