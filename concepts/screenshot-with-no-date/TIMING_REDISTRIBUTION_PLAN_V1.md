# Timing Redistribution Plan V1

Date: 2026-05-19
Preview baseline: `preview_animatic_v8.mp4`
Current timing baseline: `SHOT_TIMINGS_V3.csv`
Candidate timing pass: `SHOT_TIMINGS_V4_CANDIDATE.csv`
Script baseline: `SCRIPT_DRAFT_V2.md`
Related notes:
- `PREVIEW_REVIEW_V9.md`
- `NARRATION_TIMING_ALIGNMENT_NOTE_V1.md`

## Purpose
Turn the beat-level pacing math into a concrete shot-level experiment.

This is **not** a greenlight and **not** a claim that the piece is final.
It is a planning pass that asks:

> If the script largely stays as written, what shot timing shape would better support plausible narration while preserving the strongest visual structure already found in `v8`?

## Candidate timing goals
This pass intentionally does four things:

1. **Give Beat 1 real breathing room** so the paradox hook and stepped reveal can read as ideas, not just flashes.
2. **Expand Beat 2 substantially** because the first reveal currently carries too many words for a 20-second dwell.
3. **Keep Beat 3 close to current shape** because prior review did not show concrete redundancy there.
4. **Recover time from Beat 6 and some of Beat 4** because those sections are currently much roomier than the narration density suggests.

## Proposed beat totals
| Beat | V3 seconds | V4 candidate seconds | Delta |
| --- | ---: | ---: | ---: |
| Beat 1 — Hook | 13.8 | 25.0 | +11.2 |
| Beat 2 — First reveal | 20.0 | 34.0 | +14.0 |
| Beat 3 — Better question | 31.0 | 30.0 | -1.0 |
| Beat 4 — Three patterns | 67.0 | 59.5 | -7.5 |
| Beat 5 — Defense routine | 16.0 | 18.0 | +2.0 |
| Beat 6 — Closing memory | 24.0 | 14.0 | -10.0 |
| **Total** | **171.8** | **180.5** | **+8.7** |

## Approximate narration density under this candidate
Using the same beat word counts from `PREVIEW_REVIEW_V9.md`:

| Beat | Words | Candidate seconds | Approx. words/sec |
| --- | ---: | ---: | ---: |
| Beat 1 — Hook | 77 | 25.0 | 3.08 |
| Beat 2 — First reveal | 107 | 34.0 | 3.15 |
| Beat 3 — Better question | 88 | 30.0 | 2.93 |
| Beat 4 — Three patterns | 171 | 59.5 | 2.87 |
| Beat 5 — Defense routine | 56 | 18.0 | 3.11 |
| Beat 6 — Closing memory | 39 | 14.0 | 2.79 |
| **Total** | **538** | **180.5** | **2.98** |

This keeps the overall piece near the faster end of the plausible range identified earlier, while avoiding the current extreme compression in Beats 1 and 2.

## Shot-level changes and rationale
### Beat 1 — Hook (`01` through `03d`)
- `01_open_crop`: `2.4 -> 3.5`
- `02a_repost_velocity_one`: `1.1 -> 1.7`
- `02b_repost_velocity_two`: `1.1 -> 1.7`
- `02_repost_velocity_stack`: `1.5 -> 2.4`
- `03a_hidden_ui_crop_only`: `1.7 -> 3.0`
- `03b_reveal_capture_date`: `1.8 -> 3.4`
- `03c_reveal_incident_log`: `1.8 -> 3.8`
- `03d_reveal_resolution`: `2.4 -> 5.5`

Rationale:
- the opening staging work already found a strong reveal order
- the problem is now dwell time, not reveal order
- this candidate spreads extra time across the reveal chain rather than dumping all of it into a single hold
- `03d` still gets the longest hold inside Beat 1 because the resolved-state reveal is the moment that changes the viewer's interpretation

### Beat 2 — First reveal (`04`)
- `04_zoomout_capture_reveal`: `20.0 -> 34.0`

Rationale:
- Beat 2 currently carries the heaviest early narration load
- the viewer needs time to integrate the timestamp, the repost, and the claim reversal without the piece feeling like it is racing past its own central evidence
- this is the cleanest place to buy narration room without disturbing later example structure

### Beat 3 — Better question (`05` and `06`)
- `05_incident_resolution_vs_repost`: `15.0 -> 14.0`
- `06_oiu_rails_overlay`: `16.0 -> 16.0`

Rationale:
- prior review suggested Beat 3 was conceptually distinct and not the first compression target
- this pass therefore keeps Beat 3 almost intact
- only a very small trim is taken from `05`

### Beat 4 — Three patterns (`07` through `11`)
- `07_claim_scope_composer`: `13.0 -> 11.5`
- `08_was_vs_is_caption_swap`: `12.0 -> 10.5`
- `09_dashboard_crop_dip`: `14.0 -> 12.0`
- `10_dashboard_range_reveal`: `14.0 -> 12.5`
- `11_old_announcement_reveal`: `14.0 -> 13.0`

Rationale:
- this block is comparatively roomy already
- the aim is not to rush it, but to reclaim a few seconds from each example rather than one brutal cut anywhere
- `11` keeps the most room inside the block because announcement resurfacing has the highest risk of turning muddy if over-compressed

### Beat 5 — Defense routine (`12`)
- `12_ten_second_timecheck_workflow`: `16.0 -> 18.0`

Rationale:
- the practical habit is worth a little more space if the piece is going to earn usefulness rather than just diagnosis

### Beat 6 — Closing memory (`13`)
- `13_return_full_context_resolved`: `24.0 -> 14.0`

Rationale:
- the current closing is visually strong but much roomier than the word count needs
- a shorter hold should still preserve the callback while giving back needed time to the dense early beats
- this is the largest single time recovery in the plan

## Why this candidate is useful even before rendering
Even without immediately rebuilding the preview, this candidate is helpful because it converts a broad pacing concern into a falsifiable next test:

- if this timing shape still feels cramped in Beats 1–2, the script or visual density really may need further adjustment
- if this timing shape feels balanced, then the main problem was probably redistribution rather than wording
- if Beat 6 becomes too abrupt, that would show the current candidate reclaimed too much from the ending

## Recommended next test
If work continues on this concept, the next meaningful experiment would be:

1. build a new preview using `SHOT_TIMINGS_V4_CANDIDATE.csv`
2. compare beat feel, not just total runtime
3. specifically evaluate:
   - whether Beat 1 now reads like a reveal sequence rather than a sprint
   - whether Beat 2 can plausibly carry its narration load
   - whether Beat 6 still lands emotionally after the trim

## Status reminder
After this plan, the concept is still:

- **not greenlit**
- **not upload-ready**
- **not phone-safe enough to claim**
- still **PROMISING BUT STILL PREVIEW-GRADE**
