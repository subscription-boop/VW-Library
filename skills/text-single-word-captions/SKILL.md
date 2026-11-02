---
name: text-single-word-captions
description: One spoken word at a time as a big, tight, bold white word in the top third, hard-swapped on each word; key words turn highlight yellow. For talking-head videos with continuous speech. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-20
  sources: [src-001]
---

# text-single-word-captions

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Only the word currently being spoken is on screen. It sits large in the top third, above the speaker's head, in a heavy sans with very tight letter-spacing, white, lowercase as spoken (capital only where the sentence starts or for names). Each new word replaces the previous one with a hard cut: no pop, no slide, no scale. A word stays until the next word starts, so short words flash for 2–4 frames and stressed or long words hold longer. Key words (the call-to-action keyword, a named thing) are shown in the highlight yellow instead of white; the CTA keyword fades in from grey to yellow over ~2 frames.

## Intended effect
Keeps the eye locked on the top of the frame and the speaker's face, makes every word readable on mute, and gives the edit a fast, punchy rhythm without any motion effects.

## Defining characteristics
- Exactly one word on screen at a time, swapped on the word's onset. [Fixed]
- Hard swaps; the caption itself does not animate. [Fixed]
- Large, heavy, tightly tracked sans, white, no box, no outline. [Rule]
- Placed in the clear space above the head, centred. [Rule]
- Highlight colour reserved for a small number of key words. [Rule]

## When to use
- Triggers: any continuous speech in a talking-head or presenter video.
- Good fit: clean background above the head; medium-fast speech.
- Avoid when: the space above the head is busy or holds another title; very slow speech (single words then hang too long, consider short phrases instead).

## Anatomy over time
- Start: the caption appears on the first word's onset.
- Development: one swap per word, timed to speech, never ahead of it.
- Resolution: the last word holds until a cut or a card.
- Repetition: continuous; it pauses only while a full-screen card, a label box, or a title takes the space.

## Relationships
- Subject: sits above the head; the head must stay clear of it.
- Speech: word-level sync; hold length follows the word.
- Cuts: unaffected by jump cuts; continues straight through them.
- Other techniques: hidden while `graphic-label-box-blur-in` ([SKILL.md](../graphic-label-box-blur-in/SKILL.md)) boxes are on screen. While `title-stacked-hook` ([SKILL.md](../title-stacked-hook/SKILL.md)) occupies the top, the reference used the separate small chest captions, `text-single-word-captions-chest` ([SKILL.md](../text-single-word-captions-chest/SKILL.md)). `text-word-as-specimen` ([SKILL.md](../text-word-as-specimen/SKILL.md)) replaces individual words with styled ones.

## Adaptation
- Adaptable: font family (follow the brand's display sans), highlight colour (brand accent), exact vertical position (keep it above the head with a small gap).
- Scaling: on 16:9 or with a tighter shot, reduce size so the longest word fits within ~75 % of width.
- Brand: caption colour, highlight colour and typeface come from the selected brand. Keep the weight heavy and the tracking tight.

## Key numbers
- Caption width ("techniques") ~74 % of frame width (observed; table in ANALYSIS.md).
- Vertical position ~22–30 % of frame height (observed; table in ANALYSIS.md).
- Cap/x height incl. descenders ("overlay") ~12 % of frame height (observed; table in ANALYSIS.md).
- Keyword fade grey → yellow ~2 frames @ 25 fps (00:25.400–00:25.480) (observed; table in ANALYSIS.md).
- Highlight yellow ~#FBE904 (observed; table in ANALYSIS.md).

These describe the references. They are not quotas or required values.

## Success criteria
- At any moment at most one caption word is visible, and it is the word being spoken (within ~1 frame).
- No caption motion other than the hard swap (and the short colour fade on a CTA keyword).
- The caption never overlaps the face.
- Highlighted words are few and each has a clear reason.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Unsure about size and position: open the `big-top` frames.
- Unsure about swap timing: open the `word-swaps` sequence and the `captions-with-cta` clip.
- Unsure about the keyword highlight: open `keyword-fade-in`.
