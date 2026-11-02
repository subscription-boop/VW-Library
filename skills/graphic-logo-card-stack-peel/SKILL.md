---
name: graphic-logo-card-stack-peel
description: While the speaker lists famous brands, a stack of their logos as tilted cards/badges sits beside his head; the front card peels away on each next name to reveal the next logo, and the last one fades out. Fits lists of examples, clients or competitors. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-28
  sources: [src-007]
---

# graphic-logo-card-stack-peel

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
"…Coca-Cola, Nike, Adidas, the biggest companies in the world…": the whole stack of logos fades in at once around the speaker's head, as flat rounded cards/badges slightly rotated (~10–15°), overlapping like a hand of cards: Coca-Cola (red card) in front, Nike (white card) behind it, Adidas (black circle) at the back. It fades in from transparent and large (the shot is still zoomed in) and gets smaller as the shot zooms out (the cards live inside the zoom). Just before "Nike" the front card slides away to the lower left and is gone in ~5–6 frames, revealing the Nike card. On "Adidas" the Nike card slides off the same way. The Adidas badge then grows with a push-in zoom, holds, and fades to transparent (~0.4 s) after the list.

## Intended effect
Makes a spoken list of famous names concrete and fast to read; the peeling stack keeps rhythm with the speech and implies "and more".

## Defining characteristics
- Real logos as flat cards/badges, tilted, overlapping in one stack near the head. [Fixed]
- The full stack is visible from the first name; each next name removes the front card (slide/peel away) to reveal the next. [Fixed]
- Peels are fast (~5–6 frames) and finish just before / on the next spoken name. [Rule]
- The last card fades out after the list. [Rule]

## When to use
- Triggers: a spoken list of 2–5 brand names (clients, competitors, examples).
- Avoid when: logos cannot be shown (rights/brand rules of the client), or the list is longer than ~5.

## Anatomy over time
- Start: stack fades in (~0.3 s) on/just before the first name.
- Development: one peel per name.
- Resolution: last badge holds through the next phrase, fades ~0.4 s.
- Repetition: once per list.

## Relationships
- Subject: stack sits at head height, to one side (overlapping the head edge is fine, never the face).
- Speech: peel on each name's onset.
- Other techniques: inside `zoom-push-hold-release` ([SKILL.md](../zoom-push-hold-release/SKILL.md)): the cards scale with the zoom; captions continue on the chest.
- Sound effects: none observed.

## Adaptation
- Adaptable: card shapes follow each logo (card, circle); 2–5 cards; tilt alternates.
- Brand: logos are the real third-party marks; the selected brand affects only shadows/edges, never the logos' colours.

## Key numbers
- Stack fade-in ~10 frames, transparent → solid; Coca-Cola card peel ~6 frames, Nike card peel ~5 frames, both sliding lower left (observed; table in ANALYSIS.md).
- Each peel leads the next spoken name by ~0.05–0.25 s (observed).
- Last badge fade-out ~0.45 s (observed).
- Layout: stack centre ≈ (0.65 W, 0.25 H) of the zoomed-out frame, ~0.35 W wide (observed).

## Success criteria
- Each logo is readable when its name is spoken; peels land on the names; the face is never covered.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Fade-in: `sequences/..._stack-fade-in.jpg`; peel speed: `sequences/..._peel.jpg`; exit: `sequences/..._last-card-fade.jpg`.
