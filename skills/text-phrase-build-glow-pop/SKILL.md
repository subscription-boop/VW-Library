---
name: text-phrase-build-glow-pop
description: White sentence-case captions (medium-weight sans with a soft white glow) on the chest; the phrase is laid out centred for its full length and each word pops in hard on its spoken onset, so the line grows left to right; the line is replaced at the end of the phrase. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-25
  sources: [src-006]
---

# text-phrase-build-glow-pop

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Captions sit across the chest/mic area, one line of 2–6 words. The **line is laid out for the whole phrase, centred**, and the words are revealed **left to right in place**: each word **pops in hard** (fully white in one frame) on its spoken onset. The text is a **medium-weight sans, sentence case with punctuation**, white with a **soft white glow** around the letters. When the phrase ends, the next phrase replaces the line with a hard swap. When a key word comes, it is added inline in red neon serif (`text-neon-serif-keyword`), and while a big neon word holds, the white caption is hidden.

## Intended effect
Calm, readable captions that feel lit in the dark set; nothing moves, so the viewer stays on the face and the voice.

## Defining characteristics
- Phrase line that accumulates word by word; layout fixed (centred for the full phrase), words revealed in place [Fixed]
- Hard pop per word on the spoken onset; no fade, no blur, no rise [Fixed]
- Medium-weight sans, sentence case with punctuation, white with soft white glow [Fixed]
- Hard swap to the next phrase [Rule]

## When to use
- Triggers: all continuous speech on the podcast shots.
- Bright footage: allowed - keep the hard word pops and layout; white text with a soft dark shadow instead of the glow, or dark text on very light backgrounds. [User]

## Anatomy over time
- Start: first word of the phrase on its onset. Development: one word per onset. Resolution: swap at the next phrase or the cut.

## Relationships
- Inline key words: `text-neon-serif-keyword`. Wide shots use `text-spaced-words-neon-lockup` instead.
- Sound effects: none.

## Adaptation
- Font: brand text sans (medium/semibold), white; glow radius ≈ 0.3–0.5× cap height at low opacity.
- Size: cap height ≈ 1.8–2 % of the frame height; width ≤ 80 % of the frame.
- Position: chest/mic height, never on the mouth.

## Key numbers
- Word pops at 00:02.292–00:02.917: "Because" 2.292, "we" 2.459, "don't" 2.542, "have" 2.709, "to." 2.876 (observed; table in ANALYSIS.md).
- Line at 00:02.950: centred (x 152–567 of 720), y ≈ 47 % of the height (observed; table in ANALYSIS.md).

## Success criteria
- Every word appears on its onset, the line never jumps sideways while growing.

## User notes
- [User] The darkness of the reference is mostly the real shooting environment, not the style; this technique must also work on bright footage (with new main colours for some texts) ("اون تیرگی محیط ... بیشتر از اینکه فیلتر باشه یا سبک ویدیو، طرز فیلمبرداری و محیط واقعی خودشه").

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
