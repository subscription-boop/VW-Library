---
name: text-keyword-blur-backdrop
description: A key phrase appears huge and heavy across the chest (blur-in), then stays as a blurred, ghosted backdrop behind the next small caption line. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-22
  sources: [src-003]
---

# text-keyword-blur-backdrop

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
On "first day", "FIRST DAY" appears in big white heavy caps across the frame, blurring in over ~0.25 s. It holds sharp ~0.3 s, then turns soft and semi-transparent while the normal small caption ("of posting my edits") builds on top of it at the same height, before both clear.

## Intended effect
The key idea lingers visually while speech moves on; layered depth in the typography.

## Defining characteristics
- Keyword: uppercase heavy sans, ≈ 85–90 % width. [Rule]
- Blur-in entrance ≈ 0.25 s. [Rule]
- After the hold it becomes blurred/translucent and stays behind the next small caption. [Fixed]

## When to use
- Triggers: the topic phrase of the hook ("FIRST DAY", "3 TIPS").
- Avoid when: more than once or twice per video.

## Relationships
- Works with `text-phrase-build-blur-rise` (the small caption on top).

## Adaptation
- Brand typeface and colour; backdrop opacity ≈ 40–60 %.

## Key numbers
- Blur-in 00:03.733–00:04.000; sharp hold 00:04.000–00:04.330 at y ≈ 53–61 %, x 6–94 %; backdrop blurred and translucent 00:04.330–00:05.200 under "of posting my edits" (observed; table in ANALYSIS.md).

## Success criteria
- Both layers stay readable; the backdrop never competes with the small caption.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md).
