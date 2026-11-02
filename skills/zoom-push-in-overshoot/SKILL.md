---
name: zoom-push-in-overshoot
description: Opening push-in: the first shot scales up fast (≈1.35x in 0.3 s), overshoots slightly, then settles at ≈1.28x. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: zoom
  status: approved
  approved: 2026-10-22
  sources: [src-003]
---

# zoom-push-in-overshoot

> Library technique (category: `zoom`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
From frame 1 the talking head scales up quickly toward the face; at ~0.3 s it is slightly past its final size, then eases back a little and holds tighter than it started.

## Intended effect
A punchy, energetic first second that pulls the viewer in.

## Defining characteristics
- Push-in (not pull-out) on the first shot. [Fixed]
- Fast: most of the move in ≈ 0.3 s. [Rule]
- Small overshoot (≈ 5–8 %) then settle. [Rule]

## When to use
- Triggers: video opening, hook line.
- Avoid when: calm or emotional openings; footage that cannot take ≈ 1.4x crop.

## Relationships
- Opposite of `zoom-cut-ease-out` (pull-out). Pairs with `title-word-behind-subject-rise`.

## Adaptation
- Scale relative to the source resolution; keep eyes in the upper third at the end.

## Key numbers
- Face width ≈ 288 px (of 720) at the start; peak ≈ 401 px (≈ 1.39x) at 0.3 s; settled ≈ 368–377 px (≈ 1.28x) from 0.45 s (observed; table in ANALYSIS.md).

## Success criteria
- The opening feels like a quick lunge in with a soft landing, no wobble.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md).
