# Video 2 Storyboard

Usage note: run `python3 tools/render_storyboard.py --video video2` to generate placeholder boards in `videos/video2/storyboard_frames/`. These are editorial planning frames for pacing and narration sync, not final art.

## Visual Direction

- Same restrained editorial language as Video 1: dark matte canvas, high-contrast type, simple geometry.
- Distinct topic palette for Video 2: teal/sand accents with calm warning colors for uncertainty.
- Human-facing diagrams only: request paths, timestamp cards, rollout windows, and region labels.
- Evidence-first labeling throughout: `Observed`, `Likely`, and `Unknown` shown explicitly.

## Planned Shots (Full Video Coverage)

### 01 - Title Card
- Purpose: establish the premise quickly.
- On-screen text: "Same URL, Different Answer" and "Evidence first. Explanation second."
- Rendered frame: `01_title_card.png`

### 02 - One URL, Opposite Results
- Purpose: show the contradiction clearly without jumping to blame.
- On-screen text: two captures one minute apart with opposite transit status lines.
- Rendered frame: `02_same_url_two_answers.png`

### 03 - Evidence Before Blame
- Purpose: set doctrine for the rest of the episode.
- On-screen text: observed facts (what/when/where) on left, inference on right.
- Rendered frame: `03_evidence_before_blame.png`

### 04 - Mechanism 1: Caching Path Split
- Purpose: explain stale vs fresh responses from different delivery paths.
- On-screen text: User A/User B path to stale cache vs refreshed origin.
- Rendered frame: `04_caching_path_split.png`

### 05 - Header Evidence Comparison
- Purpose: model what concrete evidence looks like.
- On-screen text: cache metadata side-by-side (`cache-status`, `Age`, response text).
- Rendered frame: `05_cache_headers_comparison.png`

### 06 - Mechanism 2: Rollout Window Timeline
- Purpose: show how deployment timing allows temporary coexistence.
- On-screen text: release window with captures inside it.
- Rendered frame: `06_rollout_window_timeline.png`

### 07 - Traffic Split During Rollout
- Purpose: visualize partial rollout behavior in plain terms.
- On-screen text: old/new versions both serving traffic during transition.
- Rendered frame: `07_rollout_traffic_split.png`

### 08 - Mechanism 3: Edge and Location Differences
- Purpose: show regional edge variance and propagation lag.
- On-screen text: US-West and US-East edges connected to origin.
- Rendered frame: `08_edge_location_map.png`

### 09 - Scope the Claim
- Purpose: prevent overclaims from a single capture.
- On-screen text: one row each for `Observed`, `Inference`, and `Unknown`.
- Rendered frame: `09_scope_claim_limit.png`

### 10 - Fast Verification Steps
- Purpose: give practical workflow viewers can run before sharing.
- On-screen text: timestamp, location/network, exact wording, metadata, observed-vs-inferred split.
- Rendered frame: `10_fast_verification_steps.png`

### 11 - One-Sentence Template
- Purpose: model calm, precise language with uncertainty discipline.
- On-screen text: concrete observed sentence plus scoped inference sentence.
- Rendered frame: `11_observed_inference_template.png`

### 12 - Closing Card
- Purpose: reinforce takeaway.
- On-screen text: "Single fetch = clue" and "Multiple context-rich fetches = evidence".
- Rendered frame: `12_closing_card.png`

## Animatic Build (Short Preview)

1. Generate frames:
   - `python3 tools/render_storyboard.py --video video2`
2. Adjust preview pacing:
   - edit `videos/video2/SHOT_TIMINGS.csv`
3. Build animatic:
   - `python3 tools/build_animatic.py --video video2`

Output: `videos/video2/video2_animatic.mp4`

## Narration Rough Cut

1. Confirm narration audio exists:
   - `videos/video2/video2_narration.mp3`
2. Adjust narration-aligned pacing:
   - edit `videos/video2/ROUGH_CUT_TIMINGS.csv`
3. Build rough cut:
   - `python3 tools/build_rough_cut.py --video video2`

Output: `videos/video2/video2_rough_cut.mp4`
