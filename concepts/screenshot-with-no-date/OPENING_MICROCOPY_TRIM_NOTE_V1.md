# Opening Microcopy Trim Note V1 — The Screenshot With No Date

Date: 2026-05-20
Scope: narrow finish-quality / microcopy-density trim in the staged Shot 3 opening reveal

## Purpose
This note records a **small wording-density refinement** to the current opening staging path.

It is **not**:
- a greenlight decision
- an upload-readiness claim
- a phone-safety claim
- a broad script rewrite
- a geometry/layout redesign

## Why this specific change happened
The clearest remaining reduced-size caution had been concentrated in the opening reveal, especially the right-side explanatory burden around Frame / Shot 3.

Relevant prior evidence:
- `SMALLER_PLAYER_REVIEW_V1.md` identified Frame 03 as the clearest opening small-player risk.
- `SMALLER_PLAYER_REVIEW_V2.md` said the structure now survives better than the microcopy, with fragility still concentrated in tiny support text and right-column explanation blocks.
- `QUALITY_REVIEW_V3.md` again named Frame 03 as the clearest small-player risk in the opening section.

That pointed toward a **narrow wording-density trim** as a better next step than another broad motion pass or geometry change.

## Files changed
- `render_opening_staging_prototype.py`

No other file was needed for the actual visual change.

## What changed
The staged Shot 3 right-side text was shortened while keeping:
- the same staging order
- the same coordinates
- the same timing
- the same reveal logic
- the same chips
- the same underlying evidence sequence

### `03a_hidden_ui_crop_only.png`
Body text trimmed from:
- `Start with the exact area / that made the repost / feel current.`

to:
- `Start with the area / that made the repost / feel current.`

### `03b_reveal_capture_date.png`
Body text trimmed from:
- `This was captured on / 2025-02-18 at 02:43 UTC.`
- `The repost is from / 2026-05-19.`
- `That alone shrinks / the claim scope.`

to:
- `This was captured / 2025-02-18 02:43 UTC.`
- `Reposted / 2026-05-19.`
- `That already narrows / the claim.`

### `03c_reveal_incident_log.png`
Body text trimmed from:
- `Now the viewer can see / updates after the first / screenshot moment.`
- `The screenshot captured / one moment inside / a longer sequence.`
- `One more reveal still matters.`

to:
- `Now later updates / are visible.`
- `The screenshot shows / one moment in / a longer sequence.`
- `One more reveal matters.`

### `03d_reveal_resolution.png`
No change.

## Validation performed
1. Rebuilt `preview_animatic_v15.mp4` through the current staged builder.
2. Confirmed rebuilt duration still ffprobed to `174.560000`.
3. Generated a temporary side-by-side reduced sheet comparing old vs new Shot 3 opening states:
   - `/tmp/v15_opening_trim_compare/shot3_old_vs_new_small.png`
4. Visually checked that the new right-side text blocks read as lighter / less burdened without changing the reveal sequence.

## Current interpretation
This change appears directionally worthwhile because it reduces wording burden in the best-known fragile opening area **without** reopening layout churn.

The appropriate claim is still narrow:
- this is a **finish-quality microcopy trim**
- it modestly improves the opening's readability margin
- it does **not** clear the full readability gate
- it does **not** justify any phone-safe claim

## Status after this change
Still:
- **not greenlit**
- **not upload-ready**
- **not phone-safe enough to claim**
- `PROMISING BUT STILL PREVIEW-GRADE`
