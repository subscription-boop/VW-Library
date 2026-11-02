---
name: template-full-back-color-green-red-flag-sfx
description: Green flag / red flag (right / wrong) talking-head game - neutral wall while a statement is read, then the whole wall behind the speaker turns green with a chime or red with an error buzz on his verdict, big "GREEN / FLAG" caps on the chest, single-word chest captions, short thinking pause before each answer, no music. Library template; apply only when the user selects it.
disable-model-invocation: true
metadata:
  kind: template
  status: approved
  approved: 2026-10-25
  uses: [graphic-wall-color-verdict, sfx-correct-answer-chime, sfx-error-buzz-low, text-single-word-captions-chest, text-caps-keyword-stack, grade-soft-warm-natural]
  sources: []
  origin: the user's project 2026-10-25-green-red-flag (v002), registered on his request
---

# template-full-back-color-green-red-flag-sfx

> Library template. Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). Selecting this template authorizes the techniques listed below. Load each by reading its SKILL.md.
> Execution part only. Analysis notes (observed reference structure, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Intention and style
A quick verdict game: a statement is read, a short beat of suspense, then the answer, and the whole background tells the viewer "right" or "wrong" before they read anything. Clean and simple: one camera, no B-roll, no cards, no music. The colour and the sound are the show.

## Techniques and roles
| Technique | Role |
| :- | :- |
| `graphic-wall-color-verdict` ([SKILL.md](../graphic-wall-color-verdict/SKILL.md)) | the wall turns green (right / green flag) or red (wrong / red flag) on every verdict; silent green → red preview on the intro question |
| `sfx-correct-answer-chime` ([SKILL.md](../sfx-correct-answer-chime/SKILL.md)) | every green verdict, first note on the colour's first frame |
| `sfx-error-buzz-low` ([SKILL.md](../sfx-error-buzz-low/SKILL.md)) | every red verdict, on the colour's first frame |
| `text-caps-keyword-stack` ([SKILL.md](../text-caps-keyword-stack/SKILL.md)) | the verdict as big white caps on the chest: "GREEN / FLAG", "RED / FLAG"; the intro question as a two-line stack ("GREEN FLAG / OR RED FLAG?") |
| `text-single-word-captions-chest` ([SKILL.md](../text-single-word-captions-chest/SKILL.md)) | every other spoken word, small white on the chest |
| `grade-soft-warm-natural` ([SKILL.md](../grade-soft-warm-natural/SKILL.md)) | the speaker's footage (warm, bright); the wall colour is applied after the grade |

A listed technique may be used zero, one or many times, as the content warrants.

## Relationships and dependencies
- Colour, sound and the big verdict word start on the same frame (the onset of "green" / "red").
- One effect per verdict: the stack's usual click (`sfx-click-graphic-hit`) is not used, the chime / buzz takes its place.
- The colour holds through his explanation and clears on the next statement's first word, so every statement is read on the neutral wall.
- Captions never take the wall colour: white with a soft dark shadow.

## Triggers and sequencing principles
- Opening: the question "green flag or red flag?" as the hook, with the caps stack; the wall flashes green on "green flag" and red on "red flag", without sounds.
- Body: statement (neutral wall, chest captions) → ~0.4 s thinking pause → verdict (colour + sound + caps stack) → short reason, if any, under the held colour.
- Which statements to keep: only the ones with a clear verdict; long "it depends" discussions are cut. The verdict decides the colour: green flag / right = green, red flag / wrong = red.
- Ending: the last verdict; the video ends on its held colour (no outro).

## Rhythm and emphasis
- One statement + verdict every ~5–8 s.
- The thinking pause is cut down to ~0.4 s (never removed: it is the suspense).
- Explanations after a verdict stay short (one or two phrases).

## Audio-visual coordination
- Chime: first note on the frame the green starts, ~12–15 dB under the voice's loud moments, tail faded after ~1 s; its two notes drive the two ripple rings.
- Buzz: on the frame the red slams in, ~12 dB under the voice (it falls on the word), high-passed ~150 Hz; the flicker and judder follow it.
- The intro colour preview has no sound.
- Music: none (user decision in the source project). Ask if he wants one; if so, keep it low so the chime and buzz stay clear.

## Scaling to other lengths and structures
- Shorter (20–30 s): 3–4 verdicts, mix of green and red, keep the intro question.
- Longer (60–90 s): more verdicts, still one every ~5–8 s; avoid more than three of the same colour in a row if the content allows reordering.
- Other verdict pairs: right / wrong, fact / myth, do / don't, the same colours and sounds.
- Busy or dark background: the wall colour does not work well; tell the user before using this template.

## Template-specific adaptations and constraints
- Needs a plain, light wall behind the speaker and a mostly static camera.
- The chair behind him takes the colour too and must stay fully coloured (person matte without furniture).
- Green = Astroshot #01F17C; red = a clean bright red (#FF343E), not a brand colour.

## Success criteria
- Muted, every verdict is clear from the wall colour alone; with sound, the chime / buzz lands with the colour.
- Every statement is read on the neutral wall; the colour never leaks onto the person, desk or laptop; the chair stays fully coloured.

## User notes
- [User] Sounds are chosen by content: right / green flag → chime, wrong / red flag → error buzz.
- [User] He likes the chair taking the colour; it must stay fully coloured.
- [User] No music in the source project.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
