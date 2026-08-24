# Phase 1 Workflow

Use this workflow when converting supplied game screenshots, transcripts, BiliSum notes, or text observations into a structured game analysis dossier.

## Boundary

Phase 1 does:

- Validate a local material pack.
- Run a visual audit for supplied screenshots or keyframes.
- Build an evidence map from supplied materials.
- Generate an eight-module outline.
- Write an illustrated module-by-module game analysis dossier.
- Run structural checks.

Phase 1 does not:

- Download or parse videos.
- Run ASR.
- Browse for market data or current facts.
- Perform multi-model review or iterative rewriting.
- Write into `game-design-workflow/core-concept.md`.

Visual extraction is allowed only for local screenshots or keyframes already supplied in the material pack. If no multimodal model is available, create the visual audit scaffold and mark frames as `not-audited`; the dossier may still use captions and text evidence, but must state that visual evidence was not independently read.

## Procedure

1. Validate inputs with `validate_material_pack.py`.
2. Read text sources and image observations from the pack.
3. If images exist, run the visual audit step:
   - Generate `visual/visual-audit.json` and `visual/visual-audit.md`.
   - Inspect each selected frame with a multimodal model or manual visual review.
   - Extract visible gameplay facts: UI layout, board state, card text, costs, action availability, feedback, affordances, and temporal state changes.
   - Mark each observation as `high`, `medium`, or `low` confidence.
   - Record contradictions against transcript/captions as conflicts.
4. Build an evidence map:

```text
evidence id -> type -> source path -> observations -> supported modules -> confidence -> audit status
```

5. Generate an outline scaffold with `scaffold_outline.py`.
6. Fill outline claims:
   - Overall thesis.
   - Claims for each of the eight modules.
   - Evidence references for each module.
   - Missing-information notes.
   - Selected image candidates for illustrated sections.
   - Diagram plans.
7. Generate a dossier scaffold with `scaffold_dossier.py`.
8. Write modules in this order:
   - Module 3: core loop.
   - Module 4: system architecture.
   - Module 2: player experience.
   - Modules 1, 5, 6, 7, 8.
9. Add image embeds only where the image directly supports the module claim. Prefer 4-10 images in the final dossier, not every frame.
10. Run `check_phase1_outputs.py`.
11. Report generated files, visual-audit status, and open gaps.

## PaperOrchestra Mapping

PaperOrchestra turns unconstrained pre-writing materials into a formal paper through outline, literature review, plotting, section writing, and refinement. Phase 1 borrows only:

- Outline first.
- Section/module writing after outline.
- Diagrams as first-class outputs.
- Deterministic helpers for structure checks.

## AutoSurvey Mapping

AutoSurvey organizes large reference sets into an outline, drafts subsections, and evaluates survey quality. Phase 1 borrows only:

- Explicit section count and section roles.
- Local evidence assignment before writing.
- Per-module writing from local evidence.

External retrieval and evaluation loops are reserved for later phases.
