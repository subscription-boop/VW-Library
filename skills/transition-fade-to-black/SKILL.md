---
name: transition-fade-to-black
description: End of a showcased section: the last card fades to black over ~1.5 s with only music, holds black ~0.6 s, then hard-cuts back to the presenter (music gone). Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: transition
  status: approved
  approved: 2026-10-22
  sources: [src-003]
---

# transition-fade-to-black

> Library technique (category: `transition`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
After "why is it telling you this?", the white card dims smoothly to black (~1.5 s) while the voice has ended and the music bed plays alone; black holds ~0.6 s; a hard cut brings back the presenter in silence for the outro.

## Intended effect
A clear chapter end: closes the example and resets attention for the outro.

## Defining characteristics
- Linear fade to black ≈ 1.5 s. [Rule]
- Black hold ≈ 0.5–0.7 s. [Rule]
- Music only during the fade; hard cut back to dry voice. [Observed]

## When to use
- Triggers: end of an embedded example/story before the presenter returns.
- Avoid when: mid-thought.

## Relationships
- Comes after `card-white-kinetic-lockup` in the reference.

## Adaptation
- Fade length can scale with the video's pace (1–2 s).

## Key numbers
- All values are stated above; the per-source table is in ANALYSIS.md.

## Success criteria
- The ending of the section feels deliberate, not like a glitch.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md).
