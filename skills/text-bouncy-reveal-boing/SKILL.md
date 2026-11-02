---
name: text-bouncy-reveal-boing
description: Letters pop one by one from tiny dots in a springy wave that overshoots and settles, with one loud falling 'boing' on the overshoot peak; letters shrink back in reverse, silent. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-11-01
  sources: [src-008]
---

# text-bouncy-reveal-boing

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

The reference is a text-animation preset demo (preset name shown: "Bouncy Reveal"); this skill records the motion and its sound as one unit.

## Observable behavior
Letters appear left to right, ~0.03 s apart, each growing from a tiny dot with a spring: it overshoots (the later letters rise above the baseline so the line forms a rising wave, about 5-10 degrees of tilt at its most extreme) and settles back to a straight line. The first letters arrive at ~9.22 s, the last ones at ~9.6 s, everything sits still by ~9.85 s. A single loud 'boing' (a sharp hit followed by a pitch that falls) lands around the overshoot peak, ~0.3 s after the first letter. The line holds ~1.8 s. It leaves in reverse: letters shrink back to dots in a wave from the right, ~0.5 s, silent.

Reference look, for context only [Observed]: very heavy geometric sans (Montserrat-ExtraBold-like), text filled with a left-to-right gradient from yellow (~#F8EC2B) through gold to orange (~#F89C1E) with a soft same-colour glow, one centred line (~63 % of the frame width, glyph height ~5 % of frame height) at ~50 % of the frame height on pure black. The motion does not depend on this look: typeface, colours and glow follow the selected brand (standing rule B7), not the reference palette.

## Intended effect
Playful, energetic reveal with weight; the bounce makes the text feel elastic.

## Defining characteristics
- Letter-level pop from tiny to full size with overshoot and settle (spring). [Fixed]
- A wave: later letters peak later and higher, so the line briefly curves upward. [Rule]
- One loud falling 'boing' timed to the overshoot peak, not to the first letter. [Fixed]
- Exit = reverse, shrink to dots, silent. [Rule]

## When to use
- Fun or energetic one/two-word titles, reveals and punchlines. Avoid for serious or calm content; the sound is the loudest of the set.
- The text of the reference (the preset's own name) is not part of the skill; the technique applies to any short line.

## Anatomy over time
- Start: first tiny dot ~9.22 s, letters visible from ~9.25 s.
- Development: each letter springs up; the wave peaks ~9.5-9.7 s.
- Resolution: straight and still by ~9.85 s; hold ~1.8 s.
- Exit: ~0.5 s, silent.

## Sound
- Type and character: A 'boing' / falling hit: very sharp attack (jump of ~55 dB within 5 ms) with two quick sub-hits at 9.585 and 9.635, then a tonal body (fundamental ~1.1 kHz, partials ~0.6, 1.6, 3.7 kHz) whose pitch falls to ~9.83 s. ~0.3 s total. The loudest sound in the set: sample peak -0.4 dBFS.
- Library file(s): `<SFX>\from-references\src-008_boing-falling-hit_01.wav` (extracted from the reference by the user's request, 2026-11-01; cut and normalised to -1 dBFS, 5 ms fades, nothing added). No search for similar library sounds was made: the user asked to use the reference's own sounds.
- Extracted from the reference: yes, same file as above; reference excerpt with picture in `references/audio/` and `references/clips/`.

## Sync rule
- Follows: Attack at 9.535 s, ~0.3 s after the first letter (9.22 s) and on the rise of the wave ('Reveal' at its highest, ~9.5-9.7 s).
- Repetition: Once per reveal.
- The exit has no sound. [Observed]

## Level
- The reference has no voice, so the level against speech is [Uncertain]. Within the whole set the peaks run from -0.4 dBFS (bouncy boing, loudest) to -12.5 dBFS (random shimmer, quietest); this technique's sample peak is stated under Sound. In a video, a starting point (not observed) is about 12 dB under the voice peaks and keep this technique's level relation to the other motions if several are used.

## Relationships
- Speech: the reference has none; when used on spoken text, start each word/letter reveal on its spoken onset and keep the sound with the visual.
- Sound and picture are one unit: use the motion without its sound only when the user asks.
- Other techniques: No close existing skill; sound is a 'boing', new type.

## Adaptation
- Adaptable: the text, its length (the stagger per word/letter stays about the same, the total follows the length), typeface, colour and glow (brand, rule B7), size and position.
- Timing scales with the line: keep the per-unit stagger from Key numbers.

## Key numbers
- First dot ~9.22 s, letters visible ~9.25 s, wave peak ~9.5-9.7 s, still by ~9.85 s. (observed; table in ANALYSIS.md)
- Letter spacing ~0.03 s; overshoot up to ~1.1x scale and ~5-10 degrees of line tilt (estimate [Uncertain]). (observed; table in ANALYSIS.md)
- Boing attack 9.535 s, ends ~9.83 s; sample peak -0.4 dBFS; fundamental ~1.1 kHz falling. (observed; table in ANALYSIS.md)
- Exit 11.70-12.20 s, silent. (observed; table in ANALYSIS.md)

## Success criteria
- The motion reads as described (unit, order, blur/bounce/flicker character), with the stagger close to the key numbers.
- The sound is heard once per unit exactly as the Sync rule says and matches the excerpt in `references/audio/`.
- The exit is silent and mirrors the entry.

## User notes
- [User] (2026-11-01) Register each text motion together with its sound as one skill; do not make a template from this video; extract only the text motions with sound shown in the middle of the video.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
