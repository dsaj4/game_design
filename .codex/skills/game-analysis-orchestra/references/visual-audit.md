# Visual Audit Standard

Use this step when the material pack contains screenshots or video keyframes. Game mechanics are often visible before they are explained in text: board layout, action affordances, card costs, UI states, animation feedback, damage resolution, deckbuilding constraints, and moment-to-moment player choices.

## Capability Boundary

Modern multimodal models are useful for game screenshot analysis, especially:

- Reading large UI labels, card titles, short card text, numbers, costs, HP, attack, counters, and button states.
- Identifying visible layout: hand, board, deck, discard, shop, map, inventory, skill tree, timeline, phase indicator, and resource bars.
- Comparing nearby frames to infer state changes such as card played, unit removed, damage dealt, resource spent, or reward gained.
- Describing feedback: highlights, animations, popups, warnings, targeting lines, and disabled controls.

They are weaker at:

- Small or stylized OCR, cropped text, low-resolution frames, fast animations, hidden rules, offscreen state, and cause-effect chains across long time gaps.
- Distinguishing real mechanics from streamer commentary unless text evidence confirms it.
- Inferring meta balance, player metrics, monetization, or complete progression from a few frames.

## Required Output

Generate:

- `visual/visual-audit.json`
- `visual/visual-audit.md`

Each audited frame should include:

```json
{
  "id": "V1",
  "image_id": "I1",
  "path": "../source/frames/f0001.jpg",
  "status": "audited",
  "confidence": "medium",
  "visible_elements": [],
  "ocr_candidates": [],
  "gameplay_observations": [],
  "ui_affordances": [],
  "state_changes": [],
  "supports_modules": ["module-3", "module-4"],
  "conflicts": [],
  "illustration_candidate": true,
  "caption_for_dossier": ""
}
```

Use `status: not-audited` when no model or manual visual review was used. Use `status: needs-review` when OCR or state interpretation is uncertain.

## Evidence Rules

- A visual observation can directly support claims about what is visible.
- A visual observation can only support hidden rules when text evidence or multiple frames confirm the rule.
- OCR candidates must stay candidates unless confidence is high or text evidence confirms the same wording/number.
- If transcript and image disagree, keep both and record a conflict instead of smoothing it over.
- Prefer concise observations over long image descriptions.

## Illustrated Dossier Rules

The final dossier should become a 图文稿 when useful visual evidence exists:

- Embed selected screenshots with Markdown image syntax near the relevant module.
- Use local relative paths from the dossier file to the image.
- Each embedded image needs a one-sentence analytical caption, not a decorative caption.
- Do not embed every frame. Pick frames that prove a mechanic, player decision, UI constraint, feedback moment, or system relation.
- In module 3, include images that show loop steps or combat resolution.
- In module 4, include images that show system surfaces such as deckbuilding, shop, evolution, resource, or board layout.

## Prompt Checklist For Multimodal Review

When using a vision model, ask it to return structured JSON and focus on:

- What UI panels, cards, resources, units, buttons, and phase indicators are visible?
- What numbers or short text can be read with confidence?
- What player action or system feedback appears to be happening?
- What gameplay rule is directly visible, and what remains only inferred?
- Which game-analysis modules can this frame support?
- Should this image be embedded in the final dossier?
