# Verify the Rails

**Verify the Rails** is a YouTube channel about evidence-first digital literacy.

It explains a practical problem many people run into online: two public web claims can both look credible and still disagree. Often the gap is not a conspiracy or bad intent. It is a systems issue: source-vs-live drift, caching layers, deployment lag, stale screenshots, and summary errors.

## Published Videos

- Video 1: [Two True Screenshots: How One Story Split in Real Time](https://youtu.be/ZXn7Z_U4S9U)
- Video 2: [Same URL, Different Answer: Why the Web Disagrees](https://youtu.be/zPqNW_zdoog)
- Video 3: [From "Associated With" to "Proves": How Summaries Drift](https://youtu.be/VzM7DNTLSSE)
- Video 4: [This Was True Yesterday: How Date and Version Drift Breaks Online Claims](https://youtu.be/QiTj5xsEPkM)
- Video 5: [The Crop Hides the Clue: How Missing Context Changes Screenshot Claims](https://youtu.be/LM0cZeE1GO8)
- Video 6: [A Big Number Is Not the Whole Story: How Missing Denominators Mislead](https://youtu.be/Ji98TbTJyfk)
- Video 7: [Same Word, Different Metric: How Definition Drift Misleads](https://youtu.be/Pjg6pNvJdu4)
- Video 8: [Three Posts Are Not a Trend: How Sample Bias Misleads](https://youtu.be/k2cvAGFPPyY)
- Video 9: [The Winners Are Not the Whole Field: How Survivorship Bias Misleads](https://youtu.be/r4CFPLNicc8)
- Video 10: [One Chart Is Not the Whole Story: How Axis and Framing Choices Mislead](https://youtu.be/RIfBW3zlE2w)

Full playlist: [Verify the Rails — Full Series](https://www.youtube.com/playlist?list=PLKhIX6uAzcqVlCbcbAM8ewWGqJ2s9M4xd)

## Published Video Assets

- [`videos/`](videos/) contains the per-video production folders for Videos 1–10, including briefs, scripts, storyboards, timings, narration files, rough cuts, thumbnails, and YouTube metadata.

## Channel Concept

The channel teaches viewers how to verify claims against primary sources and current state, then explain disagreements in plain language.

The goal is not to make everyone a developer. The goal is to make people more reliable readers of online claims.

## Audience

- Curious non-experts who regularly see conflicting claims online
- Professionals who share links, dashboards, or screenshots in their work
- Students and lifelong learners building stronger media habits

## Tone

- Calm, specific, and fair-minded
- Skeptical without being cynical
- Clear about uncertainty and limits
- Focused on what viewers can actually do

## Current Status

This repo now contains the first published **Verify the Rails** batch plus ongoing preproduction work for slower follow-on concepts.

Current phase:
- Ten evidence-first explainer videos are published
- The reusable production pipeline is established and documented
- New concepts are being developed cautiously; current drafts are planning/preview-stage, not upload-ready

## Project Notes

- [`CHANNEL_STRATEGY.md`](CHANNEL_STRATEGY.md) — audience, value proposition, style rules, and quality bar for the channel.
- [`DAY413_QUALITY_REVIEW.md`](DAY413_QUALITY_REVIEW.md) — the Day 413 quality-reset note after the first 10-video batch, including the analytics snapshot and stricter bar for anything new.
- [`NEXT_VIDEO_CONCEPTS_DAY413.md`](NEXT_VIDEO_CONCEPTS_DAY413.md) — the early post-batch concept-branching note that fed into later preproduction work.

## Preproduction Concepts

- [`concepts/screenshot-with-no-date/`](concepts/screenshot-with-no-date/) — the most developed current concept; still preview-grade and not upload-ready
- [`concepts/search-snippet-is-not-the-page/`](concepts/search-snippet-is-not-the-page/) — rough prototype / planning-stage concept; not upload-ready
- [`concepts/same-clip-different-moment/`](concepts/same-clip-different-moment/) — newer seed-stage concept exploration; not upload-ready
- [`concepts/CONCEPT_BACKLOG_V1.md`](concepts/CONCEPT_BACKLOG_V1.md) — lightweight backlog for future directions

## Validation

- Run the built-in test suite with:
  ```bash
  python3 -m unittest discover -s tests -p 'test_*.py' -q
  ```

## Local Dependencies

- Install the minimal Python dependency set with:
  ```bash
  pip install -r requirements.txt
  ```
- `requirements.txt` currently installs Pillow, which the storyboard, thumbnail, and image-QC helpers use.
- `ffmpeg` is required locally for the animatic and rough-cut builders.
- `edge-tts` is optional and only needed if you want `tools/build_narration.py` to render narration audio locally.

## Production Scripts

- `tools/render_storyboard.py` renders placeholder storyboard frames for a selected published-video folder.
  ```bash
  python3 tools/render_storyboard.py --video video1
  ```
- `tools/build_animatic.py` builds a simple frame-timed storyboard animatic from a video's storyboard frames and shot timings.
  ```bash
  python3 tools/build_animatic.py --video video1
  ```
- `tools/build_narration.py` generates a narration MP3 from `videos/<video>/NARRATION.md` using `edge-tts` if it is installed locally.
  ```bash
  python3 tools/build_narration.py --video video1
  ```
- `tools/build_rough_cut.py` builds a narration-length rough cut from storyboard frames and rough-cut timings for local review.
  ```bash
  python3 tools/build_rough_cut.py --video video1
  ```
- `tools/render_thumbnail.py` renders a restrained editorial thumbnail PNG for a selected published-video folder.
  ```bash
  python3 tools/render_thumbnail.py --video video1
  ```

## Local QC Helpers

- `tools/derive_shot_timing_windows.py` derives cumulative shot windows from a timing CSV for planning and review.
  Duplicate numeric shot prefixes are rejected to avoid ambiguous shot-window review.
  ```bash
  python3 tools/derive_shot_timing_windows.py \
    --timings concepts/search-snippet-is-not-the-page/SHOT_TIMINGS_PROVISIONAL_V1_NO_SHOT9.csv \
    --focus-shots 3 7 10
  ```
- `tools/make_legibility_mosaic.py` builds a labeled PNG contact sheet from frame stills for local small-player/frame-review checks. It is a QC aid, not a readiness or upload-quality claim.
  ```bash
  python3 tools/make_legibility_mosaic.py \
    --input-dir concepts/search-snippet-is-not-the-page/rough_frames \
    --glob '*.png' \
    --output concepts/search-snippet-is-not-the-page/rough_frames/legibility_mosaic_local_qc.png
  ```
- `tools/annotate_image_boxes.py` draws labeled rectangle overlays on a single PNG/JPG input and saves a PNG for local geometry/coverage QC only (not a readiness/upload/phone-safe claim).
  ```bash
  python3 tools/annotate_image_boxes.py \
    videos/video10/storyboard_frames/04_example1_truncated_axis.png \
    --output /tmp/example1_box_qc.png \
    --box 120,80,520,280,chart_region,#00ff00 \
    --box 550,90,880,300,axis_label,red
  ```
- `tools/export_image_box_crops.py` exports one padded crop row per box into a dark PNG contact sheet for local QC only (not a readiness/upload/phone-safe proof).
  ```bash
  python3 tools/export_image_box_crops.py \
    videos/video10/storyboard_frames/04_example1_truncated_axis.png \
    --output /tmp/example1_box_crops_qc.png \
    --box 120,80,520,280,chart_region,#00ff00 \
    --box 550,90,880,300,axis_label,red \
    --padding 4 \
    --scale 2
  ```
- `tools/compare_image_box_crops.py` compares the same labeled box regions across multiple still images in one dark PNG sheet for local QC only, not a readiness proof.
  ```bash
  python3 tools/compare_image_box_crops.py \
    videos/video10/storyboard_frames/04_example1_truncated_axis.png \
    videos/video10/storyboard_frames/05_example2_full_axis.png \
    --output /tmp/example_box_compare_qc.png \
    --box 120,80,520,280,chart_region,#00ff00
  ```
  These helpers are for local QC and planning only.
