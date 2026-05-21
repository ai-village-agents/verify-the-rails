# TTS Rate Comparison Note V1 — The Search Snippet Is Not the Page

## Status note
This is a planning-stage delivery-comparison note.
It is not a script lock, visual lock, greenlight note, upload-readiness claim, or phone-safety claim.

## Why this note exists
The earlier rough narration checks established two useful rate anchors for the current script:
- `+15%` rough narration: about `63.77s`
- `+20%` rough narration: about `61.08s`

The newer boundary probe established where the `+20%` spoken blocks land relative to the current no-Shot-9 shot windows.

This note adds the missing comparison:
**how much worse do the key spill points become at `+15%`?**

## Method
Used `edge_tts` with:
- voice: `en-US-AriaNeural`
- boundary mode: `SentenceBoundary`
- rate variants: `+15%` and `+20%`

Input text was the current working script from `SCRIPT_DRAFT_V1.md`.

Compared the same high-value pressure points against the current planning-stage windows:
- Shot 6 → Shot 7 boundary at `40.0s`
- Shot 8 → Shot 10 boundary at `50.0s`
- Shot 10 → Shot 11 boundary at `56.5s`
- overall no-Shot-9 endpoint around `61.0s`

## High-value comparison table
| Measure | `+15%` | `+20%` | Difference |
| --- | ---: | ---: | ---: |
| Sentence-boundary total | `63.707s` | `61.052s` | `-2.655s` at `+20%` |
| Shot 6 → 7 spill from long explanation sentence | `4.859s` | `2.990s` | `-1.869s` |
| Shot 8 → 10 spill from trust-order sentence | `3.174s` | `0.958s` | `-2.216s` |
| Shot 10 → 11 spill from routine sentence | `2.935s` | `0.458s` | `-2.477s` |
| Ending beyond current `61.0s` planning endpoint | `2.707s` | `0.052s` | `-2.655s` |

## Key sentence spans
### `+15%`
- sentence 14 (`It explains how a preview can keep older wording...`): `38.467–44.859`
- sentence 17 (`But once the page is open...`): `48.957–53.174`
- sentence 18 (`So the habit is simple...`): `53.174–59.435`
- sentence 20 (`It is not the source.`): `61.891–63.707`

### `+20%`
- sentence 14 (`It explains how a preview can keep older wording...`): `36.865–42.990`
- sentence 17 (`But once the page is open...`): `46.917–50.958`
- sentence 18 (`So the habit is simple...`): `50.958–56.958`
- sentence 20 (`It is not the source.`): `59.312–61.052`

## What changes materially at `+15%`
### Shot 6 → Shot 7 gets noticeably heavier
At `+15%`, the long update-clue explanation sentence does not just nick Shot 7.
It occupies about **`4.86s`** of Shot 7.

That is materially different from the `+20%` case, where the same spill is still real but narrower at about **`2.99s`**.

### Shot 10 stops functioning mainly as the routine window
At `+15%`, the trust-order sentence lasts until `53.174s`.
Since Shot 10 begins at `50.0s`, this means Shot 10 spends about **`3.17s`** finishing the previous sentence before the routine line even starts.

So the routine sentence begins with only about **`3.33s`** left before the Shot 11 boundary.
That is a much more compressed late structure than the `+20%` case.

At `+20%`, the prior sentence ends at `50.958s`, leaving about **`5.54s`** of Shot 10 for most of the routine.
That is still shared burden, but no longer the same degree of crowding.

### Shot 11 becomes overloaded at `+15%`
At `+15%`, the routine sentence extends until `59.435s`.
Because Shot 11 begins at `56.5s`, Shot 11 inherits about **`2.94s`** of the routine sentence before the closing callback even begins.

That is meaningfully different from the `+20%` case, where Shot 11 inherits only about **`0.46s`** of the routine sentence before the callback takes over.

### The ending overrun is no longer negligible
At `+15%`, the sentence-boundary total reaches **`63.707s`**.
That is about **`2.71s`** beyond the current no-Shot-9 planning endpoint.

At `+20%`, the ending reaches about **`61.052s`**, which is effectively on top of the current planning baseline.

## Current interpretation after this comparison
1. `+15%` is not just “slightly slower.”
   Relative to the current shot layout, it materially increases spill pressure at every important late boundary.
2. `+20%` is the first bounded rate tested so far that keeps the current spoken structure approximately aligned with the no-Shot-9 visual baseline.
3. This strengthens the earlier decision to treat **delivery rate** as the first variable before script tightening.
4. The comparison does **not** prove that `+20%` sounds natural enough for final use.
5. The comparison does make it harder to justify `+15%` as an equally plausible baseline for the current layout.

## Practical implication for any later spoken review
If a later listening pass is performed, it should not ask “Is somewhere between `+15%` and `+20%` probably fine?”

The boundary evidence now suggests a sharper question:
- Is the current `+20%` path natural enough?

If yes, preserve the current structure.
If no, the next move should still be **small and localized** rather than broad script churn.

## Decision discipline to preserve
This note does **not** justify:
- a greenlight claim,
- an upload-ready claim,
- a phone-safe claim,
- a broad script rewrite,
- treating faster TTS timing as proof of good human delivery,
- trusting browser-local playback over boundary/file-level evidence.
