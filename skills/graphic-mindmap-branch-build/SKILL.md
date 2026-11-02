---
name: graphic-mindmap-branch-build
description: A mind map built live with speech: a white outlined centre box whose label is typed letter by letter with keystroke sounds, then one black label box per spoken item pops in (small black block that stretches into a box with white text) on a thin curved connector to the centre. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-25
  sources: [src-005]
---

# graphic-mindmap-branch-build

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
In the canvas centre a **white box with a thin black outline and rounded corners** holds the main subject. Its label is **typed letter by letter** with a cursor ("dent" → "dentis" → "dentistry") and a short keystroke sound per letter group. Then, for **each item the speaker names**, a branch appears: a **small black block** pops at the branch position, **stretches horizontally** into a black rounded box and its **white label** appears inside within ~3 frames; a thin black **curved connector** runs from the box to the centre box. Branches alternate above and below the centre (top row first, then bottom row). The first time in the reference, six generic branches appear together on the word "brainstorm".

## Intended effect
Shows the method visually as the speaker thinks it through; each spoken item gets its own visible "slot", which makes a list feel organised and complete.

## Defining characteristics
- Centre: white box, thin black outline, black bold label typed with cursor [Fixed]
- Branch: black rounded box with white bold label, popped in on the item's spoken word [Fixed]
- Pop = small black block → stretches to full width → label appears (~0.1–0.15 s) [Rule]
- Thin curved connectors to the centre, drawn with the box [Rule]
- One branch per spoken item, in speech order [Rule]

## When to use
- Triggers: brainstorm, categories, sub-topics, examples of a niche, "X can be A, B, C, D…".
- Avoid when: items are sequential steps (use a numbered layout) or more than ~8 items.

## Anatomy over time
- Start: centre box fades/rises in or its label types in on the subject word.
- Development: branches pop one by one on each spoken item (~0.6–0.7 s apart in the reference).
- Resolution: the full map holds ~1 s after the last item, then hard cut.

## Relationships
- Captions: `text-caption-pill-grey` under the map.
- Sound effects: keystrokes on the typed centre label (`sfx-keyboard-typing-captions` sound family); clicks in the rhythm of the list (`sfx-click-graphic-hit`) - their exact visual trigger is uncertain (see References).
- Canvas: `layout-split-canvas-speaker-card`.

## Adaptation
- Box fonts: brand bold sans; branch boxes may use brand black/dark surface; one accent colour max.
- Scaling: centre box ≈ 35 % of frame width; branch boxes ≈ 18 % wide; map stays inside the canvas above the caption pill.

## Key numbers
- Label "dentistry" typed over 00:16.170–00:16.580 in ~4 letter groups, keystroke clicks at 16.138 / 16.264 / 16.350 / 16.432 / 16.560 (observed; table in ANALYSIS.md).
- Branch pop: block (1 frame) → stretched (2nd frame) → label (3rd frame) (observed).
- Branch appearances at 18.84 / 19.52 / 20.23 / 20.89 / 21.44 / 22.15 on "brushing, flossing, cavities, veneers, mouth guards", one per item (observed).

## Success criteria
- Every named item gets its branch exactly on its word; the final map is balanced and readable.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
