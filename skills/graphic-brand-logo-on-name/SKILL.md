---
name: graphic-brand-logo-on-name
description: When the speaker says the brand's name, the brand's own logo/wordmark appears large on the chest in place of the caption, blurring in from grey with a slight shrink-settle, holds, then fades out. Fits any mention of the company or product name. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-28
  sources: [src-007]
---

# graphic-brand-logo-on-name

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (observed measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
"At **Bellucci Production** …": instead of the word caption, the company's wordmark (a script "Bellucci" over a bold sans "Production") appears across the speaker's chest, large (~75 % of the frame width). It enters from a grey, blurred, translucent and slightly bigger state and settles to sharp white in ~0.3 s, holds for the rest of the name (~0.5 s), then fades back to grey/transparent in ~3–4 frames, and the word captions continue.

## Intended effect
Brands the video in the speaker's own voice: the name becomes the logo the viewer should remember.

## Defining characteristics
- The real brand logo/wordmark, not typed text. [Fixed]
- Replaces the caption on the spoken name; same zone (chest). [Rule]
- Blur + grey + slight scale → sharp white in ~0.3 s; quick fade-out. [Rule]

## When to use
- Triggers: the brand/company/product name is spoken.
- Avoid when: the name is said many times in a row (use it on the first or most important mention), or no clean logo file exists.

## Anatomy over time
- Start: the first syllable of the name.
- Development: ~0.3 s blur-in with a small shrink.
- Resolution: hold to the end of the name, ~0.1 s fade to grey/transparent.
- Repetition: once in the body; the logo returns on the end card.

## Relationships
- Speech: syllable sync to the name.
- Other techniques: replaces `text-single-word-captions-chest` for those words; the same logo returns in `card-cta-fade-to-black` ([SKILL.md](../card-cta-fade-to-black/SKILL.md)).
- Sound effects: none observed.

## Adaptation
- Brand: always the selected brand's logo (white/monochrome version on footage); keep it ≤ ~80 % of frame width and clear of the face.

## Key numbers
- Blur-in ~9 frames (grey/translucent → white, slight shrink); hold ~0.3 s; exit fade ~3 frames (observed; table in ANALYSIS.md).
- Layout: centred, y ≈ 0.55–0.64 H, ≈ 0.75 W wide (observed).

These describe the references. They are not quotas or required values.

## Success criteria
- The logo is the brand's real mark, readable, on the spoken name; the face is clear.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
