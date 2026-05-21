# TTS Pause Proxy Note V1

Status: planning-stage evidence only for `The Search Snippet Is Not the Page`.

This note adds one narrow follow-up to the earlier duration and boundary checks: a limited **pause / pacing proxy** using `edge_tts` word and sentence boundary events on the current `SCRIPT_DRAFT_V1.md`.

It is **not** a human read-through, not a claim that the narration is natural, not script lock, not visual lock, not greenlight, not upload readiness, and not phone-safety evidence.

## Why this check was worth doing

The current strongest timing result is that `+20%` is mechanically much better aligned than `+15%` with the no-Shot-9 visual baseline. But a remaining open question was whether `+20%` looked structurally worse as a **pause / phrasing pattern**, even before any human-performance review.

This check therefore asked a narrow question:

> Within the TTS system itself, do the key late sentences at `+20%` show obviously degraded pause structure or wildly compressed word pacing compared with `+15%`?

That is still a weak proxy for naturalness, but it is better grounded than browser-local impression alone.

## Method

- source text: `concepts/search-snippet-is-not-the-page/SCRIPT_DRAFT_V1.md`
- voice: `en-US-AriaNeural`
- boundary modes used: `SentenceBoundary` and `WordBoundary`
- compared rates:
  - `+15%`
  - `+20%`
- measured only the current critical late lines:
  1. `It explains how a preview can keep older wording, or shorter wording, long enough to support the wrong current conclusion.`
  2. `But once the page is open, the page is stronger present-tense evidence.`
  3. `So the habit is simple: open the page, compare the wording, and check one update clue with an absolute date.`
  4. `A preview can point you to a source.`
  5. `It is not the source.`

For each sentence, I noted:
- total sentence span
- word count
- approximate words per second across the sentence span
- average and max inter-word gap inside the sentence

I also checked the sentence-to-sentence pauses across this late sequence.

## Results

### Sentence-level pacing summary

| Rate | Sentence | Span (s) | Words | Approx. wps | Avg inter-word gap (s) | Max inter-word gap (s) |
|---|---|---:|---:|---:|---:|---:|
| `+15%` | long explanation sentence | `6.391` | 20 | `3.13` | `0.033` | `0.261` |
| `+20%` | long explanation sentence | `6.125` | 20 | `3.27` | `0.032` | `0.250` |
| `+15%` | trust-order sentence | `4.217` | 12 | `2.85` | `0.033` | `0.250` |
| `+20%` | trust-order sentence | `4.042` | 12 | `2.97` | `0.031` | `0.240` |
| `+15%` | routine sentence | `6.261` | 20 | `3.19` | `0.037` | `0.207` |
| `+20%` | routine sentence | `6.000` | 20 | `3.33` | `0.036` | `0.198` |
| `+15%` | callback line 1 | `2.457` | 8 | `3.26` | `0.011` | `0.011` |
| `+20%` | callback line 1 | `2.354` | 8 | `3.40` | `0.010` | `0.010` |
| `+15%` | callback line 2 | `1.815` | 5 | `2.75` | `0.011` | `0.011` |
| `+20%` | callback line 2 | `1.740` | 5 | `2.87` | `0.010` | `0.010` |

### Sentence-to-sentence pause summary inside the checked late sequence

- Between the explanation sentence and the later trust-order sentence there is an apparent multi-second gap in the extracted subset, but that is because two short intervening sentences are omitted from this comparison (`The preview still matters.` / `It points you to the source.`).
- More relevantly, the late landing run from:
  - `But once the page is open...`
  - `So the habit is simple...`
  - `A preview can point you to a source.`
  - `It is not the source.`
  shows **no extra sentence pause** at either `+15%` or `+20%` in the TTS boundary output.

## Main observations

1. **`+20%` does not show a radically different internal pause pattern from `+15%` in the tested lines.**
   - Average and maximum inter-word gaps stay very close.
   - The change is mostly a modest contraction of the full sentence spans.

2. **The critical late sequence is inherently continuous even at `+15%`.**
   - The trust-order sentence, routine sentence, and callback lines already form a near-unbroken run.
   - So the late-sequence continuity is not a new problem introduced only by `+20%`.

3. **`+20%` still meaningfully improves boundary fit without showing a dramatic pause-collapse signal in this proxy.**
   - Relative to `+15%`, the sentence spans shrink enough to reduce shot-boundary spill.
   - But the TTS-internal micro-gap pattern remains broadly similar rather than obviously breaking down.

4. **This does not prove the delivery sounds natural.**
   - TTS-internal pacing similarity is only a bounded structural clue.
   - A human spoken review could still find `+20%` too brisk, especially through the Shot 6 → Shot 7 and Shot 10 → Shot 11 handoffs.

## Updated interpretation

This check slightly strengthens the restrained case for keeping `+20%` as the current working timing baseline.

The strongest supported reading is now:
- `+15%` remains mechanically worse for the current shot layout.
- `+20%` improves the fit substantially.
- In this limited TTS pause proxy, `+20%` does **not** show an obvious extra collapse of phrasing relative to `+15%`.

That still falls well short of proving naturalness. It only means the existing mechanical preference for `+20%` is **not contradicted** by this additional proxy.
