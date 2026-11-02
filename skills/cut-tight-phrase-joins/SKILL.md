---
name: cut-tight-phrase-joins
description: Rough-cut pacing for talking head - every pause and breath between phrases removed down to 1-3 frames, picture cuts placed inside that tiny gap so the next word starts 0-2 frames after the cut, and a pause kept only before a stressed or final word. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: cut
  status: approved
  approved: 2026-10-21
  sources: [src-002]
---

# cut-tight-phrase-joins

> Library technique (category: `cut`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (observed measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
The voice runs almost without breathing room. Between phrases there is only a 30–110 ms gap (1–3 frames at 30 fps). Every picture cut lands inside one of these gaps, at a clause or sentence boundary, and the next word starts 0–2 frames after the cut. The video opens on the first word (speech from frame 1) and ends ~0.3 s after the last word. The only longer silences (~0.2–0.25 s) sit right before a word the speaker wants to land.

## Intended effect
Dense, fast-feeling delivery at a normal speaking speed: no dead air, so attention never drops, while the few kept pauses make the key words hit.

## Defining characteristics
- Gaps between phrases: 30–110 ms; no breath left audible between sentences. [Observed]
- Picture cut placed in the gap, next word starts within 0–2 frames after it. [Observed]
- Cuts at clause/sentence boundaries (after "video.", "3 steps.", "Step 1", "tips.", "next.", "simple,", "comparison,", "works,"). [Observed]
- Kept pause only for emphasis: before the stressed repeat ("over… over-edit") and before the final word ("…copy | blindly."). [Observed]
- Speech starts at frame 1; tail after the last word ≈ 0.3 s. [Observed]
- Tightness comes from removing gaps. Whether the voice was also sped up was not tested. [Uncertain]

## When to use
- Triggers: talking-head videos at normal speaking speed where the user wants a fast, dense feel.
- Avoid when: the user wants a calm, breathing edit, or the speaker's pauses carry emotion (story moments).

## Relationships
- Works with `cut-rhythm-phrase-shots` (where picture changes happen) and `cut-section-header-beat`.
- The pauses kept for emphasis are where emphasis visuals sit (for example `text-flicker-in` on the final word, tier-3 serif in `text-caption-emphasis-tiers`).

## Adaptation
- Cut on the end of the last word's sound, leave 1–3 frames, start the next phrase. Add short audio fades (a few ms) at every join to avoid clicks.
- Keep at most one or two emphasis pauses per video, ~0.2–0.3 s each.
- If a breath or mouth noise survives a join, trim it rather than leaving a longer gap.

## Key numbers
- Speech density ~69 words in 25.95 s of speech ≈ 2.7 words/s (~160 wpm); word count from captions (observed; table in ANALYSIS.md).
- Gap around the cut 40–110 ms at cuts 2.467, 4.167, 4.767, 7.2, 11.667, 15.067, 17.667, 18.367, 19.867, 22.267, 24.5 (observed).
- Next word starts 0–10 ms after the cut at 11.067, 13.4, 20.4, 23.167 (cut on the word onset) (observed).
- Kept pauses ~0.23 s: before stressed "over-edit" at 12.17–12.40, before "blindly." at 25.30–25.53 (observed).
- First word at 0.04 s; last word ends 25.99 s; video ends 26.27 s (observed).
- Where the audio joins sit under B-roll is not detectable from the level trace [Uncertain].

## Success criteria
- No audible breath or dead air between phrases; no clipped first or last syllables; no clicks.
- The one or two kept pauses feel intentional.

## User notes
- None yet.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md): voice-level maps with every cut, close-ups of gaps and kept pauses, clips.
