---
name: graphic-ui-stat-popup
description: A real app screenshot card (dark, rounded, e.g. Instagram "Profile activity 13,860") fades in and rises a few pixels under the spoken number, proving the claim. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-21
  sources: [src-002]
---

# graphic-ui-stat-popup

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Right as the speaker says the number, a dark rounded UI card (a crop of the real app screen) appears below the serif number caption, over the lower chest. It fades from transparent to opaque over ~7 frames while rising a few pixels, then holds still until the next cut (~2.3 s). No shadow drama; it reads like a floating screenshot.

## Intended effect
Proof: the viewer sees the real stat while hearing it.

## Defining characteristics
- Real screenshot crop of the claim (not a redrawn chart). [Fixed]
- Fade + small upward drift entrance, ~0.2–0.25 s. [Rule]
- Sits under the matching number caption; leaves on the next cut. [Rule]

## When to use
- Triggers: a stated metric, result or notification the user has a real screenshot for.
- Avoid when: no real source screenshot exists (never fabricate numbers or UI).

## Relationships
- Under a tier-3 serif number from `text-caption-emphasis-tiers`; captions continue beneath/around it.

## Adaptation
- Card width ~80 % of frame, lower-middle; keep the face clear. Screenshot content always from the user.

## Key numbers
- Hold ~2.1 s after the fade-in (observed; table in ANALYSIS.md). The ~7-frame fade-in and rise are stated above.

## Success criteria
- The number on the card matches the spoken number; entrance is soft and short.

## User notes
- (none yet)

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
