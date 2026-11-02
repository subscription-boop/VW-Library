---
name: fx-echo-rgb-trail
description: On a music drop, a moving subject (a car) leaves a stack of stepped echo copies behind it that grow over ~0.4 s, with red/cyan colour fringing on the edges, before the shot spins out. Fits the drop of a montage on a moving object. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: fx
  status: approved
  approved: 2026-10-28
  sources: [src-007]
---

# fx-echo-rgb-trail

> Library technique (category: `fx`, new category: in-shot visual effects applied to the footage itself). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (observed measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Exactly when the music's heavy bass section starts, the yellow car shot gains an echo: semi-transparent copies of the car from previous frames trail behind it in clear steps (like a stack of cards), getting longer over ~0.4 s. Edges show red/cyan colour separation (chromatic split), increasing with the echo. The frame also darkens toward the edges. The effect then flows into the spin transition.

## Intended effect
Visualises the bass drop: the image "stutters" and smears with the music, building tension before the spin.

## Defining characteristics
- Stepped echo copies (discrete, not smooth motion blur) trailing a moving subject. [Fixed]
- Growing over the effect's duration; red/cyan fringing on edges. [Rule]
- Starts on the drop. [Rule]

## When to use
- Triggers: a music drop/heavy section on a shot with a clearly moving subject or camera.
- Avoid when: the subject is static (no echo visible), or under speech.

## Anatomy over time
- Start: on the drop (first echo frame ≈ 00:22.92).
- Development: echo and fringing grow for ~0.4–0.5 s.
- Resolution: handed over to `transition-spin-blur-drop` ([SKILL.md](../transition-spin-blur-drop/SKILL.md)).
- Repetition: once.

## Relationships
- Music: start aligned with the bass drop (sub level jumps ≈ +15 dB at ≈ 00:22.9–00:23.0).
- Sound effects: none separable from the music.
- Other techniques: leads into `transition-spin-blur-drop` ([SKILL.md](../transition-spin-blur-drop/SKILL.md)).

## Adaptation
- Adaptable: echo count/spacing by subject speed.
- Brand: none.

## Key numbers
- Echo stack + RGB fringing at maximum at 00:23.12–00:23.32 with ~6–8 copies visible; spin-out begins at 00:23.39 (observed; table in ANALYSIS.md).

These describe the references. They are not quotas or required values.

## Success criteria
- Echo copies are distinct steps; the effect starts on the drop and grows.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
