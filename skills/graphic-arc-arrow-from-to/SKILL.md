---
name: graphic-arc-arrow-from-to
description: Two labels sit left and right above the speaker ("2026" → "2027"); a glowing yellow arc arrow grows from the left label toward the right one, the rest of the path is a dotted line ending in a glowing orange dot on the target. Fits "from now to next" statements. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-28
  sources: [src-007]
---

# graphic-arc-arrow-from-to

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (observed measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
On "the year's almost over", two big heavy white numbers appear at the speaker's head height, one at each side of the frame ("2026" left, "2027" right, slightly translucent with a soft shadow). Above them an arc path curves from the left number to the right one. The travelled part is a **solid, glowing yellow line with an arrowhead**; the remaining part is a **thin dotted white line** that ends in a **small glowing orange dot** over the target number. The yellow arrow keeps growing steadily along the arc toward the target while the speaker talks (it never quite arrives). The graphic disappears with the flash transition on the next cut.

## Intended effect
Visualises progress or time running out ("from here to there"); the growing arrow creates gentle urgency without words.

## Defining characteristics
- Two labels (start, target) left and right, connected by an arc above the head. [Fixed]
- Solid glowing warm line + arrowhead for the travelled part; dotted line for the rest; glowing dot on the target. [Fixed]
- The arrow grows continuously (linear) along the arc for the whole time on screen. [Rule]
- Leaves on the next cut/transition. [Rule]

## When to use
- Triggers: a time span or change ("2026 → 2027", "now → in 30 days", "beginner → pro", "start → launch").
- Avoid when: there is no clear start and target, or the top third is already busy.

## Anatomy over time
- Start: on the phrase's first word, labels fade in, the arrow starts drawing from the start label (~0.1–0.2 s to first visible segment).
- Development: tip moves steadily, ~0.35 frame-widths per second in the reference.
- Resolution: removed by the next cut/transition (no exit animation).
- Repetition: once.

## Relationships
- Subject: arc passes over the head; labels at head height, outside the face.
- Speech: appears on the sentence about time/change; captions continue on the chest.
- Sound effects: none observed.
- Other techniques: exits through `transition-glow-flicker-streak` ([SKILL.md](../transition-glow-flicker-streak/SKILL.md)) in the reference.

## Adaptation
- Adaptable: label text, arc height, growth speed (so the tip is near but not on the target when the shot ends).
- Brand: line/glow colour = brand accent (yellow in the reference), dot = second accent (orange), labels in brand heavy sans.

## Key numbers
- Graphic appears at 00:01.434, right after the cut at 00:01.401; gone with the flash transition / cut at 00:02.836 (observed; table in ANALYSIS.md).
- Arrow tip x ~0.36 W → ~0.73 W over 00:01.63–00:02.70, nearly linear (~0.35 W/s) (observed).
- Layout: labels y ≈ 0.40 H at x ≈ 0.02–0.30 W and 0.70–0.99 W; arc top y ≈ 0.25 H (observed).

These describe the references. They are not quotas or required values.

## Success criteria
- Start and target are readable at a glance; the travelled vs remaining path is obvious.
- The arrow visibly grows while on screen; nothing covers the face.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Look: `frames/..._early.jpg`, `frames/..._late.jpg`. Entry: `sequences/..._entry.jpg`. Growth over time: `clips/..._year-arc-arrow.mp4`.
