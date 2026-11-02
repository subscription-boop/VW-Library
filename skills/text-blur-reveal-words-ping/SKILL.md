---
name: text-blur-reveal-words-ping
description: A line builds one word at a time: each word comes out of heavy defocus into sharp focus while brightening, with a soft bell 'ping' just before each word is sharp; words leave in reverse by blurring out, silent. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-11-01
  sources: [src-008]
---

# text-blur-reveal-words-ping

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

The reference is a text-animation preset demo (preset name shown: "Blur Reveal Words"); this skill records the motion and its sound as one unit.

## Observable behavior
Whole words (not letters) emerge from a heavy blur: each word starts as a wide, dark, orange-tinted smear, and over ~0.3 s it sharpens and brightens to the final look. Words follow ~0.21 s apart (starts ~12.37, ~12.58, ~12.80 s; sharp ~12.55, ~12.90, ~13.15 s). A bell-like ping is heard for each word, ~0.05-0.12 s before that word is fully sharp (so the pings are ~0.33 s apart, slower than the visual spacing). The line holds ~1.2 s. It leaves in reverse: the last word blurs out and darkens first, then the previous ones, ~0.4 s in total; silent.

Reference look, for context only [Observed]: very heavy geometric sans (Montserrat-ExtraBold-like), text filled with a left-to-right gradient from yellow (~#F8EC2B) through gold to orange (~#F89C1E) with a soft same-colour glow, one centred line (~63 % of the frame width, glyph height ~5 % of frame height) at ~50 % of the frame height on pure black. The motion does not depend on this look: typeface, colours and glow follow the selected brand (standing rule B7), not the reference palette.

## Intended effect
A smooth, premium word-by-word focus reveal with a gentle musical accent.

## Defining characteristics
- Word-level build; each word defocus -> sharp with brightening. [Fixed]
- Blur is heavy (a word is unreadable at its start). [Fixed]
- One ping per word, landing slightly before the word is fully sharp; the same ping each time. [Fixed]
- Exit = reverse word order, blur out, silent. [Rule]

## When to use
- Short phrases of 2-4 words where each word matters; elegant or premium tone. Avoid on long lines.
- The text of the reference (the preset's own name) is not part of the skill; the technique applies to any short line.

## Anatomy over time
- Start: first word is a blur smear ~0.07 s before its ping.
- Development: next word starts ~0.21 s later; pings every ~0.33 s.
- Resolution: all sharp ~13.2 s; hold ~1.2 s.
- Exit: ~0.4 s reverse blur-out, silent.

## Sound
- Type and character: A soft bell-like ping: fundamental ~1.05 kHz with partials ~2.09, 2.79 and 4.2 kHz, quick attack, ring of ~0.3 s decaying; the three pings are the same sample. Sample peak -6.3 dBFS.
- Library file(s): `<SFX>\from-references\src-008_ping-bell-word_01.wav` (extracted from the reference by the user's request, 2026-11-01; cut and normalised to -1 dBFS, 5 ms fades, nothing added). No search for similar library sounds was made: the user asked to use the reference's own sounds.
- Extracted from the reference: yes, same file as above; reference excerpt with picture in `references/audio/` and `references/clips/`.

## Sync rule
- Follows: Attacks at 12.445, 12.780 and 13.110 s, i.e. +0.07 / +0.20 / +0.31 s after each word starts to appear and 0.05-0.12 s before each word is sharp.
- Repetition: Per word; same sample every time.
- The exit has no sound. [Observed]

## Level
- The reference has no voice, so the level against speech is [Uncertain]. Within the whole set the peaks run from -0.4 dBFS (bouncy boing, loudest) to -12.5 dBFS (random shimmer, quietest); this technique's sample peak is stated under Sound. In a video, a starting point (not observed) is about 12 dB under the voice peaks and keep this technique's level relation to the other motions if several are used.

## Relationships
- Speech: the reference has none; when used on spoken text, start each word/letter reveal on its spoken onset and keep the sound with the visual.
- Sound and picture are one unit: use the motion without its sound only when the user asks.
- Other techniques: Possible overlap with `text-phrase-build-blur-rise` (word-by-word grey/blur -> white): that one is a light caption build with no sound; this one is a heavy defocus reveal with a ping per word (registered as a separate skill, user decision 2026-11-01).

## Adaptation
- Adaptable: the text, its length (the stagger per word/letter stays about the same, the total follows the length), typeface, colour and glow (brand, rule B7), size and position.
- Timing scales with the line: keep the per-unit stagger from Key numbers.

## Key numbers
- Word starts ~12.37 / 12.58 / 12.80 s (spacing ~0.21 s); sharp ~12.55 / 12.90 / 13.15 s; each deblur ~0.3 s. (observed; table in ANALYSIS.md)
- Ping attacks 12.445 / 12.780 / 13.110 s (spacing ~0.33 s); ring ~0.3 s; sample peak -6.3 dBFS; fundamental ~1.05 kHz. (observed; table in ANALYSIS.md)
- Exit 14.37-14.78 s (last word first), silent. (observed; table in ANALYSIS.md)

## Success criteria
- The motion reads as described (unit, order, blur/bounce/flicker character), with the stagger close to the key numbers.
- The sound is heard once per unit exactly as the Sync rule says and matches the excerpt in `references/audio/`.
- The exit is silent and mirrors the entry.

## User notes
- [User] (2026-11-01) Register each text motion together with its sound as one skill; do not make a template from this video; extract only the text motions with sound shown in the middle of the video.
- [User] (2026-11-01) Approved as a separate skill from `text-phrase-build-blur-rise` ("add all"); the overlap recommendation was to keep them separate.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
