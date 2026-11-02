---
name: sfx-burn-hit-open
description: A short, loud noise hit with low body (~0.35 s, peaking ~0.1 s in) on the opening film-burn frames; louder than the voice for an instant, then gone. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: sfx
  status: approved
  approved: 2026-10-25
  sources: [src-006]
---

# sfx-burn-hit-open

> Library technique (category: `sfx`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (overlaps, registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
With the 3 film-burn frames at the very start, a **short broadband noise hit with a low "thump" body** is heard: it starts with the video, peaks at ~0.11 s (as the burn ends) and dies out by ~0.35 s. It is the loudest moment of the whole video (≈ 6 dB above the voice's loud moments).

## Intended effect
Gives the burn physical impact and makes the cold open hit hard.

## Defining characteristics
- Noise + low body, ~0.35 s, peak ~0.1 s after start [Observed]
- On the opening flash/burn frames only [Rule]
- Loud: ≈ 6 dB above the voice's loud moments for an instant [Observed]

## Sound
- Type and character: noise burst/impact, low-mid weighted (spectral centroid ≈ 850 Hz on the separated stem), broadband top
- Library file(s): closest by features `<SFX>\Whosh 2.mp3` (Close only loosely - a longer swell); `<SFX>\Hit 3.mp3` (cinematic hit, longer tail) as an alternative
- Extracted from the reference: `<SFX>\from-references\2026-10-25-kith-podcast_burn-hit-open_01.wav` (voice-removed stem; NOT clean - speech "we don't" lay under it, residue possible; the file keeps the analysis-ID prefix of src-006)

## Sync rule
- Follows: the first frame of the burn; peak at the end of the burn frames (≈ 0.1 s).
- Repetition: once, at the opening.

## Level
- Peak (50 ms RMS) ≈ +6 dB over the voice's loud moments; keep it short so it doesn't mask the first word.

## When to use
- Triggers: `transition-film-burn-open` / any opening flash.
- Avoid when: the first word starts on frame 1 and must be clear (shift the first word or lower the hit).

## Relationships
- Visual: `transition-film-burn-open`.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
