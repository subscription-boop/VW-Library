---
name: text-phrase-build-blur-rise
description: Small white heavy captions that show a short phrase, building word by word: each new word fades from grey and soft to solid white; the phrase line enters by rising a little out of blur. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-22
  sources: [src-003]
---

# text-phrase-build-blur-rise

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Captions sit on the chest (moving with the framing). A phrase of 2–5 words is visible at once. When a new phrase starts, the line rises a few percent of the frame height from below while it un-blurs and fades in (~0.3 s). Inside the phrase, each next word appears on its spoken onset as grey, slightly blurred text and turns solid white within ~0.1–0.15 s. The phrase is replaced (quick fade) at the end of the chunk.

## Intended effect
Easy reading with a soft, modern, "typing as he speaks" feel; less jumpy than single-word swaps.

## Defining characteristics
- Phrase-level line (2–5 words) that accumulates, not single-word swaps. [Fixed]
- Upcoming/just-spoken word: grey + blur → white. [Fixed]
- Line entrance: small rise + blur-in + fade. [Rule]
- Small, heavy, tight white sans with soft shadow. [Rule]

## When to use
- Triggers: continuous talking-head speech.
- Avoid when: when a single huge emphasis word is needed (use a big-word technique).

## Relationships
- Icons may ride under it: `graphic-emoji-icon-under-caption`.

## Adaptation
- Typeface/colour from the brand; keep line width ≤ ~60 % of the frame.

## Key numbers
- Caption box at 00:01.000: y ≈ 65–68 %, x ≈ 27–61 % (observed; table in ANALYSIS.md).
- Word build at 00:00.533–00:00.933: "my" white, "name's" grey→white ≈ 0.13 s, "Kai" grey→white (observed; table in ANALYSIS.md).
- Line rise at 00:02.000–00:02.470: ≈ 4 % of frame height, blur→sharp (observed; table in ANALYSIS.md).

## Success criteria
- Words never appear before they are spoken; the grey→white step is visible but subtle.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md).
