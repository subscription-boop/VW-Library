---
name: layout-inset-card-demo
description: Hard cut to a "stepped back" view where the vertical video becomes a smaller card on a flat light background, so it can be shown as an example with overlays and other clips swapped inside; hard cut back to full screen. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: layout
  status: approved
  approved: 2026-10-20
  sources: [src-001]
---

# layout-inset-card-demo

> Library technique (category: `layout`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
On a hard cut, the full-screen talking head is replaced by a light blue-grey background with a faint dot grid, and the vertical video sits in the middle as a smaller card (~75 % of frame width). Overlays that explain the point are drawn on the card (here a red striped frame and a small green "safe zone" pill that fades in over ~6 frames). The single-word captions continue, now inside the card. While the voice continues, the card's content hard-cuts between examples (two other videos of the speaker, then his current footage). A hard cut returns to full screen.

## Intended effect
Turns the video into an object the viewer looks at, which is ideal when the point is about how a video looks on a phone or a feed. It also gives room to show several examples without leaving the explanation.

## Defining characteristics
- Hard cut in and out; no animated shrink. [Observed], keep unless the user wants motion.
- Video becomes a framed card on a flat background. [Fixed]
- Voice and captions continue uninterrupted across the change. [Fixed]
- Example clips swap inside the card, not full screen. [Rule]

## When to use
- Triggers: talking about the video itself (format, layout, safe zones, how it appears in the feed), or showing several examples of one idea.
- Avoid when: the speaker's expression is the point of the moment.

## Anatomy over time
- Start: hard cut on the sentence that introduces the reason or example.
- Development: overlays fade in on the card; examples cut every ~1.4 s.
- Resolution: hard cut back to full screen, keeping any overlay that should persist.
- Repetition: once in the reference.

## Relationships
- Speech: covers one sentence.
- Other techniques: `text-single-word-captions` ([SKILL.md](../text-single-word-captions/SKILL.md)) continue inside the card. Any explanatory overlay drawn on the card is content-specific; in the reference it was the creator's own safe-zone overlay, which the user chose not to save as a technique.

## Adaptation
- Adaptable: background colour (brand light colour), card size, overlay content.
- Brand: background and pill colours follow the brand.

## Key numbers
- Inset duration 4.36 s (00:18.000–00:22.360) (observed; table in ANALYSIS.md).
- Example swaps inside the card ~1.3–1.4 s apart (observed).
- Card scale relative to full frame ~0.69–0.75 (observed, approximate).

## Success criteria
- The change to the card reads as stepping back to look at the video.
- Voice and captions never break.
- Return to full screen is clean and immediate.

## User notes
- (none yet)

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Look: `card-with-pill`, `example-swap` frames. In/out cuts: `card-in`, `card-out` sequences. Full passage with audio: `inset-card` clip.
