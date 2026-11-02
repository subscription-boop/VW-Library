---
name: graphic-level-meter
description: A thin vertical bar at the frame's left edge that grows from short red to tall green as the speaker describes improvement, then falls back. A quick visual promise of before/after. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-20
  sources: [src-001]
---

# graphic-level-meter

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
A narrow vertical bar (~1.5 % of frame width) appears at the left edge at chest height. It starts as a short red stub, grows taller and turns yellow, then taller and green, on the words "from this … to this". It holds green briefly, then shrinks back through yellow to a red stub and vanishes. Colour changes are stepped (red, yellow, green), not a gradient.

## Intended effect
A small, fast "quality going up" gauge that makes the promise of improvement visible without covering the speaker.

## Defining characteristics
- Height and colour change together: short/red = bad, tall/green = good. [Fixed]
- Driven by the words that describe change. [Rule]
- Small and at the frame edge; never over the face. [Rule]

## When to use
- Triggers: "from this to this", "before vs after", "level up", any spoken improvement or decline.
- Avoid when: nothing is being compared; a big before/after visual is already on screen.

## Anatomy over time
- Start: red stub on the first "this".
- Development: grows to yellow then green in steps over ~0.7 s, peak on the second "this".
- Resolution: holds ~0.6 s, falls back to red and disappears within ~0.8 s.
- Repetition: once in the reference.

## Relationships
- Speech: tied to the comparison words.
- Other techniques: ran under `title-stacked-hook` and into `text-single-word-captions`.

## Adaptation
- Adaptable: side, height range, colours (keep the bad→good meaning clear).
- Brand: may use brand colours only if bad/good is still obvious.

## Key numbers
- Green, tallest ~8 % of frame height at 00:03.120–00:04.000; first appearance (red) 00:02.440, gone 00:04.480, total ~2.0 s (observed, approximate; table in ANALYSIS.md).

## Success criteria
- Peak green lands on the "after" word.
- The bar never draws attention away from the speaker for long (≤ ~2 s).

## User notes
- (none yet)

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Growth and colours: `rise-fall` sequence; in context with audio: `meter-in-context` clip.
- Uncertainty: the meaning (quality gauge) is inferred from the speech, not stated in the video.
