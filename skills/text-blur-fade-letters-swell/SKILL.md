---
name: text-blur-fade-letters-swell
description: A word or line builds letter by letter, each letter growing out of a soft blurred dot into a sharp glyph, under one soft noise swell; letters leave in reverse as they blur and shrink, silent. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-11-01
  sources: [src-008]
---

# text-blur-fade-letters-swell

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

The reference is a text-animation preset demo (preset name shown: "Blur Fade"); this skill records the motion and its sound as one unit.

## Observable behavior
From a soft blurred dot at the left of the line, letters appear one after another left to right, ~0.07 s apart. Each letter starts as a tiny blurred, dim, orange-tinted blob and in ~0.2 s grows to full size, loses the blur and brightens to the final colour. The whole line is sharp ~0.7 s after the first dot. One noise swell (soft airy whoosh) plays across the second half of the build. The line holds. It leaves in reverse: the last letter blurs, darkens, shrinks to a dot and disappears first, then the previous ones, over ~0.8 s; the exit is silent.

Reference look, for context only [Observed]: very heavy geometric sans (Montserrat-ExtraBold-like), text filled with a left-to-right gradient from yellow (~#F8EC2B) through gold to orange (~#F89C1E) with a soft same-colour glow, one centred line (~63 % of the frame width, glyph height ~5 % of frame height) at ~50 % of the frame height on pure black. The motion does not depend on this look: typeface, colours and glow follow the selected brand (standing rule B7), not the reference palette.

## Intended effect
A soft focus-pull feel; text materialises like a camera finding focus.

## Defining characteristics
- Letter-level build left to right (not words). [Fixed]
- Each letter: blurred dot -> sharp glyph, growing and brightening together. [Fixed]
- One noise swell for the whole build, not a sound per letter. [Fixed]
- Exit = reverse letter order, blur + shrink to dot, silent, slower than the entry. [Rule]

## When to use
- One-word or two-word titles; a calm 'focus in' reveal. Avoid when the line is long (letter stagger makes it slow).
- The text of the reference (the preset's own name) is not part of the skill; the technique applies to any short line.

## Anatomy over time
- Start: a blurred dot appears at the left (~0.25 s before the swell).
- Development: letters grow in ~0.07 s apart; swell runs from the 'Bl' letters to the last letter sharpening.
- Resolution: all letters sharp ~0.7 s after the first dot; hold ~1.7 s.
- Exit: ~0.8 s reverse blur-out, silent.

## Sound
- Type and character: One soft noise swell / airy swish, ~0.33 s above -50 dBFS, broadband (median energy ~3.4 kHz, 95 % below ~9.9 kHz), made of a few rising bursts; no pitched tone. Sample peak -3.6 dBFS.
- Library file(s): `<SFX>\from-references\src-008_swell-noise-soft_01.wav` (extracted from the reference by the user's request, 2026-11-01; cut and normalised to -1 dBFS, 5 ms fades, nothing added). No search for similar library sounds was made: the user asked to use the reference's own sounds.
- Extracted from the reference: yes, same file as above; reference excerpt with picture in `references/audio/` and `references/clips/`.

## Sync rule
- Follows: Starts at 6.065 s, ~0.25 s after the first dot (5.82 s), when the first letters are readable, and ends at 6.40 s as the last letters sharpen.
- Repetition: Once per build.
- The exit has no sound. [Observed]

## Level
- The reference has no voice, so the level against speech is [Uncertain]. Within the whole set the peaks run from -0.4 dBFS (bouncy boing, loudest) to -12.5 dBFS (random shimmer, quietest); this technique's sample peak is stated under Sound. In a video, a starting point (not observed) is about 12 dB under the voice peaks and keep this technique's level relation to the other motions if several are used.

## Relationships
- Speech: the reference has none; when used on spoken text, start each word/letter reveal on its spoken onset and keep the sound with the visual.
- Sound and picture are one unit: use the motion without its sound only when the user asks.
- Other techniques: Compare in the library: `sfx-whoosh-main-start`, `sfx-whoosh-swell-scene-in` (soft airy swells) - the reference swell is a short noise swell; library match was not checked (see ANALYSIS.md).

## Adaptation
- Adaptable: the text, its length (the stagger per word/letter stays about the same, the total follows the length), typeface, colour and glow (brand, rule B7), size and position.
- Timing scales with the line: keep the per-unit stagger from Key numbers.

## Key numbers
- First dot 5.82 s; letters ~5.94-6.50 s, ~0.07 s apart; all sharp by ~6.55 s. (observed; table in ANALYSIS.md)
- Each letter grows ~0.2 s (dot -> full size, blur -> sharp). (observed; table in ANALYSIS.md)
- Swell 6.065-6.40 s, peak -3.6 dBFS, centroid ~3.5 kHz. (observed; table in ANALYSIS.md)
- Exit 8.30-9.10 s, reverse letters, silent. (observed; table in ANALYSIS.md)

## Success criteria
- The motion reads as described (unit, order, blur/bounce/flicker character), with the stagger close to the key numbers.
- The sound is heard once per unit exactly as the Sync rule says and matches the excerpt in `references/audio/`.
- The exit is silent and mirrors the entry.

## User notes
- [User] (2026-11-01) Register each text motion together with its sound as one skill; do not make a template from this video; extract only the text motions with sound shown in the middle of the video.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
