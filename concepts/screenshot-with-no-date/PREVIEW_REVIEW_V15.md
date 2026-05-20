# Preview Review V15 — Long-Hold Audit After the Shot 4 Motion Fix

Date: 2026-05-20
Artifact reviewed: `preview_animatic_v12.mp4`
Candidate timings: `SHOT_TIMINGS_V7_MOTION_CANDIDATE.csv`
Related notes:
- `PREVIEW_REVIEW_V14.md`
- `PREVIEW_REVIEW_V13.md`
- `/tmp/v12_longhold_review/`

## Why this review exists
`PREVIEW_REVIEW_V14.md` concluded that the motion-enhanced Shot 4 likely improved the whole sequence shape and shifted the next likely pacing-risk zone later in the piece.

This pass tests that directly.

The goal here is narrow:
- inspect the three longest remaining static-hold candidates that now look most likely to drag
- see whether they behave like the old static Shot 4 problem
- identify the next best target for either staged motion or narrow timing redistribution

## Review method
File-level sampling again remained primary.

Shots tested:
- `05_incident_resolution_vs_repost.png` — `14.0s`
- `06_oiu_rails_overlay.png` — `16.0s`
- `12_ten_second_timecheck_workflow.png` — `18.0s`

Method used:
- extract frames from `preview_animatic_v12.mp4` at 2-second intervals inside each target hold
- measure frame-to-frame mean absolute difference between each adjacent sample
- compare the resulting change pattern to the old Shot 4 static-hold diagnosis

Artifact directory:
- `/tmp/v12_longhold_review/`

## Measured results
### Shot 5 — `05_incident_resolution_vs_repost.png` (`53.0s–67.0s`)
Sample times:
- `[53.0, 55.0, 57.0, 59.0, 61.0, 63.0, 65.0]`

Diff sequence:
- `[11.7924, 0.0, 0.0, 0.0, 0.0, 0.0]`

Interpretation:
- one initial entry jump, then no internal visible state changes across the remaining sampled hold

### Shot 6 — `06_oiu_rails_overlay.png` (`67.0s–83.0s`)
Sample times:
- `[67.0, 69.0, 71.0, 73.0, 75.0, 77.0, 79.0, 81.0]`

Diff sequence:
- `[14.3057, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`

Interpretation:
- again, one initial entry jump followed by a flat line through the rest of the hold

### Shot 12 — `12_ten_second_timecheck_workflow.png` (`142.5s–160.5s`)
Sample times:
- `[142.5, 144.5, 146.5, 148.5, 150.5, 152.5, 154.5, 156.5, 158.5]`

Diff sequence:
- `[15.8575, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`

Interpretation:
- same pattern: one entry jump, then effectively no sampled internal state changes across the long hold

## Findings
### 1) The new likely bottlenecks are real
The V14 suspicion was correct.

All three tested long holds now show the same basic pattern the old static Shot 4 showed:
- an entry jump into the shot
- then an essentially static plateau

Practical judgment:
- the earlier Shot 4 bottleneck was not a one-off accident
- the same measurement method now identifies the next likely pacing pressure later in the piece

### 2) Shot 12 is the strongest candidate for the next narrow intervention
All three shots are static by this sampling method, but `12_ten_second_timecheck_workflow.png` is the strongest next candidate for focused intervention because:
- it is the longest of the three at `18.0s`
- it sits late enough that drag would be especially costly
- it is a procedural / checklist shot, which makes it a natural fit for staged internal emphasis

Practical judgment:
- if only one long-hold shot gets the next motion-style treatment, Shot 12 is the best first target

### 3) Shot 5 and Shot 6 may still be acceptable as static if their semantic job is narrower
The measurement result alone does **not** prove that every static hold is bad.
It only proves that these shots do not generate internal visible state changes on their own.

Possible distinction:
- Shot 5 may still function as a simpler explanatory pause if its role is just to let the first example settle
- Shot 6 may still function if the overlay reading experience truly needs the time
- Shot 12 is less defensible as a totally static long hold because it represents a workflow and therefore naturally invites stepwise reveal

Practical judgment:
- do **not** assume all three shots need equal intervention
- prioritize the one whose role most obviously benefits from staged progression

## Overall interpretation
The Shot 4 motion fix appears to have succeeded strongly enough that the next bottlenecks are now visible.
That is progress.

Updated diagnosis:
- Beat 2 is no longer the main suspect
- the next static-plateau risks are now concentrated in Shots 5, 6, and especially 12
- the project’s next best move is **not** to reopen Shot 4
- it is to decide whether Shot 12 should gain internal staged motion, or whether one of these later holds should be trimmed narrowly

## Recommended next move
Keep the next pass narrow.

Best next step:
1. prototype staged internal emphasis for `12_ten_second_timecheck_workflow.png`
   - sequentially reveal or emphasize the checklist steps rather than showing the whole workflow at once
2. only after that decide whether Shots 5 or 6 also need treatment
3. if Shot 12 remains static, test a narrow trim before touching earlier beats again

## Decision
- **Status:** next bottleneck candidates confirmed by file-level sampling
- **Strongest next target:** `12_ten_second_timecheck_workflow.png`
- **Strategic implication:** continue solving pacing through staged internal progression, not by reopening solved Shot 4 work
- project status remains:
  - **not greenlit**
  - **not upload-ready**
  - **not phone-safe enough to claim**
  - still **PROMISING BUT STILL PREVIEW-GRADE**
