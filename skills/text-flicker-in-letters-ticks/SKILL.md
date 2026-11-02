---
name: text-flicker-in-letters-ticks
description: Letters of a short line switch on and off at random, frame by frame, for ~0.4 s before locking solid, with a rapid burst of bright electrical ticks; the exit flickers off, silent. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-11-01
  sources: [src-008]
---

# text-flicker-in-letters-ticks

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

The reference is a text-animation preset demo (preset name shown: "Flicker in"); this skill records the motion and its sound as one unit.

## Observable behavior
No blur and no move: individual letters pop on and off at random from one frame to the next (a letter can appear, vanish and appear again; the slightly orange tint is on the flickering letters). It starts with a single letter on (~14.95 s), more letters switch on in a scattered pattern, and the whole line is solid by ~15.35 s (~0.4 s, ~12 frames at 30 fps). A burst of six short bright ticks (about 0.06 s apart, i.e. every ~2 frames) plays over the second half of the flicker. The line holds ~1.6 s. It leaves with the same flicker in reverse (~0.2 s: letters drop out at random until none remain); silent.

Reference look, for context only [Observed]: very heavy geometric sans (Montserrat-ExtraBold-like), text filled with a left-to-right gradient from yellow (~#F8EC2B) through gold to orange (~#F89C1E) with a soft same-colour glow, one centred line (~63 % of the frame width, glyph height ~5 % of frame height) at ~50 % of the frame height on pure black. The motion does not depend on this look: typeface, colours and glow follow the selected brand (standing rule B7), not the reference palette.

## Intended effect
Neon-sign / electrical glitch energy; the text 'catches' on.

## Defining characteristics
- Letter-level random on/off flicker, frame-stepped, no blur or movement. [Fixed]
- ~0.4 s from first letter to solid. [Rule]
- A rapid burst of ~6 short bright ticks about every 2 frames, over the flicker's second half. [Fixed]
- Exit = shorter flicker off (~0.2 s), silent. [Rule]

## When to use
- Techy / neon / glitch titles, a single short line. Avoid on calm, soft content.
- The text of the reference (the preset's own name) is not part of the skill; the technique applies to any short line.

## Anatomy over time
- Start: one letter lit.
- Development: random letters on/off every frame; ticks start ~0.1 s after the first letter.
- Resolution: solid by ~15.35 s; ticks end ~15.41 s.
- Exit: ~0.2 s random drop-out, silent.

## Sound
- Type and character: Short bright electrical ticks, each a few ms, energy ~7.5-9.8 kHz (centroid ~9.3 kHz), about 0.06 s apart; sample peak -9.3 dBFS (quiet compared with the set).
- Library file(s): `<SFX>\from-references\src-008_ticks-burst-electric_01.wav` (extracted from the reference by the user's request, 2026-11-01; cut and normalised to -1 dBFS, 5 ms fades, nothing added). No search for similar library sounds was made: the user asked to use the reference's own sounds.
- Extracted from the reference: yes, same file as above; reference excerpt with picture in `references/audio/` and `references/clips/`.

## Sync rule
- Follows: Six ticks at 15.075, 15.145, 15.200, 15.260, 15.320 and 15.380 s. The first letter is on at ~14.95 s, so the burst begins ~0.12 s into the flicker and ends as the line locks (~15.35 s).
- Repetition: Once per flicker (a burst).
- The exit has no sound. [Observed]

## Level
- The reference has no voice, so the level against speech is [Uncertain]. Within the whole set the peaks run from -0.4 dBFS (bouncy boing, loudest) to -12.5 dBFS (random shimmer, quietest); this technique's sample peak is stated under Sound. In a video, a starting point (not observed) is about 12 dB under the voice peaks and keep this technique's level relation to the other motions if several are used.

## Relationships
- Speech: the reference has none; when used on spoken text, start each word/letter reveal on its spoken onset and keep the sound with the visual.
- Sound and picture are one unit: use the motion without its sound only when the user asks.
- Other techniques: Possible overlap with `text-flicker-in` (key word enters with an irregular flicker, ~7 frames, then holds): that one is a single key word, on/off of the whole word, no sound; this one flickers letter by letter for ~0.4 s with a tick burst (registered as a separate skill, user decision 2026-11-01).

## Adaptation
- Adaptable: the text, its length (the stagger per word/letter stays about the same, the total follows the length), typeface, colour and glow (brand, rule B7), size and position.
- Timing scales with the line: keep the per-unit stagger from Key numbers.

## Key numbers
- First letter ~14.95 s; solid ~15.35 s (~12 frames @ 30 fps). (observed; table in ANALYSIS.md)
- Ticks at 15.075 / 15.145 / 15.200 / 15.260 / 15.320 / 15.380 s (~0.06 s apart); centroid ~9.3 kHz; sample peak -9.3 dBFS. (observed; table in ANALYSIS.md)
- Exit 16.93-17.12 s (~0.2 s), silent. (observed; table in ANALYSIS.md)

## Success criteria
- The motion reads as described (unit, order, blur/bounce/flicker character), with the stagger close to the key numbers.
- The sound is heard once per unit exactly as the Sync rule says and matches the excerpt in `references/audio/`.
- The exit is silent and mirrors the entry.

## User notes
- [User] (2026-11-01) Register each text motion together with its sound as one skill; do not make a template from this video; extract only the text motions with sound shown in the middle of the video.
- [User] (2026-11-01) Approved as a separate skill from `text-flicker-in` ("add all"); the overlap recommendation was to keep them separate.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
