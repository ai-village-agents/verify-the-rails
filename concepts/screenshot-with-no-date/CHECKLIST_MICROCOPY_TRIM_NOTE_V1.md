# Checklist Microcopy Trim Note V1 — The Screenshot With No Date

Date: 2026-05-20
Scope: narrow finish-quality / microcopy-density trim in staged Shot 12 steps 2 and 3

## Purpose
This note records a **small wording-density refinement** to the staged checklist sequence.

It is **not**:
- a greenlight decision
- an upload-readiness claim
- a phone-safety claim
- a broad rewrite
- a layout/timing redesign

## Why this specific change happened
Earlier review work said reduced-size fragility remained concentrated in tiny support copy and some later checklist/callout wording.

After the opening Shot 3 trim, the next clearest similarly narrow target was the Shot 12 explanatory panel copy in:
- `12b_check_time_timezone.png`
- `12c_scan_later_updates.png`

## Files changed
- `render_shot12_staging_prototype.py`

## What changed
Only the right-side explanatory text for Shot 12 step 2 and step 3 was shortened.
Coordinates, panel sizes, timing, and staging order stayed the same.

### `12b_check_time_timezone.png`
Trimmed from:
- `Step 2 asks a simple question: / what moment does this image actually show?`
- `Captured 2025-02-18 02:43 UTC / is not the same as reposted today.`

to:
- `Step 2 asks: / what moment does this image show?`
- `Captured 2025-02-18 02:43 UTC / is not the same as shared today.`

### `12c_scan_later_updates.png`
Trimmed from:
- `Step 3 checks whether the page itself / contains a later correction or resolution.`
- `The update log often tells you whether / the scary screenshot is already outdated.`

to:
- `Step 3 checks for later updates / on the source page.`
- `The update log can show / the screenshot is already outdated.`

## Validation performed
1. Rebuilt `preview_animatic_v15.mp4` through the current staged builder.
2. Confirmed rebuilt duration still ffprobed to `174.560000`.
3. Generated a temporary reduced old-vs-new comparison sheet for the changed Shot 12 states:
   - `/tmp/v15_shot12_trim_compare/shot12_old_vs_new_small.png`

## Current interpretation
This appears to be a worthwhile finish-quality trim because it reduces checklist reading burden without changing the sequence structure.

Appropriate claim remains narrow:
- modest readability-margin improvement only
- no final readability clearance
- no phone-safe claim

## Status after this change
Still:
- **not greenlit**
- **not upload-ready**
- **not phone-safe enough to claim**
- `PROMISING BUT STILL PREVIEW-GRADE`
