# Preview Review V18 — Staged Shot 6 Prototype Check

Date: 2026-05-20
File under review: `concepts/screenshot-with-no-date/preview_animatic_v14.mp4`
Timing table: `concepts/screenshot-with-no-date/SHOT_TIMINGS_V9_SHOT6_MOTION_CANDIDATE.csv`
Builder: `concepts/screenshot-with-no-date/build_preview_with_shot4_shot6_shot12_staging.py`
Prototype source: `concepts/screenshot-with-no-date/render_shot6_staging_prototype.py`

## What changed
This prototype keeps the current staged Shot 4 and staged Shot 12 work from V8 and replaces the static `16.0s` Shot 6 hold with three cumulative states:

- `06a_observed_only.png` — `5.0s`
- `06b_inference_added.png` — `5.0s`
- `06c_unknown_added.png` — `6.0s`

The goal was narrow: test whether Shot 6 behaves better when the `Observed / Inference / Unknown` split is built step by step instead of held as one static explanatory panel.

## Review method
As with the recent Shot 4 and Shot 12 checks, I treated file-level extraction as primary evidence.

Method used:
- extract frames from `preview_animatic_v14.mp4` at 2-second intervals inside Shot 6
- measure frame-to-frame mean absolute difference between adjacent samples
- compare the resulting pattern to the old static Shot 6 result from `PREVIEW_REVIEW_V15.md`

Artifact directory:
- `/tmp/v14_shot6_review/`

Artifacts generated:
- `/tmp/v14_shot6_review/shot6_midpoint_sheet.png`
- `/tmp/v14_shot6_review/summary.txt`

## Measured results
### Shot 6 — staged version (`67.0s–83.0s`)
Sample times:
- `[67.0, 69.0, 71.0, 73.0, 75.0, 77.0, 79.0, 81.0]`

Diff sequence:
- `[0.6541, 0.0, 0.6226, 0.0, 0.0, 14.221, 0.0]`

### Previous static Shot 6 baseline from V15
Sample times:
- `[67.0, 69.0, 71.0, 73.0, 75.0, 77.0, 79.0, 81.0]`

Diff sequence:
- `[14.3057, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`

## Interpretation
### 1) The staged version no longer behaves like one entry jump followed by a flat line
The static Shot 6 baseline had the same old pattern seen earlier in static Shot 4 and static Shot 12:
- one initial jump entering the shot
- then no recurring internal visible changes

The staged version changes that pattern materially.

Instead of a single front-loaded jump, the measured change now lands at later points inside the hold, especially around:
- `71–73s`
- `77–79s`

That matches the intended cumulative-reveal logic reasonably well:
- first state: `Observed`
- second state: `Observed + Inference`
- third state: `Observed + Inference + Unknown`

### 2) The strongest visible change appears when the full three-part split completes
The largest measured change is:
- `14.221` at `77–79s`

That likely corresponds to the entry of `06c_unknown_added.png`, where the final `UNKNOWN` layer completes the reasoning structure.

Practical read:
- the shot now has a visible destination instead of merely sitting in place for `16s`
- the last reveal appears to carry the clearest perceptual shift

### 3) The intermediate state change is present, but subtler than the final one
The earlier non-zero measurement is much smaller:
- `0.6226` at `71–73s`

This still matters, because it indicates the shot is no longer totally static between entry and completion.
But it also suggests the second state transition is relatively gentle.

That is not automatically bad:
- this shot’s job is explanatory, not flashy
- cumulative reasoning can tolerate quieter transitions than a hook shot

Still, it means the strongest proof of improvement is the overall pattern change, not just the magnitude of the middle transition.

## Practical judgment
Current judgment:
- this is a **real improvement** over the static Shot 6 hold
- the Shot 6 bottleneck now appears more defensible at the same total runtime
- the result fits the emerging project rule that long sequential-explanation shots perform better when internal meaning arrives in stages

What this review does **not** prove yet:
- that the whole piece is now solved
- that Shot 5 no longer matters
- that this is upload-ready or phone-safe

## Next question
The right next check is a whole-piece follow-up on `preview_animatic_v14.mp4`, with special attention to the former middle plateau around Shots 5–6.

If the full-piece review agrees with the local measurement, the remaining pacing pressure may narrow further toward Shot 5 and/or later finish-quality issues rather than the old static Shot 6 hold itself.

## Current status
Still:
- **not greenlit**
- **not upload-ready**
- **not phone-safe enough to claim**
- **promising but still preview-grade**
