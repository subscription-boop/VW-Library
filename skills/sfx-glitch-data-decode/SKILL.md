---
name: sfx-glitch-data-decode
description: A ~0.6 s digital glitch/data chatter (stuttering high-frequency texture with steady high tones around 8.5, 11 and 16.5 kHz) that plays exactly while a lower third glitches in and its letters scramble-decode. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: sfx
  status: approved
  approved: 2026-10-25
  sources: [src-006]
---

# sfx-glitch-data-decode

> Library technique (category: `sfx`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Both lower thirds come with the same sound: a **thin digital chatter** - fast stuttering high-frequency texture plus **two or three steady high tones** (≈ 8.5, 11 and 16.5 kHz) - starting with the first glitch slices and stopping when the decoded text settles (~0.6 s). It sits quietly under the speech.

## Intended effect
Sells the "data / terminal decode" look as a real digital event.

## Defining characteristics
- Digital stutter + steady high tones, no low end, ~0.6 s [Observed]
- Covers exactly the glitch-in + decode of a graphic [Rule]
- Quiet: ≈ 14–16 dB under the voice's loud moments [Observed]

## Sound
- Type and character: glitch/data chatter, bright (energy mostly above 2 kHz), ~0.6 s
- Library file(s): no close match in `<SFX>` (closest by features `Glitch Beat.wav`, far; `Glitch 1.mp3` is a different, harder burst) - None
- Extracted from the reference: `<SFX>\from-references\2026-10-25-kith-podcast_glitch-data-decode_01.wav` and `..._02.wav` (voice-removed stem, high-passed at 2 kHz; NOT clean - speech residue; files keep the analysis-ID prefix of src-006)

## Sync rule
- Follows: the first glitch frame of the graphic (±1 frame); ends when the text has decoded (~0.5–0.6 s later).
- Repetition: once per lower third; use `_01` and `_02` alternately.

## Level
- ≈ 14–16 dB under the voice's loud moments (50 ms RMS); audible but never over a word.

## When to use
- Triggers: `graphic-lower-third-glitch-decode`; any glitch/scramble text reveal.
- Avoid when: the moment already has another effect.

## Relationships
- Visual: `graphic-lower-third-glitch-decode`.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
