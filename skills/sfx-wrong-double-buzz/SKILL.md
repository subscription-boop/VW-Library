---
name: sfx-wrong-double-buzz
description: A quiz-show "eh-eh" double buzzer (two short harsh pulses, ~0.3 s in total) on a wrong answer, a rejected option or an "X" mark - shorter and sharper than the low error buzz. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: sfx
  status: approved
  approved: 2026-10-25
  sources: []
  origin: sound file supplied by the user (SFX library), not from a reference video
---

# sfx-wrong-double-buzz

> Library technique (category: `sfx`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Behavior
On a wrong answer or a rejected option, two quick harsh buzzer pulses sound ("eh-eh"), like a quiz show: each pulse ~0.12–0.14 s, a short gap between them, the whole thing over in ~0.3 s.

## Intended effect
A fast, punchy "nope" that keeps the rhythm moving; works well in quick lists and quiz-style edits.

## Defining characteristics
- Two short harsh buzzer pulses with a small gap, ~0.3 s total [Fixed]
- On a wrong / rejected item [Rule]
- One per item; never stacked with another effect [Rule]

## When to use
- Triggers: "no", "wrong", crossing out an option, a wrong guess, a ❌ mark, a "don't do this" item in a fast list.
- Avoid when: calm or serious moments; more than ~3 times per minute.

## Sound
- Type and character: harsh double buzzer, broadband (energy up to ~8 kHz), dry
- Library file(s): `<SFX>\freesound_community-wrong-47985.mp3` (Same type; only the first ~0.4 s of the file has sound)

## Sync rule
- Follows: the frame the wrong mark / rejected item appears, or the spoken "no"/"wrong"; first pulse on that frame.
- Repetition: one per wrong item.

## Level
- Peak (50 ms RMS) ≈ 10–12 dB under the voice's loud moments (it is harsh, keep it lower than the low error buzz).

## Relationships
- Opposite: `sfx-correct-answer-chime`. Alternative: `sfx-error-buzz-low` (heavier, longer, more comic).

## Adaptation
- Use only the first 0.4 s of the file; a 5 ms fade-out after the second pulse.

## Success criteria
- Reads instantly as "wrong", stays short, never covers a word.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
