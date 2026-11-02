# Analysis part: text-slide-left-words-click

Source: `src-008` (file_0000.mp4, 19.476 s, 720x1280, 29.97 fps, with audio). Preset name shown in the video: "Slide Left Words".

## Observed measurements
| Time (s) | What |
| :- | :- |
| 2.90 | 'Slide' first visible, tick 2.905 |
| 3.07 | 'Left' first visible, tick 3.075 |
| 3.23 | 'Words' first visible, tick 3.240 |
| 3.5-5.3 | line holds |
| 5.30-5.74 | exit, reverse order, silent |

All times are from the start of the file; picture times come from frames at 30-60 fps, sound times from the 5 ms energy envelope. They describe the reference and are not quotas. [Observed]

## Why the reference works / where it came from
A tutorial video that shows seven text-animation presets one after another, each with its own sound. The user asked to keep only the motions and their sounds. The call-to-action line shown at the top of the frame for the whole video ("Comment 'Presets' ...") was not analysed as a motion (it is the creator's own overlay).

## Related but different
Related but different from `text-slide-up-words-click` (vertical rise, duller tick, slower spacing).

## Uncertain
- The sound was extracted from the reference as `<SFX>\from-references\src-008_tick-bright-word_01.wav`; by the user's decision (2026-11-01) it was not compared with existing library sounds.
- Pixel and degree values are estimated from 360-px-wide crops and are approximate.
- The loudness against speech is unknown (no voice in the reference).
