---
name: text-caption-emphasis-tiers
description: Single-word captions in three tiers: normal words small medium sans, stressed words bigger bold sans, key numbers/concepts in a larger italic serif; all hard-swapped on the word. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-21
  sources: [src-002]
---

# text-caption-emphasis-tiers

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
One word at a time sits centred on the upper chest (about the mic head). Three looks are used inside the same caption track:
- Tier 1, normal words: small white sans, medium/semibold weight, about 2.4 % of frame height.
- Tier 2, stressed words ("over", "clear,", "overwhelming.", "apply"): the same sans, bolder and noticeably larger (about 1.7–2x width).
- Tier 3, key numbers and concepts ("13,000 followers", "Actionable tips", "'Youtube'", "content.", "blindly."): a high-contrast italic serif, larger again (about 6–7 % of frame height), can hold a 2-word phrase.
Swaps are hard cuts; the caption itself does not move. Tier 3 may get a flicker entrance (see `text-flicker-in`).

## Intended effect
Readable on mute while creating a rhythm of emphasis: the viewer hears and sees which words matter, and the serif words feel premium and "quotable".

## Defining characteristics
- Three distinct tiers in one track, chosen by meaning, not at random. [Fixed]
- Tier 3 is a different typeface family (italic serif) from tiers 1–2 (sans). [Fixed]
- Tier 3 is rare: about one per sentence or less; tier 2 a few per step. [Rule]
- One word (or one short key phrase) at a time, hard swaps. [Fixed]

## When to use
- Triggers: tier 2 on the stressed word of a sentence; tier 3 on the number, named concept or closing word.
- Avoid when: speech has no clear stresses; more than ~30 % of words would be emphasised.

## Anatomy over time
- Start: on each word's onset.
- Development: none; tier 2/3 words often hold longer because they are said slower.
- Repetition: tier 3 marks the hook number, each concept and the final word.

## Relationships
- Tier 1 is the existing `text-single-word-captions-chest` ([SKILL.md](../text-single-word-captions-chest/SKILL.md)), adapted: a little higher (upper chest) and medium weight. This technique adds tiers 2 and 3 on top of it.
- Continues over B-roll and on inset cards (placed above the card there).
- Pairs with `text-flicker-in` for tier-3 closing words, and with `graphic-ui-stat-popup` under a tier-3 number.

## Adaptation
- Adaptable: serif and sans families (brand fonts), colours (brand white; tier 3 may take the brand accent).
- Scaling: keep tier ratios: tier 2 ≈ 1.6–2x tier 1; tier 3 ≈ 2.5–3x tier 1 in height.

## Key numbers
- Tier 1 word centred at x 43–57 %, y ~47–50 %, h ~2.4 % (observed; table in ANALYSIS.md).
- Tier 2 word ("clear,") w ~24 %, h ~5.4 % (observed; table in ANALYSIS.md).
- Tier 3 serif ("Step 1") w ~22 %, h ~6.2 % (observed; table in ANALYSIS.md).

## Success criteria
- A viewer can name the three tiers after watching.
- Emphasis lands on words the speaker actually stresses.

## User notes
- [User] Agreed: the normal small captions are the existing chest captions; this skill only adds the emphasis tiers.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md): tier frames; `tier1-to-tier2` sequence; two clips in context.
