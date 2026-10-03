---
name: gdd-toolkit
description: Review specified game-design goals, system interactions, pairwise edge cases, MDA hypotheses, or explicitly requested GDD-versus-code drift. Use for focused GDD consistency checks and qualified GDD drafting under the project's registered workflow; not for automatic project discovery, generic idea generation, or creating a second document system.
license: MIT
metadata:
  upstream_version: "2.3.0"
  upstream_author: "Mamoru Miyagawa"
  adaptation: "game-project-1"
---

# GDD Toolkit — project methods edition

Read [project-integration.md](references/project-integration.md) before reading game documents or writing outputs. Follow the project's material scope, qualification gates and existing document locations. This adaptation preserves the upstream method references but replaces its automatic discovery, sidecar storage and CLI workflow. The repository-root gdd.py and installers are not included; do not invoke or fetch them to initialize this project.

## Choose one focused mode

| Request | Work |
| --- | --- |
| Check a feature against goals | Trace player decisions to the already-stated goals; expose support, tension and tradeoffs |
| Check system interactions | Select relevant pairs, state input/output and timing assumptions, find conflicting boundaries |
| MDA analysis | Separate mechanics, predicted behavior and intended experience; keep predictions unverified |
| Audit GDD against code | Only when requested: compare named design and implementation versions; record differences without making code the design authority |
| Draft a formal GDD | First apply the project's qualification and material review process, then its registered GDD template |

Use the narrowest mode that answers the task. Do not run every tool, inspect every system or open external code at session start. No project automatically inherits another project's gameplay.

## Relevant references

- Goals and tradeoffs: references/pillars-reference.md.
- Failure hypotheses and review questions: references/failure-modes.md.
- Mechanics, behavior and experience: references/templates/mda-reference.md.
- Core-loop reasoning: references/templates/core-loop-canvas.md; its example durations are not requirements.
- Numeric relationships: references/templates/balance-table.md; accepted project parameters remain authoritative for their version.
- Interface reasoning: references/templates/system-design.md; use its questions, not its storage/template contract.

The other upstream templates, domain adapter example, flowcharts and Obsidian layout are retained for provenance and optional method comparison. They do not authorize scaffolding, automatic code access or new formal templates. Their operational instructions are overridden by project-integration.md. Load only relevant references.

## Review procedure

1. Name the decision, target Project/DIR, fixed source versions and allowed file/section list. Preserve Unknown and unread coverage.
2. Extract the stated goals, player actions and rule interfaces from those materials. Distinguish accepted rules, candidates, historical records and implementation evidence.
3. Review the selected objects. For a pair, record A/B, shared state, timing/conditions, expected effect, source, contradiction or Unknown. A justified non-interaction is valid.
4. Separate document ambiguity from actual design conflict and absent player evidence. Recommendations do not resolve undecided gameplay.
5. Record results at the existing project location authorized for this task. Raw analysis stays in the direction or inbox; qualified formal documents use registered templates. Technical details remain in the implementation repository.
6. State coverage, findings, tradeoffs, remaining questions and the smallest next decision or validation. Batch independent clarification questions with recommendations and impacts.

Writing a review does not change design status. Code divergence does not automatically justify modifying GDD. A matrix or MDA prediction does not prove fun or completeness. Explicitly authorized implementation or testing follows the target repository workflow; this skill does not start it on its own.

Source: [source-lock.json](source-lock.json). License: [MIT](LICENSE).
