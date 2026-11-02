---
name: zoom-open-settle-out
description: The opening wide shot appears already tighter (~1.15-1.2x) right after the film-burn flash and eases out to its normal framing in ~0.6-0.8 s (fast start, soft settle, no overshoot), then holds. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: zoom
  status: approved
  approved: 2026-10-25
  sources: [src-006]
---

# zoom-open-settle-out

> Library technique (category: `zoom`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Right after the 3-frame film burn, the wide two-shot is **slightly tighter than its final framing** and immediately **eases out**: about 60 % of the move happens in the first ~0.25 s, the rest settles softly by ~0.8 s. No overshoot. Then the shot is static (the slow creep of `zoom-slow-creep-every-shot` is not visible on this first wide shot).

## Intended effect
The opening "lands" and opens up, like the camera settling after the flash.

## Defining characteristics
- Starts tight on the first clean frame after the flash [Fixed]
- Pull-out, strong ease-out, no overshoot [Fixed]
- ≈ 1.15–1.2× → 1.0× in ≈ 0.6–0.8 s [Observed]

## When to use
- Triggers: the very first shot, right after an opening flash/burn.

## Relationships
- Follows `transition-film-burn-open`; carries `text-spaced-words-neon-lockup`.

## Adaptation
- Scale and duration as observed; centre on the subjects.

## Key numbers
- Scale vs settled: 1.143 at 00:00.209 (first measurable frame), then 1.049 / 1.015 / 1.002 at 00:00.417 / 00:00.626 / 00:00.834 (observed; table in ANALYSIS.md).
- Start scale is not measurable under the burn; ≈ 1.18–1.2 by extrapolation (uncertain).

## Success criteria
- Smooth settle, no bounce, finished before the first big word lands.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
