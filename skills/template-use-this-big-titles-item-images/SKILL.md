---
name: template-use-this-big-titles-item-images
description: "Use this" recommendation reel - a locked-off talking head with a poster-style promise headline (small row over huge condensed caps), a picture of each thing he names above his head on that topic's cut, tiny single-word chest captions, and a typed "comment the word" call to action at the end; quiet music bed, no sound effects. Library template; apply only when the user selects it.
disable-model-invocation: true
metadata:
  kind: template
  status: approved
  approved: 2026-10-24
  uses: [title-small-row-over-condensed-caps, text-single-word-captions-chest, graphic-topic-images-above-head, text-cta-typewriter-cursor]
  sources: [src-004]
---

# template-use-this-big-titles-item-images

> Library template. Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). Selecting this template authorizes the techniques listed below. Load each by reading its SKILL.md.
> Execution part only. Analysis notes (observed reference structure, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Intention and style
A calm "use this / try these" reel: one wide, static shot of the speaker with free space above his head. All the design lives in the top third: a big poster headline first, then a picture of each thing he recommends while he talks about it, then a typed comment keyword. Tiny single-word captions sit on the chest the whole time. Premium, clean, screenshot-friendly.

## Techniques and roles
| Technique | Role |
| :- | :- |
| `title-small-row-over-condensed-caps` | the promise headline from frame 1 until the first cut |
| `text-single-word-captions-chest` | one caption track for the whole video |
| `graphic-topic-images-above-head` | the picture(s) of each recommended thing, on that topic's cut |
| `text-cta-typewriter-cursor` | "comment the word X" at the end, held to the last frame |

## Relationships and dependencies
- The top third holds one thing at a time: headline → topic images → CTA; each change happens on a jump cut.
- Captions stay small on the chest so the top third stays free.

## Triggers and sequencing principles
- Hook (~0–4 s): headline + captions over the promise sentence.
- Topics (~2–3 s each): jump cut on the first word of each item → its image(s) appear on that cut.
- CTA (last ~5 s): jump cut, images gone; offer sentence in captions; lead line + typed keyword on "comment the word…"; holds to the end.

## Rhythm and emphasis
- Locked-off framing; jump cuts only at topic starts (pauses removed there). No zooms, no B-roll, no transitions, no flashy emphasis.

## Audio-visual coordination
- Sound effects: none in the reference (sound pass 2026-10-24; the reference audio stops at ~16 kHz, so very quiet effects under speech could be missed).
- Music (measured only): a quiet bed under the whole video, ~20–25 dB under the speech; louder alone in the pause before the CTA; stops on the last frame. Ask before choosing music; if the user supplies a track, `music-bed-drop-entry` sets level and ducking.

## Scaling to other lengths and structures
- 1–6 topics; one image set per topic, image count per topic follows the content (one is fine).
- No real images for a topic: show the headline-style text instead of inventing an image, or ask.
- No comment CTA in the script: end on the last topic.

## Template-specific adaptations and constraints
- Fonts: an ultra-condensed heavy sans for the headline and the CTA keyword, a tight bold sans for topic headers, from the brand when it has them.
- Colours: white type by default; one brand accent allowed (a headline word, the CTA keyword or the cursor).

## Success criteria
- Every recommended thing is shown as a real picture while it is named; the face is never covered; the CTA keyword is typed and blinking at the end.

## References
- `references/src-004_0000000-0011750_structure-1.jpg`, `references/src-004_0012000-0017133_structure-2.jpg` (4 fps contact sheets of the whole video). Per-technique evidence lives in each technique's own `references/`.
