---
name: text-flicker-in
description: A key caption word enters with a quick irregular on/off flicker (about 0.2 s) before holding steady. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-21
  sources: [src-002]
---

# text-flicker-in

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Instead of a hard appear, the key word blinks: on, faint, faint, on, faint, on over ~6–7 frames, then holds solid. Seen on "Instead" (white card) and the final serif word "blindly.".

## Intended effect
Draws the eye to the pivot or closing word and adds a tiny glitchy energy.

## Defining characteristics
- Irregular flicker (not a smooth pulse), ~0.2 s, then solid hold. [Fixed]
- Only on one key word at a time; rare. [Rule]

## When to use
- Triggers: pivot word, final word of the video.
- Avoid when: used on normal words.

## Relationships
- Works with tier 3 of `text-caption-emphasis-tiers` and on `card-white-word-beat`.

## Key numbers
- Flicker lengths seen: ~7 frames @ 30 fps (00:19.867–00:20.067) and ~5 frames (00:25.500–00:25.667) (observed; table in ANALYSIS.md).

## Success criteria
- Reads as a deliberate flicker; the word is solid well before it ends.

## User notes
- (none yet)

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
