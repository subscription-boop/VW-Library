---
name: text-slide-left-words-click
description: A line builds one word at a time: each new word fades in over the end of the previous one and slides right into its place, with a very short bright tick on every word; words leave in reverse, sliding back left, silent. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-11-01
  sources: [src-008]
---

# text-slide-left-words-click

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

The reference is a text-animation preset demo (preset name shown: "Slide Left Words"); this skill records the motion and its sound as one unit.

## Observable behavior
The first word fades in sliding ~40 px from the left into place. Each next word starts about where the previous word ends (for a moment the two touch, e.g. 'SlideLeft'), fades in from dark and slides right ~40 px (about one word gap) into its own place with an ease-out over ~0.25 s. Words follow ~0.17 s apart. Each word's arrival has one very short, bright tick. The finished line holds. It leaves in reverse order: the last word slides back left over the previous one while it fades (~0.1 s each, ~0.16 s apart); the exit is silent.

Reference look, for context only [Observed]: very heavy geometric sans (Montserrat-ExtraBold-like), text filled with a left-to-right gradient from yellow (~#F8EC2B) through gold to orange (~#F89C1E) with a soft same-colour glow, one centred line (~63 % of the frame width, glyph height ~5 % of frame height) at ~50 % of the frame height on pure black. The motion does not depend on this look: typeface, colours and glow follow the selected brand (standing rule B7), not the reference palette.

## Intended effect
A quicker, tighter word build than slide-up; the line seems to unfold from the left, good for short punchy titles.

## Defining characteristics
- Word-level build left to right; each word enters moving rightward from the end of the previous word. [Fixed]
- No blur, no vertical move. [Fixed]
- One very short bright tick on each word's first frame. [Fixed]
- Words follow ~0.15-0.2 s apart (faster than slide-up). [Rule]
- Exit = reverse order, slide back left + fade, silent. [Rule]

## When to use
- Short punchy titles of 2-4 words. Avoid on long lines.
- The text of the reference (the preset's own name) is not part of the skill; the technique applies to any short line.

## Anatomy over time
- Start: first word slides in with its tick.
- Development: next word every ~0.17 s, each slide ~0.25 s ease-out, so slides overlap.
- Resolution: line settles slightly wider than the build (words finish spacing out) and holds ~1.7 s in the reference.
- Exit: reverse order, ~0.1 s each, silent.

## Sound
- Type and character: Very short bright tick, ~30 ms, energy concentrated near 8.7-9.1 kHz (centroid ~8.0-8.5 kHz); same sample each time; sample peak -0.9 to -2.6 dBFS. Higher and shorter than the slide-up tick.
- Library file(s): `<SFX>\from-references\src-008_tick-bright-word_01.wav` (extracted from the reference by the user's request, 2026-11-01; cut and normalised to -1 dBFS, 5 ms fades, nothing added). No search for similar library sounds was made: the user asked to use the reference's own sounds.
- Extracted from the reference: yes, same file as above; reference excerpt with picture in `references/audio/` and `references/clips/`.

## Sync rule
- Follows: Attack at 2.905, 3.075 and 3.240 s, on each word's first visible frame (0-1 frame).
- Repetition: Per word; same sample every time.
- The exit has no sound. [Observed]

## Level
- The reference has no voice, so the level against speech is [Uncertain]. Within the whole set the peaks run from -0.4 dBFS (bouncy boing, loudest) to -12.5 dBFS (random shimmer, quietest); this technique's sample peak is stated under Sound. In a video, a starting point (not observed) is about 12 dB under the voice peaks and keep this technique's level relation to the other motions if several are used.

## Relationships
- Speech: the reference has none; when used on spoken text, start each word/letter reveal on its spoken onset and keep the sound with the visual.
- Sound and picture are one unit: use the motion without its sound only when the user asks.
- Other techniques: Related but different from `text-slide-up-words-click` (vertical rise, duller tick, slower spacing).

## Adaptation
- Adaptable: the text, its length (the stagger per word/letter stays about the same, the total follows the length), typeface, colour and glow (brand, rule B7), size and position.
- Timing scales with the line: keep the per-unit stagger from Key numbers.

## Key numbers
- Word starts ~2.90 / 3.07 / 3.23 s (spacing ~0.17 s). (observed; table in ANALYSIS.md)
- Slide ~40 px (about one word gap) rightward, ~0.25 s ease-out. (observed; table in ANALYSIS.md)
- Tick attacks 2.905 / 3.075 / 3.240 s; ~30 ms each; centroid ~8.0-8.5 kHz; sample peak -0.9 to -2.6 dBFS. (observed; table in ANALYSIS.md)
- Exit: 'Words' ~5.30-5.42 s, 'Left' ~5.46-5.60 s, 'Slide' ~5.62-5.74 s; silent. (observed; table in ANALYSIS.md)

## Success criteria
- The motion reads as described (unit, order, blur/bounce/flicker character), with the stagger close to the key numbers.
- The sound is heard once per unit exactly as the Sync rule says and matches the excerpt in `references/audio/`.
- The exit is silent and mirrors the entry.

## User notes
- [User] (2026-11-01) Register each text motion together with its sound as one skill; do not make a template from this video; extract only the text motions with sound shown in the middle of the video.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
