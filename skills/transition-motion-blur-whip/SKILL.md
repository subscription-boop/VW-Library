---
name: transition-motion-blur-whip
description: Between B-roll shots, the outgoing shot smears with strong directional motion blur (any direction, often with a slight rotation), the cut happens inside the smear, and the incoming shot starts smeared and slightly tilted, then resolves sharp in ~3–4 frames. Fits beat-cut B-roll montages. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: transition
  status: approved
  approved: 2026-10-28
  sources: [src-007]
---

# transition-motion-blur-whip

> Library technique (category: `transition`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
In the montage, many shot changes are hidden in a fast camera-like whip: over ~2–3 frames the outgoing shot streaks with heavy directional blur (diagonal, horizontal or curved/rotational, following or continuing the shot's own camera motion). The cut sits inside the streak. The incoming shot begins as a strong streak too, often slightly rotated (a few degrees) and offset, and resolves to sharp over ~3–4 frames while the rotation settles. The blur direction changes from whip to whip.

## Intended effect
Keeps a fast montage fluid and energetic: shots seem to fly into each other on the beat instead of jumping.

## Defining characteristics
- Heavy directional motion blur on both sides of the cut. [Fixed]
- Total ≈ 5–7 frames: ~2–3 out, ~3–4 in. [Rule]
- Incoming shot settles from a slight tilt/offset as it sharpens. [Rule]
- Direction may vary (diagonal, horizontal, rotational); it should feel like it continues the camera motion. [Rule]
- The cut lands on a music beat (kick/bass hit). [Rule]

## When to use
- Triggers: shot changes inside a music-driven B-roll montage; every 1–3 cuts (alternating with hard cuts).
- Avoid when: under speech that needs focus, or between two very slow, calm shots.

## Anatomy over time
- Start: 2–3 frames before the beat.
- Development: cut on the beat inside the blur.
- Resolution: 3–4 frames to sharp and level.
- Repetition: ~8 of ~19 cuts in the reference montage.

## Relationships
- Music: cut on the kick/bass onset.
- Sound effects: [Uncertain] the music has bright swells before several beats; a separate whoosh could not be separated from the music (see ANALYSIS Sound).
- Other techniques: part of `cut-beat-broll-montage` ([SKILL.md](../cut-beat-broll-montage/SKILL.md)); hard cuts in between.

## Adaptation
- Adaptable: direction per cut (follow the outgoing camera motion), blur strength by resolution.
- Brand: none.

## Key numbers
- Measured example (van to building): cut ≈ 00:21.588; incoming shot tilted, sharp by ≈ 00:21.75 (observed; table in ANALYSIS.md).
- The other measured whips are listed only as time windows; the roof to worker whip (00:28.83–00:28.87) is short (observed).

## Success criteria
- No visible hard jump; the blur carries the eye across the cut on the beat; the incoming shot is sharp within ~4 frames.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Frame by frame: the three `sequences/`; with music: the `clips/`.
