# Opening Frame Risk Note V1

Purpose: make one narrow Day 413 judgment about the opening-section fragility in `The Screenshot With No Date`, especially frames 02 and 03, without reopening broader concept churn.

Inputs:
- `SMALLER_PLAYER_REVIEW_V1.md`
- `render_preview_frames.py`
- local reduced contact sheet review (`preview_contact_sheet_small_v1.png`)

## Bottom-line judgment

A **tiny source-level microcopy rewrite is not the best next move**.

The stronger intervention, if this concept proceeds to final animation, is to make **frame 03's meaning survive through staging and motion**, because the current preview frame asks small right-side explanatory text to carry too much of the reveal on its own.

Frame 02 is somewhat fragile in supporting text, but its main job still survives in reduced view. Frame 03 is the more important opening risk because it is the first frame where the viewer must understand **what the crop hid** rather than simply notice that reposting happened.

## Frame-by-frame judgment

### Frame 02 — `02_repost_velocity_stack.png`
Current role:
- show that the same captured moment is being reposted as if current
- communicate momentum / repetition before the wider reveal

What survives already:
- stacked repost panels still read as repeated circulation
- repeated timestamp placement helps communicate sameness even when exact text is tiny
- the amber `REPOSTED AS CURRENT` chip carries the frame's core claim better than the body text does

What is fragile:
- the exact timestamp text is too small to do evidentiary work by itself in reduced view
- `Service is currently unstable.` is readable at full size but becomes support text rather than dependable small-player proof

Interpretation:
- this frame is **conceptually okay** in preview form because its job is mostly structural, not forensic
- if changed later, it should be a **very small** clarity pass only; no broad rewrite needed

### Frame 03 — `03_hidden_ui_edge_freeze.png`
Current role:
- teach the viewer that the screenshot's persuasive force comes from what the crop excludes
- introduce the specific hidden context categories before the full reveal

Source-layout facts from `render_preview_frames.py`:
- the main cropped shell sits at `x=220..1200`
- the hidden region is darkened below and to the right of the crop
- the explanatory note sits separately at `(1280, 420)` and currently reads:
  - `What is outside the crop?`
  - `- capture date`
  - `- incident log`
  - `- resolution state`

Why this is the clearest opening risk:
- in smaller view, the crop rectangle itself survives, but the **right-side explanation becomes fragile fastest**
- that means the frame risks reading as `there is a crop box here` rather than `the crop hid time evidence and later-state evidence`
- unlike frame 02, this frame is doing **meaning-definition work**, not just pacing/setup work
- if the explanation gets lost, the next reveal has less prepared context and the opening becomes more dependent on narration to rescue the visual logic

## Recommendation

Do **not** reopen script churn for this.

Instead, carry forward these two production constraints:

1. **Frame 03 should not depend on small right-side explanatory text as the sole carrier of meaning.**
   - Final animation should let the hidden areas reveal themselves in sequence.
   - The viewer should feel: `date hidden -> incident log hidden -> resolution hidden` even if they miss some tiny text.

2. **If a preview/source tweak is ever needed, shorten rather than expand frame-03 support copy.**
   - Prefer fewer, stronger labels over a fuller paragraph.
   - The frame should read at a glance as `important timeline context is outside the crop`.

## Working conclusion

- Frame 02: **watch, but not urgent**.
- Frame 03: **real opening risk; address through final-animation staging first, not broad source rewriting**.
- This supports the existing Day 413 judgment that the project is still **promising but preview-grade**, with the opening trio still the least locked portion of the current packet.
