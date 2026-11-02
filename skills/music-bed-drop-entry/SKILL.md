---
name: music-bed-drop-entry
description: Standard way to add a music track under a talking-head short - the track enters on a strong downbeat (a drop or section re-entry) exactly when the opening SFX/riser ends, runs as one continuous piece, is EQ'd and levelled about 9-10 dB under the voice with smooth ducking, and fades out after the last word. Library technique; apply only when the user selected it or asked for music.
disable-model-invocation: true
metadata:
  kind: technique
  category: music
  status: approved
  approved: 2026-10-22
  sources: []
  origin: user-approved practice from project 2026-10-21-3-skills-beat-a-degree (v005-music), not from a reference video
---

# music-bed-drop-entry

> Library technique (category: `music`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (project-example measurements, registration history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Behavior
No music under the hook's opening SFX. The moment the riser/whoosh peaks and ends, the track comes in on a strong downbeat, ideally the "drop" right after a quieter bar, so the music feels like the payoff of the riser and the start of the main content. It then plays as one continuous piece under the voice, clearly present but never competing with speech, and resolves with a short, smooth fade after the final word.

## Intended effect
Energy and polish without hurting clarity: the riser → drop gives the opening a lift, the bed carries pace, and the ending feels finished instead of cut off.

## Defining characteristics
- Asset: only a track the user supplied or approved (ask first). [Rule]
- Entry point: a strong downbeat after a quieter passage (drop, section re-entry, chorus start), never mid-phrase. [User]
- Entry time: exactly where the opening SFX ends (or, with no SFX, on the first cut into the main content); 5–10 ms fade-in only, so the transient stays punchy. [User]
- One continuous section of the track; no internal edits. If the track must be shortened or extended, cut only on bar lines. [Rule]
- Level: voice ≈ −14 LUFS; music bed ≈ −23 LUFS before ducking, ducked ≈ 3 dB while the speaker talks with ~300 ms smoothing (no pumping). Result: music ≈ 9–10 dB under the voice. [User]
- Voice space: high-pass ≈ 35 Hz, wide cut ≈ −4 dB around 2.8 kHz, ≈ −1.5 dB around 250 Hz on the music. [User]
- Ending: the last word lands with the music at full bed level; hold the last shot ~0.4–0.6 s longer when the footage allows; then a cosine fade of ~0.8–1.0 s that ends exactly on the last frame. [User]
- Master: limiter, true peak ≤ −1 dBFS, final mix ≈ −14 LUFS integrated. [Rule]

## When to use
- Triggers: the user asks for a music version / adds a track.
- Avoid when: the user's standing rule for that content is "no music" (for example his @zadrox reels default) unless he asks for an extra music version.

## Procedure (tool-independent)
1. Analyse the track: tempo, beat grid, downbeats (strongest low-end/kick beats), section boundaries and their loudness before/after.
2. Choose the entry: a downbeat where energy jumps up after a quieter bar. Find the exact transient (a few ms) by waveform energy.
3. Place it so that transient sits on the end of the opening SFX. Check the riser/whoosh tail does not overlap a second hit.
4. Cut the section to the video length (+ the extended tail), EQ, loudness-match, apply smooth ducking from the voice envelope.
5. Ending: extend the last shot if possible, fade with a cosine curve to silence on the last frame.
6. Mix with voice and SFX, limit, measure: integrated loudness, true peak, and music-vs-voice difference per section (target 8–11 dB). Report what was measured and that it was not listened to, if no listening was possible.

## Relationships
- Follows an opening SFX such as `sfx-whoosh-main-start` (or a riser chosen by the user).
- Works with any template; when a template says "ask before adding music", this skill is what to apply once the user supplies a track.

## Key numbers
- Project example entry at 00:02.730: track "Money So Big (Instrumental sped up)" @ 84.52 s, the drop after a quiet bar (−25 → −17 dB), ~161 BPM (project example; table in ANALYSIS.md).
- Music 9–10 dB under the voice; bed −23 LUFS, −3 dB ducking (stated above).
- Ending: last shot +0.55 s, 0.87 s cosine fade after "Successful."; master −14.7 LUFS, −0.9 dBFS peak (project example).

## Success criteria
- The drop hits as the riser ends; nothing sounds early or late.
- Every word is clear on phone speakers; the music is felt, not fought.
- No audible pumping, clicks, or abrupt stop; the ending feels resolved.

## User notes
- [User] Music starts when the opening SFX goes quiet and its peak ends; volume, sync, continuity, start and end done professionally by short-video standards.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md).
