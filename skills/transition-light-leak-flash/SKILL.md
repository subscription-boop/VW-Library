---
name: transition-light-leak-flash
description: A 2–4 frame warm light-leak burst with thin hand-drawn scribble lines hides a jump cut, then the picture recovers through a warm/teal tint. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: transition
  status: approved
  approved: 2026-10-22
  sources: [src-003]
---

# transition-light-leak-flash

> Library technique (category: `transition`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
At a jump cut inside the talking head, one frame shows a warm orange-white light leak with a few thin black scribble lines across the frame, the next is almost fully overexposed, then 2 frames come back with orange and teal colour cast before returning to normal.

## Intended effect
Turns a jump cut into an energetic accent right after a payoff word.

## Defining characteristics
- Duration ≈ 0.2 s (5–6 frames at 30 fps). [Rule]
- Warm leak/overexposure + thin dark scribbles. [Fixed]
- Colour-tinted recovery frames. [Rule]

## When to use
- Triggers: right after a payoff/emphasis word, on a jump cut.
- Avoid when: more than once per video; calm content.

## Relationships
- Follows `text-neon-glow-word` in the reference.
- Happens on the same cut as `transition-negative-flash` (the negative-style colour flip); this skill covers the warm leak, overexposure and scribble lines.

## Adaptation
- Leak colour can follow the brand; keep scribbles thin.

## Key numbers
- Timing measured: leak + scribbles at 00:06.633, near white at 00:06.700, orange/teal tinted recovery 00:06.767–00:06.900 (observed; table in ANALYSIS.md).

## Success criteria
- Feels like a flash, not a glitch; the cut disappears inside it.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md).
