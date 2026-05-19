# Frame Finish Priorities V1 — The Screenshot With No Date

Date: 2026-05-19
Based on:
- `PRODUCTION_BLUEPRINT_V1.md`
- `PREVIEW_REVIEW_V2.md`
- `PREVIEW_REVIEW_V3.md`
- `PREVIEW_REVIEW_V4.md`
- current V3 preview state after `e3524d7`

## Priority legend
- **A — major production upgrade needed**: this frame likely needs real finish work beyond minor polish
- **B — moderate polish needed**: structure works, but production quality likely depends on better motion, copy trimming, or layout refinement
- **C — mostly keep / protect**: current preview already demonstrates the right idea and should mainly be preserved

## Frame-by-frame priorities

| Frame | Priority | Why | Finish-pass focus |
|---|---|---|---|
| `01_open_crop.png` | C | The opening paradox is already one of the clearest and strongest parts of the piece. | Preserve the tight-crop urgency and make sure the opening motion feels deliberate, not generic. |
| `02_repost_velocity_stack.png` | B | The logic works, but this frame can still feel preview-like if the repost build is too static. | Strengthen motion rhythm and make repost pressure feel more alive without adding clutter. |
| `03_hidden_ui_edge_freeze.png` | B | The crop-boundary logic is clear, but the frame risks feeling like an explanatory placeholder if not staged carefully. | Make the missing-context boundary feel intentional and elegant rather than merely diagrammatic. |
| `04_zoomout_capture_reveal.png` | C | The capture-date reveal is central and now benefits from the typography improvement. | Protect the reveal timing and keep the capture-date line highly legible. |
| `05_incident_resolution_vs_repost.png` | C | The V2 trim improved this hold, and V3 still supports it. | Keep timing near current trim and ensure the resolved-vs-repost contrast lands quickly. |
| `06_oiu_rails_overlay.png` | C | This was one of the densest frames, but the readability pass materially helped it in motion. | Preserve current spacing discipline and avoid adding more explanatory copy. |
| `07_claim_scope_composer.png` | B | The trimmed hold works, but the frame still depends heavily on callout clarity and could feel staged rather than finished. | Refine pin-drop motion and simplify any nonessential text so the scope shift reads instantly. |
| `08_was_vs_is_caption_swap.png` | C | The conceptual job is simple and strong. | Keep the same-evidence / different-caption contrast crisp and fast. |
| `09_dashboard_crop_dip.png` | B | The example is good, but charts often look dry unless the crop/reveal staging is especially clean. | Emphasize the deceptive present-tense feeling before the range context appears. |
| `10_dashboard_range_reveal.png` | B | The meaning shift is important, but the chart sequence may need stronger final animation logic to feel production-grade. | Make the range reveal and recovery logic feel smooth, readable, and unmistakable. |
| `11_old_announcement_reveal.png` | A | This is the most likely frame to still feel text-heavy and preview-grade even after the date-line size increase. | Reduce cognitive load, simplify the visible copy, and stage the publish/follow-up metadata as a cleaner reveal. |
| `12_ten_second_timecheck_workflow.png` | B | Readability is better now and the V2 trim helped, but this frame still carries a lot of on-screen instruction at once. | Keep the four-step routine, but consider whether any supporting text can be reduced while preserving clarity. |
| `13_return_full_context_resolved.png` | B | Structurally essential, but Firefox end-state ambiguity and callback impact make this a finish-sensitive shot. | Ensure the closing callback feels conclusive and visually memorable even if the player UI is unhelpful. |

## Top 3 finish-pass targets

### 1) `11_old_announcement_reveal.png`
Why it is highest priority:
- likely the most text-heavy frame in the later sequence
- depends on multiple dates and a follow-up reveal
- easy for this section to drift from "specific and clear" into "busy and explanatory"

Desired outcome:
- publish date, repost date, and follow-up clarification all read quickly without the frame feeling like a document screenshot dump

### 2) `10_dashboard_range_reveal.png`
Why it matters:
- the chart segment needs to feel alive enough that the range selector changes the viewer's interpretation, not just the visible labels
- a weak motion treatment here would make the pattern feel generic

Desired outcome:
- the viewer instantly feels how a hidden time window changes the story

### 3) `12_ten_second_timecheck_workflow.png`
Why it stays important:
- it carries the practical payoff of the piece
- even after the readability pass, this is still one of the densest screens
- if this frame feels too instructional, the ending momentum weakens

Desired outcome:
- practical, memorable, and quick to scan

## Frames to protect from over-editing
These currently appear to be doing their jobs well and should not be rewritten casually:
- `01_open_crop.png`
- `04_zoomout_capture_reveal.png`
- `05_incident_resolution_vs_repost.png`
- `06_oiu_rails_overlay.png`
- `08_was_vs_is_caption_swap.png`

## Recommended next step
Use this priority map to guide a finish-oriented revision of the blueprint and renderer, starting with frames `11`, `10`, and `12`, while preserving the already-strong opening/reveal chain.
