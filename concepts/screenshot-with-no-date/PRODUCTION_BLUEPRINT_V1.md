# Production Blueprint V1 - The Screenshot With No Date

## Production intent
This production should feel more reveal-based and visually intentional than the Day 412 batch. The viewer should repeatedly update their interpretation on screen through crop-to-context reveals, timeline placement, and explicit claim-scope framing rather than static explanation cards.

## Likely frame set

| Frame filename suggestion | Purpose | Key visual elements | Key on-screen text | Depends on crop/reveal/timeline motion in animatic/rough-cut stage? |
|---|---|---|---|---|
| `01_open_crop.png` | Hook with apparent certainty before context appears. | Tight status-page crop with red `Major Outage - Investigating` banner; no visible date/time UI. | `REAL SCREENSHOT` then `WRONG CONCLUSION` | `Yes` - opening must start tightly cropped and hold before any widening. |
| `02_repost_velocity_stack.png` | Show how fast reposting amplifies incomplete evidence. | Stacked repost cards with repeated claim language over the same cropped screenshot. | `No date visible` | `Yes` - repost cards should animate in rapid sequence to create pressure. |
| `03_hidden_ui_edge_freeze.png` | Create first doubt that the crop is hiding relevant context. | Freeze frame with subtle frame-edge hints of hidden UI outside the crop. | `Wrong moment?` | `Yes` - freeze and edge-highlight reveal are timing-dependent. |
| `04_zoomout_timestamp_reveal.png` | Deliver first major reveal by exposing timestamp. | Camera pullback to full status card with top-right `Updated 8:12 AM UTC`. | `Zoom out` / `Updated 8:12 AM UTC` | `Yes` - this beat only works if timestamp is revealed by animated zoom-out. |
| `05_incident_timeline_overlay.png` | Establish sequence: capture moment vs later repost moment. | Horizontal timeline rail with outage updates and later repost marker. | `Capture -> Updates -> Repost` | `Yes` - timeline markers should animate left-to-right for causal order. |
| `06_oiu_rails_overlay.png` | Lock in evidence taxonomy used throughout. | Blue/amber/gray chips and rails mapped to the same outage scene. | `Observed` / `Inference` / `Unknown` | `Yes` - label placement should appear progressively to match narration. |
| `07_authentic_not_current_composer.png` | Reframe from authenticity question to claim question. | Phone-style repost composer; screenshot attachment pin (`Captured at 8:12 AM UTC`) plus claim pin (`Still down`). | `Authentic != Current` | `Yes` - two callout pins should land in sequence. |
| `08_was_vs_is_caption_swap.png` | Clarify claim-scope difference with one image and two captions. | Same screenshot toggling between two interpretation captions. | `Was down` vs `Is down now` | `Yes` - caption swap timing carries the meaning. |
| `09_pattern1_incident_outlives_resolution.png` | Pattern example A: incident screenshot persists after resolution. | Crop-to-full status thread with `Resolved` state visible in expanded view. | `Pattern 1: Incident outlives resolution` | `Yes` - mini reveal from crop to resolved thread is required. |
| `10_pattern2_hidden_date_range.png` | Pattern example B: chart interpretation flips with date window. | Analytics chart with hidden date-range selector, then full UI showing `Last 1 hour`; secondary comparison with `Last 30 days`. | `Pattern 2: Hidden date range` | `Yes` - date-range toggle and comparison are motion-dependent. |
| `11_pattern3_old_post_new_panic.png` | Pattern example C: old announcement recirculates as current. | `Breaking` repost card, pullback to old source date plus later correction on timeline. | `Pattern 3: Old post, new panic` | `Yes` - old-date and correction markers must appear in sequence. |
| `12_ten_second_timecheck_workflow.png` | Provide practical routine viewers can execute quickly. | Pause-before-reshare UI; four-step checklist over real UI targets; quick second-screenshot pass indicator. | `Pause first` / `When captured?` / `Original source` / `Timezone` / `What changed after?` / `10 extra seconds` | `Yes` - checklist ticks and second-pass flash should animate in order. |
| `13_return_full_context_resolved.png` | Close with full-circle return and final memory line. | Return to opening status page now fully uncropped with highlighted timeline (`Investigating -> Identified -> Monitoring -> Resolved`) settling on `Resolved`. | `Same image. New reading.` / `Check the time before you share.` | `Yes` - closing return depends on tracing timeline then resting on `Resolved`. |

## Reusable visual components
- Status-page shell (header, incident banner, update thread, timestamp area).
- Timeline rail component with timestamp nodes and a repost marker style.
- Social repost card stack (single source card, quote/repost variants).
- Phone-style repost composer shell with attach area and caption field.
- Date-range selector module (`Last 1 hour`, `Last 24 hours`, `Last 30 days`).
- O/I/U chips and rail kit (`Observed`, `Inference`, `Unknown`) with consistent color mapping.
- Callout pin style for claim-vs-evidence annotations.
- Four-step verification checklist overlay with tick animation states.
- Resolution badge/state token (`Investigating`, `Identified`, `Monitoring`, `Resolved`).

## What must be solved before production
- Lock one canonical status-page visual design that is platform-neutral but believable.
- Decide exact color values for O/I/U so they remain legible over both light and dark UI cards.
- Confirm whether examples B and C use synthetic assets only or require adapted real-world references.
- Define standard motion speed for crop reveals and timeline tracing to avoid pacing drift across shots.
- Choose narration lock target (expected ~232s cut) and decide whether any beats can be tightened to ~220s.
- Decide text density limits per frame so overlays stay readable on mobile.
- Specify final handoff format for frame art (dimensions, naming, and export variants) for future `videos/video11` integration.

## Minimum quality bar for greenlight
- Every major claim shift must be shown via a visible reveal, not only told in voiceover.
- Opening and closing must use the same base screenshot so the conclusion reversal is unmistakable.
- At least one explicit timestamp and one explicit repost-later marker must be readable on screen.
- O/I/U framework must appear on-screen in a consistent visual system, not ad-hoc labels.
- Pattern examples must each include a before/after context change that can be understood without audio.
- Verification routine must map to actionable UI targets, not abstract advice.
- Frame naming and timing must be immediately compatible with existing storyboard and animatic tooling conventions.
