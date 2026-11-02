---
name: zoom-slow-creep-every-shot
description: Every shot slowly and steadily pushes in (digital scale ~2 % per second, linear with a soft start) from its first frame to the cut, then the next shot starts again from normal framing, so the picture is never completely still. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: zoom
  status: approved
  approved: 2026-10-25
  sources: [src-006]
---

# zoom-slow-creep-every-shot

> Library technique (category: `zoom`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
None of the shots is static. From the first frame after each cut, the picture **scales up slowly and evenly** (a digital push-in), about **2 % per second**, until the next cut. The move has a very soft start (the first ~0.3 s barely move) and then a constant speed - no easing at the end, no settle. The next shot starts again at its normal framing and creeps in again. Long shots therefore end noticeably tighter (≈ 1.16–1.18× after 7–8.5 s); short shots barely move (≈ 1.01–1.02×).

## Intended effect
Keeps a static podcast camera alive and adds slow tension, so long takes don't feel frozen; the viewer doesn't notice the move, only the "breathing" picture.

## Defining characteristics
- Every shot, from its first frame to its cut [Fixed]
- Direction: always in [Fixed]
- Speed constant ≈ 2–2.2 % per second; soft start, no end ease [Observed]
- Resets on each cut (the next shot starts at normal framing) [Rule]

## When to use
- Triggers: long static shots (podcast, interview, seated talking head).
- Avoid when: the shot already has camera motion, or a template uses punch-in/pull-out zooms as accents (they would fight).

## Anatomy over time
- Start: cut; first ~0.3 s almost still. Development: linear growth. Resolution: the cut.

## Relationships
- Coexists with `zoom-cut-ease-out` on the opening shot only (see that skill / the overlap note in the review).
- Captions and graphics stay fixed on screen (not scaled with the picture). [Observed]

## Adaptation
- Rate 1.5–2.5 %/s; cap the end scale at ~1.2× for very long shots (lower the rate) so resolution holds; centre the push on the face.

## Key numbers
- Measured: medium shots 1.00 → 1.157 and 1.00 → 1.182 (≈ 2.2 %/s); closing wide shot 1.00 → 1.086 (≈ 2.1 %/s) (observed; table in ANALYSIS.md).
- Close-ups: push visible but tracking unreliable (dark, few features, overlays) (uncertain).

## Success criteria
- Viewers do not notice a zoom, but the frame never feels frozen; no jump at cuts.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
