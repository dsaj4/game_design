# Material Pack Standard

Use `assets/materialpack.schema.json` as the structural source of truth.

## Required Sections

`project`:

- `game_name`: Display name of the analyzed game or sample.
- `slug`: Lowercase identifier for output filenames.
- `analysis_scope`: Full dossier, combat-only, economy-only, screenshot-only test, etc.
- `status`: Usually `Research / Prototype Lab` in Phase 1.
- `target_questions`: Questions the dossier must answer.

`text_sources`:

- Local Markdown/text sources such as transcripts, BiliSum visual notes, playtest notes, or manual observations.
- Each source needs `path`, `role`, and optional `description`.

`images`:

- Local screenshots or keyframes.
- Each image needs `path`, `caption`, and `observations`.
- Add `evidence_tags` such as `core-loop`, `combat-system`, `economy`, `content`, `ui`, `narrative`.

`draft_seed`:

- Optional structured notes for deterministic scaffolding.
- Use only as a starting point; do not treat it as verified truth.

## Evidence Rules

- Every important claim should cite one or more evidence ids, or be marked as inference.
- Image evidence proves visible UI layout, states, affordances, feedback, or visual hierarchy.
- Text evidence proves recorded rules, player actions, transcript claims, and manual observations.
- Missing materials must produce “未确认信息”, not fabricated facts.

## Suggested Evidence IDs

Use stable ids in outlines and dossiers:

```text
T1: materials.md
I1: images/battle-layout.svg
```

When line numbers are available, include them:

```text
T1:L12-L18
```
