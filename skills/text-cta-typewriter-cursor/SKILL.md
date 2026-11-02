---
name: text-cta-typewriter-cursor
description: Closing call to action in the top third - a tiny uppercase lead line ("COMMENT THE WORD") and under it a huge condensed keyword in quotes ("“MUSIC”") typed letter by letter with a tall text cursor that keeps blinking after the word is complete. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-24
  sources: [src-004]
---

# text-cta-typewriter-cursor

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
As the speaker says "just comment the word…", a tiny uppercase line appears word by word ("COMMENT", "THE", "WORD", each blurring in), and a tall thin white cursor bar appears. Then the keyword is typed under it, one character every ~2 frames, in a huge ultra-condensed heavy uppercase white, including the opening and closing quotation marks ("“", "“M", "“MU" … "“MUSIC”"). The cursor sits just right of the last character while typing, and after the word is complete it keeps blinking (on ~0.3 s, off ~0.3 s) until the end of the video.

## Intended effect
Makes the comment keyword impossible to miss and feels like someone is typing the comment for you, which nudges the viewer to do it.

## Defining characteristics
- Two lines: tiny uppercase lead line + huge condensed keyword in quotes. [Fixed]
- Keyword typed character by character (~15 characters per second), quotes included. [Fixed]
- Tall thin cursor bar right of the text; blinks after typing. [Fixed]
- Lead-line words blur in one by one just before the typing. [Observed]
- Holds to the last frame. [Rule]

## When to use
- Triggers: a "comment the word X" / "type X" / "DM me X" call to action at the end.
- Avoid when: the keyword is longer than ~8 characters (shrink or use a phrase caption instead).

## Anatomy over time
- Start: on the spoken "comment" (lead line + cursor).
- Development: keyword typed in ~0.5 s.
- Resolution: cursor blinks; text holds to the end.

## Relationships
- Speech: lead line on "comment the word"; typing ends around the spoken keyword.
- Captions: the chest captions keep running underneath.
- Sound effects: none observed (no audible typing in the reference, see analysis limitations). A keystroke per character (`sfx-keyboard-typing-captions` style) is a possible addition only if the user asks.
- Other techniques: same type family as `title-small-row-over-condensed-caps` (book-ends the video).

## Adaptation
- Fonts/colour from the brand (condensed heavy sans for the keyword; brand accent allowed for the keyword or the cursor).
- Keyword = the user's real comment keyword.

## Key numbers
- Lead line at 00:14.615–00:14.882: "COMMENT" blurs in 14.615, cursor 14.681, "THE" 14.748, "WORD" 14.882 (observed; table in ANALYSIS.md).
- Typing at 00:14.748–00:15.349: “ → “M (14.88) → “MU (15.02) → “MUS (15.09) → “MUSI (15.15) → “MUSIC (15.22) → “MUSIC” (≈15.28) (observed; table in ANALYSIS.md).
- Cursor blink at 00:15.4–00:17.0: on/off about every 0.3 s, irregular (observed; table in ANALYSIS.md).
- Layout at 00:15.600: lead line y ≈ 0.11 H; keyword ≈ 0.13–0.28 H, ≈ 0.75 W; cursor ≈ 0.11–0.30 H (observed; table in ANALYSIS.md).

## Success criteria
- The keyword is typed in under ~0.6 s and fully readable; the cursor blinks visibly to the end.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Typing speed and cursor: `sequences/…_typing/`, `clips/…_cta-typing-cursor.mp4`.
