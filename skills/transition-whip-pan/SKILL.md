---
name: transition-whip-pan
description: Whip-pan cut: the outgoing shot smears sideways with strong horizontal motion blur for ~2 frames, the incoming shot arrives smeared for ~1 frame, then sharp. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: transition
  status: approved
  approved: 2026-10-22
  sources: [src-003]
---

# transition-whip-pan

> Library technique (category: `transition`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
When the video jumps from the presenter to the showcased clip, the presenter frame streaks horizontally (stretched motion blur) for two frames, the new shot starts with one streaked frame and snaps sharp.

## Intended effect
Fast, energetic change of scene or source.

## Defining characteristics
- Horizontal directional blur across the cut, ≈ 3 frames total. [Fixed]
- No dissolve; snap to sharp. [Rule]

## When to use
- Triggers: change of location/source (presenter → example clip, card → footage).
- Avoid when: within the same shot (use a jump cut or blur bridge).

## Relationships
- Different from `transition-blur-bridge` (defocus, not directional). Used as the exit of `transition-word-scale-through`.

## Adaptation
- Direction can follow the next shot's movement.

## Key numbers
- All values are stated above (2 frames outgoing smear, 1 incoming smear frame, then sharp); the per-source table is in ANALYSIS.md.

## Success criteria
- The jump reads as one fast camera whip.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md).
