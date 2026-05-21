# Rough Cut Rate+20 Assembly Check V1 — The Search Snippet Is Not the Page

## Status note
This is a planning-stage assembly check.
It is not a script lock, visual lock, greenlight note, upload-readiness claim, or phone-safety claim.

## Why this check exists
`ROUGH_NARRATION_DURATION_CHECK_V1.md` showed that:
- default rough AriaNeural pace is too slow for the current no-Shot-9 baseline
- a bounded `+20%` rate test lands at about **61.08s**, almost exactly on top of the current rough animatic length of about **61.04s**

That raised one practical follow-up question:
- can the current no-Shot-9 animatic and the current `+20%` rough narration actually be assembled into one temporary reviewable rough cut without immediate duration mismatch problems?

This note answers that narrower question.

## Inputs used
- current rough animatic:
  - `concepts/search-snippet-is-not-the-page/rough_animatic_v1_no_shot9.mp4`
- temporary rough narration:
  - `/tmp/search_snippet_script_current_flat_rate20.mp3`
- script source behind that narration:
  - current working script from `SCRIPT_DRAFT_V1.md`

## Method
1. Measured the current rough animatic duration with `ffprobe`.
2. Measured the temporary `+20%` rough narration duration with `ffprobe`.
3. Muxed the animatic video stream with the temporary narration audio into a temporary MP4 review artifact.
4. Measured the resulting rough cut duration with `ffprobe`.
5. Checked the `ffmpeg` log tail for obvious assembly failure signals.

## Temporary artifact produced
- `/tmp/search_snippet_rough_cut_rate20.mp4`

## Direct results
### Measured durations
- rough animatic: **61.04s**
- rough narration (`+20%`): **61.08s**
- muxed temporary rough cut: **61.08s**

### Assembly result
The mux completed successfully.
The resulting temporary rough cut duration tracks the narration duration closely, as expected.

### Log interpretation
`ffmpeg` completed the mux and wrote the output file successfully.
The log included some MP3 decoder `overread` warnings during input handling, but these did **not** prevent output creation and are not, by themselves, evidence that the rough cut failed.

## Main findings
### 1. The current faster-delivery baseline is mechanically compatible
The present no-Shot-9 visual baseline and the temporary `+20%` narration are close enough in runtime to assemble cleanly into one rough cut artifact.

That is useful because it moves the question forward from:
- `Could a faster delivery fit in theory?`

to:
- `A faster rough delivery can at least be assembled against the current visual baseline without obvious runtime mismatch.`

### 2. This supports delivery-speed testing before script tightening
The earlier duration note already suggested that faster delivery may be the first lever worth testing.
This assembly check strengthens that conclusion.

There is now concrete evidence that:
- the current script does not immediately force a timing breakdown
- a bounded faster-delivery proxy can coexist with the current no-Shot-9 animatic length

### 3. This still does not prove the rough cut is editorially good
Mechanical assembly is not the same as editorial success.
This note does **not** establish that:
- the pacing feels natural
- the spoken transitions land well
- the proof beats feel unhurried
- the routine and close feel earned

Those remain separate review questions.

### 4. The next useful question is about feel, not basic fit
Because the artifact assembled cleanly, the next useful validation target is likely:
- whether this faster rough delivery still sounds and feels natural enough through the main pressure points,
especially:
- Shot 6
- Shot 7
- Shot 10

## Safest current interpretation
The strongest restrained reading is:
- current default-TTS pace is too slow
- current `+20%` rough pace is close enough to the visual baseline to assemble successfully
- so the project has now earned a more specific next step: review whether this faster rough delivery feels natural enough before considering script tightening

That remains a planning-stage conclusion only.

## What this note does not justify
This note does not justify saying the piece is:
- locked
- visually finished
- narration-finished
- upload-ready
- phone-safe

It only establishes that the current no-Shot-9 animatic and a bounded faster rough narration can be combined into a workable temporary review artifact.

## Bottom line
A temporary narrated rough cut at `+20%` delivery was assembled successfully at about **61.08s**.
That does not settle pacing quality, but it does show that the current baseline is mechanically compatible with a faster rough-delivery path.
So the next useful validation step is probably to review that rough cut for pacing feel, not to assume immediate script tightening.
