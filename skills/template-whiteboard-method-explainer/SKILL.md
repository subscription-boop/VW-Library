---
name: template-whiteboard-method-explainer
description: Whiteboard-style method explainer - the speaker talks from a rounded card at the bottom while a light gridded canvas above him builds the whole method live (black word-by-word headlines, step headers on an arc, mind maps, grids that assemble, phone proof scenes with hand-drawn marks), cutting to full-screen talking head for asides; quiet music bed, soft UI clicks, whoosh swells into new scenes and rare shimmer tones on reveals. Library template; apply only when the user selects it.
disable-model-invocation: true
metadata:
  kind: template
  status: approved
  approved: 2026-10-25
  uses: [layout-split-canvas-speaker-card, text-canvas-headline-build, text-caption-pill-grey, text-single-word-captions-chest, text-caps-keyword-stack, text-caption-emphasis-tiers, text-countdown-on-canvas, graphic-step-header-arc-number, graphic-mindmap-branch-build, graphic-scatter-assemble, transition-board-rotate-reveal, graphic-phone-mockup-feed, graphic-hand-drawn-annotation, text-serif-sans-mixed-line, graphic-emoji-icon-under-caption, sfx-click-graphic-hit, sfx-whoosh-swell-scene-in, sfx-shimmer-tone, sfx-keyboard-typing-captions]
  sources: [src-005]
---

# template-whiteboard-method-explainer

