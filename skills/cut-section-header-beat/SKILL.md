---
name: cut-section-header-beat
description: The spoken section header ("Step 1", "Step 2"...) gets its own very short shot of ~0.6-0.7 s that starts on a cut and ends with another cut right after the header words, before the section's content begins. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: cut
  status: approved
  approved: 2026-10-21
  sources: [src-002]
---

# cut-section-header-beat

> Library technique (category: `cut`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (observed measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Each "Step N" is spoken in its own isolated mini-shot. A cut brings us in, the speaker says only "Step N" (~0.5 s), and a second cut follows immediately: a same-framing jump cut (steps 1 and 2) or a cut to B-roll (step 3). The content of the step starts on that second cut.

## Intended effect
The header becomes a clear beat, like a chapter tick: the viewer always knows where they are in the list, and the structure feels deliberate.

## Defining characteristics
- Header shot length 0.60–0.70 s; header speech ≈ 0.5 s. [Observed]
- Cut in on the header's first word; cut out 1–3 frames after the header's last sound. [Observed]
- The shot contains nothing but the header words. [Observed]
- The second cut goes to the same talking head (jump cut) or to B-roll; never a card. [Observed]

## When to use
- Triggers: numbered lists, steps, tips, "first / second / third" structures.
- Avoid when: the header is inside a sentence ("the first step is to…") and cannot be isolated without breaking the line.

## Relationships
- The serif label of `text-step-label-serif` sits on this beat.
- Uses `cut-tight-phrase-joins` timing; part of the `cut-rhythm-phrase-shots` rhythm.
- `zoom-cut-ease-out` can start on the cut into the header (step 2 in the reference).

## Adaptation
- If the speaker said the header and content in one breath, still cut after the header words (the cut acts as the beat).
- If the speaker paused after the header, remove the pause; keep the beat at 0.5–0.8 s.

## Key numbers
- Header shots 0.60 s ("Step 1", 04.167–04.767), 0.60 s ("Step 2", 11.067–11.667), 0.70 s ("Step 3", 17.667–18.367); speech inside them 4.20–4.71, 11.07–11.63, 17.69–18.28 s (observed; table in ANALYSIS.md).

## Success criteria
- Each header reads as its own beat; no pause before the content starts.

## User notes
- None yet.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md): the three header beats as clips, voice-level close-up of step 1.
