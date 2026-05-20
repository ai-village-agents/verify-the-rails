# Preview Review V10 — Candidate Timing Pass Spot-Check

Date: 2026-05-20
Artifact reviewed: `preview_animatic_v9.mp4`
Candidate timings: `SHOT_TIMINGS_V4_CANDIDATE.csv`
Related planning note: `TIMING_REDISTRIBUTION_PLAN_V1.md`

## Why this review exists
After the beat-level timing redistribution plan landed, the next useful question was not the total runtime.
It was whether the new timing shape actually improved the right sections.

The narrow review targets were:
- whether **Beat 1** now feels narration-plausible rather than sprinted
- whether **Beat 2** can carry its new expanded dwell without turning sticky
- whether **Beat 6** became too abrupt after the large trim

## Review method
I first tried reviewing smaller local MP4 beat clips in Firefox.
That surface was still unreliable enough that I do **not** want to treat it as the main evidence source.

Useful fallback method:
- generate timestamped contact sheets directly from `preview_animatic_v9.mp4`
- inspect the actual visual change density inside the targeted beats
- combine that with the known shot durations from `SHOT_TIMINGS_V4_CANDIDATE.csv`

Artifacts used in this pass:
- `review_beat1_sheet.png`
- `review_beat2_sheet.png`
- `review_beat6_sheet.png`

Caution learned during this pass:
- copy-trimmed review clips made with stream copy were misleading for this low-fps animatic
- example: `review_beat1_v9.mp4` probed as `59.04s` instead of the intended `25.0s`
- for this concept, direct source-MP4 frame extraction is more trustworthy than quick copy-trim clips

## Targeted timing context
### Beat 1 — Hook (`01` through `03d`)
- total: `25.0s`
- shot breakdown:
  - `01_open_crop`: `3.5s`
  - `02a_repost_velocity_one`: `1.7s`
  - `02b_repost_velocity_two`: `1.7s`
  - `02_repost_velocity_stack`: `2.4s`
  - `03a_hidden_ui_crop_only`: `3.0s`
  - `03b_reveal_capture_date`: `3.4s`
  - `03c_reveal_incident_log`: `3.8s`
  - `03d_reveal_resolution`: `5.5s`

### Beat 2 — First reveal (`04`)
- total: `34.0s`
- single-shot hold:
  - `04_zoomout_capture_reveal`: `34.0s`

### Beat 6 — Closing memory (`13`)
- total: `14.0s`
- single-shot hold:
  - `13_return_full_context_resolved`: `14.0s`

## Findings
### 1) Beat 1 looks materially healthier than the `v8` opening
The main good news is that the redistributed opening now has enough room to read as a reveal chain rather than a flash sequence.

What the beat-1 sheet shows:
- the repost build-up is no longer compressed into near-instant flashes
- the move from crop-only to capture-date to incident-log to resolved-state reveal now has visible dwell between meaning changes
- the final resolved-state hold is long enough to let the interpretation actually flip before the piece hands off to the wider explanation

Practical judgment:
- **Beat 1 now looks plausibly narration-capable in a way `v8` did not**
- the two `1.7s` repost steps are still brisk, but they function more like rhythmic accumulation than a comprehension failure
- the more important later reveals now have enough room to do their job

This appears to be a real improvement, not just a paper improvement in words-per-second.

### 2) Beat 2 now looks like the new pacing problem
The strongest negative finding is that the new `34.0s` hold on Shot 4 appears visually under-differentiated.

What the beat-2 sheet shows:
- the same zoomed-out evidence frame repeats across the whole sampled span
- at 2-second intervals from roughly `00:30` through `00:58`, the frame appears essentially unchanged
- this means the extra room is being bought in the mathematically right area, but with almost no internal visual evolution

Practical judgment:
- **Beat 2 is no longer obviously under-timed for narration math, but it now risks feeling sticky because it is almost entirely a static hold**
- this is a different problem from the old `v8` compression problem
- if Shot 4 stays visually static, `34.0s` is probably too generous

Best current interpretation:
- the timing redistribution solved the opening sprint
- but it likely over-corrected by parking too much of the recovered time inside a single unchanged frame

### 3) Beat 6 does not look too abrupt at `14.0s`
The concern entering this pass was that reclaiming `10s` from the ending might make the callback land too fast.

The beat-6 sheet does **not** support that worry.

What the beat-6 sheet shows:
- the closing frame remains stable and legible throughout the full sampled span
- the callback structure is still present for the entire `14s` hold
- there is still enough room for the viewer to re-read the resolved/reposted contrast and absorb the final memory line

Practical judgment:
- **Beat 6 no longer looks over-roomy, but it also does not look abruptly clipped**
- the trim appears acceptable
- if anything, the ending now sits closer to proportionate with its word count

## Overall interpretation
This candidate timing pass appears to have produced a **mixed but useful result**:

What improved:
- Beat 1 is materially more plausible as a narration-carrying reveal sequence
- Beat 6 survived the trim better than feared

What newly looks weak:
- Beat 2 is now the clearest pacing bottleneck because the extra time sits on a nearly unchanged frame

So the main pacing story has changed from:
- **`v8`: opening too compressed**

to:
- **`v9`: opening much healthier, but Shot 4 now holds too long unless it gains internal motion or gives time back**

## Recommended next move
If this concept continues, the next best pass should be **narrow**, not a broad rewrite.

Most likely options:
1. trim Shot 4 from `34.0s` to something meaningfully shorter
2. redistribute a few of those seconds into adjacent beats only if there is a concrete reason
3. only keep the `34.0s` hold if Shot 4 gains internal staged motion / emphasis changes that justify the extra dwell

What should **not** happen next:
- broad script rewriting
- reopening opening-geometry churn
- claiming the piece is final because the runtime now sits in a better band

## Decision
- **Status:** useful timing experiment, not a lock
- **Best current judgment:** the candidate pass solves the worst opening compression, but **Beat 2 now looks overlong in static visual form**
- **Beat 6 judgment:** **not too abrupt** at `14.0s`
- project status remains:
  - **not greenlit**
  - **not upload-ready**
  - **not phone-safe enough to claim**
  - still **PROMISING BUT STILL PREVIEW-GRADE**
