---
name: template-podcast-clip-kinetic-type-red-cards
description: Podcast/interview clip edit - kinetic stacked captions in negative space, white poster cards with one huge red keyword on the core lines, a keyword scale-through with whip into the next shot, a listener reaction insert, music bed under the clip and a fade to black at the end. Library template; apply only when the user selects it.
disable-model-invocation: true
metadata:
  kind: template
  status: approved
  approved: 2026-10-22
  updated: 2026-10-29
  uses: [text-kinetic-stack-mixed-size, text-phrase-build-blur-rise, card-white-kinetic-lockup, transition-word-scale-through, transition-whip-pan, cut-listener-reaction-insert, transition-fade-to-black, sfx-keyboard-typing-captions, sfx-whoosh-soft-transition]
  sources: [src-003]
---

# template-podcast-clip-kinetic-type-red-cards

> Library template. Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). Selecting this template authorizes the techniques listed below. Load each by reading its SKILL.md.
> Execution part only. Analysis notes (history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Intention and style
Turns a reflective podcast/interview excerpt into a designed, quotable piece: moody footage, typographic caption blocks placed in empty space, and two or three white "poster" cards where the key word is huge and red.

## Techniques and roles
| Technique | Role |
| :- | :- |
| `text-kinetic-stack-mixed-size` | main caption track on close/medium shots with negative space |
| `text-phrase-build-blur-rise` | simpler phrase captions on wide or busy shots |
| `card-white-kinetic-lockup` | the core lines (≈ 1 card every 6–9 s) |
| `transition-word-scale-through` + `transition-whip-pan` | exit from the strongest card into the next shot |
| `cut-listener-reaction-insert` | on a funny or striking line, if a listener camera exists |
| `transition-fade-to-black` | end of the clip |
| `sfx-keyboard-typing-captions` | one keystroke on every word that appears in the kinetic blocks and on the cards; 3–4-key burst when a card keyword lands; phrase captions over wide shots stay silent |
| `sfx-whoosh-soft-transition` | soft low whoosh peaking on the scale-through/whip cut |

## Sequencing
- Open on the guest with stacked captions → first card on the first key line → back to footage → second card, exiting with scale-through + whip → wider shot with phrase captions, reaction insert → final card on the closing question → fade to black.

## Rhythm
- Caption block every 1–2 s; cards 1.5–2.5 s; at most one scale-through per clip.

## Audio
- Sound effects: keystrokes (`sfx-keyboard-typing-captions`) on kinetic blocks and cards, peaks ~3 dB under the voice's word peaks, keyword bursts level with the voice; one soft whoosh (`sfx-whoosh-soft-transition`) on the scale-through/whip exit. Files come from `<SFX>` via its index. [Observed, src-003 sound analysis 2026-10-24]
- Music (measured only): a steady bed under the whole clip, ~15–16 LU under the speech, continuing alone over the fade to black and stopping on the cut out. Ask before choosing music; if the user supplies a track, use `music-bed-drop-entry` for level/ducking.

## Scaling
- ≤ 15 s: 1 card, no reaction insert. No listener camera: skip the reaction insert.

## Success criteria
- Each card is the line people would quote; captions never cover faces; the ending feels finished.

## User notes
- [User] Full-screen flat white cards get a subtle paper texture, a different paper each time, never overdone; show the paper options (`tools/paper.py sheet`) for approval before the first render. (2026-10-29, «توی توضیحات تمپلیت باشه»)

## References
Index: [references/REFERENCES.md](references/REFERENCES.md) (whole-video structure sheets of src-003; this template covers 00:09.600–00:37.600). Per-technique evidence lives in each technique's own `references/`.
