---
name: sfx-noise-burst-flash
description: A short bright burst of static/air noise (~0.2 s) with a small click inside, played exactly on a light flash transition. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: sfx
  status: approved
  approved: 2026-10-24
  sources: [src-003]
---

# sfx-noise-burst-flash

> Library technique (category: `sfx`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
When the picture flashes to bright light (the light-leak / negative flash over the jump cut after "client"), a short wide-band noise burst is heard, like a puff of static, with a small click at the brightest frame. It sits in the pause between two sentences.

## Intended effect
Sells the flash as a physical event and marks the jump to the next thought.

## Defining characteristics
- Broadband noise (up to ~18 kHz), ~0.2 s, hard start, short tail. [Fixed]
- Locked to the flash frames, click on the brightest frame. [Fixed]
- Lives in a speech gap. [Rule]

## When to use
- Triggers: `transition-light-leak-flash`, `transition-negative-flash`, other single-frame-to-few-frame flashes.
- Avoid when: the flash happens over a word (shorten or skip it).

## Sound
- Type and character: static/air noise burst with a click, ~0.2 s, bright.
- Extracted from the reference: `<SFX>\from-references\src-003_noise-burst-flash_01.wav` (clean; taken from a speech gap). Library alternatives: `Glitch 1.mp3` (Close, more digital), `Vintage Flash.wav` (Close, longer tail).

## Sync rule
- Follows: the flash; start ~1 frame before the first bright frame, click on the brightest frame.
- Repetition: once per flash.

## Level
- Peaks ~1 dB under the speech peaks (reference: burst ~-6.2 dBFS vs presenter words ~-5.3 dBFS peak).

## Relationships
- Cuts: on the jump cut that the flash covers.
- Speech: in the gap.
- Other techniques: pairs with `transition-light-leak-flash` / `transition-negative-flash`.

## Adaptation
- Adaptable: length to the flash (trim the tail), level ±3 dB.
- Brand: none.

## Key numbers
- All values are stated above; the per-source table is in ANALYSIS.md.

## Success criteria
- The burst starts with the flash and is gone by the time the next word starts.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Timing: `clips/src-003_0006200-0007100_flash-burst.mp4`.
- Spectrum: `frames/src-003_0006400-0006950_spectrogram-flash.png`.
