---
name: card-white-word-beat
description: Hard cut to a plain white full-screen card where a short transitional phrase plays one word at a time in small black sans (key word in larger serif), then hard cut back. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: card
  status: approved
  approved: 2026-10-21
  updated: 2026-11-01 (papers A–E approved for every card, no question; paper texture added 2026-10-22)
  sources: [src-002]
---

# card-white-word-beat

> Library technique (category: `card`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Mid-sentence, the picture hard-cuts to a flat white (#FDFDFD) full-screen card. The speech continues; the caption track continues on the card in black: one small sans word at a time, centred slightly above the middle ("Here's", "how", "you", "do", "it"), and the key phrase in a larger black italic serif ("3 steps."). Words replace each other (they do not accumulate). A hard cut returns to the footage. A single key word on the card may flicker in ("Instead").

## Intended effect
A breath and a pattern break before a list or a turn ("Instead"), focusing all attention on the words.

## Defining characteristics
- White, nothing on the card but the words. [Fixed] (The reference card is flat white [Observed].)
- The white carries a subtle, photographic, detailed paper texture (cotton, cold-press, recycled… ), never a flat digital white. [User]
- Use a different paper each time a card appears, so cards don't repeat; keep the texture subtle, never so strong that it competes with the words. [User]
- Words replace one at a time, same rules as the captions, colours inverted to black. [Fixed]
- Short: 0.5–1.7 s. [Rule]
- Hard cut in and out. [Fixed]

## When to use
- Triggers: set-up lines ("Here's how you do it"), pivot words ("Instead", "But").
- Avoid when: the line carries emotion on the face.

## Relationships
- Key word may use `text-flicker-in`. A low sub hit may sit on the cut [Uncertain].

## Adaptation
- Card colour may follow the brand's light surface; type follows brand fonts.
- Paper: the five papers of `tools/paper.py` (A smooth, B coldpress, C recycled, D laid, E cotton) are all approved; use them without asking, a different one per card. [User 2026-11-01] The paper may change on each word swap inside one card when only one card exists in the video (approved in project 2026-10-21-3-skills-beat-a-degree).
- Paper textures can be generated (no third-party rights) or taken from free stock photos the user approves; keep detail photographic (fibres, tooth, soft uneven light).

## Key numbers
- Card length 0.5–1.7 s (above). Word size ~2.5 % of frame height, centred at y ~45–47 % (observed; table in ANALYSIS.md).

## Success criteria
- The card feels like a pause, not a title; words stay in sync with speech.

## User notes
- [User] Give full-screen flat white cards a paper texture; use a different paper each time for variety, but don't overdo it. (به صحنه‌هایی که صفحه‌های سفید تخت کامل دارن یه تکسچر کاغذی بده … هربار یه مدل … زیاده روی نکن)
- [User] The texture should look photographic and detailed. (یکم تکسچر عکسی‌تر باشه و پر جزییات‌تر)
- [User 2026-11-01] All five papers (A–E) are approved; register them and use them from now on without asking each time; this replaces the earlier "show the texture before applying it". (همشون اوکیه، ازین به بعد همینارو برای کارت کاغذی ثبت و استفاده کن تا نیاز نباشه هربار بپرسی)

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
