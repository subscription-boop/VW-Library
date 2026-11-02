# References: graphic-wall-color-verdict

No reference-video media: this technique was designed in the user's own project 2026-10-25-green-red-flag (v002, approved by him), not taken from an analysed reference. The frames and clips below come from that delivered version.

## Quick guide
- Green motion and timing → `frames/..._green-flood.jpg` (time from the chime hit on each frame) and `clips/..._green-chime.mp4` (with sound)
- Red motion and timing → `frames/..._red-slam.jpg` and `clips/..._red-buzz.mp4` (with sound)
- Exact behaviour → `code/`

## Items
| File | Source @ time | Shows | Notes |
| :- | :- | :- | :- |
| frames/2026-10-25-green-red-flag-v002_0005200-0006160_green-flood.jpg | project v002 @ 00:05.200–00:06.160 | green flood from behind the head, ripple rings, hold | −0.04 to +0.92 s around the chime |
| frames/2026-10-25-green-red-flag-v002_0015560-0017400_red-slam.jpg | project v002 @ 00:15.560–00:17.400 | red slam, flicker, hold, fade on the next statement | −0.04 to +1.80 s around the buzz |
| clips/2026-10-25-green-red-flag-v002_0004600-0006600_green-chime.mp4 | project v002 @ 00:04.600–00:06.600 | green + `sfx-correct-answer-chime` | audio included, 540x960 |
| clips/2026-10-25-green-red-flag-v002_0014900-0017500_red-buzz.mp4 | project v002 @ 00:14.900–00:17.500 | red + `sfx-error-buzz-low` | audio included, 540x960 |
| code/render_reference.py | - | `wall_state(t)` (motion of each look), `wall_mask()` (desk line + dark objects out), paint with the wall's shading, judder/zoom | events come from events.json (t0, t1, colour) |
| code/track_reference.py | - | head position (flood origin) and per-shot desk-edge line | |
| code/matte_reference.py | - | person matte with Robust Video Matting (use the ResNet50 model; the MobileNetV3 model caught parts of the chair) | |

## Uncertainty
- Only tested on one setup: a light wall, white desk, white chair, static camera.
