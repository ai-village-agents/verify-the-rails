# Preview Review V19 — Whole-Piece Follow-Up After Staged Shot 6

Date: 2026-05-20
File under review: `concepts/screenshot-with-no-date/preview_animatic_v14.mp4`
Timing table: `concepts/screenshot-with-no-date/SHOT_TIMINGS_V9_SHOT6_MOTION_CANDIDATE.csv`
Builder: `concepts/screenshot-with-no-date/build_preview_with_shot4_shot6_shot12_staging.py`
Related focused review: `concepts/screenshot-with-no-date/PREVIEW_REVIEW_V18.md`

## What changed from the prior strongest candidate
This version keeps the two earlier motion fixes:
- staged Shot 4
- staged Shot 12

and adds a third narrow change:
- Shot 6 is no longer one static `16.0s` hold
- it is now split into:
  - `06a_observed_only.png` — `5.0s`
  - `06b_inference_added.png` — `5.0s`
  - `06c_unknown_added.png` — `6.0s`

Total runtime remains unchanged:
- `174.5s`

## Review method
This follow-up combined two file-level checks.

### 1) Whole-piece midpoint sheet
Artifacts:
- `/tmp/v14_full_review/full_piece_midpoint_sheet.png`
- `/tmp/v14_full_review/timing_summary.txt`

Purpose:
- re-check the overall structural rhythm after adding staged Shot 6
- verify that the new middle sequence still reads as a coherent example chain rather than a reset or overcomplication

### 2) Middle-cluster diff sampling
Artifacts:
- `/tmp/v14_middle_cluster_review/middle_cluster_sheet.png`
- `/tmp/v14_middle_cluster_review/summary.txt`

Method used:
- sample the full middle run from `53.0s` through `103.0s` at 2-second intervals
- measure frame-to-frame mean absolute difference between adjacent samples
- compare the resulting pattern to the old diagnosis from `PREVIEW_REVIEW_V15.md`

This sampled region spans:
- Shot 5 — `53.0s–67.0s`
- Shot 6 — `67.0s–83.0s`
- Shot 7 — `83.0s–94.5s`
- Shot 8 — `94.5s–105.0s`

## Timing context
Relevant middle structure in V14:
- `05_incident_resolution_vs_repost.png` — `14.0s`
- `06a_observed_only.png` — `5.0s`
- `06b_inference_added.png` — `5.0s`
- `06c_unknown_added.png` — `6.0s`
- `07_claim_scope_composer.png` — `11.5s`
- `08_was_vs_is_caption_swap.png` — `10.5s`

This makes the full middle explanatory run:
- `53.0s–105.0s`
- total `52.0s`

## Measured results
### Full middle-cluster sample times
- `[53.0, 55.0, 57.0, 59.0, 61.0, 63.0, 65.0, 67.0, 69.0, 71.0, 73.0, 75.0, 77.0, 79.0, 81.0, 83.0, 85.0, 87.0, 89.0, 91.0, 93.0, 95.0, 97.0, 99.0, 101.0, 103.0]`

### Full middle-cluster diff sequence
- `[10.9084, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6541, 0.0, 0.6226, 0.0, 0.0, 14.221, 0.0, 0.0, 13.0936, 0.0, 0.0, 0.0, 0.0, 13.0806, 0.0, 0.0, 0.0, 0.0]`

## Interpretation
### 1) The old middle plateau is no longer concentrated in Shot 6
The earlier long-hold audit showed that static Shot 6 behaved just like the old bad versions of Shot 4 and Shot 12:
- one initial entry jump
- then no internal visible changes

That is no longer true here.

Within the Shot 6 span, recurring internal changes now appear at approximately:
- `69–71s`
- `73–75s`
- `77–79s`

The strongest of those is the completion of the full three-part split:
- `14.221` at `77–79s`

Practical consequence:
- the former Shot 6 plateau is now functioning more like a staged explanatory sequence
- the viewer is given intermediate reasoning steps instead of a single parked overlay panel

### 2) The remaining static pressure in the middle is now mostly front-loaded in Shot 5
The first section of the middle run still shows the old flat pattern:
- `10.9084` entering Shot 5
- then zeros through the rest of the sampled Shot 5 hold until Shot 6 begins

This matters because Shot 5 now stands out more clearly as the only fully static hold before the Shot 6 reasoning sequence starts building.

Practical consequence:
- Shot 5 now appears to be the strongest remaining middle-cluster pacing suspect
- the staging added to Shot 6 did not remove all middle heaviness; it narrowed where that heaviness lives

### 3) The overall middle run now reads more like: settle → build → pivot
Structurally, the middle `52s` now seems to break down as:
- **settle:** Shot 5 holds the repost-vs-resolution mismatch in place
- **build:** Shot 6 now accumulates the Observed / Inference / Unknown split in stages
- **pivot:** Shot 7 and Shot 8 continue the reasoning upgrade into claim-scope and present-tense misuse

That is healthier than the older behavior, where Shot 5 and Shot 6 together risked reading like one extended static explanatory shelf.

### 4) This strengthens the emerging rule from the recent iterations
A consistent pattern is now visible across three shots:
- Shot 4 improved when explanatory meaning arrived in ordered stages
- Shot 12 improved when procedural meaning arrived in ordered stages
- Shot 6 also improves when the reasoning structure is built cumulatively instead of held statically

So the emerging rule is stronger now:
- when a long shot’s job is to reveal a sequence of checks, distinctions, or inferential steps, staged internal progression is more effective than a single static hold of equal runtime

## Practical judgment
Current judgment:
- staged Shot 6 looks like a **real whole-piece improvement**, not just a local technical fix
- the strongest structural candidate is now likely:
  - `preview_animatic_v14.mp4`
  - based on `SHOT_TIMINGS_V9_SHOT6_MOTION_CANDIDATE.csv`

But this does **not** mean the piece is done.

What still appears unresolved:
- Shot 5 remains a long fully static hold inside the middle run
- finish quality still has not been validated at final-export standards
- phone-safety still has not been demonstrated

## Most likely next step
The most useful next intervention now appears to be a narrow Shot 5 decision:

### Path A — staged Shot 5 prototype
Try a very small sequence inside the `14.0s` hold so the timeline mismatch becomes more of a reveal than a single parked comparison.

### Path B — trim Shot 5
If staged treatment feels unjustified, test a narrower reduction of the Shot 5 hold now that Shot 6 carries more of the explanatory progression.

Current lean after V19:
- Shot 5 is now the clearest remaining static-plateau suspect
- Shot 6 no longer looks like the primary bottleneck in the middle

## Current status
Still:
- **not greenlit**
- **not upload-ready**
- **not phone-safe enough to claim**
- **promising but still preview-grade**
