# Analysis part: text-flicker-in-letters-ticks

Source: `src-008` (file_0000.mp4, 19.476 s, 720x1280, 29.97 fps, with audio). Preset name shown in the video: "Flicker in".

## Observed measurements
| Time (s) | What |
| :- | :- |
| 14.95 | first letter on |
| 15.075-15.380 | six ticks |
| 15.35 | line solid |
| 15.4-16.93 | line holds |
| 16.93-17.12 | exit flicker, silent |

All times are from the start of the file; picture times come from frames at 30-60 fps, sound times from the 5 ms energy envelope. They describe the reference and are not quotas. [Observed]

## Why the reference works / where it came from
A tutorial video that shows seven text-animation presets one after another, each with its own sound. The user asked to keep only the motions and their sounds. The call-to-action line shown at the top of the frame for the whole video ("Comment 'Presets' ...") was not analysed as a motion (it is the creator's own overlay).

## Related but different
Possible overlap with `text-flicker-in` (key word enters with an irregular flicker, ~7 frames, then holds): that one is a single key word, on/off of the whole word, no sound; this one flickers letter by letter for ~0.4 s with a tick burst (registered as a separate skill, user decision 2026-11-01).

## Uncertain
- The sound was extracted from the reference as `<SFX>\from-references\src-008_ticks-burst-electric_01.wav`; by the user's decision (2026-11-01) it was not compared with existing library sounds.
- Pixel and degree values are estimated from 360-px-wide crops and are approximate.
- The loudness against speech is unknown (no voice in the reference).
