---
name: graphic-step-header-arc-number
description: Step header on the canvas: a thin black arc sweeps in from the left edge, a dot rides up the arc carrying a huge italic black numeral that fades to transparent at its bottom, then the step title builds beside it (tiny lead word + bold italic title, grey to black). Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-25
  sources: [src-005]
---

# graphic-step-header-arc-number

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
On a clean canvas, a **thin black arc** (part of a large circle whose centre is off-screen left) appears at the left edge. A **black dot** travels up along the arc from the bottom, and a **huge italic heavy numeral** rides with it, motion-blurred, settling next to the dot in ~0.3 s. The numeral has a **vertical gradient**: solid black at the top fading to transparent at the bottom. Then the step title builds to the right of the numeral: a tiny lead word ("Find") and a **bold italic** title ("Winning Topics", "Formats"), each word grey → black on its spoken word. The header holds until the step's content starts.

## Intended effect
A clear, premium "chapter" marker inside the canvas world; the arc and dot read like a progress dial.

## Defining characteristics
- Thin arc from the left edge + dot that travels on it [Fixed]
- Huge italic heavy numeral with top-to-bottom black → transparent gradient [Fixed]
- Numeral flies in along the arc with motion blur, ease-out, ~0.3 s [Rule]
- Title beside it: tiny lead word + bold italic title, word by word grey → black [Rule]

## When to use
- Triggers: "first…", "step two…", "next we need…"; each numbered step of a method.
- Avoid when: the step number is not spoken or there are more than ~6 steps.

## Anatomy over time
- Start: hard cut to the empty canvas; arc already drawn on the first frame.
- Development: dot + numeral rise along the arc (0.0–0.3 s); title words on speech (0.7–1.2 s later in the reference).
- Resolution: holds ~1–2 s, hard cut to the step's first graphic.

## Relationships
- Precedes the step's content scene (`graphic-mindmap-branch-build`, `graphic-scatter-assemble`).
- Sound effects: step 2 is accompanied by `sfx-shimmer-tone` starting on the reveal; step 1 had no clear sound of its own (it follows the countdown).

## Adaptation
- Numeral and title in the brand's heaviest italic sans (or oblique); arc/dot near-black; the dot may take the brand accent.
- Scaling: numeral cap height ≈ 8–10 % of frame height; arc radius ≈ 1.2× frame height.

## Key numbers
- Numeral rise along the arc ≈ 7 frames, motion blur, ease-out (observed; table in ANALYSIS.md).
- Title words "Find" / "Winning" / "Topics" at 00:08.750 / 08.920 / 09.090, grey → black on speech (observed).
- Step 2 reveal at 00:36.080 with the shimmer tone at 00:36.06–00:37.0 (observed).

## Success criteria
- The numeral reads instantly and the gradient makes it feel dimensional, not flat.
- Title words land on the spoken words.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
