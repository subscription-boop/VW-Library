---
name: graphic-scatter-assemble
description: Many small elements (calendar dates, video thumbnails) fly in from scattered positions with motion blur and snap into an ordered grid, or a grid breaks apart and only the chosen items collect into a tray while the rest fade; usually carried by a soft whoosh swell. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-25
  sources: [src-005]
---

# graphic-scatter-assemble

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
A set of many small items assembles itself on the canvas: they start **scattered** (off their final places, some off-screen, at different depths, motion-blurred), then all **fly to their slots in an arc and snap into a clean grid** within ~0.5–0.7 s, with slight stagger so it reads as a swarm, not a slide. In the reverse variant, a finished grid **breaks apart** and only the **chosen items fly up into a grey rounded tray** while the others fade out.

Examples: calendar date numbers flying into the month grid; 20 video thumbnails flying in large and blurred, shrinking into a 5×4 grid; "pick 5 of these" collecting five thumbnails into a tray.

## Intended effect
Turns "there are many of these" and "pick some of them" into a satisfying physical moment; shows quantity and selection without text.

## Defining characteristics
- Many items (10–30) moving at once from scattered start positions to an ordered layout [Fixed]
- Arced/curved paths, motion blur during flight, quick ease-out settle, slight stagger [Rule]
- Selection variant: chosen items move into a container (tray), the rest fade [Rule]
- Duration ~0.5–0.8 s [Observed]

## When to use
- Triggers: counts of many things ("30 days", "20 formats"), choosing a subset ("pick 5"), a schedule filling up.
- Avoid when: fewer than ~6 items (use single pops instead).

## Anatomy over time
- Start: on the cut or the noun that introduces the set.
- Development: flight 0.3–0.6 s, settle 0.1–0.2 s.
- Resolution: the grid holds while the speaker continues; thumbnails may keep playing.

## Relationships
- Sound effects: `sfx-whoosh-swell-scene-in` under the flight (calendar, thumbnails); `sfx-shimmer-tone` on the selection into the tray.
- Titles: `text-canvas-headline-build` above the grid.

## Adaptation
- Items are real content (the user's dates, real thumbnails/screens); tray and grid use the brand's light neutral and radius.
- Scaling: keep the flight under ~0.7 s regardless of item count.

## Key numbers
- Dates into the calendar ≈ 0.6 s, arcs from below, staggered (observed; table in ANALYSIS.md).
- Thumbnails into the grid ≈ 0.25 s from large/blurred to settled (observed).
- Pick-5 collect into the tray ≈ 0.8 s, others fade (observed).

## Success criteria
- The motion reads as a swarm settling into order; the final grid is perfectly aligned.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
