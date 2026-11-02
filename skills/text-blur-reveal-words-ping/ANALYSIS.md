# Analysis part: text-blur-reveal-words-ping

Source: `src-008` (file_0000.mp4, 19.476 s, 720x1280, 29.97 fps, with audio). Preset name shown in the video: "Blur Reveal Words".

## Observed measurements
| Time (s) | What |
| :- | :- |
| 12.37 | 'Blur' smear starts, ping 12.445 |
| 12.58 | 'Reveal' starts, ping 12.780 |
| 12.80 | 'Words' starts, ping 13.110 |
| 13.2-14.37 | line holds |
| 14.37-14.78 | exit, reverse words, silent |

All times are from the start of the file; picture times come from frames at 30-60 fps, sound times from the 5 ms energy envelope. They describe the reference and are not quotas. [Observed]

## Why the reference works / where it came from
A tutorial video that shows seven text-animation presets one after another, each with its own sound. The user asked to keep only the motions and their sounds. The call-to-action line shown at the top of the frame for the whole video ("Comment 'Presets' ...") was not analysed as a motion (it is the creator's own overlay).

## Related but different
Possible overlap with `text-phrase-build-blur-rise` (word-by-word grey/blur -> white): that one is a light caption build with no sound; this one is a heavy defocus reveal with a ping per word (registered as a separate skill, user decision 2026-11-01).

## Uncertain
- The sound was extracted from the reference as `<SFX>\from-references\src-008_ping-bell-word_01.wav`; by the user's decision (2026-11-01) it was not compared with existing library sounds.
- Pixel and degree values are estimated from 360-px-wide crops and are approximate.
- The loudness against speech is unknown (no voice in the reference).
