# Module Writing Standard

Write the dossier from the outline, not directly from the raw material pack.

## General Rules

- Write the dossier in Simplified Chinese. English is allowed only for fixed game terms, file paths, evidence ids, JSON keys, Mermaid syntax, or short bilingual structural aliases.
- Use Chinese-first stable headings for required sections, optionally with English aliases for scripts: `## 证据地图 / Evidence Map`, `## 图文证据 / Visual Evidence`, `## 模块1：... / Module 1`, `## 对本项目的转化 / Project Transfer`, and `## 未确认信息 / Unknowns`.
- Start each module with a conclusion.
- Then explain evidence and reasoning.
- Add “对本项目的启示” when the module is relevant.
- If evidence is thin, say so directly.
- Avoid broad praise or review language. Tie judgments to player actions, system purpose, output, cost, feedback, and risk.
- When visual audit evidence exists, write as a 图文稿: embed selected images next to the claim they support, then explain what the image proves and what it does not prove.

## Module Priorities

Module 3 and module 4 determine whether the dossier is a real game-design breakdown.

### Module 3: Core Loop

Must include:

- Mermaid core loop diagram.
- 1-3 screenshot embeds when available, showing loop steps, action choice, combat resolution, or feedback.
- Player input.
- Player action.
- System output.
- Cost or constraint.
- Feedback.
- Return path.

### Module 4: System Architecture

Must include:

- Mermaid system relation diagram.
- 1-3 screenshot embeds when available, showing system surfaces such as deckbuilding, shop, resource, evolution, map, or board layout.
- Major systems.
- Inputs and outputs.
- How systems reinforce or dilute the core loop.

## Conservative Modules

If materials do not support a module:

- Module 1: do not invent release, revenue, retention, or rating data.
- Module 5: describe only visible or documented content structure.
- Module 6: separate combat cost from long-term economy.
- Module 7: describe only visible narrative, UI, audio, or visual evidence.

## Visual Writing Rules

- Cite visual audit ids (`V1`, `V2`) when making image-based claims.
- Use raw image ids (`I1`, `I2`) only as timestamp/frame anchors when no visual audit was performed.
- Do not rely on low-confidence OCR for exact card text, numbers, or rule wording.
- Keep image captions analytical: “这张图支撑了什么机制判断”, not “画面如上”.
- If visual and text evidence disagree, add the disagreement to “未确认信息”.

## Project Transfer

This repository’s current project is a 2D turn-based card battler around one unique core card. In “对本项目的转化”, prioritize:

- Unique core card identity.
- Common support card pool.
- Cost tradeoffs.
- Combo rules.
- Dynamic balance at the combo/rule layer.

Do not suggest adding world maps, full trading markets, AI generation pipelines, or long-term monetization systems in Phase 1 unless the user explicitly asks.
