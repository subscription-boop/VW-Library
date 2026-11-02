---
name: text-caption-pill-grey
description: Captions on a graphics canvas sit inside a small semi-transparent grey rounded pill with white bold text, centred between the diagram and the speaker card; one word or short phrase at a time, hard swaps. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-25
  sources: [src-005]
---

# text-caption-pill-grey

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
While the canvas layout is on screen, the spoken words are shown one at a time (sometimes two or three short words) inside a **grey rounded pill** (semi-transparent mid grey, white bold sans text, pill hugs the text). It sits centred on the canvas, below the graphic and above the speaker card. Each new word replaces the previous one with a hard swap; the pill resizes to the new word.

## Intended effect
Keeps mute viewers following the voice without competing with the black graphics: the grey pill reads as "secondary layer".

## Defining characteristics
- Rounded pill, mid grey, partly transparent; white bold text [Fixed]
- One word or a very short phrase at a time, hard swaps, word-synced [Rule]
- Fixed position between the graphic and the speaker card, centred [Rule]
- Only on canvas scenes; full-screen talking-head shots use plain chest captions [Rule]

## When to use
- Triggers: any speech while `layout-split-canvas-speaker-card` is on.
- Avoid when: the canvas scene already has the sentence as a headline (full-canvas proof scenes).

## Anatomy over time
- Start: word onset. Development: swap per word. Resolution: last word holds until the cut.

## Relationships
- Pairs with `layout-split-canvas-speaker-card`; switches to `text-single-word-captions-chest` on full-screen shots.
- Sound effects: none.

## Adaptation
- Pill colour: neutral grey at ~70 % opacity (or the brand's dark neutral at ~60 %); text white; radius ≈ 30 % of pill height.
- Size: text cap height ≈ 2.5 % of frame height.

## Key numbers
- Pill at y ≈ 765–825 of 1280 (0.62 H), grey ≈ #8A8A8A, white text (observed; table in ANALYSIS.md).

## Success criteria
- The caption is always readable and never touches the graphic or the speaker card.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
