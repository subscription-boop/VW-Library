---
name: text-neon-serif-keyword
description: The one key word or short phrase of a line is set in a bold italic serif in pure red with a strong red neon glow, popping on hard on its spoken word - inline at the end of the white caption line, as a big word under a row of small words, or alone on a short shot (the interviewer's "Why?"). Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-25
  sources: [src-006]
---

# text-neon-serif-keyword

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
The single word (or two-word phrase) that carries the point is not shown as a normal caption. It is set in a **heavy italic serif** (high contrast, ball terminals, lowercase as spoken), coloured **pure saturated red** (core ≈ #DF0003) with a **wide red glow** around it (halo ≈ #5A0306 falling off over ~0.5–1 cap heights), so it looks like a lit neon sign in the dark shot. It appears **hard, in one frame**, on the spoken onset (±2 frames). Three placements occur:
- **Inline**: the white phrase caption builds ("I'm not interested in") and the key words land at the end of the same line in red serif ("doubling", then "up." on its own word). Same baseline, slightly larger than the white words.
- **Big**: the word alone, large (≈ 40–45 % of the frame width), centred over the chest; the white caption is hidden while it holds ("organically", held ~2.7 s to the cut).
- **Alone on a short shot**: the interviewer's one-word question "Why?" sits on his chest for his whole 0.7 s shot, already there on the cut's first frame.
On the wide shots it is the large line of `text-spaced-words-neon-lockup`.

## Intended effect
Makes the punchline word glow like a sign in a dark, premium set; the colour and the change of typeface tell the viewer "this is the word to remember" without any motion.

## Defining characteristics
- Heavy italic serif, lowercase as spoken, one strong main colour (red in the reference) with a wide neon glow of the same colour - always [Fixed]
- Hard pop on the spoken onset (no fade, no flicker, no scale) [Fixed]
- One word or a two-word phrase; 1–2 per sentence at most, ~6 in 35 s [Observed]
- Placement follows the shot: inline at the end of the caption line, big alone over the chest, or alone on a reaction/question shot [Rule]
- Holds until the phrase ends or the cut; no exit animation [Rule]

## When to use
- Triggers: the payoff/contrast word ("paid marketing", "doubling up", "organically", "curiosity"), a one-word question or reaction from the other person.
- Good fit: dark, low-key podcast or interview footage where a red glow reads as light.
- Bright footage: allowed - keep the neon glow, always [User]; use a strong saturated main colour chosen for the video (red, the brand accent or a new colour the user picks) and make the glow strong enough to read on the light background (denser core glow, slightly darker halo than on dark footage).
- Avoid when: more than ~2 key words per sentence.

## Anatomy over time
- Start: the frame of the spoken onset (paid 0.709 s, doubling 5.130 s, up 5.547 s, organically 7.674 s, curiosity 34.117 s).
- Development: none; in the closing lockup the glow dims a little when the next small words appear (34.74–35.0 s). [Observed]
- Resolution: hard out with the phrase or the cut.

## Relationships
- Captions: inline partner of `text-phrase-build-glow-pop` (same line, same baseline); large line of `text-spaced-words-neon-lockup`.
- Sound effects: none - the pops are silent in the reference (checked on the voice-removed stem at 0.7, 1.0, 5.1, 5.5, 7.7 and 34.1 s).

## Adaptation
- Colour: red, the brand accent or a new main colour the user gives; the neon glow is always on, on dark and bright footage. [User] Glow radius ≈ 0.4–0.8× the cap height, glow opacity high.
- Font: a heavy italic display serif (brand serif if any).
- Scaling: inline ≈ 1.1–1.3× the caption size; big ≈ 40–45 % of the frame width, never covering the face.

## Key numbers
- Entrance: full word in 1 frame, 2 frames before the spoken onset (00:07.674) (observed; table in ANALYSIS.md).
- Big word hold 2.67 s to the cut (00:07.674–00:10.344) (observed; table in ANALYSIS.md).

## Success criteria
- The red word reads instantly as the key word and looks lit, not printed.
- It lands on the spoken word, never ahead of the sentence's meaning.

## User notes
- [User] The darkness of the reference is mostly the real shooting environment, not the style; this technique must also work on bright footage (with new main colours for some texts) ("اون تیرگی محیط ... بیشتر از اینکه فیلتر باشه یا سبک ویدیو، طرز فیلمبرداری و محیط واقعی خودشه").
- [User] The neon glow is always kept, on dark and on bright footage ("نه درخشش نئونی رو همیشه داشته باشه"), 2026-10-25.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
