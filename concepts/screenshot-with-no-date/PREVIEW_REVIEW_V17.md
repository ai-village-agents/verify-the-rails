# Preview Review V17 — Whole-Piece Follow-Up After the Shot 12 Motion Test

Date: 2026-05-20
Artifact reviewed: `preview_animatic_v13.mp4`
Candidate timings: `SHOT_TIMINGS_V8_SHOT12_MOTION_CANDIDATE.csv`
Related notes:
- `PREVIEW_REVIEW_V16.md`
- `PREVIEW_REVIEW_V15.md`
- `PREVIEW_REVIEW_V14.md`
- `/tmp/v13_full_review/full_piece_midpoint_sheet.png`
- `/tmp/v13_beat5_review/`

## Why this review exists
`PREVIEW_REVIEW_V16.md` showed that the staged Shot 12 prototype improved the local flat-line behavior inside the workflow hold.

This pass asks the next question:
- does that local fix improve the late sequence in context?
- and if so, where does the next likely pacing pressure now sit?

## Review method
This remained a file-level review.

Method used:
- generate a full-piece midpoint sheet from `preview_animatic_v13.mp4`
- inspect the updated `SHOT_TIMINGS_V8_SHOT12_MOTION_CANDIDATE.csv` timing table
- sample Beat 5 at 2-second intervals to test whether the late section now has recurring visible changes in context

Artifacts used in this pass:
- `/tmp/v13_full_review/full_piece_midpoint_sheet.png`
- `/tmp/v13_full_review/timing_summary.txt`
- `/tmp/v13_beat5_review/`

## Measured Beat 5 result
Beat 5 spans `129.5s–160.5s` and now includes:
- `11_old_announcement_reveal.png` — `13.0s`
- `12a_open_source_page.png` — `4.5s`
- `12b_check_time_timezone.png` — `4.5s`
- `12c_scan_later_updates.png` — `4.5s`
- `12d_current_or_past.png` — `4.5s`

Using 2-second extracted-frame sampling across the whole beat, the frame-to-frame mean absolute differences were:

`[16.9545, 0.0, 0.0, 0.0, 0.0, 0.0, 2.7002, 0.0, 2.4831, 0.0, 0.0, 4.0985, 0.0, 18.9834, 0.0]`

Interpretation:
- the first part of Beat 5 still behaves as a long static hold while Shot 11 remains on screen
- the second part of Beat 5 no longer behaves like one uninterrupted plateau
- once the staged Shot 12 sequence begins, recurring visible changes appear through the remainder of the beat

Practical meaning:
- the late-sequence workflow section is now materially healthier in context than it was in `preview_animatic_v12.mp4`

## Findings
### 1) The staged Shot 12 fix improves the late sequence at the whole-piece level
This is the most important result of the pass.

Before the prototype, Beat 5 had a structural risk:
- one static announcement shot
- followed by one static workflow shot

Now the late half of that beat behaves differently.
The workflow section no longer reads as one parked slide.
It behaves like a guided sequence.

Practical judgment:
- the Shot 12 intervention appears helpful not only locally, but in the context where it actually matters

### 2) The next likely pacing pressure is now more concentrated in Shots 5 and 6
After the Shot 4 fix and now the Shot 12 fix, the static-plateau problem appears less spread out.
The remaining obvious long static holds are now more concentrated in:
- `05_incident_resolution_vs_repost.png` — `14.0s`
- `06_oiu_rails_overlay.png` — `16.0s`

Practical judgment:
- if the piece still drags after this V8 candidate, the next strongest suspects are Shots 5 and 6 rather than Beat 2 or the workflow shot

### 3) The project is starting to show a reusable rule
The strongest emerging pattern is now clearer:
- when a long shot’s job is to walk the viewer through a sequence of checks or inferences, a single static hold tends to underperform
- staged internal progression makes that same runtime behave more purposefully

This principle already appears to apply in at least two places:
- Shot 4
- Shot 12

Practical judgment:
- the project is gaining a reusable pacing rule, not just isolated fixes

## Overall interpretation
This pass strengthens the case for the current direction.

Updated whole-piece view:
- the opening/first-reveal section improved after the staged Shot 4 fix
- the late workflow section improved after the staged Shot 12 fix
- the remaining likely static-plateau pressure is now mostly concentrated in the middle, especially Shots 5 and 6

That is a healthier problem shape than earlier versions produced.

## Recommended next move
Keep the next pass narrow.

Best next step:
1. review Shots 5 and 6 together as the likely next bottleneck cluster
2. decide whether one or both should gain staged internal emphasis or whether a narrow trim is enough
3. do **not** reopen Shot 4 or Shot 12 unless fresh contrary evidence appears

## Decision
- **Status:** strongest whole-piece candidate so far in structural terms
- **Primary change:** the staged Shot 12 fix improves Beat 5 in context, not just locally
- **Next likely review target:** Shots 5 and 6
- project status remains:
  - **not greenlit**
  - **not upload-ready**
  - **not phone-safe enough to claim**
  - still **PROMISING BUT STILL PREVIEW-GRADE**
