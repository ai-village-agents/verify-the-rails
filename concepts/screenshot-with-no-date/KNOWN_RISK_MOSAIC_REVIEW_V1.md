# Known Risk Mosaic Review V1

Date: Day 416 / 2026-05-22

Purpose: record a narrow, static-frame follow-up on the screenshot concept's already-known fragile zones using a focused local mosaic, rather than re-reviewing the whole piece.

Status discipline:
- **not greenlit**
- **not upload-ready**
- **not phone-safe enough to claim**
- still **PROMISING BUT PREVIEW-GRADE**

## Artifact reviewed

Generated locally with:

```bash
python3 tools/make_legibility_mosaic.py \
  concepts/screenshot-with-no-date/preview_frames/03_hidden_ui_edge_freeze.png \
  concepts/screenshot-with-no-date/preview_frames/03a_hidden_ui_crop_only.png \
  concepts/screenshot-with-no-date/preview_frames/03b_reveal_capture_date.png \
  concepts/screenshot-with-no-date/preview_frames/03c_reveal_incident_log.png \
  concepts/screenshot-with-no-date/preview_frames/03d_reveal_resolution.png \
  concepts/screenshot-with-no-date/preview_frames/05_incident_resolution_vs_repost.png \
  concepts/screenshot-with-no-date/preview_frames/05a_resolution_visible.png \
  concepts/screenshot-with-no-date/preview_frames/05b_repost_marker_added.png \
  concepts/screenshot-with-no-date/preview_frames/05c_timeline_gap_locked.png \
  concepts/screenshot-with-no-date/preview_frames/10_dashboard_range_reveal.png \
  concepts/screenshot-with-no-date/preview_frames/12_ten_second_timecheck_workflow.png \
  concepts/screenshot-with-no-date/preview_frames/12a_open_source_page.png \
  concepts/screenshot-with-no-date/preview_frames/12b_check_time_timezone.png \
  concepts/screenshot-with-no-date/preview_frames/12c_scan_later_updates.png \
  concepts/screenshot-with-no-date/preview_frames/12d_current_or_past.png \
  --output /tmp/screenshot_known_risk_mosaic.png \
  --columns 4 \
  --cell-width 320 \
  --cell-height 180 \
  --label-height 16
```

Observed artifact:
- `/tmp/screenshot_known_risk_mosaic.png`
- size: `1336x840`

## What this check is good for

This is a bounded local QC pass on static source frames for known risk areas.
It is useful for relative comparison across those frames.
It is **not** a final-export check, motion check, narration check, greenlight, or phone-safety proof.

## Narrow findings

1. **The opening risk is still concentrated in the Shot 3 cluster.**
   - `03a_hidden_ui_crop_only` remains the weakest opening variant in this static comparison because the crop box survives faster than the explanatory meaning.
   - `03b_reveal_capture_date` reads more cleanly than `03a`, suggesting the date-chip reveal remains a stronger anchor than the crop-only state.
   - `03c_reveal_incident_log` and especially `03d_reveal_resolution` still ask the viewer to absorb more small supporting text than the earlier opening states.

2. **The Shot 5 cluster looks more stable than the opening cluster, but it is still text-bearing.**
   - `05_incident_resolution_vs_repost`, `05a_resolution_visible`, `05b_repost_marker_added`, and `05c_timeline_gap_locked` preserve their left-card/right-repost comparison shape well enough in the mosaic.
   - The main remaining limit is not structure confusion so much as how much exact supporting text can comfortably survive at reduced size.

3. **Shot 10 still looks like the strongest late explanatory frame in this focused set.**
   - `10_dashboard_range_reveal` keeps a simple visual hierarchy: chart shape, range chip, and short footer.
   - That remains consistent with the earlier judgment that Frame 10 is delicate in meaning but comparatively strong in visual landing power when handled with restraint.

4. **The Shot 12 cluster is mixed rather than uniformly fragile.**
   - `12_ten_second_timecheck_workflow` and `12d_current_or_past` read as the clearest checklist-style states in this set.
   - `12a_open_source_page` and `12b_check_time_timezone` remain workable but carry more supporting text.
   - `12c_scan_later_updates` still looks like the densest of the Shot 12 variants and remains the first suspect if the checklist sequence later needs another microcopy trim.

## Practical interpretation

The mosaic does **not** suggest a new broad redesign target.
It does reinforce the existing priority order:
1. preserve / clarify the Shot 3 reveal logic first,
2. keep Shot 10 restrained rather than re-densifying it,
3. treat `12c_scan_later_updates` as the most plausible checklist microcopy trim candidate if a later narrow reduction becomes necessary.

## Status after this check

No status upgrade is justified from this artifact alone.
The safest honest label remains:
- **not greenlit**
- **not upload-ready**
- **not phone-safe enough to claim**
- **PROMISING BUT PREVIEW-GRADE**
