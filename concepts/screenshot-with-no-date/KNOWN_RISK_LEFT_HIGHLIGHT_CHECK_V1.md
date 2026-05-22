# Known Risk Left Highlight Check V1

Date: 2026-05-22
Concept: `The Screenshot With No Date`
Scope: bounded source-side measurement for `12c_scan_later_updates`
Status impact: none by itself. This does **not** greenlight the concept, does **not** make it upload-ready, and does **not** justify any phone-safety claim.

## Why this check exists

`KNOWN_RISK_MOSAIC_REVIEW_V1.md` made `12c_scan_later_updates` look like the densest frame in the Shot 12 checklist cluster.
`KNOWN_RISK_TEXT_BBOX_CHECK_V1.md` then showed the right-panel copy in `12c` is **not** uniquely wide.
That left a narrower question:

> Is `12c` feeling dense because of the **left-side highlighted source region**, rather than because the right-side copy is too large?

## Method

I inspected `render_shot12_staging_prototype.py` and `render_preview_frames.py`, then measured the actual coordinates used by the `12c` green highlight and the incident-log text drawn by `status_shell(...)`.

Static source values for `12c`:
- base shell origin: `x=100, y=260, w=860, h=580`
- green highlight rectangle: `(132, 686) → (928, 816)`
- highlight size: `796x130 px`

Measured incident-log content boxes:
- `incident_log_header`: `(158, 697) → (319, 720)` — fully inside highlight
- `row_1_text`: `(236, 739) → (822, 764)` — fully inside highlight
- `row_2_text`: `(236, 797) → (894, 822)` — only partial overlap; bottom extends beyond highlight
- `row_3_text`: `(236, 855) → (807, 875)` — not highlighted at all

Marker-line check:
- row 1 marker line fully inside highlight
- row 2 marker line fully inside highlight
- row 3 marker line outside highlight

## Finding

The `12c` left-side highlight does **not** frame the whole update sequence.
Instead, it creates a mixed emphasis zone:

1. fully highlights the incident-log label
2. fully highlights the first update row
3. clips the second row at the bottom edge
4. excludes the third / resolved row entirely

This is a more specific explanation for `12c`'s apparent density than "the right panel is too text-heavy."
The left side is carrying a visually busy, only-partially-contained emphasis region, which likely makes the frame feel less settled in reduced-size review.

## Interpretation

This result supports a narrower constraint:

- **Do not trim `12c` right-panel copy just because the contact-sheet view made it feel dense.**
- If `12c` is revisited later, the first evidence-backed suspect is the **scope of the left-side source highlight**, not the right-side checklist text width.

This still does **not** prove that `12c` needs a change.
It only narrows the most plausible source of its apparent fragility.
