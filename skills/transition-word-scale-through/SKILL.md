---
name: transition-word-scale-through
description: Exit from a white text card: the red keyword jumps to ~3x size (cropping off the frame), holds oversized while drifting, then smears sideways into a whip cut to the next shot. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: transition
  status: approved
  approved: 2026-10-22
  sources: [src-003]
---

# transition-word-scale-through

> Library technique (category: `transition`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
At the end of "we can never predict the outcome", the lockup suddenly scales up ~3x in one or two frames (with blur), so "predict" fills and overflows the frame; it holds ~0.6 s drifting slowly left, then smears horizontally and fades, and the next shot enters with a whip blur.

## Intended effect
A bold, energetic way out of a text card that keeps the keyword in the viewer's eye.

## Defining characteristics
- Instant scale-up ≈ 2.5–3x, overflowing the frame. [Fixed]
- Oversized hold ≈ 0.5–0.6 s with slow drift. [Rule]
- Exit by horizontal smear into `transition-whip-pan`. [Fixed]

## When to use
- Triggers: leaving a card on its strongest line.
- Avoid when: when the next shot needs a calm entrance.

## Relationships
- Exit for `card-white-kinetic-lockup`; joins `transition-whip-pan`.

## Adaptation
- Scale and drift direction may change; keep the keyword partly readable during the hold.

## Key numbers
- Scale jump measured ≈ 2.8x in 1–2 frames; oversized hold drifts left; the smear exit follows, and the incoming shot's first frame is whip-blurred (observed; table in ANALYSIS.md).

## Success criteria
- The jump feels intentional and punchy; the cut lands on the next phrase.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md).
