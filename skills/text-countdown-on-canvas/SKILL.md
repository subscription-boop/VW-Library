---
name: text-countdown-on-canvas
description: A spoken "3, 2, 1, GO" shown as one huge heavy black numeral at a time in the centre of the canvas, each fading in from light grey to black on its word; the first number lands with a click. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-25
  sources: [src-005]
---

# text-countdown-on-canvas

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
The canvas clears and a single huge heavy black numeral appears in the centre on each spoken word: "3", "2", "1", "GO". Each enters light grey (slightly soft) and darkens to black within a few frames; the previous one is simply replaced. A soft click marks the first number.

## Intended effect
A playful "let's start" beat between the overview and the first step; resets attention.

## Defining characteristics
- One big centred numeral/word at a time, black on the light canvas [Fixed]
- Grey → black entry on each spoken word, hard replacement [Rule]
- Very short: ~0.25 s per beat [Observed]

## When to use
- Triggers: the speaker actually counts down / says "ready, go".

## Relationships
- Follows the overview graphic, precedes `graphic-step-header-arc-number`.
- Sound effects: `sfx-click-graphic-hit` on the first number.

## Adaptation
- Brand heavy sans; the "GO" may take the brand accent.

## Key numbers
- 3 / 2 / 1 / GO at 00:07.080 / 07.330 / 07.580 / 07.750, ≈ 0.25 s apart, on speech; click at 00:07.110 (observed; table in ANALYSIS.md).

## Success criteria
- Each number lands on the spoken number; nothing else on the canvas.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
