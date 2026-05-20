# Opening Re-Extract Timing Check V1

This note records a narrow validation check on the current opening reveal sequence in `preview_animatic_v15.mp4`.

It is **not** a greenlight note, **not** an upload recommendation, and **not** a phone-safety claim.

Current overall status remains unchanged:
- **not greenlit**
- **not upload-ready**
- **not phone-safe enough to claim**
- **PROMISING BUT STILL PREVIEW-GRADE**

## Why this check existed

After `d7583a2`, the next unresolved question was whether the opening reveal sequence still contained one more extremely narrow, evidence-backed Shot 3 trim candidate.

A temporary opening strip had already been created from rough re-extraction times around:
- `8.95s`
- `10.70s`
- `12.50s`
- `14.60s`

That rough strip was only intended as a quick look, but a follow-up check showed it was **not reliable enough for state labeling**.

## Inputs reviewed

- `render_opening_staging_prototype.py`
- `build_preview_with_shot4_shot5_shot6_shot12_staging.py`
- `preview_animatic_v15_concat.txt`
- current source stills in `preview_frames/`
- fresh sweep artifact:
  - `/tmp/v15_opening_secondsweep/opening_secondsweep_strip.png`
- fresh accurate re-extractions:
  - `/tmp/v15_reextract_opening_accurate/05_03a_at_10_8.png`
  - `/tmp/v15_reextract_opening_accurate/06_03b_at_14_0.png`
  - `/tmp/v15_reextract_opening_accurate/07_03c_at_17_6.png`
  - `/tmp/v15_reextract_opening_accurate/08_03d_at_22_25.png`
  - `/tmp/v15_reextract_opening_accurate/09_04a_at_28_5.png`
  - `/tmp/v15_reextract_opening_accurate/opening_accurate_strip.png`

## What the check found

### 1) The original rough opening times were not trustworthy enough

The first opening strip used approximate timestamps that were simply too rough to support a confident per-state judgment.

### 2) Even with accurate seeking, naive midpoint labeling across the encoded preview can slide into the next staged state

The current V15 concat file clearly lists the intended opening sequence and durations:
- `03a_hidden_ui_crop_only.png` — `3.0s`
- `03b_reveal_capture_date.png` — `3.4s`
- `03c_reveal_incident_log.png` — `3.8s`
- `03d_reveal_resolution.png` — `5.5s`
- then `04a_capture_time_visible.png`

But when I re-extracted using accurate `ffmpeg` seeking (`-i ... -ss ...`) at the nominal midpoint times derived from the concat/CSV timing logic, the extracted stills matched the **next** source state instead:
- nominal `03a` midpoint `10.80s` matched **`03b`**
- nominal `03b` midpoint `14.00s` matched **`03c`**
- nominal `03c` midpoint `17.60s` matched **`03d`**
- nominal `03d` midpoint `22.25s` matched **`04a`**

This means that for this preview-stage still-concat MP4, a simple “extract the midpoint timestamp from the encoded file” method is **not reliable enough for precise adjacent-state labeling**.

### 3) The opening reveal chain itself still appears to be functioning as intended

A broader second-by-second sweep across the opening window showed the expected progression from the Shot 3 reveal states into Shot 4, and source review still supports the same editorial judgment as before:
- Frame 03 remains the clearest opening caution
- but this recheck did **not** reveal a comparably narrow, clearly justified new microcopy trim

## Practical takeaway

For this preview-stage opening sequence:
- **do not** trust rough timestamp probes
- **do not** assume a nominal midpoint timestamp in the encoded preview maps cleanly to the intended staged still
- prefer:
  1. direct source-still inspection
  2. a broader time sweep across the encoded file
  3. source-to-extract comparison before naming a state

## Conclusion

This check supports **restraint**, not another Shot 3 content change.

The opening sequence still deserves caution and disciplined review, but this specific validation pass did **not** justify another microcopy edit.
