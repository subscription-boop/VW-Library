---
name: transition-board-rotate-reveal
description: The whole canvas board (grid with its labels and title) spins ~90 degrees in a fast motion-blurred turn with a soft settle, so a new axis label comes up on top - used to move from one dimension of a framework to the other. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: transition
  status: approved
  approved: 2026-10-25
  sources: [src-005]
---

# transition-board-rotate-reveal

> Library technique (category: `transition`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
The board that is on screen (a grid with the label "TOPICS" on top and the title "6/5 method") **rotates as one object** around its centre by about **90°**. The first part is fast and motion-blurred (≈ 0.3 s for most of the turn), then it **slows and settles** (≈ 0.6 s more). After the turn, the former top label sits on the side and a new label ("FORMATS") reads on top. A soft click lands at the start of the spin.

## Intended effect
Explains a two-dimensional framework physically: "this side is topics, turn it, this side is formats".

## Defining characteristics
- Entire board rotates as one rigid object, ~90° [Fixed]
- Fast start with motion blur, long soft ease-out [Rule]
- New label revealed on the new top edge [Rule]

## When to use
- Triggers: switching from one axis/dimension to another of the same framework ("rows are X, columns are Y"), "flip side", "on the other hand".

## Anatomy over time
- Start: on the second dimension's spoken word ("five formats").
- Development: 0–0.3 s blur turn (~70 % of the angle), 0.3–1.0 s settle.
- Resolution: holds, or hard cut to the next scene.

## Relationships
- Sound effects: `sfx-click-graphic-hit` on the start of the spin (click at 00:06.146).

## Adaptation
- Works for any rigid board (table, card, diagram) on the canvas; keep labels readable after the turn.

## Key numbers
- Fast part of the turn ≈ 9 frames with motion blur, then a slow ease-out settle to ~90° (observed; table in ANALYSIS.md).

## Success criteria
- The turn is readable (not a blur-only flash) and the new label is upright at the end.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
