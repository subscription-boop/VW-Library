---
name: text-caps-keyword-stack
description: On full-screen talking-head shots, the key concept replaces the small chest caption as a much bigger heavy white uppercase word, and its second word stacks under it on the next beat ("CONTRARIAN / PERSPECTIVES", "CONTENT / SYSTEM"), each hit with a soft click. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-25
  sources: [src-005]
---

# text-caps-keyword-stack

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Normal captions on full-screen shots are small white words on the chest. When the speaker says the key concept, the caption is replaced by the concept in **large heavy white uppercase** (≈ 2.5–3× the normal caption) at the same position. The first word pops in instantly (hard, no fade); when the second word is spoken it **stacks directly under the first**, tight line spacing. The stack holds while it is relevant and then the normal small captions return.

## Intended effect
Marks the one or two concepts the viewer must remember; the size jump is the emphasis, no colour needed.

## Defining characteristics
- Uppercase, heavy sans, white, ≈ 2.5–3× the regular caption size [Fixed]
- Hard pop per word on its spoken onset; second word stacks below, line spacing ≈ 0.85 [Rule]
- Used sparingly: 2–3 concepts per minute [Observed]
- A soft click on each word (`sfx-click-graphic-hit`) [Observed]

## When to use
- Triggers: named concept, the "answer" of the video, the lead-magnet keyword ("Comment Formats").
- Avoid when: every sentence would qualify (keeps its power only if rare).

## Anatomy over time
- Start: word 1 onset → word 1 pops. Development: word 2 onset → word 2 added below. Resolution: replaced by the next small caption word.

## Relationships
- Caption system: an emphasis tier on top of `text-single-word-captions-chest`.
- Sound effects: `sfx-click-graphic-hit` on each word.

## Adaptation
- Font: brand heaviest sans, uppercase, white; may take the brand accent on one word.
- Width ≤ 75 % of the frame; long words scale down to fit.

## Key numbers
- Reference second word added 0.5 s after the first, on speech (observed; table in ANALYSIS.md).
- Reference clicks land ≈ 2 frames after each word appears, on the spoken onset (observed; table in ANALYSIS.md).

## Success criteria
- The concept is readable at a glance and clearly bigger than every other caption.
- Each word appears with its spoken word; the click lines up within ~1 frame.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
