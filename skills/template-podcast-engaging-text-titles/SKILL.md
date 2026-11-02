---
name: template-podcast-engaging-text-titles
description: Podcast/interview clip with engaging text and titles - a film-burn cold open with a typographic lockup, long slowly creeping shots, phrase captions whose key words switch to a big italic serif in a strong main colour with a neon glow (always), glitch-decode lower thirds for the name and the full-conversation CTA, a quiet music bed and a closing lockup. Works on dark and bright footage. Library template; apply only when the user selects it.
disable-model-invocation: true
metadata:
  kind: template
  status: approved
  approved: 2026-10-25
  uses: [cut-multicam-podcast-bookends, transition-film-burn-open, sfx-burn-hit-open, zoom-open-settle-out, zoom-slow-creep-every-shot, text-phrase-build-glow-pop, text-neon-serif-keyword, text-spaced-words-neon-lockup, graphic-lower-third-glitch-decode, sfx-glitch-data-decode, grade-cool-lowkey-spotlight]
  sources: [src-006]
---

# template-podcast-engaging-text-titles

> Library template. Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). Selecting this template authorizes the techniques listed below. Load each by reading its SKILL.md.
> Execution part only. Analysis notes (observed reference structure, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Intention and style
A podcast/interview excerpt presented like a scene from a premium show. Calm and confident: few cuts, no zoom accents, no flashy transitions after the opening. The emphasis comes from the typography: one key word per sentence in a big italic serif in the video's main colour with a neon glow, typographic lockups at the start and the end, and tech-style lower thirds.

## Techniques and roles
| Technique | Role |
| :- | :- |
| `cut-multicam-podcast-bookends` ([SKILL.md](../cut-multicam-podcast-bookends/SKILL.md)) | structure: wide open, short interviewer question, guest angles held 4–8.5 s, wide close |
| `transition-film-burn-open` ([SKILL.md](../transition-film-burn-open/SKILL.md)) | 3-frame film burn on frame 0 |
| `sfx-burn-hit-open` ([SKILL.md](../sfx-burn-hit-open/SKILL.md)) | the hit under the burn |
| `zoom-open-settle-out` ([SKILL.md](../zoom-open-settle-out/SKILL.md)) | the opening wide lands tight and settles out |
| `zoom-slow-creep-every-shot` ([SKILL.md](../zoom-slow-creep-every-shot/SKILL.md)) | every other shot creeps in ~2 %/s |
| `text-phrase-build-glow-pop` ([SKILL.md](../text-phrase-build-glow-pop/SKILL.md)) | captions on all guest/interviewer shots |
| `text-neon-serif-keyword` ([SKILL.md](../text-neon-serif-keyword/SKILL.md)) | the key word(s) of a sentence, inline or big; the interviewer's one-word question |
| `text-spaced-words-neon-lockup` ([SKILL.md](../text-spaced-words-neon-lockup/SKILL.md)) | first and last sentences on the wide shots (and one big-word moment) |
| `graphic-lower-third-glitch-decode` ([SKILL.md](../graphic-lower-third-glitch-decode/SKILL.md)) | guest name + title after the first cut to him; "full conversation" CTA near the end |
| `sfx-glitch-data-decode` ([SKILL.md](../sfx-glitch-data-decode/SKILL.md)) | sound of each lower-third entrance |
| `grade-cool-lowkey-spotlight` ([SKILL.md](../grade-cool-lowkey-spotlight/SKILL.md)) | optional: only when the footage itself is dark; never forced onto bright footage |

A listed technique may be used zero, one or many times, as the content warrants.

## Relationships and dependencies
- One key-word accent per sentence at most; the white captions hide while a big key word holds.
- Lower thirds sit lower left, never at the same moment as a big key word.
- Text and graphics do not scale with the creeping zoom.
- The key-word colour, the lockup's big line and the lower-third bar share one main colour.

## Triggers and sequencing principles
- 0.0 s: film burn + hit, wide shot settling out, first sentence as a lockup with the key words in the main colour.
- Interviewer question on its own short shot (one key word).
- Guest answer: close → medium → close… cuts on phrase starts; name lower third ~0.1 s after the first guest shot that is held long enough.
- Last ~8 s: "full conversation" lower third.
- Last sentence: cut to the wide, closing lockup with the final key word; the video ends on it (no outro).

## Rhythm and emphasis
- First ~3.3 s: 3 quick cuts (≈ 1.5 / 0.7 / 1.0 s); then holds of 4–8.5 s.
- About one key word every ~5–6 s.
- No punch-ins, no whips, no flashes after the opening.

## Audio-visual coordination
- Music: one continuous bed under the whole clip, ≈ 13 LU under the voice, no audible ducking, cut with the video at the end (measured only; ask the user for music; if he supplies a track, `music-bed-drop-entry` sets level and entry).
- Opening hit: loud (≈ +6 dB over the voice's loud moments for ~0.1 s) on the burn.
- Glitch/data sound only on lower-third entrances, ≈ 14–16 dB under the voice.
- Everything else silent: no sounds on captions, key words, cuts or zooms.

## Scaling to other lengths and structures
- 20–30 s: one lower third (name), keep both wide bookends.
- 45–90 s: add the CTA lower third in the last third; keep holds long, add angle changes only on phrase starts.
- Single-camera footage: see `cut-multicam-podcast-bookends` adaptation (digital crops); without a wide shot, open on the medium with the lockup in empty space.

## Template-specific adaptations and constraints
- **Dark and bright footage both work** [User]. The darkness of the reference is the real studio and lighting, not the style.
  - Dark footage: key words, lockup big line and lower-third bar in red (or the brand accent if it reads as light) with the neon glow; white captions with soft glow; `grade-cool-lowkey-spotlight` optional.
  - Bright footage: pick a strong main colour for the key words with the user (red, brand accent or a new colour) - always with the neon glow; captions white with a soft dark shadow (or dark text on very light areas); lower-third text dark or white by contrast; keep the user's normal grade for his own footage (warm and bright, never grey or dark) and do not apply the low-key grade.
- Fonts: heavy italic display serif for key words, a medium sans for captions, a monospace for lower thirds (brand fonts where they exist).
- Real names, titles and links only (from the user).

## Success criteria
- Looks like a premium show clip; every sentence has at most one key word in the main colour; the opening hits in the first 0.2 s and the ending rests on the wide.

## User notes
- [User] Do not limit the template to dark footage: the darkness is the real shooting environment; with new main colours for some texts the template can be used for bright videos too ("تمپلیت رو به فضای تاریک محدود نکن ...").
- [User] The neon glow is always kept, on dark and on bright footage ("نه درخشش نئونی رو همیشه داشته باشه"), 2026-10-25.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
