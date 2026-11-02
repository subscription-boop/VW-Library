---
name: grade-warm-lowkey-practicals
description: Warm low-key talking-head look - near-black background with warm practical bulbs, soft bright key on the face, deep blacks, soft highlight roll-off, warm neutrals, slightly muted saturation. Applied to the speaker's own footage only. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: grade
  status: approved
  approved: 2026-10-22
  updated: 2026-10-22 (scope limited to the speaker's footage at the user's request)
  sources: [src-002]
---

# grade-warm-lowkey-practicals

> Library technique (category: `grade`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (observed measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
The speaker sits in a dark room. The background (shelves, wall) is almost black, broken only by a few warm tungsten-looking bulbs that glow yellow-amber and fall into soft bokeh. The face and the light-grey hoodie are lit by a large, soft, frontal key, so the subject reads bright against the dark. The whole image is warm: greys lean slightly yellow-red, skin is peachy, shadows are brown-black, never teal. Blacks are deep, but highlights roll off softly (nothing on the person clips). Saturation is moderate, a little muted. B-roll is even darker (low-key, centre-lit, heavy falloff to black), the "thinking" shots warm, the gym shot more neutral.

## Intended effect
Premium, intimate, "late-night studio" mood: the eye goes straight to the face, and the warm bulbs make it feel cozy and cinematic.

## Defining characteristics
- Low-key: background near black (L* ≈ 3–5), subject 35–45 L* brighter than it. [Observed]
- Warm practicals in the background (yellow-amber, soft bokeh). [Observed]
- Soft, frontal, wrap-around key on the face; no hard shadows. [Observed]
- Warm white balance: neutral greys sit at about a* +3…+4, b* +3…+4; highlights lean yellow (b* ≈ +9). [Observed]
- Shadows warm brown (a* ≈ +5, b* ≈ +4), no teal/orange split. [Observed]
- Deep blacks (1 % of pixels at L* ≈ 0), soft shoulder: most highlights stop around L* 80, only the bulbs go higher. [Observed]
- Saturation moderate (mean HSV S ≈ 0.34 on the talking head). [Observed]
- B-roll darker than the talking head (median L* ≈ 10 vs ≈ 40), with natural centre-to-edge falloff. [Observed] (observation only; see the scope rule below)
- Scope: apply only to footage of the speaker. Never to B-roll, stock clips, inset cards, motion graphics, white cards, captions or labels. [User]

## When to use
- Triggers: talking heads and B-roll that should feel premium, calm, cinematic, "night studio".
- Best fit: footage shot in a dim room with a soft key and a few warm lamps behind the speaker.
- Avoid when: the footage is bright/daylit with a white background and the user wants it to stay natural; brand looks that require bright, clean, high-key images.

## Relationships
- Typical partner of `template-n-steps-normal-speed-full-cards-broll` (same source).
- Captions, white cards, inset cards, motion graphics and B-roll are not graded. [User]

## Adaptation
- **Best result comes from the shoot, not the grade:** dark room, soft key in front, 2–4 warm bulbs or lamps (≈2700 K) behind, shallow depth of field.
- On already-dark footage: warm the white balance, set a deep black point, add a soft highlight shoulder, lower saturation slightly, keep skin natural (hue ≈ 44°, chroma ≈ 20 in a*/b*).
- On bright/white-background footage the look can only be approximated: lower exposure, darken the background with a large soft vignette centred on the face, warm the balance, deep blacks, soft shoulder. A white wall will turn grey, not black, and there are no warm bulbs; say this to the user before applying. See the test frame in references.
- Do not grade B-roll or motion graphics with this look. [User] If a B-roll clip clashes badly with the graded speaker shots, tell the user and ask before touching it.
- Keep the speaker's skin consistent across takes.

## Key numbers
- Talking head (59 frames) L* at 1/5/25/50/75/95/99 % = 0.4 / 1.5 / 8 / 40 / 65 / 80 / 91 (observed; table in ANALYSIS.md).
- Mean a*, b* of the whole frame +5.2, +7.1; background beside the head L* ≈ 3.5 (observed).
- Skin (44 faces, measured on 360 px frames): L* 42, a* +15, b* +14 (hue ≈ 44°); grey hoodie L* 46, a* +3.6, b* +3.3 (observed).
- Shadows (L* < 25) a/b +5.0/+3.7; highlights (L* > 70) a/b +0.5/+8.9; bulbs very bright, a* −4, b* +26 (yellow) (observed).
- B-roll (33 frames): L* median ≈ 10, 95 % ≈ 40; centre ≈ 12 L* brighter than the edges (observed).
- How much of the look is lighting vs grade cannot be separated from the finished video [Uncertain].

## Success criteria
- The face is the brightest, warmest focus; the background falls to near black.
- Greys look slightly warm, skin natural, no teal shadows, no clipped skin.
- Talking head and B-roll feel like one mood.

## User notes
- [User] Apply only to the footage of the person in the video, not to B-roll or motion graphics. (این اسکیل فقط باید رو ویدیوهای فوتیج شخص داخل ویدیو اعمال شه نه روی بی‌رول‌ها و موشن‌ها)
- [User] Learn only the light shape, colour and temperature of the creator's own footage. (فقط فرم نور و رنگ و دما رو یادبگیر)

## References
Index: [references/REFERENCES.md](references/REFERENCES.md): look frames, tone swatches + histogram, a test on the user's own footage.
