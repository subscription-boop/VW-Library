---
name: graphic-lower-third-glitch-decode
description: A lower third (name + role, or show name + "Full Conversation on YouTube") glitches in as torn horizontal slices with colour fringing, a red neon vertical bar appears at its left, and the monospace letters scramble through random characters until they decode into the real text left to right (~0.25-0.3 s), then glow; it fades out slowly or leaves with the cut. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-25
  sources: [src-006]
---

# graphic-lower-third-glitch-decode

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
In the lower left of the frame a two-line lower third appears: a **monospace** uppercase title (name, show name) and a smaller monospace line under it (role, "Full Conversation on YouTube"), with a **thin vertical red neon bar** to the left of both lines.
- **In (≈ 0.5 s)**: for ~4 frames only **torn horizontal slices** of the text flicker in, offset sideways, with RGB colour fringing (digital glitch). Then the red bar is there and the text area shows **random letters that keep changing** ("URQQLH" → "SPOOJF RUQS" → "RONNIE LOKM" → "RONNIE ILHJ" → "RONNIE GJFH"); the correct letters lock in **from left to right** until the real text stands ("RONNIE FIEG") ~0.3 s later. Finally a **soft white glow** blooms around the letters.
- **Hold**: ~2.5–4.5 s.
- **Out**: a slow fade over ~0.8 s (the name), or a hard cut (the CTA).
The first one appears ~0.1 s after the cut to the guest; the second appears mid-shot while he speaks.

## Intended effect
A "data/terminal" identity card that feels high-tech and premium; the decode makes the name feel revealed rather than typed.

## Defining characteristics
- Monospace title + smaller monospace subline, white with glow, thin red neon bar on the left [Fixed]
- Glitch-in: torn horizontal slices with sideways offset and colour fringing, ~4 frames [Fixed]
- Scramble-decode: random characters cycling every frame, real letters lock in left to right, ~0.25–0.3 s [Fixed]
- Glow blooms after the decode [Observed]
- Out: slow fade (~0.8 s) or with the cut [Rule]
- Synced sound: `sfx-glitch-data-decode` for the whole entrance [Observed]

## When to use
- Triggers: introducing a guest (name + title), naming the show/source, a "full video on YouTube" call to action.
- Avoid when: the lower third would cover hands/mic in a busy area; more than 2 per minute.

## Anatomy over time
- Start: ~0.1 s after a cut to the person (name), or on a calm moment mid-shot (CTA).
- Development: slices 0–0.17 s → bar + scramble 0.17–0.45 s → decoded 0.45 s → glow 0.5–0.6 s.
- Resolution: hold, then fade ~0.8 s or hard out on a cut.

## Relationships
- Sound: `sfx-glitch-data-decode` starts with the first slices and ends as the text settles.
- Colour: the red bar matches `text-neon-serif-keyword` red.

## Adaptation
- Brand: bar in the brand accent; monospace font (or the brand's mono/tech font); text white.
- Position: lower left, x ≈ 11–13 % from the left edge, title cap height ≈ 1.6 % of the frame height; keep inside safe areas.
- Content: real names/titles only (from the user).

## Key numbers
- Scramble → "RONNIE FIEG" with left-to-right lock ≈ 0.21 s; second card in ≈ 0.46 s with the same sequence (observed; table in ANALYSIS.md).
- Other values (4 glitch frames, fade out ≈ 0.8 s, hard out with the cut) are stated above.

## Success criteria
- The glitch reads as digital interference, the decode resolves cleanly into the correct text, and the sound covers exactly the entrance.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
