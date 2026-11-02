---
name: zoom-cut-ease-out
description: On the cut that opens a section, the shot starts digitally punched in (~1.25–1.3x) and immediately eases back out to normal framing: fast at first, then a long soft settle (~1.5–2.3 s). Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: zoom
  status: approved
  approved: 2026-10-21
  sources: [src-002]
---

# zoom-cut-ease-out

> Library technique (category: `zoom`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
A hard cut lands on a tighter framing of the talking head (about 1.25–1.3x of the normal shot). From the very first frame the image starts scaling back down toward the normal framing. The move is quick at first (about half of it done in ~0.4–0.6 s, ~80 % in ~0.7–1.0 s) and then slows to a gentle settle, reaching normal framing after ~1.5–2.3 s. It is a pull-out, never a push-in. Other sections stay on a static framing.

## Intended effect
Gives the start of a section energy and "arrival" without a visible effect; the viewer feels the frame breathe open as the new idea starts.

## Defining characteristics
- Starts on a cut, already tight. [Fixed]
- Direction is always out (tight → normal). [Fixed]
- Strong ease-out: fast start, long soft tail; no bounce, no overshoot. [Fixed]
- Used on a few section starts only, not on every cut. [Rule]

## When to use
- Triggers: the hook (first frame of the video), the start of a step/section, the closing action line.
- Avoid when: the source cannot take ~1.3x crop cleanly; during B-roll; when a static framing is needed for an overlay that must stay aligned with the speaker.

## Anatomy over time
- Start: hard cut to ~1.25–1.3x.
- Development: exponential-style ease-out; ~50 % at 0.4–0.65 s, ~80 % at 0.7–1.0 s.
- Resolution: settles at 1.0x by ~1.5–2.3 s and holds static.
- Repetition: 3 times in a 26 s reel (hook, step 2, closing).

## Relationships
- Captions and labels stay fixed on screen while the picture scales under them.
- Pairs with `text-step-label-serif` on section starts and with the hook's `graphic-ui-stat-popup`.

## Adaptation
- Start scale follows source resolution (keep the crop sharp) and framing (eyes in the upper third at both ends).
- Duration may shorten to ~1 s for fast edits; keep the ease shape.

## Key numbers
- Hook pull-out: ~1.24–1.3x → 1.0x; 50 % at ~0.4 s, 80 % at ~0.85 s, settled ~2.2 s (observed; table in ANALYSIS.md).
- Step 2 pull-out: ~1.3x → 1.0x; 50 % at ~0.65 s, 80 % at ~1.0 s, settled ~1.5 s (observed).
- Closing pull-out, from the cut on "apply": ~1.3x → 1.0x; settled ~1.4 s (observed).
- Other talking segments stay static (scale 1.000 ±0.002) (observed).

## Success criteria
- No visible zoom "effect"; the move reads as the frame relaxing.
- Fast-then-slow curve, no overshoot, no jitter.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md): `*-pullout` sequences at 10 fps show the curve; clips show it with sound.
