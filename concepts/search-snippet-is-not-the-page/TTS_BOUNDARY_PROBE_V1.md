# TTS Boundary Probe V1 — The Search Snippet Is Not the Page

## Status note
This is a planning-stage delivery-probe note.
It is not a script lock, visual lock, greenlight note, upload-readiness claim, or phone-safety claim.

## Why this note exists
Earlier evidence showed that a bounded faster narration path at `+20%` was mechanically compatible with the current no-Shot-9 rough cut.

That still left a narrower question: **where do the spoken blocks actually land inside the current shot windows?**

This note answers that question using `edge_tts` boundary events rather than browser-local playback impressions.

## Method
Used `edge_tts` with:
- voice: `en-US-AriaNeural`
- rate: `+20%`
- boundary modes: `SentenceBoundary` and `WordBoundary`

Input text was the current working script from `SCRIPT_DRAFT_V1.md`.

Measured total from the sentence-boundary stream: **~61.052s**.
That is close to the earlier rough narration measurement of **~61.08s** and therefore directionally consistent with the current no-Shot-9 animatic baseline.

## Current planning-stage shot windows used for comparison
- Shot 6: `0:27.5–0:40.0`
- Shot 7: `0:40.0–0:47.5`
- Shot 8: `0:47.5–0:50.0`
- Shot 10: `0:50.0–0:56.5`
- Shot 11: `0:56.5–1:01.0`

## Sentence-level overlap findings
Relevant measured sentence spans:

| Sent. | Spoken span | Current line role | Shot overlap |
| --- | --- | --- | --- |
| 10 | `25.812–27.875` | `Another is quoting the page.` | tail enters Shot 6 |
| 11 | `27.875–29.958` | `Both are looking at something real.` | Shot 6 |
| 12 | `29.958–34.354` | `Then the missing clue appears: Updated March 14, 2026.` | Shot 6 |
| 13 | `34.354–36.865` | `That date does not make the preview fake.` | Shot 6 |
| 14 | `36.865–42.990` | `It explains how a preview can keep older wording...` | Shots 6–7 |
| 15 | `42.990–44.969` | `The preview still matters.` | Shot 7 |
| 16 | `44.969–46.917` | `It points you to the source.` | Shot 7 |
| 17 | `46.917–50.958` | `But once the page is open...` | Shots 7–8–10 |
| 18 | `50.958–56.958` | `So the habit is simple...` | Shots 10–11 |
| 19 | `56.958–59.312` | `A preview can point you to a source.` | Shot 11 |
| 20 | `59.312–61.052` | `It is not the source.` | Shot 11 |

## What this means by review area
### Shot 6
Shot 6 does **not** begin on a perfectly clean paragraph boundary.
It receives only a very small carry-in from the previous sentence (`25.812–27.875`, or about `0.375s` inside the Shot 6 window).

The more important finding is that the main update-clue explanation block remains concentrated here:
- `Both are looking at something real.`
- `Then the missing clue appears...`
- `That date does not make the preview fake.`
- the first part of `It explains how a preview can keep older wording...`

So Shot 6 still reads as the **tightest major explanatory block**, but now with a more exact boundary finding:
- the block is mostly contained,
- yet the long explanation sentence continues about **`2.99s` into Shot 7**.

### Shot 7
Shot 7 is doing more bridge work than the earlier prose summary alone made obvious.
It contains:
1. the end of the long update-clue explanation sentence,
2. `The preview still matters.`,
3. `It points you to the source.`,
4. the beginning of `But once the page is open...`

That means Shot 7 is not just a single trust-order line landing cleanly inside one window.
It is a **handoff zone** between the explanation block and the late-sequence trust-order block.

### Shot 8
Shot 8 remains narration-light in the sense that it does not carry a whole new sentence by itself.
However, it is **not silent** at this pace.
It carries the middle section of the trust-order sentence:
- `...the page is open, the page is stronger present-tense evidence.`

So the earlier guidance still holds in spirit — do not add more narration burden here — but the measured boundary result is slightly sharper:
Shot 8 already functions as a **brief spoken bridge**, not just a purely visual pause.

### Shot 10
Shot 10 begins with the **tail end** of the trust-order sentence and then holds almost all of the practical routine sentence.
Measured structure:
- sentence 17 ends at `50.958`, about **`0.958s` into Shot 10**,
- sentence 18 then runs `50.958–56.958`,
- this leaves about **`5.54s` of Shot 10** for most of the routine line,
- the routine sentence then spills about **`0.46s` into Shot 11**.

This sharpens the previous concern.
The question is not simply whether the Shot 10 routine sentence “fits” inside a nominal `6.5s` slot.
The current spoken flow gives Shot 10 a **shared late-sequence burden**:
- finish the trust-order sentence,
- begin and mostly carry the three-step routine,
- then hand off the final routine tail into Shot 11.

### Shot 11
Shot 11 begins with the final fraction of the routine sentence and then carries the full closing callback.
The final two closing sentences remain compact.
The measured ending reaches about `61.052s`, which is only a negligible overrun relative to the current `61.0s` planning-stage window endpoint.

## Word-boundary clues at the key transitions
The sentence-level findings above are already enough to guide review, but a few word-boundary details are especially useful:

### Shot 6 → Shot 7
The phrase `older wording, or shorter wording` crosses the Shot 6 / Shot 7 boundary almost exactly:
- `wording` ends around `40.042s`
- Shot 7 starts at `40.000s`

So the key explanation sentence is not ending cleanly before the handoff.
The handoff occurs inside the sentence itself.

### Shot 8 → Shot 10
The final words of the trust-order sentence cross the Shot 8 / Shot 10 boundary:
- `present-tense` runs around `49.229–49.729`
- `evidence` runs around `49.740–50.271`
- Shot 10 starts at `50.000s`

So Shot 10 inherits the very end of the trust-order statement before the routine line begins.

### Inside Shot 10
The three routine actions themselves start cleanly enough once sentence 18 begins:
- `open` around `52.250s`
- `compare` around `53.083s`
- `check` around `54.135s`

This supports the idea that the routine remains orderly **once it starts**, even though Shot 10 is already partly occupied by the tail of the previous sentence.

## Current interpretation after this probe
1. The `+20%` path remains **mechanically plausible** at the sentence-boundary level.
2. The probe does **not** prove naturalness, script lock, or readiness.
3. Shot 6 remains the tightest major explanation area.
4. Shot 7 is better understood as a **handoff zone** than as a self-contained trust-order window.
5. Shot 8 should still avoid any extra narration burden, but it already carries part of the trust-order sentence.
6. Shot 10 still matters, but its pressure is more specific than “the routine sentence might be too long”:
   it currently inherits the trust-order tail before carrying the routine.
7. Shot 11 still functions mainly as the taper-and-close zone, though it now clearly inherits a small routine tail before the callback.

## Practical implication for any later listening pass
If a later spoken review is performed, the best questions are now even narrower:
- Does the Shot 6 → Shot 7 sentence carry sound calm and intelligible?
- Does the trust-order line remain clear even though it spans Shots 7–8–10?
- Does Shot 10 still feel practical once it begins the routine after inheriting the end of the prior sentence?
- Does the small routine spill into Shot 11 feel natural, or like preventable crowding?

## Decision discipline to preserve
This note does **not** justify:
- a broad script rewrite,
- reopening Shot 9 as a narration sink,
- treating browser-local playback as verification,
- any greenlight / upload-ready / phone-safe claim.

It only narrows where later evidence-gathering would be most informative.
