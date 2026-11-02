---
name: graphic-topic-images-above-head
description: What the speaker is talking about appears as picture(s) above his head - one or more real images of the named thing (cover, app, product, screenshot, place), optionally under a short tight-kerned header; they blur in and rise slightly on the cut that starts the topic and are swapped on the next topic's cut. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-24
  sources: [src-004]
---

# graphic-topic-images-above-head

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
While the speaker talks about something, that thing is shown as a picture above his head, in the empty top third of the frame. In the reference each topic is a category of songs: on the cut that starts the topic, a short header ("“Storytelling” Content", category word in quotes) appears with a row of square album covers under it, each with a tiny title. The group enters blurred and slightly low, then sharpens and rises a few percent into place in ~0.2–0.25 s, stays for the whole topic while the small chest captions run below, and is replaced on the next topic's cut. At the end of the list it disappears on a cut.

## Intended effect
The viewer sees what is being talked about instead of only hearing it: the topic becomes concrete, memorable and screenshot-able.

## Defining characteristics
- Real image(s) of the thing being talked about, placed above the head in the top third. [Fixed]
- How many images follows the content: one image is enough; several sit in one row of equal tiles. Never a fixed count. [User]
- Optional short header line above the image(s) (category/topic, tight letter spacing, the key word may be in quotes) and tiny titles under each image. [Observed]
- Enters on the topic's cut: blur + slight rise → sharp, ~0.2–0.25 s. [Rule]
- Swaps or leaves only on cuts; no exit animation. [Rule]
- Never over the face. [Rule]

## When to use
- Triggers: the speaker names or describes something that has a real picture (a song, tool, app, product, book, place, person's work, a screenshot of a result).
- Good fit: list videos, recommendations, "use this", comparisons; locked-off talking head with space above the head.
- Avoid when: there is no real image (never invent covers, logos or titles); the top third is already used by a title.

## Anatomy over time
- Start: the cut that starts the topic (cut frame clean; the image group appears from the next frame).
- Development: blur → sharp + small rise over ~6–7 frames.
- Resolution: holds until the next topic's cut.
- Repetition: once per topic; keep the same layout for every topic in a video.

## Relationships
- Cuts: lives on the jump cuts at topic starts.
- Captions: `text-single-word-captions-chest` continues below.
- Titles: comes after the opening title (`title-small-row-over-condensed-caps`) has left; they never share the top third.
- Sound effects: none observed.

## Adaptation
- Images: real images from the user or official sources, with their real names.
- One image: centred, larger (≈ 0.35–0.45 W). Several: one row, equal squares (≈ 0.18 W each for three).
- Brand: header font and colour from the brand; images may get the brand's corner radius.

## Key numbers
- First entry after a jump cut: blur → sharp in ~4–5 frames (observed; table in ANALYSIS.md).
- Swap to the next topic: new set rises ≈3 % H, sharp by ≈00:06.106 (observed).
- Layout (three images): header y ≈ 0.11 H; tiles y ≈ 0.16–0.26 H; titles ≈ 0.012 H (observed). Tile width ≈ 0.18 W is stated above.

## Success criteria
- The picture matches what is being said at that moment and appears exactly on the topic's cut.
- Readable within ~0.3 s; the face is never covered.

## User notes
- [User] Don't register it as "three images": the style is that what he is talking about appears as a picture above his head; it may be just one. ("لزوما به عنوان اینکه 3 تا تصویره ثبت نکن. این استایل رو به این شکل که چیزی که داره میگه رو به صورت تصویر بالا سرش داشته باشیم. شاید یدونه باشه")

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Entry/swap motion: `sequences/src-004_0005873-0006406_swap/`, `clips/src-004_0003400-0006600_header-in-and-swap.mp4`.
- Layout of each topic: `frames/`.
