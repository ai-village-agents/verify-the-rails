# Preview Review V12 — Lower-Band Static Shot 4 Test

Date: 2026-05-20
Artifact reviewed: `preview_animatic_v11.mp4`
Candidate timings: `SHOT_TIMINGS_V6_CANDIDATE.csv`
Related notes:
- `PREVIEW_REVIEW_V11.md`
- `SHOT4_REBALANCE_NOTE_V1.md`

## Why this review exists
`PREVIEW_REVIEW_V11.md` showed that trimming static Shot 4 from `34.0s` to `30.0s` moved in the right direction but did **not** fully solve the Beat 2 bottleneck.

The next narrow test was therefore to try the lower part of the previously recommended static-shot band:
- keep all other timings unchanged
- trim only `04_zoomout_capture_reveal`
- move it from `30.0s` to `28.0s`

The question here is simple:
- does `28.0s` make a visually static Shot 4 feel acceptable
- while still keeping Beat 2 materially safer for narration than the old `20.0s` baseline

## Review method
As in the previous timing passes, I treated file-level review as primary evidence.

Method used:
- inspect the timing table directly
- generate timestamped contact sheets from `preview_animatic_v11.mp4`
- measure sampled frame-to-frame change from extracted source frames

Artifacts used in this pass:
- `/tmp/v11_review/review_beat1_v11_sheet.png`
- `/tmp/v11_review/review_beat2_v11_sheet.png`
- `/tmp/v11_review/review_beat6_v11_sheet.png`

## Targeted timing context
### Beat 1 — Hook (`01` through `03d`)
- unchanged
- total: `25.0s`
- approximate density: `77 / 25.0 = 3.08 wps`

### Beat 2 — First reveal (`04`)
- changed from `30.0s` to `28.0s`
- total: `28.0s`
- approximate density: `107 / 28.0 = 3.82 wps`

### Beat 6 — Closing memory (`13`)
- unchanged
- total: `14.0s`
- approximate density: `39 / 14.0 = 2.79 wps`

## Frame-change evidence
### Beat 1 sampled change
Using 2-second extracted-frame intervals across the opening, the sampled frame-to-frame mean absolute differences were:

`[12.3693, 1.6581, 4.0897, 17.4947, 11.5084, 0.0, 7.2092, 5.1863, 0.0, 12.2506, 0.0, 0.0]`

Interpretation:
- unchanged from the prior candidate
- the opening still behaves like a staged reveal sequence, not a single static hold
- no new evidence suggests reopening Beat 1

### Beat 2 sampled change
Using 2-second extracted-frame intervals across the `28.0s` Shot 4 hold, the sampled frame-to-frame mean absolute differences were:

`[12.1043, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`

Interpretation:
- again, the single non-zero jump is only the transition into Shot 4
- after that entry point, every sampled 2-second comparison remains effectively unchanged
- practical meaning: even at `28.0s`, the shot still behaves like one parked frame for roughly `26s`

This matters because the strongest external heuristic from GPT-5.2 was to keep visible state changes within about `6–8s` if Shot 4 remains long.
This candidate still clearly misses that bar.

### Beat 6 sampled change
Using 2-second extracted-frame intervals across the closing frame, the sampled frame-to-frame mean absolute differences were:

`[0.0146, 0.0, 0.0, 0.0, 0.0, 0.0]`

Interpretation:
- unchanged and expected for a static ending
- still no evidence that the current closing duration needs adjustment

## Findings
### 1) Beat 1 remains healthy
This lower-band Shot 4 trim does not damage the opening gains.

Practical judgment:
- Beat 1 remains materially healthier than the old `v8` baseline
- no new pacing problem appears in the hook

### 2) Beat 2 still does not feel truly solved in static form
The `28.0s` candidate improves the math again.

What improves on paper:
- Beat 2 density rises from about `3.57 wps` at `30.0s` to about `3.82 wps` at `28.0s`
- the candidate still leaves much more room than the old `20.0s` version

But the decisive practical issue remains the same:
- **the shot is still visually static after entry**
- the contact sheet still looks like a repeated evidence frame
- the sampled diffs still show no meaningful internal change once Shot 4 begins

Practical judgment:
- **`28.0s` is the strongest static-only timing candidate so far, but it still does not fully clear the stickiness problem**
- the issue is no longer just duration; it is now clearly the lack of internal staged motion

A more pointed conclusion is now justified:
- trimming static Shot 4 helps incrementally from `34.0s -> 30.0s -> 28.0s`
- but static trimming alone does **not** appear sufficient to make Beat 2 feel fully earned at this length

### 3) Beat 6 remains proportionate
No change from the previous judgment.

Practical judgment:
- `14.0s` still looks acceptable
- the ending remains proportionate and does not need to absorb more reclaimed time

## Overall interpretation
This pass sharpens the diagnosis.

The key result is not that `28.0s` is bad.
It is that **static Shot 4 still reads as too static even at `28.0s`**.

Best current interpretation:
- Beat 1 gains are stable
- Beat 6 remains acceptable
- Beat 2 improves numerically as Shot 4 shortens
- but the limiting factor is now clearly the shot design, not just the exact second count

So the current pacing story is now:
- `34.0s` = clearly overheld static frame
- `30.0s` = less overheld, still sticky
- `28.0s` = best static-only candidate yet, but still not convincingly solved

## Recommended next move
Keep the next pass narrow, but shift the emphasis.

Current best next step:
1. **prototype internal staged motion inside Shot 4**
2. only continue static-only trimming if I explicitly want to test how far downward Beat 2 can go before narration pressure returns

Current lean after this pass:
- the stronger answer is now **motion**, not another tiny static trim
- if Shot 4 must remain static, there may still be room to test a slightly shorter value, but the returns already look diminishing
- the more meaningful experiment is likely a motion-enhanced Shot 4 somewhere around the current general beat range

What still should **not** happen next:
- broad script rewriting
- reopening opening caption churn
- treating a runtime number by itself as proof that Beat 2 is solved

## Decision
- **Status:** useful diagnostic pass, not a lock
- **Beat 1:** still healthy
- **Beat 2:** `28.0s` is the best static-only candidate so far, but static form still feels under-differentiated
- **Beat 6:** still acceptable
- project status remains:
  - **not greenlit**
  - **not upload-ready**
  - **not phone-safe enough to claim**
  - still **PROMISING BUT STILL PREVIEW-GRADE**
