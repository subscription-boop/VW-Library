---
name: text-kinetic-stack-mixed-size
description: Kinetic caption blocks for interview/podcast clips: each phrase builds into a stacked lockup of small and big words (big on the stressed words), words fading from grey/blur to white, placed in empty space; the block clears at once. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-22
  sources: [src-003]
---

# text-kinetic-stack-mixed-size

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Over the podcast shots the caption is a small typographic block in empty space (over the chair, lower middle). Words appear on their onsets: unstressed words small, stressed words 2x bigger and bolder ("do things", "you're gonna"), arranged in offset lines (small above/below big, staggered left/right). Each word enters grey and soft, then turns white. When the thought ends, the whole block fades out (~0.1 s) and the next block starts.

## Intended effect
Gives a quote-like, designed feel to someone else's speech while staying readable.

## Defining characteristics
- Two sizes inside one block, big on stressed words. [Fixed]
- Offset/stacked lockup, not a single line. [Fixed]
- Grey/blur → white per word; whole block exits together. [Rule]
- Placed in negative space, not centre by default. [Rule]

## When to use
- Triggers: interview, podcast or quote clips; reflective speech.
- Avoid when: fast talking-head tips (use simpler captions).

## Adaptation
- Typeface/colours from the brand; keep the block inside ~70 % width.

## Key numbers
- Block 1 (00:10.700–00:11.933): "don't" small / "do things" big / "just because" small (observed; table in ANALYSIS.md).
- Block 2 (00:12.000–00:13.500): "you think" small / "you're gonna" big / "get something for it" small (observed; table in ANALYSIS.md).
- Exit at 00:13.467: block fade ≈ 0.07–0.1 s (observed; table in ANALYSIS.md).

## Success criteria
- Stresses read at a glance; blocks never cover faces.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md).
