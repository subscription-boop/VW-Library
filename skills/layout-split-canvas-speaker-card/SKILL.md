---
name: layout-split-canvas-speaker-card
description: The frame becomes a light "whiteboard" canvas (grey with a fine dot/line grid, or cream with a plus-sign grid) for motion graphics in the upper ~70 %, while the speaker keeps talking inside a rounded video card at the bottom whose top edge his head breaks out of; hard cuts switch between this layout and the full-screen talking head. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: layout
  status: approved
  approved: 2026-10-25
  sources: [src-005]
---

# layout-split-canvas-speaker-card

> Library technique (category: `layout`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Most of the video is not the speaker's frame but a clean, light **canvas** that fills the screen. All graphics (titles, grids, diagrams, mock-ups, captions) live on it. The speaker's own footage sits in a **rounded rectangle card** across the bottom (~87 % of the width, top edge at ~73 % of the frame height, running off the bottom edge), and his head and cap **overlap the card's top edge** as if he leans out of it. The video alternates, with hard cuts, between this split layout and the normal full-screen talking head (with small chest captions).

Two canvas styles appear:
- Grey canvas (#E0E0E0) with a very fine dot grid and a faint square grid that fades out toward the edges (sections inside the main explanation).
- Cream canvas (#F7F5EE) with a thin square grid and small plus marks at the crossings (product/proof sections: phone mock-ups, tables, calendar, lead magnet). Here the speaker card may also disappear completely for a full-canvas scene.

## Intended effect
Turns the talking head into a live whiteboard lesson: the viewer keeps the speaker's face and voice, but the eye is pulled to the explanation that is built while he talks. Cutting back to full screen marks asides, opinions and transitions.

## Defining characteristics
- Light, flat, gridded canvas behind all graphics; no footage behind the graphics [Fixed]
- Speaker in a rounded card at the bottom, about a quarter of the frame tall, slightly inset from the sides [Fixed]
- The speaker's head and cap break out above the card's top edge (subject cut out over the card border) [Fixed]
- Hard cuts in and out of the layout; no transitions between layout and full screen [Rule]
- Graphics never cover the speaker card [Rule]

## When to use
- Triggers: explaining a method, steps, a framework, a diagram, a tool, numbers, a schedule - anything that can be drawn.
- Good fit: educational/explainer talking heads, 45–90 s.
- Avoid when: the moment is personal or emotional (stay full screen), or there is nothing to draw.

## Anatomy over time
- Start: hard cut into the layout (or the video opens in it); canvas is empty or the first graphic starts building on frame 1.
- Development: graphics build in sync with speech; the speaker card stays still.
- Resolution: hard cut to full-screen talking head for a comment, then back to the canvas for the next idea.
- Repetition: in the reference the layout covers ~60 % of the runtime, in blocks of 2–10 s.

## Relationships
- Captions: on the canvas, captions move into a grey pill between the graphic and the card (`text-caption-pill-grey`); on full-screen shots they are small chest captions.
- Graphics built on the canvas: `text-canvas-headline-build`, `graphic-mindmap-branch-build`, `graphic-scatter-assemble`, `graphic-step-header-arc-number`, `transition-board-rotate-reveal`, `graphic-phone-mockup-feed`, `graphic-hand-drawn-annotation`.
- Sound effects: none tied to the layout itself; switching into a new full-canvas scene may get `sfx-whoosh-swell-scene-in`.

## Adaptation
- Canvas colour: light neutral of the brand (or the reference grey/cream when the brand has none); grid lines a few percent darker than the canvas.
- Card radius ~3 % of the frame width; card height 25–30 % of the frame; keep the head-break-out (needs a person matte or rotoscope of the head).
- Brand: graphics on the canvas use brand fonts and one brand accent.

## Key numbers
- Card box x ≈ 50–675 px of 720, top ≈ 940 of 1280 (0.73 H), runs off the bottom (observed; table in ANALYSIS.md).
- Canvas colours and runtime share are stated above.

## Success criteria
- The canvas reads as one clean board; graphics never overlap the speaker card.
- The head clearly overlaps the card edge without a visible matte edge.
- Every switch between layout and full screen is a hard cut on a phrase boundary.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
