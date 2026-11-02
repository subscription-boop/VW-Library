---
name: text-word-as-specimen
description: When the speaker names a font (or any visual style), that caption word is shown in that style, in the highlight colour, so the word demonstrates itself. For list-style explainers. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-20
  sources: [src-001]
---

# text-word-as-specimen

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Inside a run of single-word captions, each time the speaker names a font, the caption for that name is set in that very font and coloured yellow (Playfair in a serif, ANTON in a condensed heavy, ENGRAVER in a high-contrast display serif over two lines, DRUK WIDE in an extended heavy, SEASALT / FRANKLIN NOTES / GABRIEL WEISS in brush or marker scripts, Creato / Helvetica / Poppins in their sans). Lead-in words about a style also take that style: "spice things up with handwritten fonts like" is shown in a white handwritten font. Ordinary words stay in the normal caption style. Swaps are hard, same as the captions.

## Intended effect
The viewer sees each example the instant they hear it, so the list explains itself and every item gets a small visual surprise.

## Defining characteristics
- The word's appearance is the thing the word names. [Fixed]
- Named items are in the highlight colour; style-describing lead-in words keep the caption colour but take the style. [Rule]
- Same position and swap timing as the surrounding captions; no extra animation. [Rule]

## When to use
- Triggers: the speaker lists fonts, colours, effects, materials or other things that can be shown in the word itself (a colour name in that colour, "blur" blurred, "bold" bold).
- Avoid when: the style would make the word unreadable at caption size, or the named item cannot be rendered honestly (do not fake a font you don't have; ask).

## Anatomy over time
- Start: on the name's onset.
- Development: none; held for the spoken length, multi-word names held as one unit (FRANKLIN NOTES, DRUK WIDE).
- Resolution: hard swap back to normal captions on the next word.
- Repetition: once per named item.

## Relationships
- Requires a single-word caption track such as `text-single-word-captions`.
- Speech: names held for the whole name; two-line stacking is allowed for long names.
- Music: some names landed near music hits in the reference [Observed], not a rule.

## Adaptation
- Adaptable: highlight colour follows the brand accent; caption size may shrink so wide styles fit in ~75 % of width.
- Brand: only the highlight colour follows the brand; the specimen style itself must stay true to what is named.

## Key numbers
- Four title fonts in sequence ~0.8–1.1 s each (00:28.300–00:31.500) (observed; table in ANALYSIS.md).
- Swap Playfair → ANTON: hard cut, 0 frames transition (00:28.920) (observed; table in ANALYSIS.md).
- Lead-in words in handwritten style: white, ~2 s (00:32.800–00:34.800) (observed; table in ANALYSIS.md).

These describe the references. They are not quotas or required values.

## Success criteria
- Every named style is shown in that style on its own name, in sync.
- The specimen words are as readable as normal captions.
- No item is shown in a style that isn't the one named.

## User notes
- (none yet)

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Look of each specimen: open the frames (one per font).
- Timing and hard swaps: open `hard-swap` and the two clips.
