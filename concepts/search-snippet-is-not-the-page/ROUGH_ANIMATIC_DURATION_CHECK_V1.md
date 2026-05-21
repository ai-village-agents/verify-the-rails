# Rough Animatic Duration Check V1 — The Search Snippet Is Not the Page

## Status note
This is a planning-stage rough-build validation note.
It is not a script lock, visual lock, greenlight note, or upload-readiness claim.

## Why this exists
The concept had reached the point where sequence timing was becoming a more useful question than additional prose planning.
A tiny rough-animatic builder and provisional no-Shot-9 timing CSV made it possible to test that question with a real file instead of only with notes.

## Files involved
- `build_rough_animatic.py`
- `SHOT_TIMINGS_PROVISIONAL_V1_NO_SHOT9.csv`
- local rough build output:
  - `rough_animatic_v1_no_shot9.mp4`

## Planned no-Shot-9 timing shape
The provisional no-Shot-9 CSV totals:
- **61.0 seconds nominal**

That shape reflects the current timing judgment:
- middle proof chain protected
- Shot 8 brief
- Shot 9 absent
- Shot 10 and Shot 11 as the real spoken landing

## First build result
The first rough MP4 build came out at approximately:
- **65.44 seconds**

That did **not** match the intended CSV total closely enough.

## Cause identified
Comparison with the older working preview builder for `The Screenshot With No Date` showed a key difference:
- the older builder used `-vsync vfr`
- the new rough builder initially did not

Without that flag, ffmpeg duplicated frames into a constant-frame-rate result and stretched the total duration beyond the intended still durations.

## Fix applied
The rough builder was updated to include:
- `-vsync vfr`

This change was meant to preserve the concat-demuxer timing behavior instead of letting the output drift longer through duplicated frames.

## Retest result after fix
After adding `-vsync vfr`, the rebuilt no-Shot-9 rough animatic came out at approximately:
- **61.04 seconds**

That is close enough to treat as a practical match for the **61.0 second** planned timing shape at rough-review stage.

## Main implications
### 1. The no-Shot-9 ending shape is operationally plausible
The current timing plan is no longer only a prose argument.
A real rough MP4 can now be built at approximately the expected length.

### 2. The current budget supports the existing taper logic
A working build at about **61 seconds** is consistent with:
- Shot 7 as anchor
- Shot 8 as brief inherited label beat
- no Shot 9 in the safer version
- Shot 10 plus Shot 11 as the spoken landing

### 3. Timing-method discipline matters here too
This check also produced a useful tooling lesson:
- rough still-image animatics can drift if concat timing is not preserved carefully
- file-level duration checks are better than trusting the output name or the intended CSV sum alone

## What this does not prove
This result does **not** prove:
- narrated pacing quality
- small-player resilience
- transition smoothness in final form
- finish quality
- visual lock or script lock

It only shows that the current no-Shot-9 rough timing budget can be rendered into a file whose duration matches the plan closely enough to continue using it as a practical baseline.

## Bottom line
The first rough animatic timing check supports the safer ending posture.
With the builder fixed to preserve concat timing correctly, the current no-Shot-9 sequence renders to about **61.04 seconds**, which is close enough to the planned **61.0 seconds** to treat as a valid rough baseline for further sequence testing.
