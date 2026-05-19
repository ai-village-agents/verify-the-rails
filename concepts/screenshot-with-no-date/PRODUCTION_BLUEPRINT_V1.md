# Production Blueprint V1 - The Screenshot With No Date

## Production intent
This version is a timestamp-specific reveal piece. Each major claim change must be shown through exact synthetic UI evidence from the three approved examples: OpsStatus incident timeline, 90-day dashboard range crop, and resurfaced policy announcement.

## Likely frame set

| Frame filename suggestion | Purpose | Key visual elements | Key on-screen text | Depends on crop/reveal/timeline motion in animatic/rough-cut stage? |
|---|---|---|---|---|
| `01_open_crop.png` | Specific paradox hook with authentic-looking urgency. | Tight `OpsStatus` crop showing `[Amber dot] Partial Service Disruption`, `Started: 02:14 UTC`, and affected components only. | `REAL SCREENSHOT` then `WRONG TIME CLAIM` | `Yes` - must open tightly cropped before any context appears. |
| `02_repost_velocity_stack.png` | Show repost pressure and present-tense framing error. | Repost feed cards using same crop; visible repost time `2026-05-19 09:12 local`. | `Reposted as current` | `Yes` - stacked repost entries need rapid timed build. |
| `03_hidden_ui_edge_freeze.png` | Signal missing context boundary. | Frozen crop with explicit mask edge showing hidden header/log outside frame. | `What is outside the crop?` | `Yes` - freeze and mask edge emphasis are timing-sensitive. |
| `04_zoomout_capture_reveal.png` | Reveal original capture time. | Pullback to full status page header with capture metadata `2025-02-18 02:43 UTC`. | `Captured 2025-02-18 02:43 UTC` | `Yes` - meaning change depends on zoom-out reveal. |
| `05_incident_resolution_vs_repost.png` | Compare resolved state against later repost. | Incident log row `Resolved 2025-02-18 03:26 UTC` plus split-frame repost marker `2026-05-19 09:12 local`. | `Resolved long before repost` | `Yes` - split-frame should appear in sequence after log reveal. |
| `06_oiu_rails_overlay.png` | Lock evidence taxonomy to scene. | Blue/amber/gray O/I/U chips pinned to status evidence and claim text. | `Observed` / `Inference` / `Unknown` | `Yes` - staggered label entry should match narration order. |
| `07_claim_scope_composer.png` | Shift from authenticity question to claim-timing question. | Phone-style composer with attached OpsStatus image and callouts (`Captured 2025-02-18 02:43 UTC` vs present-tense caption). | `Authentic != Current` | `Yes` - pin drops must happen sequentially. |
| `08_was_vs_is_caption_swap.png` | Show claim flip on same evidence. | Same screenshot alternating captions: `Was disrupted` and `Is disrupted now`. | `One moment, not all moments` | `Yes` - alternating captions carry the point. |
| `09_dashboard_crop_dip.png` | Pattern B setup with hidden range control. | Cropped `Operations Analytics` chart and tooltip: `2026-04-06 03:00 UTC`, `Core Checkout: 88.4%`, `Express Checkout: 87.9%`. | `Looks like now` | `Yes` - should hold crop before revealing range. |
| `10_dashboard_range_reveal.png` | Pattern B resolution with full timeframe context. | Upward reveal of selector `Last 90 days (2026-02-01 to 2026-04-30)` and scrub to recovery above `98.9%` by `2026-04-06 05:00 UTC`. | `Range changes meaning` | `Yes` - reveal + scrub timing are required. |
| `11_old_announcement_reveal.png` | Pattern C in compact form. | Product update crop with retention sentence; pullback to `Published 2025-05-12 16:00 UTC`; scroll to clarification `2025-05-20 09:30 UTC`; repost tag `2026-05-19`. | `Old post, new panic` | `Yes` - must reveal publish and follow-up metadata in order. |
| `12_ten_second_timecheck_workflow.png` | Deliver practical routine with concrete UI anchors. | Pause-before-share state and four step overlays: source page, timestamp/timezone, later updates, claim check prompt. | `Open source` `Check time + timezone` `Scan later updates` `Current or past?` | `Yes` - checklist should tick left-to-right in one pass. |
| `13_return_full_context_resolved.png` | Close loop with timeline contrast and memory line. | Full OpsStatus page with timeline trace from `Started 02:14 UTC` to `Resolved 2025-02-18 03:26 UTC`, held beside repost marker `2026-05-19 09:12 local`. | `Same image. Different conclusion.` / `Check the time before you share.` | `Yes` - timeline trace and hold are required for final impact. |

## Reusable visual components
- Synthetic `OpsStatus` shell with incident banner, affected component list, update thread, and metadata header.
- Timeline rail component with node styles for `Started`, `Mitigation`, `Resolved`, and repost marker.
- Social repost feed cards with optional present-tense caption styling.
- Phone composer shell with attachment card and claim/evidence callout pins.
- `Operations Analytics` chart module with crop-safe and full-view variants.
- Date-range selector module fixed to `Last 90 days (2026-02-01 to 2026-04-30)` for pattern B.
- `Product Updates` announcement template with publish metadata row and follow-up entry row.
- O/I/U chip set with locked colors and contrast checks.
- Four-step verification checklist overlay and tick states.

## What must be solved before production
- Lock one canonical synthetic visual style across all three examples so they read as one piece.
- Set text-size minima for mobile legibility (metadata rows, timestamps, and tooltip numbers).
- Confirm crop masks exactly match storyboard boundaries for each reveal shot.
- Set one motion-duration standard so reveal cadence stays consistent with the 216s timing sheet.
- Validate that every example includes both original-time evidence and repost-time evidence on screen.
- Enforce per-frame text-density limits so overlays remain readable at playback speed.

## Minimum quality bar for greenlight
- Opening paradox uses the specific OpsStatus incident example, not generic outage language.
- At least two absolute timestamps are readable in each pattern segment where applicable.
- Dashboard segment must visibly reveal `Last 90 days (2026-02-01 to 2026-04-30)` and `05:00 UTC` recovery.
- Announcement segment must visibly reveal `Published 2025-05-12 16:00 UTC` and `2025-05-20 09:30 UTC` follow-up.
- O/I/U framework appears on screen in a consistent visual system.
- Closing returns to the same opening image with resolved timeline trace and repost contrast.
