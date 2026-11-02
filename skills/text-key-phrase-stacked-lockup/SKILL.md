---
name: text-key-phrase-stacked-lockup
description: The key phrase becomes a big white stacked lockup (a smaller first line, a huge heavy second line), built word by word on speech with a grey-blur-to-white entrance and a small tilt/scale settle; it often sits behind the speaker's head, a line can swap to the next word, and it fades out to grey. Fits hooks, promises and punchlines. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: text
  status: approved
  approved: 2026-10-28
  sources: [src-007]
---

# text-key-phrase-stacked-lockup

> Library technique (category: `text`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, overlaps, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
When the speaker says a key phrase, its words appear as a designed typographic block instead of the normal small caption:
- **Two or three stacked lines**, tight leading so the lines nearly touch or overlap: a smaller line ("Treasure", "NEXT", "BIGGER", "PEOPLE", "business") over a **huge heavy line** ("Coast", "LEVEL", "IMPACT", "BUY THE / FEELING", "owners…"). The huge line is ~2–2.5x the cap height of the small line.
- Very heavy, wide geometric sans, white, with a soft shadow. Mostly uppercase; the opening hook used title case ("Treasure Coast / business owners…").
- **Word by word on speech.** Each word enters from a grey, blurred, semi-transparent state to solid white in ~5–7 frames; big words also settle from a slightly larger or tilted (a few degrees) position into place.
- **Depth:** when the block overlaps the head, the speaker is cut out and stands **in front of** the text (his head covers part of "Coast", "BUY THE", "SEND").
- **Line swap:** a later word can replace the big line while the small line stays ("BIGGER IMPACT" → "BIGGER BRAND"); the new word blurs in over the old one.
- While a lockup word is spoken, the normal chest caption is hidden; for the other words of the sentence the small chest caption keeps running under the block.
- **Exit:** the whole block fades to grey/transparent in ~4–6 frames, or leaves with the cut.

## Intended effect
Turns the one sentence the viewer must remember into a poster inside the shot. The depth (text behind the head) makes it feel filmed, not typed on top, and premium.

## Defining characteristics
- Stacked lines with strong size contrast (small line + huge heavy line), tight leading. [Fixed]
- White, very heavy wide sans, soft shadow. [Rule] (typeface follows the brand)
- Word-by-word build on the spoken words; grey/blur/transparent → white in ~5–7 frames. [Fixed]
- Big words settle from a slight tilt or scale into place. [Rule]
- Behind the speaker whenever it overlaps the head/body (subject matte). [Rule]
- Fade to grey/transparent exit or out on the cut. [Rule]

## When to use
- Triggers: the hook/addressee of the opening ("Treasure Coast business owners…"), a promise ("bigger impact, bigger brand"), a punchline/insight ("people buy the feeling"), the closing CTA ("send us a message").
- Good fit: shots with free space above or around the speaker (wide shots, walk-and-talks).
- Avoid when: every sentence would qualify (in the reference: 5 lockups in 57 s), or no clean subject matte is possible and the block would have to cover the face.

## Anatomy over time
- Start: first word of the phrase, on its spoken onset.
- Development: one word per spoken word (~0.15–0.5 s apart); line swaps on the replacing word.
- Resolution: holds ~0.5–1 s after the last word, then fades to grey (~0.15–0.2 s) while small captions continue; or leaves on the cut.
- Repetition: ~every 5–15 s at most; always on a new idea.

## Relationships
- Subject: placed above the head or across the upper body; never covers the face (the head stays in front).
- Speech: word-level sync.
- Cuts: may start right after a cut or a reveal (`zoom-cut-in-tight-pull-reveal`), may end on a cut.
- Sound effects: none observed.
- Other techniques: chest captions (`text-single-word-captions-chest` ([SKILL.md](../text-single-word-captions-chest/SKILL.md))) pause for the lockup words; `zoom-push-hold-release` ([SKILL.md](../zoom-push-hold-release/SKILL.md)) can push in on the lockup and the text scales with the zoom.

## Adaptation
- Adaptable: number of lines (2–3), alignment (left in medium shots, centred in wide shots), which word is huge (the content word, not "the"/"a").
- Scaling: huge line ~60–90 % of frame width; small line ~40–45 % of the huge line's height.
- Brand: typeface = brand's heaviest sans; colour white by default; the brand accent colour may take one word if the brand asks for it.

## Key numbers
- Opening hook: "Treasure" then "Coast" blur in from 00:00.000 ("Coast" partly behind the head at 00:00.400), "business" at 00:00.370, "owners…" at 00:00.630 (observed; table in ANALYSIS.md).
- "NEXT" at 00:04.537, "LEVEL" at 00:04.770 (tilted a few degrees, ghosted, settles in ~5 frames) (observed; table in ANALYSIS.md).
- "BIGGER" at 00:06.540, "IMPACT" at 00:06.810 (enters slightly larger and rotated, settles by ~00:06.94) (observed; table in ANALYSIS.md).
- "IMPACT" → "BRAND" swap at 00:07.75–00:08.00; exit at 00:08.81–00:08.98, caption "Having" continues below (observed; table in ANALYSIS.md).
- "PEOPLE" / "BUY THE" / "FEELING" at 00:37.42–00:38.15 (three lines, "BUY THE" partly behind the head); exit grey fade ~5 frames at 00:39.04–00:39.20 (observed; table in ANALYSIS.md).
- "SEND US A MESSAGE" at 00:54.85–00:55.36 behind the walking speaker, then kept on the black end card (observed; table in ANALYSIS.md).
- Wide-shot layout at 00:08.30: huge line ≈ 0.88 W wide, block y ≈ 0.12–0.22 H (observed; table in ANALYSIS.md).

These describe the references. They are not quotas or required values.

## Success criteria
- Reads as one designed block with a clear small/huge contrast.
- Each word appears with its spoken word, from grey blur to white.
- When it overlaps the speaker, the head is in front of the text; the face is never covered.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Entrance speed: `sequences/..._word-blur-in.jpg`; tilt/scale settle: `sequences/..._big-word-tilt-settle.jpg`.
- Depth (behind the head): `frames/..._treasure-coast.jpg`, `frames/..._people-buy-the-feeling.jpg`, `frames/..._cta-behind-head.jpg`.
- Line swap: `sequences/..._second-line-swap.jpg`. Exit: `sequences/..._exit-fade.jpg`.
