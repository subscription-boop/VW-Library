---
name: zoom-push-hold-release
description: On a static medium or wide talking shot the whole frame (captions and graphics included) pushes in smoothly by ~1.15–1.6x on a key phrase, holds there for the phrase, then glides back out to the normal framing. Fits long single takes that need life without cutting. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: zoom
  status: approved
  approved: 2026-10-28
  sources: [src-007]
---

# zoom-push-hold-release

> Library technique (category: `zoom`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
The speaker stands in one long, static wide shot. When he starts a key phrase, the picture glides in toward his chest/upper body: slow start, quick middle, soft landing (an S-curve), done in ~0.4–0.55 s. The tighter framing then **holds** for the whole phrase (~0.7–1.7 s). When the phrase is over, the picture glides back out to the original framing with the same S-shaped motion in ~0.5–0.7 s. Everything on screen is inside the zoom: the single-word captions and graphics (logo cards, lockups) grow and shrink with the picture. No overshoot, no shake, no motion blur. The move is digital (the background scales with the speaker).

A stepped variant appears on a medium shot: two short pushes in a row on two consecutive key words ("NEXT" → "LEVEL"), each ~0.2–0.25 s, held tight until the cut (no release).

## Intended effect
Keeps a long single take alive and tells the viewer "this phrase matters" without a cut. The release back out marks the end of the emphasis, so the next sentence starts calm again. On a wide shot the push makes the speaker readable for the important line.

## Defining characteristics
- Smooth S-curve in (slow-fast-slow), no overshoot. [Fixed]
- Holds tight for the phrase, then releases back to the same base framing (push → hold → release). [Fixed]
- Captions and graphics scale with the picture (the zoom is applied to the whole composite). [Rule]
- Zoom centre ≈ speaker's chest / upper body, so the face rises toward the upper-middle of the frame. [Rule]
- Strength follows shot size: wide shots ~1.35–1.6x, medium shots ~1.1–1.2x. [Rule]
- Stepped variant: one push per key word, held to the next cut. [Observed]

## When to use
- Triggers: the key phrase of a sentence (named examples, the strongest claim, a question to the viewer, "that's so important"), a lockup title appearing, a list of logos/examples.
- Good fit: long static takes (5–20 s) of a standing or seated speaker, especially wide shots where the face is small.
- Avoid when: the shot is already tight on the face (no room), the camera is moving a lot (walk-and-talk), or two pushes would land less than ~1 s apart.

## Anatomy over time
- Start: ~0–2 frames before or on the first word of the phrase.
- Development: S-curve, steepest in the middle; ~0.4–0.55 s for 1.35–1.6x.
- Resolution: hold for the phrase; release S-curve ~0.5–0.7 s starting right after the phrase (often under the first words of the next sentence).
- Repetition: in the 20 s dock take: 5 push/release pairs, ~2–10 s apart; never overlapping.

## Relationships
- Subject: the speaker's torso stays centred; nothing important is pushed into the red zones (B6).
- Speech: in on the phrase start, release after the phrase end.
- Cuts: used inside a single take; the stepped variant ends on a cut.
- Music and beats: not tied to the beat in the reference.
- Sound effects: none observed (no whoosh on the zoom).
- Other techniques: pairs with `text-key-phrase-stacked-lockup` ([SKILL.md](../text-key-phrase-stacked-lockup/SKILL.md)) and `graphic-logo-card-stack-peel` ([SKILL.md](../graphic-logo-card-stack-peel/SKILL.md)); the graphics live inside the zoom.

## Adaptation
- Adaptable: strength (by shot size), hold length (by phrase length), centre point (by where the speaker is).
- Scaling: needs enough source resolution; on 1080x1920 output from a 4K/1080 source keep ≤ ~1.6x so the picture stays sharp.
- Brand: no brand properties.

## Key numbers
- Logos push ("Adidas"): ×1.52 in ~0.53 s, hold ~0.75 s, release back to base (×0.60) in ~0.67 s, S-curve (observed; table in ANALYSIS.md).
- "marketing": push ×1.32 in ~0.35 s, release back in ~0.35 s (observed).
- "PEOPLE BUY THE FEELING": push ×1.14 in ~0.3 s, hold ~0.95 s (observed).
- "important… want everyone else": push ×1.50 in ~0.55 s, hold ~1.6 s, release ~0.6 s (observed).
- Seated medium ("authentic content"): push ×1.15 in ~0.2 s, back ×0.86 (observed).
- Stepped variant ("NEXT", "LEVEL"): ×1.12 then ×1.17 (≈1.27 total), held to the cut (observed).
- Landing tight after a white-flash cut, then releasing: ~1.6x → base in ~0.5 s (observed).

## Success criteria
- Push, hold and release are clearly three phases; no bounce or overshoot.
- The pushed framing matches the phrase it emphasises; it releases when the phrase ends.
- Captions/graphics move with the picture and never leave the safe area.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Curve shape (in / hold / out): the two `sequences/` and the `push-hold-release-*` clips.
- Stepped variant: `clips/..._stepped-double-push.mp4`.
