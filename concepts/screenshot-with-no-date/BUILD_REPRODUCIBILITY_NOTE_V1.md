# Build Reproducibility Note V1 — The Screenshot With No Date

Date: 2026-05-20
Status: validation note only; not a publish or quality greenlight

## Purpose
Record one narrow validation result for the current strongest preview candidate:
- `preview_animatic_v15.mp4`
- timing table: `SHOT_TIMINGS_V10_SHOT5_MOTION_CANDIDATE.csv`

This note is about **build reproducibility**, not readability, finish quality, or phone safety.

## What changed
Commit `c3ac9af` updated the V15 builder:
- `build_preview_with_shot4_shot5_shot6_shot12_staging.py`

Before that fix, the builder explicitly rendered staged Shot 4 / 5 / 6 / 12 assets, but it did **not** explicitly render the staged opening assets used by the V15 timing table:
- `02a_repost_velocity_one.png`
- `02b_repost_velocity_two.png`
- `03a_hidden_ui_crop_only.png`
- `03b_reveal_capture_date.png`
- `03c_reveal_incident_log.png`
- `03d_reveal_resolution.png`

Those files existed locally in `preview_frames/`, but the build path relied on their prior presence.

After `c3ac9af`, the V15 builder now explicitly calls the opening-stage renderer as part of the build.

## Validation performed
To test the fix, I:
1. deleted the staged opening PNGs listed above from `preview_frames/`
2. ran the V15 builder again
3. confirmed that all staged opening PNGs were regenerated from code
4. confirmed that the rebuilt `preview_animatic_v15.mp4` still existed and ffprobed to:
   - `174.560000`

## Result
The current V15 preview candidate is now **more reproducible as a build artifact**.

Narrow claim supported by this check:
- the strongest current preview candidate no longer depends on leftover local opening-stage PNGs in order to rebuild successfully

Claims **not** supported by this check:
- that the piece is greenlit
- that the piece is upload-ready
- that the piece is phone-safe
- that any readability issue is solved
- that the preview is equivalent to a final export

## Practical implication
This improves validation discipline in a modest but real way:
- the current strongest preview candidate can now be regenerated more reliably from the checked-in build path
- future review work can trust the V15 assembly path slightly more than before

## Current status remains
- **not greenlit**
- **not upload-ready**
- **not phone-safe enough to claim**
- `PROMISING BUT STILL PREVIEW-GRADE`
