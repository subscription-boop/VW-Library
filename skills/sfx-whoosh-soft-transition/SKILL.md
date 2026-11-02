---
name: sfx-whoosh-soft-transition
description: A soft, low "hoof" whoosh (an air puff of ~0.2–0.45 s) across a fast transition such as a whip pan or a card exit, ending on the cut. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: sfx
  status: approved
  approved: 2026-10-24
  sources: [src-003]
---

# sfx-whoosh-soft-transition

> Library technique (category: `sfx`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
On a fast moving transition (the whip pan from the presenter into the podcast, the smeared exit of the scaled-up keyword) a short, soft, low-mid whoosh is heard, like a puff of air passing the camera. It is muffled rather than bright (energy mostly 200–3000 Hz) and is gone within half a second.

## Intended effect
Gives the motion a physical push so the jump between shots feels intentional, without the drama of a big cinematic whoosh.

## Defining characteristics
- Soft, dark-to-mid air swell, no metallic or bright top. [Fixed]
- Short: ~0.2–0.45 s. [Rule]
- Spans the transition and ends on/just after the cut. [Rule]

## When to use
- Triggers: `transition-whip-pan`, the exit of `transition-word-scale-through`, other fast sideways moves between shots or from a card back to footage.
- Avoid when: plain jump cuts inside one shot; calm fades (`transition-fade-to-black`).

## Anatomy over time
- Start: ~0.1–0.2 s before the cut (as the outgoing frame starts to smear).
- Development: quick swell to a peak around the cut.
- Resolution: soft decay of ~0.2–0.3 s into the new shot.
- Repetition: once per transition; at most one per few seconds.

## Sound
- Type and character: soft low "puff" whoosh, centroid ~450–550 Hz, ~0.2–0.45 s.
- Library file(s): `<SFX>\Simple Whoosh 1.wav` (closest, **Close**), `<SFX>\Simple Whoosh 2.wav` (shorter/darker, for very quick cuts). Avoid the bright `Short Whoosh Metal.mp3` and the long `Deep Whoosh` files for this behavior.
- Extracted from the reference: none (both reference instances overlap speech or the music bed; the library sounds are close).

## Sync rule
- Follows: the transition cut; place the whoosh so its peak lands on the cut frame (±1 frame).
- Repetition: per transition.

## Level
- Peaks about level with the speech peaks (reference: whoosh ~-5.6 dBFS vs presenter words ~-5.3 dBFS peak), but it is low and soft, so it does not mask words; duck it 3–4 dB if a word starts right on the cut.

## Relationships
- Cuts: on the cut.
- Speech: usually in the gap between sentences.
- Music and beats: independent of the bed.
- Other techniques: pairs with `transition-whip-pan` and `transition-word-scale-through`.

## Adaptation
- Adaptable: length to the transition length; choose the shorter file for 2–3 frame whips.
- Brand: none.

## Key numbers
- Reference whip-pan whoosh ~0.45 s, low-mid, peaking shortly after the cut; scale-through exit whoosh ~0.2 s, ending on the cut; centroid ~460–550 Hz (observed; table in ANALYSIS.md).

## Success criteria
- Every whip/scale-through exit has one soft whoosh peaking on the cut; none on plain jump cuts.
- It reads as air movement, not as a hit or a bright swish.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Whip into the podcast: `clips/src-003_0009200-0010400_whip-presenter-to-podcast.mp4`.
- Scale-through exit: `clips/src-003_0021200-0022400_scale-through-whip-exit.mp4`.
- Spectrum: `frames/src-003_0009300-0025400_spectrogram-whooshes.png` (top left and top right panels).
