---
name: title-small-row-over-condensed-caps
description: Two-line hook title in the top third from frame 1 - a row of small title-case words spread across the exact width of a huge, ultra-condensed white uppercase phrase below it; words appear one by one, the big words fade in from grey and blur; it vanishes on the first cut. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: title
  status: approved
  approved: 2026-10-24
  sources: [src-004]
---

# title-small-row-over-condensed-caps

> Library technique (category: `title`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
From the first frame a headline builds above the speaker's head. The bottom line is huge: a very condensed, very heavy uppercase sans in white ("THESE SONGS"), each word fading in from a grey, blurred, semi-transparent state to solid white in ~0.2 s. Above it, a row of small words in title case ("You  Need  To  Use") appears one word at a time; the small words are spread out so the row is exactly as wide as the big line (left edge to right edge). The headline is not the spoken sentence; it is the video's promise. It holds while the speaker talks (small chest captions run underneath) and disappears with a hard cut on the first jump cut.

## Intended effect
States the promise of the video in a poster-like way in the first second, with a strong typographic contrast (tiny words vs giant condensed caps).

## Defining characteristics
- Two lines: small title-case words on top, huge ultra-condensed uppercase below. [Fixed]
- The small row is justified to the full width of the big line (words spread apart). [Fixed]
- Big words: grey + blur + low opacity → solid white, ~0.2 s each, word by word. [Rule]
- Small words: appear one by one, ~0.1–0.2 s apart. [Observed]
- On screen from frame 1; leaves with a hard cut (no animation out). [Rule]
- Placed above the head, never over the face. [Rule]

## When to use
- Triggers: the video opening; a short promise/topic of 2–4 words plus a small lead-in.
- Good fit: calm talking head with background space above the head.
- Avoid when: the top third is busy with another graphic, or the hook is spoken as a punchline that should not be pre-revealed.

## Anatomy over time
- Start: frame 1 (after a single black frame in the reference), first big word already fading in.
- Development: big words one by one (~0.5 s apart); small words one by one in the same 0.7 s.
- Resolution: holds (~3 s in the reference) until the first cut, then gone.

## Relationships
- Speech: independent of the spoken words (the title is the written promise).
- Captions: small single-word chest captions run at the same time (`text-single-word-captions-chest`).
- Cuts: exits on the first jump cut.
- Sound effects: none observed.

## Adaptation
- Fonts: an ultra-condensed heavy sans for the big line (brand font if it has one; otherwise the brand's heaviest sans, horizontally condensed) and the brand sans for the small row.
- Colour: white by default; brand colour allowed for one word.
- Scaling: big line ≈ 85–90 % of frame width; small row ≈ 1/6 of the big line's height.

## Key numbers
- "THESE" fades grey/blur → white ~7 frames (00:00.033–00:00.267) (observed; table in ANALYSIS.md).
- "SONGS" added at 00:00.750, line complete (observed; table in ANALYSIS.md).
- Layout at 00:02.000: small row y ≈ 0.12 H; big line y ≈ 0.15–0.28 H, ≈ 0.88 W wide (observed; table in ANALYSIS.md).

## Success criteria
- The two lines read as one designed headline; the small row starts and ends exactly with the big line.
- Nothing covers the face; the headline is fully built within ~0.8 s.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Build speed: `sequences/…_title-build/` and `clips/…_hook-title-build-and-cut.mp4`.
- Layout: `frames/…_title-held.jpg`.
