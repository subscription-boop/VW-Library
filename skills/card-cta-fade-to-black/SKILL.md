---
name: card-cta-fade-to-black
description: The call to action builds as a big stacked lockup behind the speaker walking toward camera, then the footage fades to black in ~0.3 s leaving the CTA and the brand logo alone on black while the music fades out. Fits the end of promos and personal-brand ads. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: card
  status: approved
  approved: 2026-10-28
  sources: [src-007]
---

# card-cta-fade-to-black

> Library technique (category: `card`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (observed measurements, distinction from a related technique, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
On the last line ("…send us a message"), a centred stacked CTA ("SEND / US  A / MESSAGE", heavy white caps, the middle line letter-spaced to the width of the others) builds word by word behind the speaker's head as he walks toward the camera, and the brand logo ("Bellucci / PRODUCTION") fades in below it. Then the footage alone fades to black in ~0.27 s while the text and logo stay at full white. The black end card holds ~1.3 s; the music fades out underneath and the video ends.

## Intended effect
A clean, readable ending: the action and the brand are the last thing on screen, with no visual distraction.

## Defining characteristics
- CTA lockup + brand logo stacked in the centre. [Fixed]
- Builds over the last talking shot (behind the speaker when overlapping). [Rule]
- Footage fades to black under the text; text stays. [Fixed]
- Black hold ~1–1.5 s with the music fading out. [Rule]

## When to use
- Triggers: final CTA sentence ("send us a message", "DM us", "book a call").
- Avoid when: the video loops into its start on purpose or ends on a joke.

## Anatomy over time
- Start: CTA words on their spoken words (lockup rules as `text-key-phrase-stacked-lockup` ([SKILL.md](../text-key-phrase-stacked-lockup/SKILL.md))).
- Development: logo fades in under it (~0.3 s).
- Resolution: footage fade to black ~0.27 s, end card ~1.3 s, music fade ~1.1 s.

## Relationships
- Speech: CTA words synced; fade starts right after the last word.
- Music: fades out over the end card (momentary loudness −21 → −47 LUFS over ~1.4 s).
- Sound effects: none observed.

## Adaptation
- Brand: brand logo (white version), brand heaviest sans for the CTA; CTA text from the user.

## Key numbers
- Footage fade to black ~8 frames (observed; table in ANALYSIS.md).
- Layout at the end card: CTA y ≈ 0.33–0.46 H, ≈ 0.55 W wide; logo y ≈ 0.55–0.6 H (observed).

These describe the references. They are not quotas or required values.

## Success criteria
- The CTA and logo are the only things on screen at the end, readable for ≥ 1 s.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
