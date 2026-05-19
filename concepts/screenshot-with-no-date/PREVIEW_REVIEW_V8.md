# Preview Review V8

Date: 2026-05-19
Artifact reviewed: `preview_animatic_v8.mp4`

## Scope of this pass
This was a targeted playback review of the new whole-piece staged-opening build.

I did not change the script or the later-sequence frames in this pass.

The purpose was to test whether the staged opening introduced in `build_preview_with_staged_opening.py` held up in full-piece context and whether the shorter runtime created any obvious pacing damage downstream.

## Source-level context for this pass
The reviewed artifact uses:
- staged Shot 2 repost spread:
  - `02a_repost_velocity_one.png`
  - `02b_repost_velocity_two.png`
  - `02_repost_velocity_stack.png`
- staged Shot 3 reveal:
  - `03a_hidden_ui_crop_only.png`
  - `03b_reveal_capture_date.png`
  - `03c_reveal_incident_log.png`
  - `03d_reveal_resolution.png`
- `SHOT_TIMINGS_V3.csv`
- local build output `preview_animatic_v8.mp4`

Runtime check:
- `preview_animatic_v8.mp4`: `171.840000`
- prior full preview baseline (`preview_animatic_v6.mp4`): `206.040000`
- delta: `-34.20s`

## Playback review judgment
I restarted playback from the beginning in Firefox, then did additional spot-checks in the middle and late sequence.

What held up:
- The staged opening still hands off cleanly into Shot 4 in whole-piece context.
- Shot 4 still has enough dwell time to absorb the quicker opening and re-establish the evidence calmly.
- Shot 4 → Shot 5 did not feel abruptly rushed in playback.
- Beat 3 (`07` / `08`) still read as two distinct ideas in motion:
  - Shot 7 = claim construction / present-tense misuse
  - Shot 8 = same evidence, different conclusion scope
- The dashboard pair (`09` / `10`) still reads coherently after the shorter opening.
- The late run (`10` / `11` / `12`) still preserves the stronger finish shape established in earlier passes.

What I did **not** conclude:
- This is still not enough to call the piece greenlit.
- This is still not enough to call the piece upload-ready.
- This is still not enough to call the piece phone-safe.

## Firefox end-state check
Firefox again appeared to end on `12_ten_second_timecheck_workflow.png` during playback of `preview_animatic_v8.mp4`.

## Direct file-level verification
The actual file still contains frame 13 as the ending callback.

Evidence:
- `preview_concat_v8.txt` ends with `13_return_full_context_resolved.png`.
- A near-end extracted frame at `170s` from `preview_animatic_v8.mp4` matched frame 13 much more closely than frame 12.

Mean absolute difference comparison:
- extracted near-end frame vs frame 13: `1.2500`
- extracted near-end frame vs frame 12: `16.2121`

## Decision
- **Status:** the staged-opening full preview is more promising in context than the older static-opening baseline, but the piece remains **preview-grade**.
- **Best current judgment:** the `SHOT_TIMINGS_V3.csv` version does **not** currently show an obvious pacing collapse from the shorter opening in the reviewed sections.
- **Action implication:** do **not** make a new timing/compression change yet. Keep `v8` as the current preview baseline unless a later playback pass reveals a more specific problem.
