# Shot 4 Rebalance Note V1

Date: 2026-05-20
Related review: `PREVIEW_REVIEW_V10.md`
Current candidate timings: `SHOT_TIMINGS_V4_CANDIDATE.csv`
Current candidate preview: `preview_animatic_v9.mp4`

## Why this note exists
`PREVIEW_REVIEW_V10.md` changed the pacing diagnosis.

The strongest new review result was:
- Beat 1 improved materially
- Beat 6 survived the trim
- **Shot 4 / Beat 2 is now the clearest pacing bottleneck**

So the next pass should be narrow:

> do not reopen the whole timing table blindly; solve the Shot 4 overhold problem as locally as possible.

## Current problem statement
Shot 4 currently holds for `34.0s`.

That solved the earlier narration-density problem on paper, but the review evidence now shows a different risk:
- the frame is almost entirely static across the hold
- the extra seconds are in the correct *region* of the story
- but they are not yet justified by enough internal visual change

In other words:
- the candidate improved **timing allocation**
- but did not yet improve **visual change density** inside Beat 2

## What should happen next
There are only two good paths from here.

### Path A — Keep Beat 2 long only if Shot 4 gains internal staging
This is the stronger creative option if the concept continues.

Possible internal staging moves inside the same shot:
1. sequence the explanatory emphasis instead of presenting all interpretation at once
2. highlight the timestamp, repost date, and claim reversal in ordered steps
3. use subtle panel emphasis / arrows / callouts so the frame earns the longer dwell
4. let the narration and visual emphasis progress together instead of sitting on one unchanged tableau

Principle:
- if Shot 4 stays long, it should **behave like a mini reveal**, not a static pause

### Path B — Trim Shot 4 if no new internal motion is added
If the frame remains visually static, the safer next move is simply to shorten it.

Good working range to test:
- roughly **`28s` to `31s`**

Why that range:
- shorter than `34.0s`, which currently looks sticky
- still materially longer than the old `20.0s`, which was too compressed
- preserves the central lesson from the candidate: Beat 2 really did need more room than `v8` gave it

## What should not happen
- do **not** reopen broad script rewriting first
- do **not** undo the Beat 1 gains just because Beat 2 now needs refinement
- do **not** put all reclaimed Shot 4 time back into the ending automatically
- do **not** treat total runtime alone as the success metric

## Best next implementation order
1. decide whether Shot 4 will gain internal staged motion
2. if yes, keep Beat 2 in the current general range and test the motion-enhanced version
3. if no, make a narrow timing candidate with Shot 4 trimmed into the `28s–31s` range
4. review the new candidate again specifically on:
   - Beat 2 stickiness
   - whether Beat 1 remains healthy
   - whether the whole piece stays inside a plausible narration band

## Current status reminder
Even after the `v10` review, this project remains:
- **not greenlit**
- **not upload-ready**
- **not phone-safe enough to claim**
- still **PROMISING BUT STILL PREVIEW-GRADE**

## Concrete midpoint candidate now built locally
A narrow midpoint test was created after this note:
- `SHOT_TIMINGS_V5_CANDIDATE.csv`
- only change vs `V4`: `04_zoomout_capture_reveal` reduced from `34.0s` to `30.0s`
- new total timing table: **`176.5s`**
- local render: `preview_animatic_v10.mp4`
- `ffprobe` duration: **`176.56s`**

Why this specific test is useful:
- it stays inside the recommended `28s–31s` trial band
- it trims the clearest static overhold without undoing the Beat 1 gains
- it remains materially longer than the old `20.0s` Shot 4 baseline

This is still only a candidate until it gets a focused review.

## V6 lower-band static test candidate
Created:
- `SHOT_TIMINGS_V6_CANDIDATE.csv`

Only change vs V5:
- `04_zoomout_capture_reveal`: **`30.0s -> 28.0s`**

Everything else remained the same as V5.

Computed total:
- **`174.5s`**

Built local:
- `preview_animatic_v11.mp4`
- `ffprobe` duration: **`174.56s`**

Purpose:
- test the lower part of the previously recommended static-shot trim band
- keep Beat 2 materially safer than the old `20.0s` baseline
- ask whether a static Shot 4 becomes tolerable once it sits closer to `28s` than `30s–34s`
- **still only a candidate until reviewed**

## V7 first motion-enhanced Shot 4 candidate
Created:
- `render_shot4_staging_prototype.py`
- `build_preview_with_shot4_staging.py`
- `SHOT_TIMINGS_V7_MOTION_CANDIDATE.csv`

Design change:
- replace the single static `04_zoomout_capture_reveal` hold with four staged Shot 4 frames:
  - `04a_capture_time_visible.png`
  - `04b_repost_gap.png`
  - `04c_claim_scope_shift.png`
  - `04d_timeline_mismatch.png`
- each stage currently holds for `7.0s`
- total Beat 2 time remains **`28.0s`**

Computed total:
- **`174.5s`**

Built local:
- `preview_animatic_v12.mp4`
- `ffprobe` duration: **`174.56s`**

Why this prototype exists:
- the static-only trims (`34 -> 30 -> 28`) showed diminishing returns
- the stronger remaining hypothesis was that Beat 2 needed **internal state changes**, not just fewer seconds
- this version tests whether staged reveal inside Shot 4 can keep Beat 2 long enough for narration while avoiding the long parked-frame feel
