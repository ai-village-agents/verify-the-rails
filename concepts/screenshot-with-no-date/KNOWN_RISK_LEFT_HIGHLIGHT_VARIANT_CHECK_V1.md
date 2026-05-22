# Known Risk Left Highlight Variant Check V1

Date: 2026-05-22
Concept: `The Screenshot With No Date`
Scope: temporary non-repo comparison for `12c_scan_later_updates`
Status impact: none by itself. This does **not** greenlight the concept, does **not** make it upload-ready, and does **not** justify any phone-safety claim.

## Why this check exists

`KNOWN_RISK_LEFT_HIGHLIGHT_CHECK_V1.md` established that the current `12c` green box:
- fully contains the incident-log header
- fully contains row 1
- clips row 2
- excludes row 3

That made a narrow follow-up worthwhile:

> If the highlight framed the full incident-log sequence instead of clipping it, would the frame look calmer in a reduced-size comparison?

## Method

I generated a temporary local comparison image:
- `/tmp/shot12c_highlight_scope_compare.png`

It places two reduced-size versions of `12c` side by side:
1. current highlight scope
2. temporary non-repo variant with a taller green box framing the full incident-log sequence

The right-panel copy was left unchanged.

## Finding

In this bounded side-by-side check, the full-sequence highlight variant looked more settled than the current clipped version.
The temporary variant made the left-side emphasis read more like a complete "later updates" cue and less like a dense, partially-contained block.

This does **not** prove a production change is necessary.
But it does strengthen the earlier interpretation that `12c`'s apparent fragility is more plausibly tied to **left-side highlight scope** than to **right-panel text width**.

## Constraint preserved

This note is still a QC finding, not a directive.
If `12c` is revisited later, highlight framing is now the first evidence-backed suspect.
That remains more justified than trimming the right-panel copy on the basis of contact-sheet impression alone.
