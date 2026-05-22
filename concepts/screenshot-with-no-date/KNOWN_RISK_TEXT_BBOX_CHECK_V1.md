# Known Risk Text BBox Check V1

Date: Day 416 / 2026-05-22

Purpose: add one narrow measurement follow-up to `KNOWN_RISK_MOSAIC_REVIEW_V1.md` by checking the right-side explanatory text payloads for the Shot 3 opening variants and Shot 12 checklist variants using the actual renderer font settings.

Status discipline remains unchanged:
- **not greenlit**
- **not upload-ready**
- **not phone-safe enough to claim**
- still **PROMISING BUT PREVIEW-GRADE**

## Method

Used Pillow `multiline_textbbox(...)` with the same font helper defined in `render_preview_frames.py`.
This is a local layout-proxy check only.
It is **not** a final-export check, motion check, or phone-safety proof.

## Shot 12 right-panel text measurements

Measured widths/heights for the staged Shot 12 side-panel strings:

- `12a_main`: `592x65`
- `12a_sub`: `495x27`
- `12b_main`: `561x65`
- `12b_sub`: `456x61`
- `12c_main`: `470x65`
- `12c_sub`: `499x61`
- `12d_main`: `620x65`
- `12d_sub`: `581x29`

### Narrow implication for Shot 12

The earlier focused mosaic made `12c_scan_later_updates` look like the most fragile Shot 12 variant.
This bbox check suggests that fragility is **not** primarily explained by the width of the right-side panel copy alone:

- `12c` is **not** the widest right-panel payload.
- `12d_main` is wider than `12c_main`.
- `12a_main` and `12b_main` are also wider than `12c_main`.

So if a later narrow trim becomes necessary, the first suspect in `12c` should be the **combined visual load** of the highlighted source-page/log area plus panel copy, not an assumption that the right-panel wording is uniquely oversized by itself.

## Shot 3 right-panel text measurements

Measured widths/heights for the staged opening explanations:

- `03a_body`: `340x100`
- `03b_body1`: `373x62`
- `03b_body2`: `196x62`
- `03b_body3`: `298x55`
- `03c_body1`: `293x62`
- `03c_body2`: `311x95`
- `03d_body1`: `339x145`
- `03d_body2`: `399x66`

### Narrow implication for Shot 3

This supports the existing opening-risk judgment:

- `03d_reveal_resolution` carries the **tallest** main explanatory block in the Shot 3 cluster.
- `03d` also carries the widest emphatic payoff line (`Same screenshot. Different conclusion.`).
- `03c` is still meaningfully text-bearing, but `03d` is the clearer right-panel burden peak.

So if the opening cluster later needs one more microcopy reduction, `03d` remains a more evidence-backed suspect than `03b` or `03c`.

## Practical takeaway

The combined evidence now points to:
1. keep treating the Shot 3 cluster, especially `03d`, as the clearest right-panel burden zone,
2. avoid trimming `12c` right-panel copy on width assumptions alone,
3. if `12c` remains fragile in later review, investigate the left-side highlighted-source complexity first.
