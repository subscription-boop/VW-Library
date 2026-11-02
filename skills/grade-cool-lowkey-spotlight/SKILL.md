---
name: grade-cool-lowkey-spotlight
description: Very low-key, cool look: near-black background and deep crushed blacks, a single hard top/side spotlight on the speaker with fast falloff, cool blue-navy shadows (b* about -3), neutral highlights, natural warm skin, muted saturation; red text glows are the only strong colour. Speaker footage only. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: grade
  status: approved
  approved: 2026-10-25
  sources: [src-006]
---

# grade-cool-lowkey-spotlight

> Library technique (category: `grade`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (observed measurements, distinction from a related technique, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Everything outside the speaker is almost black: the median of the frame is L* ≈ 4–5 and only ~5 % of pixels are brighter than L* ≈ 35–40. A **single hard light from above/side** lights the face, cap and shoulders; the light falls off quickly into black, and in the wide shot it forms a **pool of light** on the floor/table in an otherwise black studio. **Shadows lean blue/navy** (b* ≈ −3), mid-tones on clothes are blue-grey, highlights are neutral, **skin stays natural and warm** (L* ≈ 35, a* +16, b* +13). Saturation is muted; the only strong colour comes from red graphics. Blacks are crushed (1 % of pixels at L* ≈ 0) with no visible noise lift.

## Intended effect
Moody, exclusive, "night studio / high-end podcast" feel; the face floats out of the dark and red neon text pops.

## Defining characteristics
- Low-key: frame median L* ≈ 4–5, 95th percentile L* ≈ 32–41 [Observed]
- One hard top/side spot on the subject, fast falloff, black surround [Observed]
- Cool blue shadows (a* ≈ +1, b* ≈ −2.5…−3.5), neutral highlights [Observed]
- Natural warm skin (a* ≈ +16, b* ≈ +12…+14) [Observed]
- Muted saturation (mean HSV S ≈ 0.33–0.39) [Observed]
- Scope: apply only to footage of the speaker(s); never to graphics or text. [Rule, as for the user's other grades]

## When to use
- Triggers: podcast/interview clips, serious or premium statements, dark studio footage.
- Best fit: footage shot in a dark room with one hard key.
- Avoid when: bright daylight/white-wall footage (it cannot become this look; see the test frame) - and note the user's standing preference for his own footage: warm and bright, never grey or dark.

## Relationships
- Partners: `text-neon-serif-keyword`, `text-phrase-build-glow-pop` (glowing text needs dark footage).

## Adaptation
- **Mostly lighting, not grading:** dark room, one hard top/side key, black surroundings.
- On dark footage: deep black point, cool the shadows only (keep skin), lower saturation ~10–15 %, gentle vignette.
- On bright footage only a rough approximation is possible (heavy exposure drop + spotlight vignette): white walls turn grey. Show the user a test frame first.

## Key numbers
- Guest close-ups (27 frames) L* at 1/5/25/50/75/95/99 % = 0.8 / 0.8 / 3.1 / 4.3 / 7.8 / 41 / 62 (observed; table in ANALYSIS.md).
- Guest medium (31 frames) L* at 1/5/25/50/75/95/99 % = 0 / 0.4 / 2.7 / 4.7 / 7.1 / 32 / 48 (observed).
- Shadows (L* < 15): a* +0.8…+1.2, b* −2.4…−2.9 (observed).
- Skin: L* 34–41, a* +16…+18, b* +10…+14 (observed).
- How much of the look is lighting vs grade cannot be separated [Uncertain].

## Success criteria
- Face clearly the brightest thing, surroundings near black, shadows cool, skin natural.

## User notes
- [User] The dark look is mostly the real shooting environment (dark studio, one hard light), not a filter; do not force it onto bright footage.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
