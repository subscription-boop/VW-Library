---
name: graphic-phone-mockup-feed
description: A realistic phone mock-up on the cream canvas shows the app being talked about scrolling through its feed; it then cuts to an extreme close-up of the phone edge, or shows competitor videos with a view counter that counts up fast. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-25
  sources: [src-005]
---

# graphic-phone-mockup-feed

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
On a cream gridded canvas (no speaker card), a **realistic black phone mock-up** with a soft shadow shows the actual app/screen, **scrolling continuously** through a feed of videos. The scene then **hard cuts to an extreme close-up**: the phone is huge, cropped at the frame edge, and one UI element is annotated. In a proof variant, the phone (cropped at the top of the frame) plays a competitor's video, its **view counter** in the corner **counts up quickly** (dozens to tens of thousands within ~2 s), and the video switches to another competitor's every ~1 s.

## Intended effect
Shows proof instead of claiming it: the real product in use, real numbers rising.

## Defining characteristics
- Realistic phone frame with the real screen content, on the light canvas [Fixed]
- The screen is alive: scrolling feed or playing videos [Rule]
- Close-up variant: hard cut to a cropped, much larger phone view plus an annotation [Rule]
- Counter variant: numbers climb fast, roughly every frame [Observed]

## When to use
- Triggers: naming an app/tool and what it shows; "your competitors already had success" (proof numbers).
- Avoid when: no real screen recording is available - never fake the app or the numbers.

## Anatomy over time
- Start: hard cut to the scene; phone already in place.
- Development: feed scrolls / counter counts while the mixed headline builds.
- Resolution: hard cut back to the speaker.

## Relationships
- Text: `text-serif-sans-mixed-line` beside or above the phone.
- Annotation: `graphic-hand-drawn-annotation` (ellipse on the close-up, connector line to the text).
- Sound effects: the scene entry carries `sfx-whoosh-swell-scene-in`; a click accent appears inside the counter scene (`sfx-click-graphic-hit`).

## Adaptation
- Use the user's real screen recordings and real figures only.
- Canvas: brand light neutral; phone shadow soft.

## Key numbers
- Phone feed scene ≈ 2.0 s, then cut to the close-up (≈ 1.8 s) (observed; table in ANALYSIS.md).
- Counter at 00:50.530–00:51.000: 37 → 120 → 247 → 418 → … rising every frame (observed).

## Success criteria
- The screen content is real and legible enough to recognise; the counter is clearly rising.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
