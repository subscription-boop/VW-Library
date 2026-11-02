---
name: sfx-click-graphic-hit
description: A soft, dry mouse-click type tick (short, often a double click ~30-80 ms apart) on graphic hits: the first countdown number, the board spin, each big uppercase concept word, list beats and grid builds; quiet, well under the voice. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: sfx
  status: approved
  approved: 2026-10-25
  sources: [src-005]
---

# sfx-click-graphic-hit

> Library technique (category: `sfx`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Short, dry, bright ticks like a mouse button, sometimes as a **double click** (a second softer tick 30–80 ms after the first). They sit on visual "hits": the first countdown number, the start of the board spin, each big uppercase concept word on the full-screen shots, the formats grid build, the competitor counter scene, and in the rhythm of the spoken list during the mind map.

## Intended effect
Gives graphic moments a tactile "UI" feel - like the graphics are being clicked into place - without drawing attention away from the voice.

## Defining characteristics
- Very short transient (~8 ms main click), bright, dry, no reverb [Fixed]
- Often doubled (press/release feel) [Observed]
- Quiet: ~17–22 dB under the loud voice moments [Rule]
- Placed on the frame the graphic hits or on the spoken onset of the word it marks [Rule]

## Sound
- Type and character: mouse/UI click, ~5–10 ms per tick, double 30–80 ms apart, bright (energy up to the top of the band)
- Library file(s): `<SFX>\1 Click Mouse.wav` (single click, Close), `<SFX>\Mouse Clicks.wav` (pick single clicks, Close)
- Extracted from the reference: none (the library clicks are close; reference clicks sit under speech and music)

## Sync rule
- Follows: the visual hit (word pop, number appear, spin start); within ~1–2 frames. For caps words it lands on the spoken onset, ≈ 2 frames after the word appears.
- Repetition: once per hit; not on every caption word. Variation: alternate between 2–3 click samples.

## Level
- Peaks ≈ 17–22 dB under the loud voice (10 ms RMS), roughly at the music-bed level; never masks a consonant.

## When to use
- Triggers: graphic pops and emphasis words in an explainer; countdown; rigid board moves.
- Avoid when: the moment already has a whoosh or shimmer (do not stack), or on every word (it would become typing).

## Relationships
- Visual techniques: `text-caps-keyword-stack`, `text-countdown-on-canvas`, `transition-board-rotate-reveal`, `graphic-scatter-assemble`, `graphic-mindmap-branch-build`.

## Key numbers
- All values are stated above (tick ~5–10 ms, double 30–80 ms apart, 17–22 dB under the voice, within ~1–2 frames). The per-moment table is in ANALYSIS.md.

## Success criteria
- Each click is felt but barely noticed; it lines up with its visual hit within ~1 frame.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
