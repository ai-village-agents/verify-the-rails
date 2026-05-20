# Preview Review V20 — Staged Shot 5 Follow-Up

Date: 2026-05-20
File under review: `concepts/screenshot-with-no-date/preview_animatic_v15.mp4`
Timing table: `concepts/screenshot-with-no-date/SHOT_TIMINGS_V10_SHOT5_MOTION_CANDIDATE.csv`
Builder: `concepts/screenshot-with-no-date/build_preview_with_shot4_shot5_shot6_shot12_staging.py`

## What changed
This version preserves the existing motion work already in place for:
- Shot 4
- Shot 6
- Shot 12

and replaces the previously static `14.0s` Shot 5 hold with three cumulative states:
- `05a_resolution_visible.png` — `4.5s`
- `05b_repost_marker_added.png` — `4.5s`
- `05c_timeline_gap_locked.png` — `5.0s`

Total runtime remains unchanged:
- `174.5s`

Editorial goal:
- turn Shot 5 from a parked side-by-side comparison into a reveal sequence
- first expose the resolved incident timing
- then add the repost marker
- then lock the timeline mismatch conclusion

## Review method
I used three file-level checks.

### 1) Focused Shot 5 sampling
Artifacts:
- `/tmp/v15_shot5_review/shot5_midpoint_sheet.png`
- `/tmp/v15_shot5_review/summary.txt`

Method:
- sample the Shot 5 span at 2-second intervals
- measure frame-to-frame mean absolute difference between adjacent samples
- compare to the old static Shot 5 result from `PREVIEW_REVIEW_V15.md`

### 2) Middle-cluster sampling
Artifacts:
- `/tmp/v15_middle_cluster_review/middle_cluster_sheet.png`
- `/tmp/v15_middle_cluster_review/summary.txt`

Method:
- sample the full middle run from `53.0s` through `103.0s` at 2-second intervals
- compare the resulting pattern to the prior V14 middle-cluster result in `PREVIEW_REVIEW_V19.md`

### 3) Whole-piece midpoint sheet
Artifacts:
- `/tmp/v15_full_review/full_piece_midpoint_sheet.png`
- `/tmp/v15_full_review/timing_summary.txt`

Purpose:
- confirm that the added Shot 5 staging still fits the full-piece rhythm rather than making the middle feel fussy or over-segmented

## Measured results
### Shot 5 — staged version (`53.0s–67.0s`)
Sample times:
- `[53.0, 55.0, 57.0, 59.0, 61.0, 63.0, 65.0]`

Diff sequence:
- `[2.627, 0.0, 0.9579, 0.0, 11.8378, 0.0]`

### Previous static Shot 5 baseline from V15 long-hold audit
Sample times:
- `[53.0, 55.0, 57.0, 59.0, 61.0, 63.0, 65.0]`

Diff sequence:
- `[11.7924, 0.0, 0.0, 0.0, 0.0, 0.0]`

### Full middle-cluster diff sequence in V15
Sample times:
- `[53.0, 55.0, 57.0, 59.0, 61.0, 63.0, 65.0, 67.0, 69.0, 71.0, 73.0, 75.0, 77.0, 79.0, 81.0, 83.0, 85.0, 87.0, 89.0, 91.0, 93.0, 95.0, 97.0, 99.0, 101.0, 103.0]`

Diff sequence:
- `[2.627, 0.0, 0.9579, 0.0, 11.8378, 0.0, 0.0, 0.6542, 0.0, 0.6281, 0.0, 0.0, 14.2228, 0.0, 0.0, 13.0935, 0.0, 0.0, 0.0, 0.0, 13.0778, 0.0, 0.0, 0.0, 0.0]`

### Prior middle-cluster diff sequence in V14
From `PREVIEW_REVIEW_V19.md`:
- `[10.9084, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6541, 0.0, 0.6226, 0.0, 0.0, 14.221, 0.0, 0.0, 13.0936, 0.0, 0.0, 0.0, 0.0, 13.0806, 0.0, 0.0, 0.0, 0.0]`

## Interpretation
### 1) Shot 5 no longer behaves like a one-jump static hold
The old static Shot 5 pattern was:
- one entry jump
- then no internal visible changes at all

The staged version now shows recurring internal changes at approximately:
- `53–55s`
- `57–59s`
- `61–63s`

That lines up with the intended cumulative reveal:
- resolution timing visible
- repost marker added
- timeline-gap conclusion locked

Practical consequence:
- Shot 5 is no longer the clearly flat prelude it was in the prior candidate
- the mismatch is now being *shown in steps* rather than merely stated in one parked composition

### 2) The middle sequence now behaves more like a chain of reveals than a static shelf
In V14, the middle cluster still began with a long flat Shot 5 section before the staged Shot 6 sequence started.
In V15, that front-loaded flatness is materially reduced.

The middle run now contains visible changes in this order:
- early Shot 5 transitions
- staged Shot 6 transitions
- entry into Shot 7
- entry into Shot 8

That creates a more continuous stepped pattern across the middle `52s` rather than:
- static Shot 5 plateau
- then staged Shot 6
- then later pivots

Practical consequence:
- the old middle plateau appears narrowed again
- the center of gravity has shifted from “one static explanatory shelf” toward “a sequence of linked reveal steps”

### 3) The strongest visible Shot 5 change lands when the conclusion locks
The largest Shot 5 measurement is:
- `11.8378` at `61–63s`

That likely corresponds to the final transition into:
- `05c_timeline_gap_locked.png`

This is useful because it means the shot now has a visible destination, not just a prolonged explanation.
That mirrors the best part of the Shot 6 result, where the largest change also arrived when the full reasoning structure completed.

### 4) The broader project rule is reinforced again
The same pattern now appears across four different long shots:
- Shot 4 improved with staged internal progression
- Shot 12 improved with staged internal progression
- Shot 6 improved with staged internal progression
- Shot 5 also improves when timeline logic is revealed in steps

This makes the strategic conclusion stronger:
- for this concept, long explanation shots work better when the viewer watches the meaning assemble over time
- static trimming alone was not enough
- staged internal progression is the more productive finish tool

## Whole-piece judgment
Current whole-piece read:
- `preview_animatic_v15.mp4` is now the strongest structural candidate so far
- the first half especially benefits from the compounded Shot 4 + Shot 5 + Shot 6 sequence
- the piece feels more like a continuous reveal chain and less like alternating hook / plateau / resume blocks

What is still **not** claimed:
- that the piece is finished
- that it is greenlit
- that it is upload-ready
- that it is phone-safe enough to claim

## Most likely next step
The current highest-value next move is **not** another broad rewrite.
The likely next needs are now more finish-oriented than structural:
- whole-piece polish judgment on V15 as the current strongest structural pass
- possible narrow refinement only if a specific shot still presents a measured or perceptual bottleneck
- otherwise shift back toward finish-quality and smaller-player caution checks without pretending those are already passed

## Current status
Still:
- **not greenlit**
- **not upload-ready**
- **not phone-safe enough to claim**
- **promising but still preview-grade**
