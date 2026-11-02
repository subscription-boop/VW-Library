---
name: zoom-open-fast-pullout-blur
description: The video opens already zoomed in (~1.3x) and snaps out to the normal framing in about 0.2 s, with motion blur on the first frames, like the camera being yanked back. Fits an aggressive, high-energy first second. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: zoom
  status: approved
  approved: 2026-10-28
  sources: [src-007]
---

# zoom-open-fast-pullout-blur

> Library technique (category: `zoom`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Frame 1 of the video is tighter than the real framing (~1.3x: the speaker is bigger, his legs cut off). From frame 2 the picture snaps out: most of the move happens in the first 3–4 frames, with strong motion blur (mostly vertical, following the walking speaker), and the normal framing is reached by ~0.2 s (frame 6–7). No overshoot, no bounce. The hook title is already building on frame 1, and speech starts at once.

## Intended effect
A punchy, aggressive start: the first frame "hits" the viewer and the fast snap with blur signals energy before a single word lands.

## Defining characteristics
- Starts on frame 1 of the video, already tight (~1.25–1.35x). [Rule]
- Pull-out (never push-in), very fast: ~0.2 s total, ~70 % of it in the first ~0.1 s. [Fixed]
- Motion blur on the fast frames. [Fixed]
- No overshoot; settles and stays. [Rule]

## When to use
- Triggers: the very first shot of a fast, aggressive promo or hook.
- Good fit: walk-and-talk or moving shots, where the blur feels natural.
- Avoid when: the video should open calm; then use `zoom-open-settle-out` ([SKILL.md](../zoom-open-settle-out/SKILL.md)) (softer, ~0.6–0.8 s, after a film burn) instead.

## Anatomy over time
- Start: frame 1 at ~1.3x.
- Development: frames 2–4 carry most of the move with blur.
- Resolution: normal framing by frame ~6–7; static (or real camera motion) afterwards.
- Repetition: once, at the opening.

## Relationships
- Speech: speech starts on frame 1; the move does not wait for a word.
- Other techniques: the hook lockup `text-key-phrase-stacked-lockup` ([SKILL.md](../text-key-phrase-stacked-lockup/SKILL.md)) builds at the same time.
- Sound effects: none observed.

## Adaptation
- Adaptable: start scale (1.25–1.35x) by source resolution; blur direction follows the camera/subject motion.
- Brand: none.

## Key numbers
- Start scale ~1.31x of the settled framing; per-frame scale 0.95, 0.92, 0.93, 0.96 at 00:00.033–00:00.133 (most of the move); settled ~1.0x at 00:00.167–00:00.200 (observed; table in ANALYSIS.md).
- Motion blur strong, mostly vertical, at 00:00.033–00:00.100 (observed).

## Success criteria
- Frame 1 is visibly tighter; the snap out takes ≤ ~0.25 s with blur; no bounce.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Frame by frame: `sequences/..._pullout.jpg`; with sound: `clips/..._opening-fast-pullout.mp4`.
