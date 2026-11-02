# Analysis part: text-blur-reveal-random-shimmer

Source: `src-008` (file_0000.mp4, 19.476 s, 720x1280, 29.97 fps, with audio). Preset name shown in the video: "Blur Reveal Random".

## Observed measurements
| Time (s) | What |
| :- | :- |
| 17.135 | shimmer attack |
| 17.17 | first blobs |
| 17.6 | line sharp |
| 17.6-19.13 | line holds |
| 19.13-19.47 | exit starts (cut by the end of the video) |

All times are from the start of the file; picture times come from frames at 30-60 fps, sound times from the 5 ms energy envelope. They describe the reference and are not quotas. [Observed]

## Why the reference works / where it came from
A tutorial video that shows seven text-animation presets one after another, each with its own sound. The user asked to keep only the motions and their sounds. The call-to-action line shown at the top of the frame for the whole video ("Comment 'Presets' ...") was not analysed as a motion (it is the creator's own overlay).

## Related but different
Compare in the library: `sfx-shimmer-tone` (steady bright tones) - this one is a noisy sweep, not steady tones; library match not checked (see ANALYSIS.md).

## Uncertain
- The sound was extracted from the reference as `<SFX>\from-references\src-008_shimmer-sweep-high_01.wav`; by the user's decision (2026-11-01) it was not compared with existing library sounds.
- Pixel and degree values are estimated from 360-px-wide crops and are approximate.
- The loudness against speech is unknown (no voice in the reference).
