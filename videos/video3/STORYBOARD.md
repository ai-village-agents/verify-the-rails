# Storyboard - Video 3

Usage note: run `python3 tools/render_storyboard.py --video video3` before edit assembly to generate placeholder boards in `videos/video3/storyboard_frames/`. These are editorial planning frames for pacing and narration sync, not final art.

## Visual Direction

- Restrained editorial look: dark matte canvas, high-contrast typography, and simple geometric panels.
- Distinct Video 3 palette: cool blue for direct evidence, warm amber for neutral checks, restrained red for overreach/inference risk.
- Wording-first visual language: exact phrase comparisons, source hierarchy, and drift markers over decorative visuals.
- Explicit evidence labels in-frame: `Observed` and `Inference` shown whenever interpretation appears.

## Planned Shots (Full Video Coverage)

### 01 - Title Card
- Purpose: establish the claim-drift premise and evidence-first tone.
- On-screen text: "When Summaries Drift From Sources" and "Quote first. Interpret second."
- Rendered frame: `01_title_card.png`

### 02 - Source vs Summary
- Purpose: show the core wording-strength mismatch at a glance.
- On-screen text: source phrase `associated with` vs summary wording `proves` / `causes`.
- Rendered frame: `02_source_vs_summary.png`

### 03 - Compare Claims, Not Tone
- Purpose: reframe from blame language to claim-comparison method.
- On-screen text: compare exact claim wording; inference about drift pressure is separate.
- Rendered frame: `03_compare_claims_not_tone.png`

### 04 - Source Hierarchy
- Purpose: establish primary -> summary -> commentary hierarchy.
- On-screen text: distance from primary source increases drift risk.
- Rendered frame: `04_source_hierarchy.png`

### 05 - Drift Mechanisms Table
- Purpose: make five common drift mechanisms concrete.
- On-screen text: compression, omission, simplification, version drift, status shift.
- Rendered frame: `05_drift_mechanisms_table.png`

### 06 - Health Report Comparison
- Purpose: run worked comparison with verbs and scope words.
- On-screen text: `associated with` / `surveyed adults` vs `proves` / `causes` with scope removed.
- Rendered frame: `06_health_report_comparison.png`

### 07 - Budget Memo Comparison
- Purpose: show status drift from proposal to approval claim.
- On-screen text: `proposes` vs `approved` and planning language vs decision language.
- Rendered frame: `07_budget_memo_comparison.png`

### 08 - Verbs, Scope, Status
- Purpose: deliver the three high-signal comparison checks.
- On-screen text: check verb strength, scope qualifiers, and status terms.
- Rendered frame: `08_verbs_scope_status.png`

### 09 - Date and Version Context
- Purpose: show how older wording can persist and conflict with newer source text.
- On-screen text: timeline with draft/update/repost sequence.
- Rendered frame: `09_date_version_context.png`

### 10 - Fast Verification Steps
- Purpose: provide practical pre-share routine.
- On-screen text: capture exact sentences, mark date/version, check verbs+scope, split observed from inference.
- Rendered frame: `10_fast_verification_steps.png`

### 11 - Observed/Inference Template
- Purpose: model reusable two-line reporting format.
- On-screen text: observed wording line plus scoped inference with confidence label.
- Rendered frame: `11_observed_inference_template.png`

### 12 - Closing Card
- Purpose: reinforce channel doctrine and close cleanly.
- On-screen text: "Read the source. Measure the drift. Share with context."
- Rendered frame: `12_closing_card.png`

## Animatic Build (Short Preview)

1. Generate frames:
   - `python3 tools/render_storyboard.py --video video3`
2. Adjust preview pacing:
   - edit `videos/video3/SHOT_TIMINGS.csv`
3. Build animatic:
   - `python3 tools/build_animatic.py --video video3`

Output: `videos/video3/video3_animatic.mp4`

## Narration Rough Cut

1. Confirm narration audio exists:
   - `videos/video3/video3_narration.mp3`
2. Adjust narration-aligned pacing:
   - edit `videos/video3/ROUGH_CUT_TIMINGS.csv`
3. Build rough cut:
   - `python3 tools/build_rough_cut.py --video video3`

Output: `videos/video3/video3_rough_cut.mp4`
