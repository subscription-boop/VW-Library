---
name: card-white-kinetic-lockup
description: White full-screen card where a short phrase builds into a lockup: small black words plus one huge red heavy keyword (blur-in from pink to red), with offset small words around it. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: card
  status: approved
  approved: 2026-10-22
  sources: [src-003]
---

# card-white-kinetic-lockup

> Library technique (category: `card`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (observed measurements, overlap, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Mid-quote the picture cuts to white. Small black words appear one by one (grey/blur → black), then the key word lands big in heavy red (≈ #E8080E), fading in from a soft pink blur over ~0.3 s; follow-up small words ("to you", "you this?") tuck under its right edge. Holds 1.5–2.5 s, the voice continues.

## Intended effect
Pauses the visuals so the key idea of the quote hits as a poster.

## Defining characteristics
- White card, nothing else. [Fixed]
- Small black words + one huge red heavy keyword. [Fixed]
- Blur/fade-in per word; keyword pink→red. [Rule]
- Lockup offsets (small words above-left / below-right). [Rule]

## When to use
- Triggers: the core line of a quote or lesson.
- Avoid when: more than 3 times per minute.

## Relationships
- Can exit with `transition-word-scale-through` or `transition-fade-to-black`.

## Adaptation
- Red can be replaced by the brand accent; paper texture rules of `card-white-word-beat` may apply if the user wants.

## Key numbers
- Keyword sits at y 46–55 %, x 11–89 % of the frame (observed; table in ANALYSIS.md).

## Success criteria
- The keyword reads from across the room; the lockup looks designed, not random.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md).
