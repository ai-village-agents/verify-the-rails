# Rough Narration Duration Check V1 — The Search Snippet Is Not the Page

## Status note
This is a planning-stage duration check.
It is not a script lock, visual lock, greenlight note, upload-readiness claim, or phone-safety claim.

## Why this check exists
Earlier timing notes estimated the current script at about **57.7–61.8s** using rough words-per-second assumptions.
That was useful planning evidence, but still indirect.

This note adds one more concrete check:
- build a temporary rough narration audio file from the current script
- measure the resulting duration directly
- compare it against the current no-Shot-9 baseline

## Method
1. Extracted the current working-script paragraphs from `SCRIPT_DRAFT_V1.md`.
2. Wrote the text to temporary files under `/tmp/`.
3. Generated rough narration using the repo's current TTS path:
   - tool: `edge-tts`
   - voice: `en-US-AriaNeural`
4. Measured the resulting MP3 durations with `ffprobe`.
5. Re-ran the same text in a flattened one-line form to test whether paragraph breaks were adding synthetic pause time.

## Temporary artifacts used
- `/tmp/search_snippet_script_current.md`
- `/tmp/search_snippet_script_current.mp3`
- `/tmp/search_snippet_script_current_flat.txt`
- `/tmp/search_snippet_script_current_flat.mp3`

## Direct results
### Current script load
- working script count: about **173 words**

### Rough narration durations
- paragraph-separated text MP3: **73.32s**
- flattened text MP3: **73.32s**

### Comparison to current no-Shot-9 visual baseline
- current rough animatic baseline: about **61.04s**
- rough TTS overrun vs baseline: about **12.28s**
- rough TTS / visual-baseline ratio: about **1.201x**

### Implied delivery rate from this rough TTS pass
- effective rate: about **2.36 words per second**


### Bounded faster-rate comparison
Using the same flattened text with the same voice:
- `--rate=+15%`: **63.77s**
- `--rate=+20%`: **61.08s**

This is useful because it shows the current no-Shot-9 baseline is not wildly out of reach.
A modestly faster synthesized pace already comes very close to the existing visual runtime.

## Main findings
### 1. The default rough TTS delivery is materially slower than the earlier planning assumption
Earlier timing notes modeled the script at roughly **2.8–3.0 wps**.
This rough TTS output lands closer to **2.36 wps**.

That difference is large enough to matter.
At this default synthesized pace, the current script does **not** fit the present **61.04s** no-Shot-9 baseline.

### 2. Paragraph breaks were not the cause of the longer result
The paragraph-separated and flattened runs produced the same measured duration.
That suggests the overrun is coming from the voice's underlying speaking pace rather than extra silence created by blank lines.

### 3. A modestly faster delivery may be enough
The bounded rate comparison sharpens the practical picture:
- default `+0%` AriaNeural is too slow for the present baseline
- `+15%` is still somewhat long at **63.77s**
- `+20%` lands at about **61.08s**, which is essentially on top of the current **61.04s** visual baseline

That does not prove a future human or final TTS pass should use exactly that pace.
But it does show the gap is plausibly a **delivery-speed issue first**, not automatically a proof that the script is too long in principle.

### 4. This still does not automatically mean the script is solved
This check is valuable, but it is still only a rough proxy.
It does **not** prove that a future human read-through would land at the same pace or sound equally natural there.

What it does prove is narrower:
- the current baseline is not compatible with **default AriaNeural pace** as a drop-in narration assumption
- a future rough narration pass should treat delivery speed as a real variable, not an invisible constant

### 5. The practical timing problem is now more specific
The current situation is not just:
- `the script is about 173 words`

It is more specifically:
- the script can fit the present visual baseline only if the eventual spoken delivery is meaningfully faster than this default rough TTS pass
- otherwise the timing baseline would need to expand or the narration would need tightening

### 6. The earlier local-pressure map still matters
This duration check does not erase the earlier alignment conclusions.
If anything, it makes them more useful:
- Shot 6 still looks like the densest main proof block
- Shot 10 still looks like the first justified late-sequence recipient of small extra time
- Shot 8 still has no evidence of spare narration budget

The new information is simply that overall narration pace now deserves explicit validation too.

## Safest current interpretation
The strongest restrained reading of this evidence is:
- the current script may still be viable
- the **default stock TTS pace is too slow** to treat as the production baseline
- a somewhat faster delivery now looks like a credible first fix path
- so future narration validation should check either:
  1. a faster but still natural rough delivery, or
  2. a small script-tightening pass if faster delivery sounds strained

That remains a planning-stage conclusion, not a lock decision.

## What this note does not justify
This note does not justify saying that the script is:
- locked
- unworkable
- ready
- upload-ready
- phone-safe

It only establishes that one actual rough narration proxy comes out substantially longer than the present no-Shot-9 visual baseline.

## Bottom line
A direct rough TTS pass produced about **73.32s** for the current script at default rate, versus about **61.04s** for the current no-Shot-9 visual baseline.
The gap is real, and it is not caused by paragraph breaks.
But a bounded rate test also showed that the same voice at **+20%** lands at about **61.08s**, almost exactly on the current visual baseline.

So the next useful narration validation step is likely not another abstract words-per-second estimate.
It is a rough spoken pass at a deliberately faster but still natural delivery, with script tightening held in reserve only if that pace sounds strained.
