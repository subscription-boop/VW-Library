---
name: transition-blur-bridge
description: A cut hidden inside full defocus: the last frame of shot A and the first ~8 frames of shot B are heavily blurred, then shot B snaps sharp in one frame. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: transition
  status: approved
  approved: 2026-10-21
  sources: [src-002]
---

# transition-blur-bridge

> Library technique (category: `transition`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
At the cut, the picture goes fully out of focus (one frame on the outgoing shot), stays blurred on the incoming shot for ~0.27 s while captions keep running (the caption is blurred with the picture on the first frame, then sharp), then snaps to full sharpness in a single frame. No zoom, no fade.

## Intended effect
A soft "reset" between thoughts; here it lands on "Keep your content clean", so the snap to sharp illustrates clarity.

## Defining characteristics
- Blur covers the cut on both sides. [Fixed]
- Snap back to sharp is instant (1 frame), not a rack-focus ramp. [Fixed]
- Blur hold ~0.25–0.3 s. [Rule]

## When to use
- Triggers: a line about clarity/focus, or a change of thought within the same setup.
- Avoid when: used more than once or twice per video (it loses meaning).

## Relationships
- Captions continue through it. Usually between two talking-head takes.

## Key numbers
- Blurred frames: 9 frames at 30 fps, measured sharpness ~5 versus ~45–100 on normal frames; snap to sharp 1 frame (observed; table in ANALYSIS.md).

## Success criteria
- The cut is invisible inside the blur; the snap feels like focus locking.

## User notes
- (none yet)

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
