---
name: sfx-shimmer-tone
description: A bright, sustained shimmer/ding made of steady high tones (~4.2 kHz and ~9.5 kHz) lasting ~0.7-0.9 s on special reveals - a step header appearing or chosen items collecting into a tray; a short single-tone ding (~6.8 kHz) for a small settle. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: sfx
  status: approved
  approved: 2026-10-25
  sources: [src-005]
---

# sfx-shimmer-tone

> Library technique (category: `sfx`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
On a few special reveals a **bright tonal shimmer** sounds: two or three steady high tones (about 4.2 kHz and 9.5 kHz, sometimes 10.5 kHz) with a soft start, held ~0.7–0.9 s and fading. It plays when the step-2 header appears and while five chosen thumbnails fly into the tray. A **shorter single-tone ding** (~6.8 kHz, ~0.14 s) marks the calendar settling at the start.

## Intended effect
A "magic/reward" accent for moments of selection or revelation; brighter and more musical than a whoosh.

## Defining characteristics
- Tonal (pitched), bright, steady tones; no noise burst [Fixed]
- Soft attack, ~0.7–0.9 s sustain/fade (short ding: ~0.15 s) [Observed]
- Rare: 2–3 times per video, only on reveals/selections [Rule]
- Quiet: about 20 dB under the voice, just above the music bed [Rule]

## Sound
- Type and character: bright shimmer/chime tones, 0.7–0.9 s; short ding 0.14 s
- Library file(s): no match in `<SFX>` (None)
- Extracted from the reference: `<SFX>\from-references\2026-10-25-6by5-method_shimmer-tone-step-header_01.wav`, `..._shimmer-tone-collect_02.wav`, `..._ding-short_01.wav` (files keep the analysis-ID prefix of src-005; separated from voice and music and high-passed; NOT clean - faint speech residue remains; a cleaner chime from a sound library would be better for production)

## Sync rule
- Follows: the reveal frame (header appears, items start collecting); starts on that frame.
- Repetition: once per reveal; never two in a row.

## Level
- ≈ 20 dB under the loud voice (50 ms RMS), ≈ 2 dB above the music bed.

## When to use
- Triggers: step header of a later step, "pick these", unlocking/reward moments, lead-magnet reveal.
- Avoid when: the beat already has a whoosh peak or a click.

## Relationships
- Visuals: `graphic-step-header-arc-number`, `graphic-scatter-assemble` (selection variant).

## Key numbers
- Reference shimmer with the step-2 header measured -32 dB (50 ms RMS) (observed; table in ANALYSIS.md).

## Success criteria
- The shimmer is noticeable as a sparkle on the reveal but never covers words.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
