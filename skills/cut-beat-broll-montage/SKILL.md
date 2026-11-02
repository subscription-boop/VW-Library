---
name: cut-beat-broll-montage
description: Mid-video, the voice stops and the music comes up to full level for a ~12 s B-roll proof montage - one shot per beat (~0.65 s at ~90 BPM), every cut on a kick/bass hit, hard cuts alternating with motion-blur whips, accents on the drop - then the voice returns over the last shot. Fits promos and portfolio moments. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: cut
  status: approved
  approved: 2026-10-28
  sources: [src-007]
---

# cut-beat-broll-montage

> Library technique (category: `cut`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (observed measurements, distinction from a related technique, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
After a claim ("…so you could be number one"), the speaker disappears and so does his voice: the music, until now a quiet bed, comes up to full level and drives a fast B-roll montage of the company's work and world (team on set, crew in harnesses, skylines, branded van, a wrap shop, cars, a jet ski, villas, roofers). Almost every shot lasts **one beat (~0.65–0.7 s)**, and **every cut lands on a kick/bass hit** of the music. About half of the changes are hard cuts, the others are motion-blur whips; the biggest music moment gets an echo effect and a spin transition; a day/night match cut and a burst of photo cards add variety. No captions while there is no speech. The voice comes back over the last B-roll shot ("There's a reason why…", with captions) and a white flash returns to the speaker.

## Intended effect
A proof-of-work burst: lots of results and energy in a few seconds, like a mini showreel inside the talk; the music change refreshes attention mid-video.

## Defining characteristics
- Voice pauses; music up to full level for the montage only. [Fixed]
- One shot ≈ one beat; cuts on kick/bass onsets (within ~1 frame). [Fixed]
- Mix of hard cuts and motion-blur whips; at most one big accent (spin/echo) on the drop. [Rule]
- Shots show the brand's real work/results/team; no talking head inside. [Rule]
- Voice re-enters over the last B-roll shot before returning to the speaker. [Rule]

## When to use
- Triggers: after a strong claim ("number one", "we create…"), or as a portfolio/proof section in a promo.
- Good fit: brand promos, agency/service ads, personal-brand reels with good B-roll.
- Avoid when: there is not enough strong B-roll (needs ~15–20 shots for ~12 s), or the piece is an educational talk where the voice must not stop.

## Anatomy over time
- Start: out of a title moment (`title-rank-number-pixel-breakup` ([SKILL.md](../title-rank-number-pixel-breakup/SKILL.md))) whose breakup crosses the first cut.
- Development: beat-length shots; whips on roughly every other cut; on the drop: `fx-echo-rgb-trail` → `transition-spin-blur-drop`.
- Resolution: voice returns over the last shot; `transition-white-flash-cut` back to the speaker on a beat.
- Repetition: once per video.

## Relationships
- Music: the music's loudest section; heavy bass "drop" around the middle of the montage. Music level ≈ speech level or slightly above (momentary loudness p90 ≈ −11 LUFS, same as the speech sections).
- Speech: none inside; resumes on the last shot.
- Sound effects: none separable from the music (see ANALYSIS Sound).
- Other techniques: `transition-motion-blur-whip`, `transition-spin-blur-drop`, `fx-echo-rgb-trail`, `graphic-photo-card-flash-burst`, `transition-white-flash-cut`.

## Adaptation
- Tempo: shot length = one beat of the chosen track (two beats for a hero shot or a transformation shot).
- Length: ~8–14 s; scale shot count with length.
- Brand: B-roll should show the selected brand's real work; grade follows the project's grade.
- Music: the user chooses the track (ask before selecting music).

## Key numbers
- Montage length ~12.6 s with ~19 shots + 1 photo-card burst, from 00:16.95 to the white flash at 00:29.56 (observed; table and full cut list in ANALYSIS.md).
- Typical shot length 0.60–0.70 s; longer for the car transformation (~1.3 s) and the house + photo cards (~1.2 s) (observed).
- Beat ≈ 0.65–0.67 s (~90–92 BPM); low-frequency onsets at e.g. 16.954, 19.610, 20.284, 23.586, 24.916, 25.574, 28.336, 29.493 s (observed).
- Bass drop at 00:22.9–00:25.9: sub level ≈ +15 dB over the rest of the montage (observed).
- The crystal → ice → real car shot at 00:24.09–00:24.36 is a transformation inside the footage, not an edit effect (observed).

These describe the references. They are not quotas or required values.

## Success criteria
- Every cut can be tapped along with the music's kick.
- The montage feels like a different "chapter" (no voice, music up) and returns cleanly to the speaker.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- One frame per shot: `sequences/..._one-frame-per-shot.jpg`. Cuts vs audio: `audio-vs-cuts.png`. Whole montage with music: `clips/..._montage-in-context.mp4`.
