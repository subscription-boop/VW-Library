---
name: graphic-flicker-icon
description: A thin red outline icon above the caption that flickers on and off like a faulty sign, then settles semi-visible, to illustrate a problem word (here "bad audio" with a muted-speaker icon). Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-20
  sources: [src-001]
---

# graphic-flicker-icon

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
A simple line icon (a speaker with an "x") in red, thin stroke, partly transparent, appears just above the caption word in the top third. It does not fade in smoothly: it blinks irregularly between off, faint and stronger for about a second, like a broken neon sign, then stays on at medium strength until the end of the video. The captions keep running underneath it.

## Intended effect
Adds a warning signal to a negative point without blocking the speaker; the flicker itself suggests something broken.

## Defining characteristics
- Outline icon, red, semi-transparent, small (~20 % of frame width). [Rule]
- Irregular flicker entrance, then hold. [Fixed]
- Placed right above the caption, linked to the problem word. [Rule]

## When to use
- Triggers: a negative or "don't" point that has a clear icon (muted audio, no signal, warning, broken).
- Avoid when: the point is positive; more than one icon at a time.

## Anatomy over time
- Start: on the problem word ("bad audio").
- Development: ~1–1.4 s of irregular on/off flicker.
- Resolution: holds semi-visible until the next section or the end.
- Repetition: once in the reference.

## Relationships
- Speech: starts on the problem word.
- Other techniques: stacks above `text-single-word-captions`.

## Adaptation
- Adaptable: the icon, colour (warning colour), position.
- Brand: icon stroke style may follow the brand's icon set; keep a warning colour.

## Key numbers
- Icon position ~25–33 % of frame height, centred (observed, approximate; table in ANALYSIS.md). Flicker period before settling ~1.4 s is stated above.

## Success criteria
- Flicker reads as irregular/broken, not as a smooth pulse.
- Icon meaning is obvious without explanation.

## User notes
- (none yet)

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Flicker pattern: `flicker` sequence. With audio: `flicker-icon` clip.
