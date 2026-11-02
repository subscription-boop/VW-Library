---
name: cut-multicam-podcast-bookends
description: A podcast clip cut as a two-camera conversation: it opens and closes on the wide two-shot, gives the interviewer one short shot for his question, and otherwise alternates the guest between a medium side angle and a close-up with long holds (4-8.5 s), cutting on phrase starts. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: cut
  status: approved
  approved: 2026-10-25
  sources: [src-006]
---

# cut-multicam-podcast-bookends

> Library technique (category: `cut`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (observed measurements, distinction from a related technique, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
The clip is built from a multi-camera podcast recording:
- **Opens on the wide two-shot** (both people at the table in a dark studio) for ~1.5 s with the first sentence as a typographic lockup.
- **Interviewer shot** only for his one-word question ("Why?", 0.7 s).
- **Guest close-up** for the first answer, then the guest **alternates between a medium side angle and a frontal close-up**, each held **4.5–8.5 s**.
- **Closes on the wide two-shot** for the last sentence (~4 s) with a lockup.
Cuts fall on **phrase starts** (within ~0.1–0.2 s before the first word), never mid-word; the audio runs continuously across cuts. Average shot ≈ 4 s; first 3.3 s are cut fast (1.5 / 0.7 / 1.0 s), the rest slow.

## Intended effect
Fast, punchy start, then calm long holds that let the guest's statement breathe; the wide shots frame the clip like a scene from a show.

## Defining characteristics
- Wide two-shot first and last [Fixed]
- Short interviewer shot only when he speaks [Rule]
- Guest alternates two angles (medium side ↔ close) with long holds 4–8.5 s [Observed]
- Cuts on phrase starts, continuous audio [Rule]
- Fast first 3 s (3 cuts), then slow [Observed]

## When to use
- Triggers: podcast/interview recordings with 2+ cameras (wide + angles on each person).
- Avoid when: only one camera exists (use digital reframes as "angles" only if the resolution allows).

## Relationships
- Each shot carries `zoom-slow-creep-every-shot`; the opening adds `transition-film-burn-open` + `zoom-open-settle-out`.
- Text: wide shots use `text-spaced-words-neon-lockup`, others `text-phrase-build-glow-pop`.

## Adaptation
- With a single camera: wide = full frame, "close" = digital crop ~1.4–1.6× (only with ≥4K source).
- Keep the long holds; don't add cuts just for rhythm.

## Key numbers
- Cuts at 0.125 (burn end), 1.585, 2.294, 3.253, 10.344, 14.806, 23.273, 31.490 s (observed; table in ANALYSIS.md).
- Shot lengths 1.46 / 0.71 / 0.96 / 7.09 / 4.46 / 8.47 / 8.22 / 4.05 s (observed).
- Cuts at 1.585 / 3.253 / 14.806 fall ≈ 0.1 s / ≈ 0 / ≈ 0 before the next word (observed).

## Success criteria
- The clip feels like a show excerpt: strong open/close frames, unhurried middle, no cut inside a word.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
