---
name: transition-glow-flicker-streak
description: Across a cut, the picture flickers with soft cool-white glow bursts (milky overexposure) and a thin horizontal light streak, about 10 frames in total, then settles on the new shot. Fits a cut between two takes of the same scene in a hook. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: transition
  status: approved
  approved: 2026-10-28
  sources: [src-007]
---

# transition-glow-flicker-streak

> Library technique (category: `transition`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Around the cut from a medium walking shot to a wider take of the same walk, the image flickers: on alternating frames a **soft, milky, cool-white glow** washes over parts of the frame (strongest at the top or bottom), sometimes with a slight blue tint in the darks, and a **thin bright horizontal line** (like an anamorphic lens streak) crosses the lower or middle part of the frame. Normal frames are interleaved between the glow frames, so it reads as a flicker, not a single flash. The cut happens in the middle of the flicker. After ~10 frames the new shot is clean. Graphics on the outgoing shot (the arc arrow) glow brighter during the flicker and leave with the cut.

## Intended effect
Hides a jump between two takes and adds a light, premium "lens" sparkle to the hook without the warmth or grit of a film light leak.

## Defining characteristics
- Cool/neutral white milky glow, not warm orange. [Fixed]
- Flicker: 3–4 glow pulses alternating with clean frames over ~0.3 s. [Rule]
- A thin horizontal light streak on some glow frames. [Rule]
- The cut sits inside the flicker. [Fixed]

## When to use
- Triggers: a cut between two takes or angles of the same scene, especially early in the video.
- Avoid when: the moment is serious/quiet; more than ~2–3 times per video.

## Anatomy over time
- Start: ~5 frames before the cut (first glow pulse).
- Development: alternating glow/clean frames; cut at the 5th–6th frame.
- Resolution: ~4 more frames of pulses on the incoming shot, then clean.
- Repetition: once in the reference.

## Relationships
- Speech: placed over continuous speech (between words "over." and "It's").
- Music: [Uncertain] whether it sits on a beat (the music bed is very quiet here).
- Sound effects: none observed.

## Adaptation
- Adaptable: number of pulses (3–4), streak position.
- Brand: glow stays near-neutral; a faint brand tint is acceptable on cool brands.

## Key numbers
- Frame sequence (observed; table in ANALYSIS.md): f81 first glow pulse + horizontal streak (00:02.669); f82 dark blue-tinted pulse; f83–f85 bright top glow; f86 cut to the wider take (00:02.836).
- After the cut: glow pulses on f88 and f90, f89 has the streak; f91 clean (00:03.003); total ≈ 10 frames (observed).

## Success criteria
- Reads as a quick cool sparkle/flicker, not a white-out; the cut is hidden inside it.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Frame by frame: `sequences/..._flicker.jpg`; with motion: `clips/..._glow-flicker-cut.mp4`.
