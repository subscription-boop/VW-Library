---
name: text-spaced-words-neon-lockup
description: On wide shots (and once on a medium shot) the spoken phrase is built as a lockup: small white words appear one by one at fixed, widely spaced positions across a row, and the key words land underneath/over them as a big red neon italic serif line; a second small row may continue under it. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-25
  sources: [src-006]
---

# text-spaced-words-neon-lockup

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
On the wide establishing shots the caption is not a line on the chest. It is a **typographic lockup in the empty space above the table**: small white words (medium-weight sans, glowing slightly) **pop in one at a time on their spoken words at fixed, widely spaced positions** across a row - the first word near the left end, the middle word near the centre, the last word near the right end - so the row is as wide as the big line it belongs to. The key words then land as a **big red neon italic serif line** (`text-neon-serif-keyword`) right under the row, overlapping it slightly. In the closing lockup a **second small row** continues under the big word ("from the consumer."). On a medium shot the same idea appears inverted: the big red word first, its follow-up small words spread underneath ("connecting  to  the  brand").

## Intended effect
Turns the wide shot into a poster: the small words carry the sentence, the big red words carry the meaning, and the empty dark set becomes the layout.

## Defining characteristics
- Small white words placed at pre-set spread-out positions (left / centre / right), not packed into a line [Fixed]
- Each small word pops in on its spoken onset, no animation [Rule]
- Big red neon serif line under/over the row, overlapping it slightly; same total width (≈ 75–80 % of the frame) [Fixed]
- Used on wide shots (opening and closing) and on one medium shot without the face in that zone [Observed]
- Leaves with the cut (no exit) [Rule]

## When to use
- Triggers: the first and last sentences of a clip on a wide shot; one strong sentence that has a clear key word.
- Bright footage: allowed - small words in a dark or white colour that contrasts with the background (soft shadow), big line in the video's main colour, always with the neon glow (see `text-neon-serif-keyword`). [User]
- Avoid when: the shot is a close-up (no empty space) or the sentence has no key word.

## Anatomy over time
- Start: first small word on its onset (from the first frame after the film burn at the opening).
- Development: small words at their slots ~0.1–0.3 s apart; big words at their onsets ("paid" 0.709, "marketing" 1.001).
- Resolution: holds to the cut (opening) or to the end of the video (closing).

## Relationships
- Big line = `text-neon-serif-keyword`; caption system elsewhere = `text-phrase-build-glow-pop`.
- Shots: `cut-multicam-podcast-bookends` gives the wide shots it lives on.
- Sound effects: none.

## Adaptation
- Brand: small words in the brand's text sans, big line in the brand accent (or red) with glow.
- Scaling: lockup width ≈ 75–80 % of the frame, small words cap height ≈ 1.6–2 % of the frame height, big line ≈ 4–5×.

## Key numbers
- Small words at 00:00.125–00:01.000: "we" 0.125, "don't" 0.167, "spend" 0.292, "on" 0.584 at x ≈ 20 % / 50 % / 78 % of the width (observed; table in ANALYSIS.md).
- Lockup width ≈ 78 % of the frame width, centred on the gap between the two people (00:01.300) (observed; table in ANALYSIS.md).

## Success criteria
- Reads as one designed lockup, not a broken caption line; never over a face.

## User notes
- [User] The darkness of the reference is mostly the real shooting environment, not the style; this technique must also work on bright footage (with new main colours for some texts) ("اون تیرگی محیط ... بیشتر از اینکه فیلتر باشه یا سبک ویدیو، طرز فیلمبرداری و محیط واقعی خودشه").
- [User] The neon glow is always kept, on dark and on bright footage ("نه درخشش نئونی رو همیشه داشته باشه"), 2026-10-25.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
