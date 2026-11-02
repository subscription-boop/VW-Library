---
name: graphic-emoji-icon-under-caption
description: A flat icon or emoji (here a country flag) appears right under the caption phrase that names it, rising and un-blurring together with the phrase. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-22
  sources: [src-003]
---

# graphic-emoji-icon-under-caption

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (observed measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
When he says "I'm from the Philippines", a flat flag graphic appears centred under the caption. It enters with the same rise + blur-in + fade as the phrase (~0.4 s), holds while the phrase is on screen, and leaves with it.

## Intended effect
Instant visual meaning for a named thing; adds colour without clutter.

## Defining characteristics
- Icon directly under the caption, centred, ≈ 20–25 % of frame width. [Rule]
- Same entrance and exit as the caption line. [Fixed]
- Flat, clean icon/emoji, no box. [Rule]

## When to use
- Triggers: a named country, brand, object or emotion that has an obvious icon.
- Avoid when: when the icon would cover the face or the product being shown.

## Relationships
- Rides with `text-phrase-build-blur-rise`.

## Adaptation
- Use official/clean icons; logos only from the user's own files.

## Key numbers
- Entrance at 00:02.000–00:02.470: rise ≈ 4 %, blur→sharp, fade in; hold at 00:02.470–00:02.950 under the caption, width ≈ 22 % (observed; table in ANALYSIS.md).

## Success criteria
- The icon reads instantly and never fights the caption.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md).
