# Preview Review V4 — Motion pass after readability update

Date: 2026-05-19
Concept: `The Screenshot With No Date`
Asset reviewed: local `preview_animatic_v3.mp4`
Timing base: `SHOT_TIMINGS_V2.csv` (206.04s total)
Related source change: `e3524d7` (`feat: improve preview typography readability`)

## What changed before this pass
V3 keeps the V2 timing trims and adds a source-only typography/readability pass in `render_preview_frames.py`, including larger chip text, larger capture-date labels, slightly larger incident-log rows, larger repost timestamps, a larger published-date line in the announcement example, and slightly larger timeline labels.

## Review setup
- Reviewed in Firefox in a reduced-size window / smaller-player condition.
- Let the animatic play through in motion, sampling all major sections and specifically watching the previously borderline text areas.
- Because Firefox again appeared to end on the checklist frame, I followed the playback review with a direct file-level verification of the near-end frame.

## New findings from the V3 motion pass

### 1) Typography changes are materially helpful in motion
The readability pass appears to buy real margin, not just still-image margin.

Most noticeable improvements:
- the capture-date label now reads more safely during the widened status-shell reveal
- incident-log timestamps and rows feel less fragile in motion
- O/I/U chips feel easier to parse at a glance
- the checklist step chips in the `Ten-second time check` frame hold together better in the reduced-size player
- the announcement-frame date lines feel more comfortable than in earlier preview passes

This does **not** mean the piece is proven phone-safe, but it is a meaningful improvement over the earlier borderline state.

### 2) I did not see new crowding or obvious collisions from the larger type
A major risk of the typography pass was that the bigger labels would start to crowd the layouts. In this motion review, I did **not** find a serious regression.

Specific judgment:
- the `Observed / Inference / Unknown` frame still feels organized rather than cramped
- the `Claim scope` frame still reads cleanly with the larger chips
- the checklist frame is denser than average, but the larger text improves clarity more than it harms spacing
- the later announcement frame still feels balanced enough for a preview-stage animatic

### 3) The V2 timing trims still hold up with the updated typography
The three previously sticky sections remain better in the trimmed timing structure:
- `05_incident_resolution_vs_repost.png`
- `07_claim_scope_composer.png`
- `12_ten_second_timecheck_workflow.png`

During the V3 motion pass, those holds still felt sharper than V1 and did not feel prematurely cut off.

### 4) Firefox again gives a misleading apparent endpoint
In Firefox, playback again appeared to stop on the checklist frame (`12_ten_second_timecheck_workflow.png`) at the exact end of the player timeline, which could falsely suggest that the callback frame is missing.

I directly checked the file after playback:
- `preview_concat_v3.txt` **does include** `13_return_full_context_resolved.png`
- an extracted near-end frame from `preview_animatic_v3.mp4` best matched `13_return_full_context_resolved.png`
- best-match MSE: **7.488**

Conclusion: the final callback frame is present in the rendered MP4; Firefox player behavior is again the source of the ambiguity.

## Overall judgment after V3 motion review
This pass is a meaningful improvement.

What I now feel confident saying:
- V3 is **clearer in motion** than V2 on the small-type problem areas
- the readability pass helped without introducing an obvious layout regression
- the trimmed pacing still works
- the callback ending is still present in the actual MP4 even though Firefox makes that hard to trust visually

What I am **not** yet ready to say:
- that this is fully production-locked
- that it is genuinely phone-safe
- that the preview-grade animatic is ready to be translated straight into a published video without another finish/quality pass

## Decision
- **Status:** improved, but still **not greenlit**
- **Best next move:** keep the stronger typography baseline, then do one more finish-oriented pass focused on whether the final production version can reduce prototype feel while preserving this improved readability margin.
