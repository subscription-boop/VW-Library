---
name: card-chapter-title
description: Hard cut from the speaker to a full-screen flat card where the section number and title build word by word as they are spoken, then a hard cut back. For numbered tips, parts and chapters. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: card
  status: approved
  approved: 2026-10-20
  sources: [src-001]
---

# card-chapter-title

> Library technique (category: `card`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (observed measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
The talking head hard-cuts to a full-screen flat colour card while the voice continues. Text on the card appears word by word, each word popping on (no motion) the moment it is spoken, left-aligned, heavy sans, tight tracking, stacked lines. A number is part of the card: either a white numeral in a solid black box, or a red numeral. One word can sit on a solid red bar that fades in just before the word appears. After the last word holds briefly, the edit hard-cuts back to the speaker.

Two variants were seen:
- Series card: full-bleed red, white "part", then a boxed "2" below it.
- Tip card: light blue-grey card with a faint dot grid, boxed "1" top-right of the title, "Framing" / "and" (white on a red bar) / "composition"; or red "2" above "font" / "selection".

Lead-in: for tip 2, the red "2" appears over the speaker 2 frames before the cut, at exactly the place it occupies on the card, so the number seems to stay while the world changes around it.

## Intended effect
Clear, fast chapter breaks: the viewer always knows which tip is next, and the full-screen colour resets attention.

## Defining characteristics
- Hard cut in and hard cut out; the card is full screen. [Fixed]
- Words appear one by one in sync with speech; no slide or scale. [Fixed]
- Numbered: the number is the first element. [Rule]
- Flat background, one accent colour, heavy black or white type. [Rule]

## When to use
- Triggers: the speaker announces a part, a tip number or a chapter title.
- Avoid when: the title is long (more than ~4 words) or speech is too fast to read word by word; then show the whole title at once.

## Anatomy over time
- Start: hard cut on the first word of the announcement (or on a music hit if one is close [Observed]).
- Development: one word per spoken word; an accent bar may fade in over ~2–3 frames just before its word.
- Resolution: last word holds ~0.4–0.8 s, then hard cut back.
- Repetition: one card per section; style consistent within a video (the reference mixes two numeral styles [Observed]).

## Relationships
- Speech: word-level.
- Cuts: replaces the picture; captions are off while the card is up.
- Music: in the reference the cut into card 1 sat on a sub-bass hit (06.52). [Observed]
- Other techniques: optional number lead-in over the previous shot.

## Adaptation
- Adaptable: card colour, accent colour and type follow the brand; number style (boxed or coloured).
- Scaling: hold time follows the spoken title length; minimum on-screen time for the full title ~0.4 s.
- Brand: background = brand light or primary colour; accent bar = brand accent.

## Key numbers
- Card lengths observed: series card 0.88 s, tip 1 card 1.72 s, tip 2 card 1.48 s (observed; table in ANALYSIS.md).
- Colours observed: red #FB0000, light #E0ECFE.

These describe the references. They are not quotas or required values.

## Success criteria
- Each word appears on its spoken onset (±1–2 frames).
- In and out are clean hard cuts.
- The card reads instantly as "section N: title".

## User notes
- (none yet)

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Build timing: `chapter1-build`, `chapter2-build` sequences. Series variant: `part-card`. Number lead-in: frame `number-lead-in` and the `chapter2-with-lead-in` clip. Music hit at the cut: audio excerpt.
