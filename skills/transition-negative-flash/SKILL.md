---
name: transition-negative-flash
description: A 2-3 frame negative-style flash on an accent - dark tones flip to bright warm colours and blues turn pale pink (solarize/invert look), peak to near white, then the picture reverts through a short magenta/teal cast. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: transition
  status: approved
  approved: 2026-10-22
  sources: [src-003]
---

# transition-negative-flash

> Library technique (category: `transition`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Right after the payoff word, the picture flips into a negative-like look for about two frames: black hair turns bright orange-brown, the blue shirt becomes pale pink, the grey background goes warm cream. It then blows out to almost white for two frames and comes back over two frames with a magenta tint on the shirt and a teal/green cast on the background before normal colour returns.

## Intended effect
A jolt of energy that feels like a camera/film glitch and resets attention, often hiding a jump cut.

## Defining characteristics
- Tonal flip: darks become bright and warm, blues pale/pink (negative/solarize look). [Fixed]
- Very short: ≈ 2 frames negative + ≈ 2 frames near-white + ≈ 2 frames tinted revert (≈ 0.2 s at 30 fps). [Rule]
- Reverts through complementary tints (magenta/teal) rather than a clean cut. [Rule]

## When to use
- Triggers: right after a payoff/goal word; on a jump cut that needs an accent.
- Avoid when: used more than once or twice per video; serious or emotional content.

## Relationships
- In the reference it happens together with `transition-light-leak-flash` (warm leak + scribbles) on the same cut; each can be used alone.
- Follows `text-neon-glow-word` in the reference.

## Adaptation
- Can be built with an invert/solarize/curves effect keyed over 2 frames; keep captions readable or let them flash with the picture.

## Key numbers
- Before: shirt RGB ≈ (23,36,119), hair ≈ (21,18,19), background ≈ (161,152,143) (observed; table in ANALYSIS.md).
- Negative frame: shirt ≈ (253,184,180), hair ≈ (164,93,42), background ≈ (246,215,162) (observed).
- Peak: near white (≈ 253) (observed).
- Revert: shirt magenta ≈ (182,116,153) → (88,70,116), background teal-grey; normal again after that (observed).

## Success criteria
- Reads as one quick deliberate flash, not as a broken file.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md).
