---
name: sfx-correct-answer-chime
description: A bright two-note "ding-ding" chime going up (~1.8 then ~2.35 kHz, ringing tail) on a correct answer, the right way to do something, a tick mark or a success moment. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: sfx
  status: approved
  approved: 2026-10-25
  sources: []
  origin: sound file supplied by the user (SFX library), not from a reference video
---

# sfx-correct-answer-chime

> Library technique (category: `sfx`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Behavior
When the right answer, the correct way, or a success moment is shown, a bright two-note chime plays: a quick "ding" and a higher "ding" right after it, then a soft ringing tail that fades over ~1.5 s.

## Intended effect
A clear, positive "yes, this one" signal - the reward after a wrong example or the payoff of a tip.

## Defining characteristics
- Two rising bright notes (~1.8 kHz then ~2.35 kHz) with a ringing tail [Fixed]
- Only on a clearly "right" / success moment [Rule]
- Once per moment; never stacked with another effect [Rule]

## When to use
- Triggers: "the right way is…", "do this instead", a correct option, a ✅ / tick graphic, a result or win being shown.
- Avoid when: nothing is being judged right or wrong; more than ~2–3 times per minute.

## Sound
- Type and character: bright notification chime, two rising notes, clean, long soft tail
- Library file(s): `<SFX>\ejah_music-notification-correct-answer-447601.mp3` (Same type)

## Sync rule
- Follows: the frame the right answer / tick appears, or the stressed word of the correct statement; first note on that frame (the sound starts ~0.07 s into the file - trim it so the note lands on the frame).
- Repetition: one per right moment.

## Level
- Peak (50 ms RMS) ≈ 12–15 dB under the voice's loud moments (it is bright and carries); fade the tail after ~1 s if the next sentence starts.

## Relationships
- Opposite of `sfx-error-buzz-low` and `sfx-wrong-double-buzz`; a typical pair: wrong sound on the mistake, this chime on the fix.

## Adaptation
- Shorten the tail with a fade when speech continues; do not pitch it.

## Success criteria
- Feels like a clear "correct" signal, bright but not louder than the voice.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
