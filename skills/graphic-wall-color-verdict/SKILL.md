---
name: graphic-wall-color-verdict
description: The plain wall behind the speaker turns fully green on a right answer (colour floods out from behind the head with two ripples, synced to the correct-answer chime) or fully red on a wrong answer (slams in, flickers and judders with the error buzz), holds through the answer and returns to normal on the next statement. Fits green flag / red flag and right / wrong verdicts. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: graphic
  status: approved
  approved: 2026-10-25
  sources: []
  origin: designed in the user's project 2026-10-25-green-red-flag (his request, v001 → v002), not from a reference video
---

# graphic-wall-color-verdict

> Library technique (category: `graphic`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
The speaker sits in front of a plain light wall. When he gives a verdict, everything behind him turns into a solid colour, as if the wall were painted:
- **Right / green flag:** on the first note of the correct-answer chime, green floods out from behind his head in a soft-edged circle and covers the whole background in ~0.3 s. Two bright rings ripple outward, one per chime note (~0.12 s apart), and the picture makes a small 2 % zoom bump that settles in ~0.3 s.
- **Wrong / red flag:** on the error buzz, red slams in on one frame. For ~0.5 s it flickers (every other frame ~20 % lighter) and the whole picture judders sideways (~±11 px at ~12 Hz, decaying), like the buzz itself.

The colour holds while he explains the answer and fades back to the normal wall in ~4 frames when the next statement starts. The paint keeps the wall's own light and shadow, so it reads as a real coloured wall, not a flat card.

## Intended effect
The viewer knows the verdict instantly, with the sound off and before reading anything. It turns a list of statements into a game-show rhythm: neutral wall for the question, colour for the answer.

## Defining characteristics
- The whole background behind the person takes the colour; the person stays untouched and sharp-edged [Fixed]
- Green = right / green flag, red = wrong / red flag [Fixed]
- Green arrives smoothly from behind the head; red arrives at once with a flicker and a judder - the motion matches the character of the sound [Rule]
- The colour starts on the same frame as the sound hit and the spoken verdict word [Rule]
- Colour holds through the answer and clears when the next question starts [Rule]
- The wall's shading is kept (colour × the wall's own brightness) [Rule]

## When to use
- Triggers: green flag / red flag lists, right vs wrong, myth vs fact, do vs don't, quiz answers.
- Good fit: a plain, light, evenly lit wall behind the speaker; a static or nearly static camera.
- Avoid when: the background is busy (shelves, windows, posters), dark, or a real coloured set; when nothing is being judged.

## Anatomy over time
- Start: the verdict word's onset ("green", "red") = the frame of the sound hit.
- Development: green: radial flood ~0.3 s + two ripple rings over ~0.45 s + zoom bump; red: instant fill + flicker + judder, decaying over ~0.5 s.
- Resolution: steady colour until the next statement's first word, then a ~0.16 s fade back to the real wall.
- Repetition: every verdict; the neutral wall between verdicts makes each hit read again.

## Relationships
- Subject: a person matte keeps the speaker (hair, hands, arms) in front of the colour; the colour flood starts behind his head.
- Furniture: the desk / table in front of him stays its own colour. The chair behind him takes the colour with the wall [User: he likes this].
- Speech: on the verdict word.
- Cuts: the look restarts if a cut falls inside it; no cut is needed for the change.
- Sound effects: `sfx-correct-answer-chime` ([SKILL.md](../sfx-correct-answer-chime/SKILL.md)) with green (first note on the onset frame, second note drives the second ripple); `sfx-error-buzz-low` ([SKILL.md](../sfx-error-buzz-low/SKILL.md)) with red (flicker and judder follow the buzz).
- Other techniques: captions stay on top and do not take the colour; a big keyword stack ("GREEN / FLAG") pairs well. An intro question ("green flag or red flag?") may preview both colours silently.

## Adaptation
- Adaptable: the colours (brand green or another clear green; a clean bright red), flood speed (0.25–0.4 s), judder amount; a different verdict pair (e.g. green / orange) if the content needs it.
- Scaling: any aspect ratio; the flood radius covers the whole frame.
- Brand: green = the brand accent when it is green (Astroshot #01F17C). Red is a content colour, not brand (used #FF343E).

## Fixed constraints
- The person must stay fully uncoloured. Use a person matte that does not include furniture (in the source project, the light matte model caught the chair and left white patches; a heavier model fixed it).

## Key numbers
- Green flood: most of the frame covered by 0.08 s (observed; table in ANALYSIS.md).
- Ripple rings: 2, on the chime notes, each ~0.45 s (observed).
- Red flicker + judder ~0.5 s, ±11 px at ~12.5 Hz, decaying (observed).
- Colour strength on the wall ~90 % paint over the wall's own shading (observed).

## Success criteria
- Muted, a viewer can tell every verdict from the wall colour alone.
- The colour change lands on the sound hit and the verdict word (within 1 frame).
- No white or pale patches on the wall or the chair while a colour holds; the person, desk and laptop keep their real colours.

## User notes
- [User] The request: "on the right answers turn the wall behind me green with a motion synced to the sound, with the correct-answer sound; the same for wrong answers but red, with the error buzz" ("توی این ویدیو روی جواب های درست، دیوار پشت سر رو سبز رنگ کن، با یه موشن هماهنگ با صدا ... برای جواب های غلط هم همینطور با این تفاوت که دیوار قرمز بشه"), 2026-10-25.
- [User] The chair taking the colour is liked and must stay fully coloured, never partly white ("از ایده رنگی کردن صندلی خوشم اومد خیلی ام اوکیه ... درستش کن که کامل سبز بمونه"), 2026-10-25.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- How the green flood moves: `frames/..._green-flood.jpg`, `clips/..._green-chime.mp4`.
- How the red slam moves: `frames/..._red-slam.jpg`, `clips/..._red-buzz.mp4`.
- Exact implementation: `code/`.
