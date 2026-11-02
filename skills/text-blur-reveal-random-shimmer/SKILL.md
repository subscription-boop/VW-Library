---
name: text-blur-reveal-random-shimmer
description: Letters of a line appear in random order, each out of a soft blur, while one high shimmer sweep plays; letters leave in random order blurring out, silent. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-11-01
  sources: [src-008]
---

# text-blur-reveal-random-shimmer

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

The reference is a text-animation preset demo (preset name shown: "Blur Reveal Random"); this skill records the motion and its sound as one unit.

## Observable behavior
Not left-to-right: letters come in at random positions, each as a soft dim orange blob that sharpens and brightens (e.g. 'ur', 'v', 'nd' first, then 'Bl', 'R', 'e', 'l' last). The first blobs show at ~17.17 s and the line is fully sharp ~0.45 s later (~17.6 s). One shimmer (a high, airy sweep with a light ringing, then a fading tail) plays across the whole reveal, starting with the first blob. The line holds ~1.5 s. It leaves the same way: random letters blur out (starts 19.13 s; the video ends at 19.47 s while the exit is still running, so the exit is only partly seen).

Reference look, for context only [Observed]: very heavy geometric sans (Montserrat-ExtraBold-like), text filled with a left-to-right gradient from yellow (~#F8EC2B) through gold to orange (~#F89C1E) with a soft same-colour glow, one centred line (~63 % of the frame width, glyph height ~5 % of frame height) at ~50 % of the frame height on pure black. The motion does not depend on this look: typeface, colours and glow follow the selected brand (standing rule B7), not the reference palette.

## Intended effect
A scattered, sparkling materialisation; feels like the text 'condenses' out of the air.

## Defining characteristics
- Letter-level, random order (no left-to-right order). [Fixed]
- Each letter: soft blob -> sharp, brightening. [Fixed]
- One shimmer sweep across the whole reveal, not per letter. [Fixed]
- Exit = random letters blur out. [Rule]

## When to use
- Magical / premium / dreamy reveals; end of a section. Avoid for fast, hard-hitting content.
- The text of the reference (the preset's own name) is not part of the skill; the technique applies to any short line.

## Anatomy over time
- Start: first blobs and the shimmer attack together (~17.14-17.17 s).
- Development: ~0.45 s of random letters sharpening.
- Resolution: sharp ~17.6 s; shimmer tail fades to ~17.85 s; hold ~1.5 s.
- Exit: random blur-out from 19.13 s (cut off by the end of the video).

## Sound
- Type and character: A shimmering sweep: sharp noisy attack (jump of ~66 dB within 5 ms) then a bright, airy body with light ringing (peaks near 5.0, 5.9, 8.9 and 11.1 kHz, noise up to ~18 kHz), ~0.45 s body, tail fading to ~17.85 s. The quietest sound in the set: sample peak -12.5 dBFS.
- Library file(s): `<SFX>\from-references\src-008_shimmer-sweep-high_01.wav` (extracted from the reference by the user's request, 2026-11-01; cut and normalised to -1 dBFS, 5 ms fades, nothing added). No search for similar library sounds was made: the user asked to use the reference's own sounds.
- Extracted from the reference: yes, same file as above; reference excerpt with picture in `references/audio/` and `references/clips/`.

## Sync rule
- Follows: Attack at 17.135 s, on (within 1 frame of) the first blob (17.17 s); the body covers the whole reveal.
- Repetition: Once per reveal.
- The exit has no sound. [Observed]

## Level
- The reference has no voice, so the level against speech is [Uncertain]. Within the whole set the peaks run from -0.4 dBFS (bouncy boing, loudest) to -12.5 dBFS (random shimmer, quietest); this technique's sample peak is stated under Sound. In a video, a starting point (not observed) is about 12 dB under the voice peaks and keep this technique's level relation to the other motions if several are used.

## Relationships
- Speech: the reference has none; when used on spoken text, start each word/letter reveal on its spoken onset and keep the sound with the visual.
- Sound and picture are one unit: use the motion without its sound only when the user asks.
- Other techniques: Compare in the library: `sfx-shimmer-tone` (steady bright tones) - this one is a noisy sweep, not steady tones; library match not checked (see ANALYSIS.md).

## Adaptation
- Adaptable: the text, its length (the stagger per word/letter stays about the same, the total follows the length), typeface, colour and glow (brand, rule B7), size and position.
- Timing scales with the line: keep the per-unit stagger from Key numbers.

## Key numbers
- First blobs ~17.17 s; all sharp ~17.6 s (~0.45 s). (observed; table in ANALYSIS.md)
- Shimmer attack 17.135 s, body to ~17.58 s, tail to ~17.85 s; sample peak -12.5 dBFS. (observed; table in ANALYSIS.md)
- Exit starts 19.13 s (random letters), unfinished at the video end (19.47 s). (observed; table in ANALYSIS.md)

## Success criteria
- The motion reads as described (unit, order, blur/bounce/flicker character), with the stagger close to the key numbers.
- The sound is heard once per unit exactly as the Sync rule says and matches the excerpt in `references/audio/`.
- The exit is silent and mirrors the entry.

## User notes
- [User] (2026-11-01) Register each text motion together with its sound as one skill; do not make a template from this video; extract only the text motions with sound shown in the middle of the video.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
