---
name: transition-spin-blur-drop
description: The outgoing shot spins away with rotational blur while darkening to near-black, and the incoming shot spins in from a rotational smear and locks sharp in ~3 frames. Fits the biggest music moment of a montage. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: transition
  status: approved
  approved: 2026-10-28
  sources: [src-007]
---

# transition-spin-blur-drop

> Library technique (category: `transition`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
After the car shot's echo effect (`fx-echo-rgb-trail` ([SKILL.md](../fx-echo-rgb-trail/SKILL.md))), the frame starts rotating with strong rotational (circular) blur and darkens toward black over ~6 frames, until only a dark swirl remains. On the cut the incoming shot (a crystal car) starts as a bright rotational swirl and stops spinning, sharp and level, within ~3 frames.

## Intended effect
A big, dramatic "drop" transition: the darkest, most chaotic moment of the montage that resets into the next scene.

## Defining characteristics
- Rotational blur on both sides; the outgoing side darkens toward black. [Fixed]
- Out ~6 frames, in ~3 frames (fast lock). [Rule]
- Used once, on the strongest music moment. [Rule]

## When to use
- Triggers: the music drop or the biggest beat of a montage; a change to a very different world/scene.
- Avoid when: used more than once per video (loses impact), or under speech.

## Anatomy over time
- Start: ~6 frames before the cut; spin accelerates, image darkens.
- Development: near-black swirl at the cut.
- Resolution: incoming swirl decelerates to still in ~3 frames.
- Repetition: once.

## Relationships
- Music: sits inside the loudest bass section (heavy sub from ≈ 00:23.0); the cut lands on a bass onset (≈ 00:23.59).
- Sound effects: none separable from the music.
- Other techniques: preceded by `fx-echo-rgb-trail` ([SKILL.md](../fx-echo-rgb-trail/SKILL.md)); part of `cut-beat-broll-montage` ([SKILL.md](../cut-beat-broll-montage/SKILL.md)).

## Adaptation
- Adaptable: spin direction, darkening amount.
- Brand: none.

## Key numbers
- Spin-out + darken 00:23.39–00:23.56 (~6 frames, ends near-black); cut at 00:23.590; spin-in lock 00:23.59–00:23.69 (~3 frames) (observed; table in ANALYSIS.md).

## Success criteria
- Reads as one spinning plunge and recovery; the incoming shot is sharp within ~0.1 s.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
