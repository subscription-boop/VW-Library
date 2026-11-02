# layout-split-canvas-speaker-card: analysis notes

The analytic part of [SKILL.md](SKILL.md), moved here on 2026-10-29 so sessions read only the execution part first. Nothing was deleted. Open it when a decision needs these notes (reference measurements, overlaps, registration history).

## Relationships (from SKILL.md)
- Related but separate (user decision 2026-10-25): `layout-inset-card-demo` also puts video in a card on a light dotted background, but there the card shows examples of the video itself; here the card is the speaker, at the bottom, with his head breaking out, and the canvas carries the explanation.

## Observed measurements (from SKILL.md)
| Source @ time | Measurement | Value | Confidence |
| :- | :- | :- | :- |
| src-005 @ 00:12.000 | card box | x ≈ 50–675 px of 720, top ≈ 940 of 1280 (0.73 H), runs off the bottom | [Observed] |
| same | canvas colour | ≈ #E0E0E0 grey, fine dot grid + faint square grid | [Observed] |
| src-005 @ 00:58.000 | cream canvas | ≈ #F7F5EE with square grid and plus marks | [Observed] |
| whole video | share of runtime in canvas layout | ≈ 60 %, blocks 2–10 s | [Observed] |

## User notes (from SKILL.md)
- [User] Analysis priority: text animation, sound effects, graphics and motion graphics, and how the sound effects are synced with them ("روی انیمیشن متن‌ها، افکت‌های صوتی، گرافیک‌ها بیشتر دقت کن. موشن گرافی ها رو خیلی خوب بررسی کن و یاد بگیر و اینکه چطور افکت های صوتی باهاشون هماهنگن").

- [User] Registered with the whole batch from the 6/5-method analysis ("همه رو اضافه کن", 2026-10-25); kept separate from `layout-inset-card-demo`.
