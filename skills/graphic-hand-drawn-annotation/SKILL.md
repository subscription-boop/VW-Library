---
name: graphic-hand-drawn-annotation
description: Marker-style hand-drawn strokes that draw themselves on screen: a red loose ellipse circling the key UI element or calendar items, and thin black curved connector lines from a phrase to the thing it describes. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-25
  sources: [src-005]
---

# graphic-hand-drawn-annotation

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Annotations look **drawn by hand with a marker** and are **written on in real time**: a **red loose ellipse** (slightly open, overlapping ends, uneven width) is drawn around the important UI element or calendar entry in ~0.25 s; a **thin black curved line** grows from a phrase toward the object it refers to (a "callout string"). They stay on screen afterwards.

## Intended effect
Points the eye exactly where it should look and adds a human, explainer feel to clean graphics.

## Defining characteristics
- Hand-drawn look (irregular, open ellipse ends, slight wobble) [Fixed]
- Draw-on animation along the stroke, ~0.2–0.3 s [Rule]
- Red for "look here" circles; black thin line for connectors [Observed]

## When to use
- Triggers: "exactly this", "right here", pointing to a number, button, view count or schedule entry.
- Avoid when: the element is already the only thing on screen.

## Anatomy over time
- Start: a beat after the target is visible (on the stressed word).
- Development: stroke draws on clockwise/top-down. Resolution: holds until the cut.

## Relationships
- Used on `graphic-phone-mockup-feed` and calendar/table scenes; connects `text-serif-sans-mixed-line` to its object.
- Sound effects: none clearly heard on the strokes.

## Adaptation
- Circle colour: red or the brand's accent; stroke width ≈ 0.6 % of frame width.

## Key numbers
- Red ellipse draw-on ≈ 6 frames; black connector line grows down ≈ 3 frames (observed; table in ANALYSIS.md).

## Success criteria
- The stroke clearly reads as hand-drawn and lands on the exact element named.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
