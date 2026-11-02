---
name: text-slide-up-words-click
description: A line builds one word at a time: each word fades in from dark while rising a few percent of the frame height, with a short dry tick on every word; words leave in reverse order dropping and fading, silent. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-11-01
  sources: [src-008]
---

# text-slide-up-words-click

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

The reference is a text-animation preset demo (preset name shown: "Slide Up Words"); this skill records the motion and its sound as one unit.

## Observable behavior
The line is built word by word. Each word starts dark and a little below its final place, fades up to full brightness while rising ~40-50 px (at 720 px width, ~3.5 % of frame height) into place in ~0.2 s with a soft ease-out. Words follow ~0.25 s apart, left to right. On every word's first visible frames a single short dry tick is heard (the same tick each time). The finished line holds still. It leaves in reverse order: the last word drops ~40 px and fades (~0.2 s), then the one before it, ~0.2 s apart; the exit is silent.

Reference look, for context only [Observed]: very heavy geometric sans (Montserrat-ExtraBold-like), text filled with a left-to-right gradient from yellow (~#F8EC2B) through gold to orange (~#F89C1E) with a soft same-colour glow, one centred line (~63 % of the frame width, glyph height ~5 % of frame height) at ~50 % of the frame height on pure black. The motion does not depend on this look: typeface, colours and glow follow the selected brand (standing rule B7), not the reference palette.

## Intended effect
A soft, readable build for a title or a short statement where each word should land as its own beat without bounce or blur.

## Defining characteristics
- Word-level build (not letters, not the whole line at once). [Fixed]
- Each word rises from below while it fades in; no horizontal move, no blur. [Fixed]
- One short tick per word, on the word's first visible frames; same tick sample every time. [Fixed]
- Exit = reverse word order, drop + fade, silent. [Rule]

## When to use
- Title or promise lines of 2-4 words; words that should arrive in spoken order. Avoid on long sentences (a tick per word becomes noise above ~4 words per second).
- The text of the reference (the preset's own name) is not part of the skill; the technique applies to any short line.

## Anatomy over time
- Start: first word visible at once with its tick (frame of first appearance).
- Development: next word every ~0.25 s; each rise ~0.2 s ease-out.
- Resolution: line holds fully readable (about 1.2 s in the reference after the last word settles).
- Exit: words leave last-to-first, ~0.2 s apart, no sound.

## Sound
- Type and character: Dry, very short tick, ~35-45 ms, clean (no tail), energy mostly 1.2-3.3 kHz (centroid ~2.3 kHz, nothing sustained above ~13 kHz). All three ticks are the same sample. Sample peak -2.7 dBFS.
- Library file(s): `<SFX>\from-references\src-008_tick-dry-word_01.wav` (extracted from the reference by the user's request, 2026-11-01; cut and normalised to -1 dBFS, 5 ms fades, nothing added). No search for similar library sounds was made: the user asked to use the reference's own sounds.
- Extracted from the reference: yes, same file as above; reference excerpt with picture in `references/audio/` and `references/clips/`.

## Sync rule
- Follows: Attack at 0.150, 0.380 and 0.650 s; the words' first visible frames are at ~0.10, ~0.35 and ~0.60 s, so the tick lands ~1-2 frames after the word starts to appear.
- Repetition: Per word; same sample every time (the reference does not vary it).
- The exit has no sound. [Observed]

## Level
- The reference has no voice, so the level against speech is [Uncertain]. Within the whole set the peaks run from -0.4 dBFS (bouncy boing, loudest) to -12.5 dBFS (random shimmer, quietest); this technique's sample peak is stated under Sound. In a video, a starting point (not observed) is about 12 dB under the voice peaks and keep this technique's level relation to the other motions if several are used.

## Relationships
- Speech: the reference has none; when used on spoken text, start each word/letter reveal on its spoken onset and keep the sound with the visual.
- Sound and picture are one unit: use the motion without its sound only when the user asks.
- Other techniques: Related but different: `sfx-keyboard-typing-captions` is a bright keystroke (up to ~20 kHz, ~5-15 ms); this tick is a duller, longer (~40 ms) tick centred ~2.3 kHz. Same per-word sync idea.

## Adaptation
- Adaptable: the text, its length (the stagger per word/letter stays about the same, the total follows the length), typeface, colour and glow (brand, rule B7), size and position.
- Timing scales with the line: keep the per-unit stagger from Key numbers.

## Key numbers
- Word starts ~0.10 / 0.35 / 0.60 s (spacing ~0.25 s). (observed; table in ANALYSIS.md)
- Rise ~40-50 px at 720 px width (~3.5 % of frame height), ~0.2 s, ease-out. (observed; table in ANALYSIS.md)
- Tick attacks 0.150 / 0.380 / 0.650 s; each ~35-45 ms; sample peak -2.7 dBFS; centroid ~2.3 kHz. (observed; table in ANALYSIS.md)
- Exit: 'Words' ~2.10-2.30 s, 'Up' ~2.40-2.57 s, 'Slide' ~2.60-2.85 s; drop ~40 px + fade; silent. (observed; table in ANALYSIS.md)

## Success criteria
- The motion reads as described (unit, order, blur/bounce/flicker character), with the stagger close to the key numbers.
- The sound is heard once per unit exactly as the Sync rule says and matches the excerpt in `references/audio/`.
- The exit is silent and mirrors the entry.

## User notes
- [User] (2026-11-01) Register each text motion together with its sound as one skill; do not make a template from this video; extract only the text motions with sound shown in the middle of the video.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
