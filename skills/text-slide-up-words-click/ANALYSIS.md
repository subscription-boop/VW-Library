# Analysis part: text-slide-up-words-click

Source: `src-008` (file_0000.mp4, 19.476 s, 720x1280, 29.97 fps, with audio). Preset name shown in the video: "Slide Up Words".

## Observed measurements
| Time (s) | What |
| :- | :- |
| 0.100-0.130 | 'Slide' first visible (dim) |
| 0.350-0.370 | 'Up' first visible |
| 0.600-0.630 | 'Words' first visible |
| 0.150 / 0.380 / 0.650 | tick attacks (+55-73 dB jump in 5 ms) |
| 1.2-2.1 | line holds still |
| 2.10-2.85 | exit, reverse order, silent |

All times are from the start of the file; picture times come from frames at 30-60 fps, sound times from the 5 ms energy envelope. They describe the reference and are not quotas. [Observed]

## Why the reference works / where it came from
A tutorial video that shows seven text-animation presets one after another, each with its own sound. The user asked to keep only the motions and their sounds. The call-to-action line shown at the top of the frame for the whole video ("Comment 'Presets' ...") was not analysed as a motion (it is the creator's own overlay).

## Related but different
Related but different: `sfx-keyboard-typing-captions` is a bright keystroke (up to ~20 kHz, ~5-15 ms); this tick is a duller, longer (~40 ms) tick centred ~2.3 kHz. Same per-word sync idea.

## Uncertain
- The sound was extracted from the reference as `<SFX>\from-references\src-008_tick-dry-word_01.wav`; by the user's decision (2026-11-01) it was not compared with existing library sounds.
- Pixel and degree values are estimated from 360-px-wide crops and are approximate.
- The loudness against speech is unknown (no voice in the reference).
