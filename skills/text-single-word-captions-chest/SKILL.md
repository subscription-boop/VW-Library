---
name: text-single-word-captions-chest
description: One spoken word at a time, small, white and bold, at the speaker's chest just under the face, hard-swapped on each word. A quieter caption layer that leaves the top of the frame free. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-20
  sources: [src-001]
---

# text-single-word-captions-chest

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Only the word being spoken is on screen, set small (about the size of a word on a T-shirt print) in a heavy sans with tight letter-spacing, white, lowercase as spoken. It sits centred on the speaker's chest, just below the chin and above the microphone. Each new word replaces the previous one with a hard cut: no pop, no slide, no scale.

## Intended effect
Keeps every word readable on mute while staying out of the way: the top of the frame stays free for a title or a graphic, and the caption reads almost like part of the shot rather than a layer on top.

## Defining characteristics
- Exactly one word at a time, swapped on the word's onset, no caption animation. [Fixed]
- Small: roughly a third of the size of the large top captions. [Fixed]
- Centred on the chest, below the face, inside the body. [Fixed]
- White, heavy, tight tracking, no box or outline. [Rule]

## When to use
- Triggers: a title or graphic occupies the top third; a calmer, more intimate stretch of talking; a section about frame layout where the top space must stay visibly empty.
- Good fit: dark or plain clothing that gives white text contrast.
- Avoid when: the speaker gestures a lot in front of the chest (hands cover the word), busy or white clothing, or the moment needs strong emphasis (use `text-single-word-captions` ([SKILL.md](../text-single-word-captions/SKILL.md)) instead).

## Anatomy over time
- Start: first word's onset.
- Development: one swap per word, never ahead of speech.
- Resolution: holds the last word until a cut, a card, or a switch to the large top captions.
- Repetition: continuous for the stretch where it is chosen; hidden while a label box covers that zone.

## Relationships
- Subject: placed on the chest; it should not touch the chin or the microphone.
- Speech: word-level sync.
- Other techniques: in the reference it ran under `title-stacked-hook` ([SKILL.md](../title-stacked-hook/SKILL.md)) and through tip 1 before the label boxes; the edit switched to `text-single-word-captions` ([SKILL.md](../text-single-word-captions/SKILL.md)) right when the title left (00:03.3).

## Adaptation
- Adaptable: typeface and colour follow the brand; size follows the speaker's chest width.
- Scaling: keep the longest word within ~25–30 % of frame width and inside the torso.
- Brand: caption colour and typeface from the selected brand; keep weight heavy.

## Key numbers
- Word width ("frame") ~25 % of frame width (observed; table in ANALYSIS.md).
- Vertical position ~57–61 % of frame height (observed; table in ANALYSIS.md).
- Text height ~4 % of frame height (approximate) (observed; table in ANALYSIS.md).
- Stretches using this placement: 00:00.000–00:03.240 and 00:08.240–00:13.000 (~3.2 s, ~4.8 s) (observed; table in ANALYSIS.md).

These describe the references. They are not quotas or required values.

## Success criteria
- One word at a time, in sync with speech.
- The word sits on the chest, never on the face, chin or microphone.
- It is readable but clearly quieter than the top captions.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Position and size: the `no-title` frames. Under a title: the `under-title` frames and clip. Swap timing: `word-swaps` sequence.
