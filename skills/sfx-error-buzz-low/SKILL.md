---
name: sfx-error-buzz-low
description: A low, buzzy "wrong answer" tone (~0.5 s body, short tail) placed on the moment a mistake, myth or bad habit is named, so the viewer hears "that is wrong" before the explanation. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: sfx
  status: approved
  approved: 2026-10-25
  sources: []
  origin: sound file supplied by the user (SFX library), not from a reference video
---

# sfx-error-buzz-low

> Library technique (category: `sfx`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Behavior
When the speaker names something wrong - a common mistake, a myth, a bad habit, the "don't" side of a comparison - one low, buzzy error tone plays right on that phrase (or in the pause just after it). It is short and heavy: a deep buzz with bright harmonics that bend down slightly, loud for ~0.5 s and gone by ~1 s.

## Intended effect
Marks the statement as wrong in a playful, game-show way; the viewer instantly knows which side of the argument this is.

## Defining characteristics
- One low buzzy tone, ~0.5 s body, ~1 s total [Fixed]
- Only on a clearly "wrong" moment (mistake, myth, "not like this") [Rule]
- Once per wrong moment; never stacked with another effect [Rule]

## When to use
- Triggers: "the biggest mistake is…", "most people do X (wrong)", "this is a myth", a wrong option in a list or quiz, a ❌ / red-cross graphic.
- Avoid when: the speaker is serious or emotional (it makes the moment comic); more than ~2–3 times per minute.

## Sound
- Type and character: low error buzz (fundamental ≈ 82 Hz with strong harmonics up to ~8 kHz, falling slightly), heavy, game-show style
- Library file(s): `<SFX>\lesiakower-error-mistake-sound-effect-incorrect-answer-437420.mp3` (Same type)

## Sync rule
- Follows: the stressed word of the wrong statement (start on its onset, or in the gap right after the phrase), or the frame a ❌ / wrong graphic appears.
- Repetition: one per wrong moment.

## Level
- Peak (50 ms RMS) ≈ 8–10 dB under the voice's loud moments; if it falls under a word, 12 dB under and high-pass the low end (~150 Hz) so the voice stays clear.

## Relationships
- Visuals: a red cross / wrong mark, a "myth" label, a negative example card.
- Opposite: `sfx-correct-answer-chime` for the right answer. Alternative wrong sound: `sfx-wrong-double-buzz` (shorter, sharper double buzzer).

## Adaptation
- Trim the tail if the next word comes fast; never pitch it up (it loses its weight).

## Success criteria
- The viewer understands "wrong" without reading anything, and no word is masked.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
