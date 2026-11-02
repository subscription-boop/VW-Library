---
name: grade-cinematic-warm-highlights
description: Cinematic colour grade - a mild orange-and-teal split: warm (about +800 K) with golden highlights and slightly cool, blue-green shadows, contrast up (S-curve), +5 % saturation. Fits: dramatic, premium or cinematic talking heads and short films. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: grade
  status: approved
  approved: 2026-10-24
  sources: []
  origin: user-approved grade option "J Cinematic" from the grade options sheet of project 2026-10-24-5-ai-apps-use-this, not from a reference video
---

# grade-cinematic-warm-highlights

> Library technique (category: `grade`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (test-frame measurements, registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
The speaker's footage gets the "Cinematic" look: a mild orange-and-teal split: warm (about +800 K) with golden highlights and slightly cool, blue-green shadows, contrast up (S-curve), +5 % saturation; a cinematic, filmic separation between skin and darks.

## Intended effect
Sets the mood of the whole video through colour alone, consistently on every shot of the speaker.

## Defining characteristics
- Highlights and skin warm/golden, shadows slightly cool teal [Fixed]
- Higher contrast than the source [Rule]
- The split stays mild: no obvious teal on skin [Rule]
- Same grade on every speaker shot of the video, so cuts between takes do not jump in colour [Rule]
- Applied to the speaker's footage only; B-roll, cards, graphics and text keep their own colours [User]

## When to use
- Good fit: dramatic, premium or cinematic talking heads and short films.
- Avoid when: bright white rooms with very few shadows (the effect barely shows) or when the user wants no cool tones.
- Choose by look: when unsure, show the user `references/before-after.jpg` of a few grade skills on a frame of their own footage and let them pick.

## Anatomy over time
- Static look over the whole video; no animated changes.
- Fix camera problems first (for example an auto-exposure ramp at the start of a take), then grade, so every shot starts from the same exposure.

## Relationships
- Other techniques: one `grade-` technique per video. Text and graphics are composited on top of the graded footage and are not graded.
- Sound effects: none.

## Adaptation
- Adaptable: strength may be scaled down for footage that is already close to the look (for example already warm or already bright); keep the direction of every change.
- Scaling: independent of resolution and aspect ratio.
- Brand: the grade does not use brand colours; brand colours appear only in graphics on top.
- Check skin and the brightest areas after grading: skin must not turn orange, red or grey, highlights must not clip.

## Key numbers
- Test frame values (white office wall, daylight; observed; table in ANALYSIS.md): wall RGB (203, 210, 205) → (226, 224, 204); skin (cheek) RGB (163, 108, 95) → (177, 109, 87); mean frame level 162 → 169 (of 255).

These describe the user's test frame (white office wall, daylight). They are not required values.

## Success criteria
- Side by side with `references/before-after.jpg`, the result reads as the same look.
- Skin looks natural for the look; no clipped highlights or crushed shadows that the source did not have.
- Every speaker shot in the video matches.

## User notes
- [User] Grade only the speaker's footage, never B-roll, cards or graphics (standing rule).

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- What the look should be: `references/before-after.jpg`.
- One exact way to reproduce it: `references/grade.py` (function `grade(rgb)`).