> Library template. Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). Selecting this template authorizes the techniques listed below. Load each by reading its SKILL.md.
> Execution part only. Analysis notes (observed reference structure, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Intention and style
A calm, premium "here is my method" explainer that feels like a live whiteboard lesson. The speaker never leaves, but most of the time he sits in a rounded card at the bottom while the method is drawn above him in clean black type on a light gridded canvas. Everything appears exactly when it is said. Full-screen talking-head moments are for asides, opinions and the CTA.

## Techniques and roles
| Technique | Role |
| :- | :- |
| `layout-split-canvas-speaker-card` ([SKILL.md](../layout-split-canvas-speaker-card/SKILL.md)) | the base layout for every explanation block |
| `text-canvas-headline-build` ([SKILL.md](../text-canvas-headline-build/SKILL.md)) | the title of each idea, word by word |
| `text-caption-pill-grey` ([SKILL.md](../text-caption-pill-grey/SKILL.md)) | captions while the canvas is on |
| `text-single-word-captions-chest` ([SKILL.md](../text-single-word-captions-chest/SKILL.md)) | captions on full-screen talking-head shots |
| `text-caps-keyword-stack` ([SKILL.md](../text-caps-keyword-stack/SKILL.md)) | the 2–3 key concepts and the CTA keyword on full-screen shots |
| `text-caption-emphasis-tiers` ([SKILL.md](../text-caption-emphasis-tiers/SKILL.md)) | spoken counts ("6 topics", "5 formats") as a big number with its word, on full-screen shots |
| `text-countdown-on-canvas` ([SKILL.md](../text-countdown-on-canvas/SKILL.md)) | optional "3, 2, 1, go" before the first step |
| `graphic-step-header-arc-number` ([SKILL.md](../graphic-step-header-arc-number/SKILL.md)) | each numbered step |
| `graphic-mindmap-branch-build` ([SKILL.md](../graphic-mindmap-branch-build/SKILL.md)) | lists/categories said aloud |
| `graphic-scatter-assemble` ([SKILL.md](../graphic-scatter-assemble/SKILL.md)) | many items arriving (calendar, formats) and "pick N of these" |
| `transition-board-rotate-reveal` ([SKILL.md](../transition-board-rotate-reveal/SKILL.md)) | switching between two axes of a framework |
| `graphic-phone-mockup-feed` ([SKILL.md](../graphic-phone-mockup-feed/SKILL.md)) | proof scenes with the real app/screen |
| `text-serif-sans-mixed-line` ([SKILL.md](../text-serif-sans-mixed-line/SKILL.md)) | the headline on proof scenes |
| `graphic-hand-drawn-annotation` ([SKILL.md](../graphic-hand-drawn-annotation/SKILL.md)) | circling the exact proof element, connector lines |
| `graphic-emoji-icon-under-caption` ([SKILL.md](../graphic-emoji-icon-under-caption/SKILL.md)) | the product/app icon under its name on full-screen shots |
| `sfx-click-graphic-hit` ([SKILL.md](../sfx-click-graphic-hit/SKILL.md)) | soft clicks on graphic hits and caps words |
| `sfx-whoosh-swell-scene-in` ([SKILL.md](../sfx-whoosh-swell-scene-in/SKILL.md)) | entries into full-canvas scenes and big assembles |
| `sfx-shimmer-tone` ([SKILL.md](../sfx-shimmer-tone/SKILL.md)) | rare sparkle on later step headers and selections |
| `sfx-keyboard-typing-captions` ([SKILL.md](../sfx-keyboard-typing-captions/SKILL.md)) | keystrokes when a label is typed on the canvas |

A listed technique may be used zero, one or many times, as the content warrants.

## Relationships and dependencies
- Canvas and full screen alternate with hard cuts on phrase boundaries; the canvas carries the method, full screen carries opinion/aside/CTA.
- On the canvas: headline on top, graphic in the middle, grey caption pill under it, speaker card at the bottom; nothing overlaps the card.
- Proof scenes switch to the cream canvas, drop the caption pill and use the mixed serif/sans headline instead.
- One sound accent per visual hit: click OR whoosh OR shimmer, never stacked.

## Triggers and sequencing principles
- Opening (0–3 s): starts directly on the canvas; the promise is built as a headline ("Here's how to PLAN your next…") and immediately answered with a visual (calendar assembling).
- Framework intro: name the method on the canvas, show its structure (grid), turn the board to show the second dimension.
- Steps: (optional countdown) → step header → the step's diagram built item by item with speech → short full-screen aside → proof scene (phone, real numbers, hand-drawn circle).
- Ending: full-screen talking head, the concept in caps ("CONTENT SYSTEM"), "Comment <word>" in caps, then the lead magnet shown on the canvas.

## Rhythm and emphasis
- A new visual element roughly every 0.3–0.7 s while explaining; every spoken item gets its own appearance.
- Full-screen asides 2–6 s; canvas blocks 2–10 s.
- Emphasis comes from building (appearing exactly on the word), size contrast and the rare caps keyword - no zooms, no flashes, no colour pops.

## Audio-visual coordination
- Music: a calm instrumental bed under the whole video, ~18–20 dB under the voice, continuous, no audible ducking and no drops (measured only). Ask before choosing music; if the user supplies a track, `music-bed-drop-entry` sets level and ducking.
- `sfx-click-graphic-hit`: on countdown start, board spin start, each caps keyword (on its spoken onset), list/grid hits; ~17–22 dB under the voice.
- `sfx-whoosh-swell-scene-in`: starts at the cut into a full-canvas scene or a big assemble, peaks 0.1–0.3 s after, ~10–15 dB under the voice.
- `sfx-shimmer-tone`: 2–3 times per video on a later step header and on "pick N" selections, ~20 dB under the voice.
- `sfx-keyboard-typing-captions` sound family: a short keystroke burst while a canvas label is typed letter by letter.

## Scaling to other lengths and structures
- Shorter (30–45 s): one framework scene, 2 steps, one proof scene, CTA.
- Longer (90 s+): keep the alternation; add a proof scene per step; do not add more sound accents per minute.
- No product/app to show: replace proof scenes with diagrams; never fake screens or numbers.

## Template-specific adaptations and constraints
- All graphics in near-black on the light canvas, one brand accent at most (numeral, dot, circle).
- Brand fonts: heavy sans for headlines/numbers, an italic serif for the mixed lines.
- Spoken counts use `text-caption-emphasis-tiers` here as a big bold number with its small word beside it (the user chose the existing skill over a separate one).

## Success criteria
- A viewer on mute can follow the whole method from the canvas alone.
- Every graphic element appears on the word that names it; sound accents land within ~1 frame of their visual hit.

## User notes
- [User] The "number + small word" callout is covered by the existing `text-caption-emphasis-tiers` ("همون اسکیل قبلی کافیه").

## References
Index: [references/REFERENCES.md](references/REFERENCES.md) (each example annotated with which technique(s) appear).
