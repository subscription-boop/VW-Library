---
name: sfx-keyboard-typing-captions
description: A crisp keyboard keystroke on every caption word as it appears, and a quick 3-4 key burst when a big keyword lands on a card. For kinetic caption blocks and text cards. Library technique; apply only when the user selected it or a selected template references it.
disable-model-invocation: true
metadata:
  kind: technique
  category: sfx
  status: approved
  approved: 2026-10-24
  sources: [src-003]
---

# sfx-keyboard-typing-captions

> Library technique (category: `sfx`). Shared rules: [CONTRACT](../../../library/CONTRACT.md). To apply this to a video, follow [QUICK-CREATE](../../../library/QUICK-CREATE.md) (full rules: [EXECUTION](../../../library/EXECUTION.md)). The name is an identifier only: read this document for behavior.
> Execution part only. Analysis notes (reference measurements, history): [ANALYSIS.md](ANALYSIS.md) - open only when a decision needs them.

## Observable behavior
Every time a word appears in the kinetic caption blocks or on a white text card, a single short, bright keyboard keystroke is heard, so the text seems to be typed live. When the big keyword of a card lands, instead of one key there is a quick burst of 3–4 keystrokes. Captions that are plain phrase lines over wide shots (and the presenter's own captions) stay silent.

## Intended effect
Makes the typography feel physical and "typed as he speaks"; adds rhythm under speech without music doing the work; the burst gives the keyword a small accent.

## Defining characteristics
- One keystroke per appearing word, on the frame the word appears. [Fixed]
- Keyword landing = burst of 3–4 rapid keystrokes (~30–40 ms apart). [Rule]
- Short, bright, dry click (a few ms, decays in ~10 ms, energy up to ~20 kHz), no reverb. [Fixed]
- Only on kinetic blocks and cards, not on every caption style. [Rule]

## When to use
- Triggers: words appearing in `text-kinetic-stack-mixed-size` blocks; small words and the keyword on `card-white-kinetic-lockup` cards.
- Good fit: interview / podcast / quote edits with word-by-word typography.
- Avoid when: captions change faster than ~6 words per second (clicks turn into noise); calm captions that should stay invisible; music-driven edits where clicks fight the beat.

## Anatomy over time
- Start: the frame the word becomes visible (the grey/blur stage counts as visible).
- Development: none; each key is a one-shot.
- Resolution: dry decay within ~10–20 ms.
- Repetition: every word; alternate between several different keystroke samples so it never sounds like a loop.

## Sound
- Type and character: single mechanical keyboard keystroke, bright click, ~5–15 ms, no room.
- Library file(s): `<SFX>\_index\cuts\mechanical-keyboard_key_01..12.wav` (single keys cut from `<SFX>\Mechanical Keyboard.wav`; match to the reference click: **Same type**, key_01–04 closest). Second choice: single keys from `<SFX>\Keyboard 1.mp3` (Close; a bit softer with more low "thock").
- Extracted from the reference: none needed (library match is close).

## Sync rule
- Follows: the caption word's appearance frame (in the reference 0–90 ms after the spoken onset, i.e. the same frame the word shows).
- Repetition: per word; keyword: 3–4 keys spaced ~30–40 ms starting on the keyword's first visible frame.
- Variation: never the same sample twice in a row; optional random level ±2 dB.

## Level
- Single keys: peaks ~3 dB under the voice's word peaks (reference: keys ~-6.5 dBFS vs words ~-3.4 dBFS peak). Being so short, they read as clearly audible but quieter than speech.
- Keyword burst: peaks about level with the voice peaks.
- Never let a key sit on top of a stressed syllable louder than the voice.

## Relationships
- Speech: one key per spoken word that appears; silent during pauses.
- Cuts: unaffected; the white card's first word gets its key on the card's first frame.
- Music and beats: ignores the music bed.
- Other techniques: rides on `text-kinetic-stack-mixed-size` and `card-white-kinetic-lockup`; not used on `text-phrase-build-blur-rise` lines in the reference.

## Adaptation
- Adaptable: sample choice (any dry single keystroke), level by ±3 dB to suit the voice and mix.
- Scaling: if words come faster than ~6 per second, key only the first word of each pair.
- Brand: none.

## Key numbers
- Reference kinetic block: 10 keys for 11 words, one per appearing word (observed; table in ANALYSIS.md).
- Reference click spectrum: full band to ~20 kHz while the podcast audio itself stops at ~16 kHz, so the keys are clearly added; decay ~9 ms (observed; table in ANALYSIS.md).

These describe the reference. They are not quotas or required values.

## Success criteria
- Each appearing word in a kinetic block or card has exactly one key on its first visible frame; the keyword gets a short burst.
- Keys are audible on a phone speaker but never cover the voice.
- No two consecutive keys use the same sample.

## References
Index: [references/REFERENCES.md](references/REFERENCES.md)
- Unsure about timing per word: open `clips/src-003_0011300-0012800_typing-per-word.mp4`.
- Unsure about the keyword burst: open `clips/src-003_0014600-0016200_card-words-keyword-burst.mp4`.
- Unsure what the click looks like in the spectrum: open `frames/src-003_0011300-0033900_spectrogram-typing.png`.
