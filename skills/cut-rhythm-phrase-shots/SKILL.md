---
name: cut-rhythm-phrase-shots
description: Rough-cut shot rhythm for a talking-head explainer - picture changes on almost every phrase (talking head, card, inset, B-roll), shots ~0.5-4 s with ~1.5 s average, very few visible jump cuts (same framing), and B-roll-to-B-roll cuts allowed mid-phrase over continuous voice. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: cut
  status: approved
  approved: 2026-10-21
  sources: [src-002]
---

# cut-rhythm-phrase-shots

> Library technique (category: `cut`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (observed measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
The picture changes roughly once per phrase. In 26.3 s there are 17 shots: talking head, white cards, one inset section and a chain of B-roll shots. Most changes are to a different kind of picture, not a jump cut on the same shot; only three visible jump cuts appear, and they keep the same framing (any running zoom simply continues across them). Over B-roll the voice continues, and B-roll-to-B-roll cuts can fall on a word.

## Intended effect
Constant visual renewal without the choppy feel of many jump cuts; the edit feels smooth and premium while still fast.

## Defining characteristics
- Shot length 0.53–3.87 s, average ≈ 1.55 s, median ≈ 1.5 s. [Observed]
- Share of screen time: talking head ≈ 51 %, B-roll ≈ 26 %, inset ≈ 15 %, white cards ≈ 8 %. [Observed]
- Picture changes at phrase boundaries (see `cut-tight-phrase-joins`); B-roll-to-B-roll cuts may land mid-phrase (21.567 on "for"). [Observed]
- Visible jump cuts: 3 in 26 s (4.767, 11.667, 24.5), same framing, no reframe. [Observed]
- Never two jump cuts in a row; a jump cut sits ~0.6 s after a section-start cut (header beat) or near the end. [Observed]
- Longest talking-head stretch without a cut ≈ 2.5 s; longest any-shot ≈ 3.9 s (inset section, which changes content inside at 8.7). [Observed]

## When to use
- Triggers: talking-head explainers with B-roll available; the user wants fast but not choppy.
- Avoid when: there is no B-roll or cards to change to (then use jump cuts with reframing instead, or a different approach).

## Relationships
- Uses `cut-tight-phrase-joins` for where exactly each cut lands.
- The non-talking shots come from other techniques: `card-white-word-beat`, `layout-inset-card-demo`, `transition-blur-bridge`, B-roll inserts.
- Running zooms (`zoom-cut-ease-out`) continue across same-framing jump cuts.

## Adaptation
- Plan one picture change per phrase; pick the picture by what the phrase says (B-roll that matches the words, a card for a set-up or pivot word, an inset for "this video / this example").
- Keep visible jump cuts rare (about one per 8–10 s); when the talking head must continue, cut to B-roll instead of jump-cutting.
- B-roll chains: 0.7–1.5 s per shot; cut on phrase gaps where possible.

## Key numbers
- 17 shots, 16 cuts, plus 1 content swap inside the inset at 8.7 (observed; table in ANALYSIS.md).
- Shot lengths (s): 2.47, 1.70, 0.60, 2.43, 3.87, 0.60, 1.73, 1.67, 2.60, 0.70, 1.50, 0.53, 1.17, 0.70, 0.90, 1.33, 1.77 (observed).
- B-roll chain at 20.40–23.17: 1.17, 0.70, 0.90 s (observed).

## Success criteria
- The picture changes about once per phrase, the edit never feels choppy, and every B-roll shot matches the words.

## User notes
- None yet.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md): shot map, B-roll chain clip, jump-cut clip.
