# Phase 1 Workflow

Use this workflow when converting supplied game screenshots, transcripts, BiliSum notes, or text observations into a structured game analysis dossier.

## Boundary

Phase 1 does:

- Validate a local material pack.
- Build an evidence map from supplied materials.
- Generate an eight-module outline.
- Write a module-by-module game analysis dossier.
- Run structural checks.

Phase 1 does not:

- Download or parse videos.
- Run ASR or VLM extraction.
- Browse for market data or current facts.
- Perform multi-model review or iterative rewriting.
- Write into `game-design-workflow/core-concept.md`.

## Procedure

1. Validate inputs with `validate_material_pack.py`.
2. Read text sources and image observations from the pack.
3. Build an evidence map:

```text
evidence id -> type -> source path -> observations -> supported modules -> confidence
```

4. Generate an outline scaffold with `scaffold_outline.py`.
5. Fill outline claims:
   - Overall thesis.
   - Claims for each of the eight modules.
   - Evidence references for each module.
   - Missing-information notes.
   - Diagram plans.
6. Generate a dossier scaffold with `scaffold_dossier.py`.
7. Write modules in this order:
   - Module 3: core loop.
   - Module 4: system architecture.
   - Module 2: player experience.
   - Modules 1, 5, 6, 7, 8.
8. Run `check_phase1_outputs.py`.
9. Report generated files and open gaps.

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
