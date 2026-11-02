---
name: title-stacked-hook
description: Opening topic title in two stacked lines above the speaker: a white word that fades in letter by letter, then a bigger yellow word that fades in whole; it leaves letter by letter. For the first seconds of a talking-head video. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: title
  status: approved
  approved: 2026-10-20
  sources: [src-001]
---

# title-stacked-hook

> Library technique (category: `title`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
From the first frame, the video's topic appears in the top third as two tightly stacked lines ("talking" / "head"). Line 1 is white, heavy, tightly tracked, and fades in letter by letter from left to right over ~0.4 s. Line 2 is larger, in the highlight yellow, sits right under line 1 with the lines almost touching, and fades in as one word while its colour goes from grey to full yellow over ~0.3 s. The title holds while the speaker talks (small single-word captions run at chest height underneath). It leaves letter by letter from right to left on line 1, with line 2 fading out at the same time, over ~0.5 s, and the main captions take the space.

## Intended effect
Tells the viewer the topic in the first second, before the first sentence ends, and marks the key word in the brand accent.

## Defining characteristics
- Two lines, stacked with near-zero leading; line 2 is the key word, larger and in the highlight colour. [Rule]
- Staggered per-letter fade on the way in (line 1) and reversed per-letter fade on the way out. [Fixed]
- Visible from frame 1; no build-up before it. [Rule]
- Sits above the head; while it is up, captions use the small chest captions instead of the large top ones. [Rule]

## When to use
- Triggers: the opening of a video with a short, nameable topic (two or three words).
- Avoid when: the topic needs a full sentence; the space above the head is not clear.

## Anatomy over time
- Start: frame 1, letters of line 1 fading in one after another.
- Development: line 2 fades in once line 1 is mostly in (~0.45 s), grey to yellow.
- Resolution: holds ~2 s, then exits right to left; out by ~3.2 s.
- Repetition: once per video.

## Relationships
- Speech: covers the first spoken sentence; the exit lines up with the sentence's turn ("...from this to this").
- Other techniques: pairs with `text-single-word-captions-chest` ([SKILL.md](../text-single-word-captions-chest/SKILL.md)) while the title is up, then hands the top over to `text-single-word-captions` ([SKILL.md](../text-single-word-captions/SKILL.md)); in the reference, `graphic-level-meter` ([SKILL.md](../graphic-level-meter/SKILL.md)) appeared during its last second.

## Adaptation
- Adaptable: the two words, colours (white + brand accent), font (brand heavy display sans).
- Scaling: line 2 width ~70–80 % of frame width; reduce if the word is long.
- Brand: line colours and typeface follow the brand.

## Key numbers
- Line 1 letter-stagger fade-in ~0.44 s (11 frames); line 2 fade + grey to yellow ~0.32 s (8 frames), starting at ~0.48 s; exit, letters right to left, ~0.48 s, from ~2.76 s to ~3.24 s (observed; table in ANALYSIS.md).
- Block position ~8–20 % of frame height, centred (observed; table in ANALYSIS.md).

## Success criteria
- Topic readable within the first second.
- Letter stagger visible on both entry and exit; exit runs in the opposite direction.
- Line 2 clearly larger and in the accent colour; the two lines read as one block.

## User notes
- (none yet)

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Entry timing: open the `enter` sequence. Exit: open `exit`. Whole thing with audio: `hook-title` clip.
