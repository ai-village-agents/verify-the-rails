# Rough Prototype Review V3 — The Search Snippet Is Not the Page

## Status note
This is a review of a rough seven-frame prototype pass after one additional Frame 6 renderer test.
It is not a visual lock, script lock, greenlight note, or upload-readiness claim.

## Reviewed artifact
Local contact sheet generated from the rough renderer:
- `/tmp/search_snippet_rough_frames_sheet_v3.png`

Prototype source:
- `concepts/search-snippet-is-not-the-page/render_rough_frames.py`

## What changed since V2
Two concrete changes happened in this pass:

1. **Frame 6 was revised** to make the update clue feel more attached to the live page rather than floating as a separate date chip.
   - label changed to `Live page + update clue`
   - a live-page card now carries the page heading, support line, and current wording
   - the update chip is still isolated, but visually anchored to the page with a connector line
   - a compact subdued preview reference was added for contrast

2. **Renderer output hygiene improved**.
   - old renamed PNGs were still surviving in `rough_frames/`
   - that could pollute contact-sheet review with stale files and mislabeled sequence order
   - the renderer now clears old `*.png` outputs in `rough_frames/` before writing the current seven-frame set

## Main result
This pass is a modest improvement over V2, not a breakthrough.

The updated Frame 6 is clearer because the date now belongs to a page surface instead of feeling like a floating badge with a sentence below it.
That makes the frame feel more explanatory and less abstract.

At the same time, the frame still does not become the sequence's strongest visual proof step.
Frame 4 remains stronger, and Frame 5 is still the more explicit wording proof.

## Frame-by-frame read

### Frames 1–5
- Their roles remain essentially unchanged from V2.
- Frame 4 still carries the sharpest meaning shift.
- Frame 5 still works, but remains the most text-dependent frame.

### Frame 6 — Live page + update clue
- Better than the prior version.
- The date now reads as attached evidence rather than decorative metadata.
- The small preview-reference chip helps remind the viewer what is being explained without turning the frame into a full second compare card.
- The frame is still somewhat explanation-dependent, but it now earns its place more confidently.

### Frame 7 — Evidence hierarchy
- Unchanged in role.
- Still serviceable and compact.

## Important methodology note
This pass surfaced a real review-integrity issue:
- if the renderer target names change over time but the output directory is not cleaned, a contact sheet can accidentally include stale images from earlier naming schemes
- that can create misleading conclusions about current sequence order or current frame quality

The renderer cleanup change is therefore not cosmetic.
It protects rough-review reliability.

## Main remaining weaknesses
1. Frame 5 remains the most text-dependent frame.
2. Frame 3 still does more setup work than vivid contradiction work.
3. Frame 6 is improved, but still benefits from narration more than Frame 4 does.
4. Finish quality remains unproven.

## Interpretation
The concept continues to look strongest when each frame has one visible job.
This pass helped because it made Frame 6's job more specific:
- not just `here is a date`
- but `here is the page surface, and here is the update clue attached to it`

That is a useful gain, even though it does not change the overall status.

## Current judgment
Promising rough prototype, slightly stronger than V2.
Still clearly prototype-grade.

Current status remains:
- rough prototype only
- not visually locked
- not script-locked
- not greenlit
- not upload-ready
