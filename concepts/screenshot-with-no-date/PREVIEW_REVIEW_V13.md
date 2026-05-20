# Preview Review V13 — First Motion-Enhanced Shot 4 Test

Date: 2026-05-20
Artifact reviewed: `preview_animatic_v12.mp4`
Candidate timings: `SHOT_TIMINGS_V7_MOTION_CANDIDATE.csv`
Related notes:
- `PREVIEW_REVIEW_V12.md`
- `SHOT4_REBALANCE_NOTE_V1.md`
- `render_shot4_staging_prototype.py`

## Why this review exists
The last two reviews established something important:
- trimming static Shot 4 from `34.0s` to `30.0s` helped, but not enough
- trimming again to `28.0s` produced the best static-only candidate so far, but it still did not fully solve Beat 2

That narrowed the problem.
The next meaningful test was no longer another tiny static trim.
It was to see whether Shot 4 could earn roughly the same duration through **internal staged motion**.

This candidate keeps Beat 2 at `28.0s`, but splits it into four stages:
1. `04a_capture_time_visible.png`
2. `04b_repost_gap.png`
3. `04c_claim_scope_shift.png`
4. `04d_timeline_mismatch.png`

Each stage currently holds for `7.0s`.

## Review method
File-level review again remained primary.

Method used:
- inspect the new timing table
- build the motion-enhanced candidate from staged Shot 4 frames
- generate a beat-2 contact sheet directly from `preview_animatic_v12.mp4`
- measure sampled frame-to-frame change across Beat 2 at 2-second intervals

Artifacts used in this pass:
- `/tmp/v12_motion_review/review_beat2_v12_motion_sheet.png`
- `render_shot4_staging_prototype.py`
- `SHOT_TIMINGS_V7_MOTION_CANDIDATE.csv`

## Targeted timing context
### Beat 2 — First reveal (`04a` through `04d`)
- total: `28.0s`
- staged as four `7.0s` holds
- approximate density remains: `107 / 28.0 = 3.82 wps`

The important change is therefore **not** runtime.
It is change density inside the beat.

## Frame-change evidence
Using 2-second extracted-frame intervals across Beat 2, the sampled frame-to-frame mean absolute differences were:

`[10.1673, 0.0, 0.0, 4.1794, 0.0, 0.0, 0.0, 6.15, 0.0, 0.0, 13.4733, 0.0, 0.0]`

Interpretation:
- unlike the static versions, this beat no longer shows one entry jump followed by a flat line
- visible state changes now recur across the beat rather than only at the beginning
- with a simple threshold check, the substantive changes land approximately at:
  - `25–27s`
  - `31–33s`
  - `39–41s`
  - `45–47s`

Practical meaning:
- after the initial entry, the beat now generates fresh visible states roughly every `6–8s`
- that is much closer to the concrete pacing bar GPT-5.2 suggested for a long Shot 4

## Findings
### 1) This is the first Shot 4 candidate that appears to address the real bottleneck
The static trims changed the math but not the visual behavior.
This candidate changes the visual behavior.

What improved:
- Beat 2 no longer behaves like one parked frame
- the internal emphasis now progresses from capture time → repost gap → claim-scope distinction → explicit timeline mismatch
- the beat gives narration room without buying that room through pure stillness

Practical judgment:
- **this is the first Shot 4 candidate that looks plausibly capable of solving the bottleneck rather than only softening it**

### 2) The motion structure matches the diagnosis better than more trimming did
The staged order is coherent with the concept’s logic:
1. reveal the original capture moment
2. compare it with the repost moment
3. shift the viewer from authenticity to claim scope
4. state the timeline mismatch explicitly

That progression makes the extra time feel purposeful instead of inert.

Practical judgment:
- the current direction now looks more promising than further tiny static trims
- the core problem was indeed **missing internal progression**, not just a slightly wrong number

### 3) This is still prototype evidence, not a final lock
Even though this is the strongest Beat 2 result so far, the project status does not change yet.

What remains true:
- this is still preview-grade work
- the new Shot 4 stages themselves may need refinement for pacing, visual polish, or wording compression
- the full piece still needs a fresh overall review if this direction continues

## Overall interpretation
This pass changes the recommendation more clearly than the last two did.

Current best interpretation:
- static Shot 4 trimming alone hit diminishing returns
- staged internal motion appears to be the more meaningful fix
- keeping Beat 2 around `28.0s` now looks much more defensible **if** it behaves like this staged reveal instead of one still frame

So the pacing story is now:
- `34.0s` static = clearly overheld
- `30.0s` static = improved but sticky
- `28.0s` static = best static-only candidate, still not solved
- **`28.0s` staged motion = first genuinely promising Beat 2 fix**

## Recommended next move
Keep the next pass narrow and stay on the motion path.

Best next step:
1. review the full `preview_animatic_v12.mp4` as a whole, not just Beat 2
2. decide whether the four-step Shot 4 sequence needs timing redistribution inside the `28.0s` total
3. only after that decide whether this motion-enhanced structure should replace the static Shot 4 baseline

What should **not** happen next:
- returning immediately to more tiny static trims as the primary strategy
- broad script rewriting
- claiming the piece is finished from this prototype alone

## Decision
- **Status:** strongest Shot 4 experiment so far, still prototype evidence
- **Beat 2:** first candidate that appears to solve the real bottleneck mechanism
- **Current lean:** continue with staged-motion Shot 4 work, not more static-only trimming
- project status remains:
  - **not greenlit**
  - **not upload-ready**
  - **not phone-safe enough to claim**
  - still **PROMISING BUT STILL PREVIEW-GRADE**
