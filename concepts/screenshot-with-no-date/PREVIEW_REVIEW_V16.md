# Preview Review V16 — First Motion-Enhanced Shot 12 Test

Date: 2026-05-20
Artifact reviewed: `preview_animatic_v13.mp4`
Candidate timings: `SHOT_TIMINGS_V8_SHOT12_MOTION_CANDIDATE.csv`
Related notes:
- `PREVIEW_REVIEW_V15.md`
- `PREVIEW_REVIEW_V14.md`
- `render_shot12_staging_prototype.py`
- `/tmp/v13_shot12_review/`

## Why this review exists
`PREVIEW_REVIEW_V15.md` confirmed that after the Shot 4 fix, the next long static-plateau risks were Shots 5, 6, and especially 12.

This pass tests the strongest next intervention target directly.

The new prototype keeps Shot 12 at the same total duration (`18.0s`) but replaces the single static workflow hold with four staged states:
1. `12a_open_source_page.png`
2. `12b_check_time_timezone.png`
3. `12c_scan_later_updates.png`
4. `12d_current_or_past.png`

Each stage currently holds for `4.5s`.

## Review method
File-level review again remained primary.

Method used:
- build `preview_animatic_v13.mp4` from the combined staged Shot 4 + staged Shot 12 candidate
- extract frames from the Shot 12 region at 2-second intervals
- measure frame-to-frame mean absolute difference across the `18.0s` hold
- compare the result against the flat-line pattern documented in `PREVIEW_REVIEW_V15.md`

Artifacts used in this pass:
- `preview_animatic_v13.mp4`
- `/tmp/v13_shot12_review/`

## Measured result
### Shot 12 — staged workflow version (`142.5s–160.5s`)
Sample times:
- `[142.5, 144.5, 146.5, 148.5, 150.5, 152.5, 154.5, 156.5, 158.5]`

Diff sequence:
- `[2.7002, 0.0, 2.4831, 0.0, 4.0985, 0.0, 18.9834, 0.0]`

Interpretation:
- unlike the old static Shot 12, this hold no longer shows one entry jump followed by a flat line
- visible state changes now recur across the shot instead of being confined to the opening frame
- because the shot is staged in `4.5s` chunks, the measured changes naturally land roughly every other 2-second sample

Practical meaning:
- the workflow shot now behaves like a step sequence rather than a parked checklist slide

## Findings
### 1) The Shot 12 bottleneck mechanism appears improved
The old Shot 12 pattern was:
- entry jump
- then no internal visible change at all

The new Shot 12 pattern is different in the right way:
- step 1 visible
- step 2 visible
- step 3 visible
- step 4 visible

Practical judgment:
- this is the first evidence that the late workflow hold may be solvable by the same staged-motion strategy that improved Shot 4

### 2) Keeping the full `18.0s` now looks more defensible
The earlier concern was not merely that Shot 12 lasted `18.0s`.
It was that the shot bought those seconds through stillness.

This prototype changes that.

Practical judgment:
- `18.0s` is more defensible if the viewer receives new checklist information in sequence rather than all at once
- the problem again looks more like **missing internal progression** than raw runtime alone

### 3) The remaining static suspects are now more concentrated in Shots 5 and 6
This review does **not** prove the whole piece is solved.
It only shows that the strongest late-stage target improved in the intended way.

Updated implication:
- if the next static-plateau pressure remains after this prototype, it is more likely to sit in Shot 5 and/or Shot 6 than in Shot 12

## Overall interpretation
This is a promising result.

Current local pacing story:
- Shot 4: improved by staged motion
- Shot 12: first staged-motion test also improves the flat-line problem
- the broader pattern is becoming clearer: when a long hold is conceptually a sequence, it performs better when the visual structure actually behaves like a sequence

## Recommended next move
Keep the next pass narrow.

Best next step:
1. run a fresh whole-piece review on `preview_animatic_v13.mp4` to check whether the staged Shot 12 fix improves the late sequence in context
2. if the piece still drags, inspect Shots 5 and 6 next
3. avoid reopening Shot 4 unless fresh evidence appears

## Decision
- **Status:** promising first Shot 12 motion result
- **Primary finding:** staged internal emphasis restores recurring visible changes inside the `18.0s` workflow shot
- **Current lean:** continue evaluating the staged Shot 12 path rather than trimming it immediately
- project status remains:
  - **not greenlit**
  - **not upload-ready**
  - **not phone-safe enough to claim**
  - still **PROMISING BUT STILL PREVIEW-GRADE**
