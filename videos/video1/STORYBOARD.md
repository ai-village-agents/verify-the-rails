# Video 1 Storyboard

Usage note: Run `python3 tools/render_storyboard.py` before edit assembly to generate reference boards in `videos/video1/storyboard_frames/`; these frames are production placeholders for pacing, narration timing, and motion planning, not final art.

## Visual Direction

- Restrained editorial look with dark background and high-contrast typography
- Limited accent colors for evidence states: primary, secondary, inference
- Geometric placeholders only (cards, lines, boxes, arrows)
- Minimal motion intent: slow push-ins, crossfades, and simple reveals

## Planned Shots (Full Video Coverage)

### 01 - Title Card (0:00-0:20)
- Purpose: Establish premise and tone immediately.
- On-screen text: "Two True Screenshots, One Wrong Conclusion"; subhead "How source, time, and delivery path create conflict".
- Visual treatment: Dark matte background, bold serif title, thin editorial divider lines, subtle corner frame.
- Rendered frame: `01_title_card.png`

### 02 - Conflicting Screenshots Setup (0:20-0:45)
- Purpose: Show the core contradiction at a glance.
- On-screen text: "Screenshot A: Free admission ends June 1" vs "Screenshot B: Extended through July 1"; timestamps under each capture.
- Visual treatment: Two side-by-side faux screenshot cards with red conflict highlight around date text.
- Rendered frame: `02_conflicting_screenshots.png`

### 03 - Assumption Reframe (0:45-1:20)
- Purpose: Move audience from accusation framing to diagnostic framing.
- On-screen text: "Conflict != Fake by default" and "Check source + time + path".
- Visual treatment: Simple flow card from "Claim conflict" to crossed-out "Fake?" then to checklist path.
- Rendered frame: `03_assumption_reframe.png`

### 04 - Source Timeline Intro (1:20-2:10)
- Purpose: Introduce source-vs-live drift with concrete event sequence.
- On-screen text: "Primary page changed at 11:40 AM" and timeline entries.
- Visual treatment: Horizontal timeline with event dots and tier color coding.
- Rendered frame: `04_source_timeline_intro.png`

### 05 - Source Timeline Detail (2:10-3:15)
- Purpose: Demonstrate how both screenshots can be authentic at different times.
- On-screen text: "8:00 Primary June 1", "9:15 Newsletter mirrors", "11:40 Update to July 1", "1:20 Blog still shows old wording".
- Visual treatment: Expanded timeline with annotated callouts and "Observed" vs "Inference" chips.
- Rendered frame: `05_source_timeline_detail.png`

### 06 - Cache/Deployment Lag Diagram (3:15-4:30)
- Purpose: Explain delivery-path variation in plain terms.
- On-screen text: "Same URL, different cache state".
- Visual treatment: User A and User B nodes feeding different cache/origin boxes; old/new state labels.
- Rendered frame: `06_cache_deployment_lag.png`

### 07 - Lag Consequence Bridge (4:30-5:15)
- Purpose: Connect infrastructure lag to viral screenshot disagreement.
- On-screen text: "Both reports can be true observations".
- Visual treatment: Split panel with "Fresh response" and "Stale response" cards plus propagation arrows.
- Rendered frame: `07_lag_consequence_bridge.png`

### 08 - Summary Error Comparison (5:15-6:00)
- Purpose: Show quote vs paraphrase drift.
- On-screen text: Left "Direct quote: ... for weekday visits"; right "Summary: Free through July 1".
- Visual treatment: Two-column comparison with condition words highlighted and omission marker.
- Rendered frame: `08_summary_error_comparison.png`

### 09 - Summary Error Impact (6:00-6:45)
- Purpose: Clarify that clean summaries can still mislead.
- On-screen text: "A summary is not a quote"; "Missing qualifier -> stronger claim".
- Visual treatment: Compression funnel graphic from source text block into shorter headline block.
- Rendered frame: `09_summary_error_impact.png`

### 10 - Five-Step Checklist (6:45-7:50)
- Purpose: Deliver actionable verification routine.
- On-screen text: Steps 1-5 (Primary source, Timestamp+TZ, Freshness test, Exact wording, Mark uncertainty).
- Visual treatment: Full-screen checklist board with clear numbered rows and checkbox icons.
- Rendered frame: `10_five_step_checklist.png`

### 11 - Checklist Applied Example (7:50-8:30)
- Purpose: Model the "observed fact vs inference" phrasing.
- On-screen text: "Observed: official page says July 1 at 2:37 PM PT" and "Inference: June 1 capture may be pre-update".
- Visual treatment: Lower-third style template card with two stacked statement blocks.
- Rendered frame: `11_checklist_applied_example.png`

### 12 - Closing Card (8:30-9:15)
- Purpose: Reinforce channel doctrine and sign off cleanly.
- On-screen text: "Source. Time. Wording." and "Check first, share second.".
- Visual treatment: Minimal closing slate with centered typography and subtle border grid.
- Rendered frame: `12_closing_card.png`

## Animatic Build (Rough Preview)

Use this when you want a quick timing preview of the storyboard frames (no narration yet).

1. Regenerate storyboard frames:
   - `python3 tools/render_storyboard.py`
2. Adjust per-shot timing if needed:
   - Edit `videos/video1/SHOT_TIMINGS.csv`
3. Build the animatic MP4:
   - `python3 tools/build_animatic.py`

Output: `videos/video1/video1_animatic.mp4`

## Narration Rough Cut

Use this to build a narration-length assembly from the same 12 storyboard frames.

1. Edit rough-cut timing if needed:
   - `videos/video1/ROUGH_CUT_TIMINGS.csv`
2. Build the rough cut with narration:
   - `python3 tools/build_rough_cut.py`

This differs from the short animatic: the animatic is a fast pacing preview, while the rough cut is stretched to track narration timing.

Output: `videos/video1/video1_rough_cut.mp4`
