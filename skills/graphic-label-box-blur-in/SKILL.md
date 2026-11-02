---
name: graphic-label-box-blur-in
description: Semi-opaque coloured rounded boxes laid over parts of the frame to name zones; each box blooms in from a soft white blur into its colour while its label types on, and leaves by erasing its letters. For explaining layout or zones. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-20
  sources: [src-001]
---

# graphic-label-box-blur-in

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
A wide rounded rectangle (about 72 % of frame width, ~10 % of height) appears over a specific zone of the frame. It enters as a blurred, glowing, almost white shape that sharpens and tints into its colour (green, yellow or red) over ~6–8 frames; the box stays slightly see-through so the speaker shows through. If it carries a label, the label (condensed, widely spaced uppercase, white) types on letter by letter from left to right while the box tints. It leaves with the letters erasing from right to left and the box fading, or, for a stack, the boxes tilt a few degrees and drop away one after another.

Two uses were seen:
- Zone stack: three unlabelled boxes, green (top), yellow (middle), red (bottom), entering one after another ~0.36 s apart to show the frame's layout.
- Labelled zones: one box at a time, "TITLE" (green, top), "FACE" (yellow, middle), "CAPTIONS" (red, lower middle), each on the zone it names, each starting on a jump cut.

## Intended effect
Makes an abstract instruction (where things go in the frame) visible and colour-coded, with a soft, premium-feeling entrance.

## Defining characteristics
- Box sits exactly over the zone it represents. [Fixed]
- Blur/glow-to-colour entrance; not a slide or a scale pop. [Fixed]
- Letter-by-letter type-on in, reversed erase out. [Fixed]
- Semi-opaque fill, rounded corners, one colour per meaning. [Rule]

## When to use
- Triggers: the speaker explains where things go in the frame, parts of a layout, or a ranked set (good / okay / bad).
- Avoid when: the zone is not on screen, or more than ~3 boxes would be needed at once.

## Anatomy over time
- Start: on the word that names the zone, ideally together with a jump cut. [Observed]
- Development: ~0.25–0.3 s blur-to-colour; labels type on over ~0.4 s.
- Resolution: hold while the zone is discussed, then erase ~0.2 s before the next box; stack exits by tilting/dropping over ~0.12 s.
- Repetition: one box per named zone; captions are hidden while a box shows.

## Relationships
- Speech: entrance on the naming word.
- Cuts: each new label coincided with a jump cut at the same framing (13.04, 14.56, 16.28). [Observed]
- Music: the TITLE box landed on a sub-bass hit (13.09). [Observed]
- Other techniques: replaces `text-single-word-captions` while visible.

## Adaptation
- Adaptable: colours (traffic-light logic, or brand colours if the meaning allows), label text and font.
- Scaling: box width follows the zone; keep inside ~14–86 % of width for 9:16 safe areas.
- Brand: label font and box colours follow the brand unless the colours carry meaning (good/bad).

## Key numbers
- Stack entrance offsets ~0.36 s, ~0.28 s (observed; table in ANALYSIS.md).
- Label erase out ~0.2 s; stack tilt/drop exit ~3 frames, a few degrees (observed).
- Box extent x 14–86 %, CAPTIONS box y ~54–75 % (observed, approximate).
- Green ~#61C334 (observed).

## Success criteria
- Each box covers the zone it names.
- Entrance reads as a soft bloom into colour, not a pop.
- Labels type on and erase in opposite directions.
- No caption collides with a box.

## User notes
- (none yet)

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Entrance look: `blur-in`, `tinting`, `label-blur-in`, `type-on` frames and the `label-in` sequence.
- Exits: `label-swap`, `label-out`, `tilt-exit`.
- Timing with speech and cuts: the two clips.
