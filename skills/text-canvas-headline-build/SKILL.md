---
name: text-canvas-headline-build
description: Black heavy sans headlines on a light canvas built word by word: each word arrives light grey, slightly blurred and a few pixels off, and settles to solid black in ~3 frames; one key word is huge, the small words tuck beside or under it. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-25
  sources: [src-005]
---

# text-canvas-headline-build

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
On the canvas, the headline of each idea is written while it is spoken. Words appear one at a time; each new word starts **light grey, softly blurred and slightly offset** (a few px right/down) and within ~3 frames becomes **solid black and sharp**. The layout is a lockup, not a sentence line: one key word or number is huge ("PLAN", "30", "6/5"), the small words sit beside it top-aligned ("days of / content / in 30 minutes", "this is called the / method") or above/below it ("Here's how to / PLAN / your next"). The lockup stays until the next scene.

## Intended effect
Gives every section a poster-like title that is readable on mute and grows with the voice, so the viewer reads and hears the same words at the same moment.

## Defining characteristics
- Near-black heavy grotesque sans on a light canvas [Fixed]
- Word-by-word build, timed to the spoken word [Rule]
- Entry per word: light grey + blur + small offset → solid black, ~0.1–0.15 s [Fixed]
- Mixed sizes in one lockup: one huge key word/number (3–5× the small words), small words tucked beside/above/below [Rule]
- No exit animation: the lockup leaves with the scene cut or the next build [Rule]

## When to use
- Triggers: the title or promise of a section ("Here's how to plan…", "this is called the 6/5 method", "pick 5 of these", "Short-Form video formats").
- Good fit: `layout-split-canvas-speaker-card` scenes, explainer content.
- Avoid when: the background is footage (use `text-kinetic-stack-mixed-size` or `title-small-row-over-condensed-caps` instead).

## Anatomy over time
- Start: first word on the word's speech onset (or 1 frame before).
- Development: each next word on its own onset; the big word may take ~1 frame longer to settle.
- Resolution: holds; other graphics build under it.

## Relationships
- Speech: word-synced.
- Other techniques: sits above the graphic it titles (calendar, grid, tray); captions in `text-caption-pill-grey` continue below.
- Sound effects: none on the words themselves in the reference; the scene may carry `sfx-whoosh-swell-scene-in` or `sfx-shimmer-tone`.

## Adaptation
- Font: the brand's heaviest sans; colour near-black; the huge word may take the brand accent once per video.
- Scaling: lockup width ≈ 60–75 % of the frame; huge word cap height ≈ 6–9 % of the frame height.

## Key numbers
- Reference words arrive one every ~0.04–0.12 s, each grey/blur → black in ~3 frames (observed; table in ANALYSIS.md).
- Reference "6" "/" "5": the "6" slides in from the left blurred; "5" and "method" go grey → black (observed; table in ANALYSIS.md).
- Reference size ratio: "PLAN" cap height ≈ 4× "Here's how to" (observed; table in ANALYSIS.md).

## Success criteria
- Each word turns black exactly when it is spoken.
- The lockup reads as one designed title (sizes deliberately mixed, edges aligned).

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
