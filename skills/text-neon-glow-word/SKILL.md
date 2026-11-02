---
name: text-neon-glow-word
description: A single payoff word in saturated neon colour with an outer glow, under the caption line, entering with a quick flicker. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-22
  sources: [src-003]
---

# text-neon-glow-word

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
On "client", the word "CLIENT" appears below the small caption in bright neon green (≈ #58FB11) heavy caps with a soft glow around it. It flickers on (faint, full, dim, full over ~0.3 s) and then holds.

## Intended effect
Marks the goal/payoff word with energy and colour.

## Defining characteristics
- One word, neon colour, heavy caps, outer glow. [Fixed]
- Flicker entrance ≈ 0.3 s, then hold. [Rule]
- Placed under the running caption. [Rule]

## When to use
- Triggers: goal, result or payoff word ("client", "money", "viral").
- Avoid when: colour clashes with the brand palette (then use the brand accent).

## Adaptation
- Colour can follow the brand accent; keep the glow soft.

## Key numbers
- All values are stated above; the per-source table is in ANALYSIS.md.

## Success criteria
- The word glows without blooming over the face.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md).
