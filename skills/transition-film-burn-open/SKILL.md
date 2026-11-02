---
name: transition-film-burn-open
description: The video opens with 3 frames of film burn over the first shot: saturated orange, red and yellow light bands with hard diagonal edges and dust specks wash over the picture, then the clean dark shot appears; a burn-hit sound plays with it. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: transition
  status: approved
  approved: 2026-10-25
  sources: [src-006]
---

# transition-film-burn-open

> Library technique (category: `transition`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
On frames 0–2 of the video a **film-burn overlay** washes over the opening wide shot: frame 0 a bright orange band with a hard diagonal top edge covering most of the picture, frame 1 a deep red band lower in the frame, frame 2 a yellow-orange wash with a diagonal lower edge, each with small dark dust specks. The shot underneath stays readable (screen-like blend) and the first caption words are already visible. On frame 3 the picture is clean and dark. A short burn-hit sound plays at the same time (`sfx-burn-hit-open`).

## Intended effect
A cinematic, analogue "ignition" that grabs attention in the first 0.1 s and sets the premium film mood before the dark shot.

## Defining characteristics
- 3 frames (≈ 0.125 s), at the very start [Observed]
- Warm saturated burn colours (orange → red → yellow), hard diagonal band edges, dust specks [Fixed]
- Screen-like blend over the shot; no black or white frame [Rule]
- Clean cut to the normal shot after it (no tinted recovery) [Observed]

## When to use
- Triggers: the first frame of a video (cold open).
- Avoid when: the brand look is clean/minimal tech; more than once per video.

## Relationships
- Sound: `sfx-burn-hit-open` on the same frames.
- Followed by `zoom-open-settle-out` on the first shot.

## Adaptation
- Use real film-burn overlays (licensed assets) or generated bands; keep to 3–4 frames; colours warm regardless of brand.

## Key numbers
- Mean luma (0–255) on the three burn frames: 149 (orange) / 79 (red) / 186 (yellow); the first clean frame: 20 (observed; table in ANALYSIS.md).

## Success criteria
- Feels like film catching light, not like a white flash; over before the first word is read.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
