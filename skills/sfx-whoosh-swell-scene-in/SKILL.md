---
name: sfx-whoosh-swell-scene-in
description: A soft airy whoosh swell that starts on (or just before) the cut into a new full-canvas scene or a big assemble move and peaks 0.1-0.3 s after the cut, ~0.6-0.8 s long, following the elements as they fly in. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: sfx
  status: approved
  approved: 2026-10-25
  sources: [src-005]
---

# sfx-whoosh-swell-scene-in

> Library technique (category: `sfx`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
When the video cuts into a new full-canvas scene (phone scene, tray scene, competitor scene, lead-magnet card) or a large group of elements flies in (calendar dates, first mind-map branch), a **soft noise swell** rises from the cut, **peaks 0.1–0.3 s after it** and fades over ~0.5 s. It is mostly low-mid air (no bright metallic top), clearly above the music bed but well under the voice.

## Intended effect
Sells the motion of the elements arriving and marks a "new scene" without a hard hit.

## Defining characteristics
- Starts at the cut (0–0.2 s before), peaks after it, decays with the settling motion [Fixed]
- Soft air/noise character, mid-low, no impact at the start [Rule]
- ~0.6–0.8 s total [Observed]
- One per scene entry; not on every cut [Rule]

## Sound
- Type and character: airy whoosh-in, 0.6–0.8 s, mid/dark
- Library file(s): `<SFX>\Short Whoosh Metal.mp3` (closest by features - Close; check that the metallic top is not too bright, roll it off), `<SFX>\Simple Whoosh 1.wav` / `Simple Whoosh 2.wav` as softer alternatives (Close)
- Extracted from the reference: none (sits under speech)

## Sync rule
- Follows: the cut into the new scene; swell start at the cut (−0.2…+0.1 s), peak +0.1…+0.3 s.
- Repetition: on full-canvas scene entries and big assemble moves only.

## Level
- Peak ≈ 9–15 dB under the loud voice (50 ms RMS), ≈ 10 dB above the music bed.

## When to use
- Triggers: entering a proof/demo scene, a grid flying in, opening a lead-magnet reveal.

## Relationships
- Visuals: `graphic-scatter-assemble`, `graphic-phone-mockup-feed`, `layout-split-canvas-speaker-card` scene changes.

## Key numbers
- Reference scene-in swells peak +0.12 / +0.31 / +0.25 / +0.12 s after the cut; -10 dB spans −0.05…+0.70, +0.10…+0.59, −0.21…+0.62 and −0.22…+0.54 s around the cut (observed; table in ANALYSIS.md).
- Calendar assemble in the reference peaks +0.69 s after its start, following the dates' flight (observed; table in ANALYSIS.md).

## Success criteria
- The swell peaks while the elements are still moving and is gone when they settle.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
