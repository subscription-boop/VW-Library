---
name: text-step-label-serif
description: A numbered section label ("Step 1") in large italic serif fades in over ~0.2 s on the speaker’s chest right after a cut, and stays while he starts the step. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-21
  sources: [src-002]
---

# text-step-label-serif

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
On the first frame after a hard cut back to the speaker, "Step N" appears centred over the upper chest in a large white italic serif. It fades in over ~6 frames (soft, slightly translucent at first) and holds ~0.5–0.7 s until the first caption word of the step replaces it. Steps 1–3 all use the same look; the cut into each step often changes framing (step 2 is a tight shot).

## Intended effect
Clear chaptering without leaving the speaker (unlike a full-screen card), keeping pace high.

## Defining characteristics
- Overlay on the speaker, not a card. [Fixed]
- Italic serif, larger than captions, centred. [Rule]
- Appears on the cut into the step, fade ~0.2 s, hold ~0.5–0.7 s. [Rule]

## When to use
- Triggers: "Step one", "Tip two", "Number three" at the start of a section.
- Avoid when: the section needs a full reset (then use a card).

## Relationships
- Cuts: placed on the cut that opens the section; framing often changes there (`zoom-cut-ease-out`).
- Captions: replaces the caption track while visible, then the tier-1 captions resume.
- Typeface shared with tier 3 of `text-caption-emphasis-tiers`.

## Adaptation
- Brand: serif face and colour follow the brand; wording follows the speech ("Tip", "Step", "Rule").

## Key numbers
- Fade-in ~6 frames @ 30 fps (00:04.167–00:04.367) (observed; table in ANALYSIS.md).
- Size w ~22 %, h ~6 %, y ~46–52 % (00:04.500) (observed; table in ANALYSIS.md).

## Success criteria
- Each section opens with its label on the cut; the label is readable before the speaker's next word.

## User notes
- (none yet)

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
