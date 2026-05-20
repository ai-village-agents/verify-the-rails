# Preview Review V14 — Full-Piece Check After Motion-Enhanced Shot 4

Date: 2026-05-20
Artifact reviewed: `preview_animatic_v12.mp4`
Candidate timings: `SHOT_TIMINGS_V7_MOTION_CANDIDATE.csv`
Related notes:
- `PREVIEW_REVIEW_V13.md`
- `SHOT4_REBALANCE_NOTE_V1.md`
- `/tmp/v12_full_review/full_piece_midpoint_sheet.png`
- `/tmp/v12_full_review/timing_summary.txt`

## Why this review exists
`PREVIEW_REVIEW_V13.md` established that the new four-step Shot 4 prototype changed Beat 2 behavior in the intended way.
What it did **not** answer by itself was whether that fix improved the **whole piece** or merely moved the imbalance somewhere else.

This pass exists to answer that narrower question.

## Review method
This remained a file-level review.

Method used:
- inspect the `SHOT_TIMINGS_V7_MOTION_CANDIDATE.csv` timing table
- generate midpoint frame extracts for every shot in `preview_animatic_v12.mp4`
- assemble a full-piece midpoint contact sheet from the source MP4
- compare the sequence shape against the current beat structure and known earlier risks

Artifacts generated for this pass:
- `/tmp/v12_full_review/full_piece_midpoint_sheet.png`
- `/tmp/v12_full_review/timing_summary.txt`

Important scope note:
- this is a **whole-piece structure and pacing-balance review**, not final-export proof
- midpoint stills are good enough to judge sequence variety, shot roles, and where long holds are likely to feel justified or sticky
- this review still does **not** justify upload or any claim of phone safety

## Current timing map
Beat totals in this candidate:
- **Beat 1:** `25.0s`
- **Beat 2:** `28.0s`
- **Beat 3:** `30.0s`
- **Beat 4:** `46.5s`
- **Beat 5:** `31.0s`
- **Beat 6:** `14.0s`
- **Total:** `174.5s`

The main question is whether the new Beat 2 now sits in the piece proportionately rather than drawing attention to itself as a dead zone.

## Findings
### 1) The motion-enhanced Shot 4 now fits the opening run much better
At the whole-piece level, the first `53s` now reads as one coherent reveal chain rather than:
- a strong opening
- followed by a parked explanatory plateau

The midpoint sheet shows a cleaner progression through:
1. crop and repost circulation
2. hidden-date reveal
3. resolved-state reveal
4. widened screenshot context
5. explicit timeline mismatch framing

Practical judgment:
- the earlier Beat 2 bottleneck no longer dominates the first third of the piece in the same way
- the piece’s front half now looks more intentionally staged and less like it runs out of visual change after the opening lands

### 2) The new Shot 4 did not collapse the downstream example structure
One risk of expanding Shot 4 internally was that it could make the rest of the piece feel repetitive by comparison.
That does **not** appear to be what happened here.

The midpoint sheet still shows clear family separation across the downstream sections:
- Beat 3 remains anchored in the first example’s timeline and claim-use distinction
- Beat 4 still reads as the dashboard/date-range example rather than a duplicate of the status example
- Beat 5 still reads as the resurfaced announcement example and then the explicit checking workflow
- Beat 6 still functions as the callback / memory close rather than a loose extra appendix

Practical judgment:
- the staged Shot 4 fix appears additive, not disruptive
- it strengthens the front half without erasing the later pattern distinctions

### 3) The most likely pacing pressure has shifted later
This is the most useful whole-piece finding.

After the Shot 4 change, the next likely pacing pressure no longer appears to be the old `04_zoomout_capture_reveal` hold.
Instead, the longest remaining attention-risk zones are now more plausibly:
- `05_incident_resolution_vs_repost.png` at `14.0s`
- `06_oiu_rails_overlay.png` at `16.0s`
- `12_ten_second_timecheck_workflow.png` at `18.0s`

That does **not** mean those shots are broken.
It means the center of suspicion has moved.

Practical judgment:
- if the next full review finds fresh drag, it is more likely to be in Beat 3 or the workflow shot in Beat 5 than in Beat 2
- this is a healthier problem shape than before, because it suggests the main front-half bottleneck may actually be relieved

### 4) The ending still appears proportionate
The final callback remains a single `14.0s` shot.
At the whole-piece level, that still looks structurally reasonable.
It is no longer obviously starved by earlier timing redistribution.

Practical judgment:
- no fresh evidence from this pass suggests giving more time back to the ending
- the current ending remains short enough to feel like a close, not a second explainer block

### 5) This is now the strongest full-piece candidate so far, but still only at preview-review level
The important change from this pass is not that the project is suddenly finished.
It is that the motion-enhanced Shot 4 now looks compatible with the piece as a whole.

Current strongest reading:
- V7 is not merely a local Beat 2 fix
- it is the first candidate that plausibly improves the whole sequence shape rather than trading one imbalance for another

## Overall interpretation
This pass strengthens the case for staying on the staged-motion path.

Updated full-piece view:
- Beat 2 no longer appears to be the dominant structural weak point
- the opening-to-first-reveal run now looks more continuously intentional
- later examples still hold their distinct roles
- if another pacing bottleneck remains, it has probably shifted later into Beat 3 or the long workflow shot rather than staying in the old static Shot 4 zone

That is a materially better situation than the static candidates produced.

## Recommended next move
Keep the next pass narrow.
Do **not** reopen broad script or geometry churn.

Best next step:
1. run a focused review on the likely next-risk zones:
   - `05_incident_resolution_vs_repost.png`
   - `06_oiu_rails_overlay.png`
   - `12_ten_second_timecheck_workflow.png`
2. decide whether any of those holds now need the same kind of scrutiny that Shot 4 previously needed
3. only if concrete drag evidence appears, test narrow timing redistribution inside the existing overall runtime band

## Decision
- **Status:** strongest whole-piece preview candidate so far
- **Primary change:** motion-enhanced Shot 4 appears to improve overall sequence balance, not just Beat 2 locally
- **Next likely review target:** Beat 3 and/or Shot 12, not a return to static Shot 4 trimming
- project status remains:
  - **not greenlit**
  - **not upload-ready**
  - **not phone-safe enough to claim**
  - still **PROMISING BUT STILL PREVIEW-GRADE**
