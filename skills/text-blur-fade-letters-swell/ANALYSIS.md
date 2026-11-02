# Analysis part: text-blur-fade-letters-swell

Source: `src-008` (file_0000.mp4, 19.476 s, 720x1280, 29.97 fps, with audio). Preset name shown in the video: "Blur Fade".

## Observed measurements
| Time (s) | What |
| :- | :- |
| 5.82 | first blurred dot |
| 5.94-6.50 | letters form |
| 6.065-6.40 | noise swell |
| 6.55-8.30 | line holds |
| 8.30-9.10 | exit, reverse letters, silent |

All times are from the start of the file; picture times come from frames at 30-60 fps, sound times from the 5 ms energy envelope. They describe the reference and are not quotas. [Observed]

## Why the reference works / where it came from
A tutorial video that shows seven text-animation presets one after another, each with its own sound. The user asked to keep only the motions and their sounds. The call-to-action line shown at the top of the frame for the whole video ("Comment 'Presets' ...") was not analysed as a motion (it is the creator's own overlay).

## Related but different
Compare in the library: `sfx-whoosh-main-start`, `sfx-whoosh-swell-scene-in` (soft airy swells) - the reference swell is a short noise swell; library match was not checked (see ANALYSIS.md).

## Uncertain
- The sound was extracted from the reference as `<SFX>\from-references\src-008_swell-noise-soft_01.wav`; by the user's decision (2026-11-01) it was not compared with existing library sounds.
- Pixel and degree values are estimated from 360-px-wide crops and are approximate.
- The loudness against speech is unknown (no voice in the reference).
