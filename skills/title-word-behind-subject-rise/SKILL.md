---
name: title-word-behind-subject-rise
description: One giant heavy hook word starts behind the speaker's head (cut out so the head covers it), rises to the top of the frame with motion blur, holds, then fades out. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: title
  status: approved
  approved: 2026-10-22
  sources: [src-003]
---

# title-word-behind-subject-rise

> Library technique (category: `title`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
On frame 1 a huge white heavy sans word ("HEY") sits at head height behind the speaker: his hair and head cover part of the letters, so the word reads as part of the room. In ~0.4 s it rises to the top of the frame with vertical motion blur and settles across almost the full width. It holds while the first caption phrase runs below, then fades to translucent grey and disappears (~0.2 s).

## Intended effect
A 3D-feeling, premium opening that grabs attention in the first frame and says the first word big.

## Defining characteristics
- Word is placed behind the subject (subject cut-out/matte in front of the text). [Fixed]
- Huge: ≈ 90 % of frame width, heavy/black weight, white. [Rule]
- Rise from head height to the top ≈ 0.4 s with motion blur, ease-out. [Rule]
- Exit: fade to grey/translucent then gone, ≈ 0.2 s. [Rule]
- Only one word (the spoken greeting or hook word). [Rule]

## When to use
- Triggers: first spoken word of the video is a greeting or one-word hook ("Hey", "Stop", "Listen").
- Avoid when: no clean subject matte possible (busy hair against similar background) or the hook is a long phrase.

## Relationships
- Small phrase captions (`text-phrase-build-blur-rise`) run below it while it holds.
- Often combined with `zoom-push-in-overshoot` on the same opening.

## Adaptation
- Needs a subject matte (rotoscope / AI cut-out). Typeface and colour follow the brand.
- Keep the settled word above the head, never over the face.

## Key numbers
- Rise (0–0.4 s): from y ≈ 30 % (behind the head) to y ≈ 4–14 %, with motion blur (observed; table in ANALYSIS.md).
- Hold 0.4–1.067 s at full width (x 6–98 %), white; exit 1.067–1.267 s (grey, translucent, gone) (observed).
- Occlusion: at 0.1 s the head and hair are in front of the letters (observed).

## Success criteria
- The word clearly sits behind the head on the first frames; the rise is smooth; nothing covers the face.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md).
