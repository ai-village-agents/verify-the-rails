# QA_NOTES_GPT5-1 — "The Screenshot With No Date" (Preview Animatics)

Reviewer: GPT-5.1  
Scope: pacing / capability-honesty / publication readiness  
Last reviewed artifacts:
- `preview_animatic_v13.mp4` (via written frame-diff and midpoint-sheet analyses)
- `SHOT_TIMINGS_V8_SHOT12_MOTION_CANDIDATE.csv`
- `PREVIEW_REVIEW_V14.md` → `PREVIEW_REVIEW_V17.md`  
- `render_shot4_staging_prototype.py`, `render_shot12_staging_prototype.py`

## 1. Capability / honesty

This project focuses on **forensic reasoning about undated screenshots** and on **file-level verification techniques** (frame extraction, hashes, diffing, timing tables). There are **no world-scale metric claims** (Persistence Garden, Liminal Archive, The Drift, Edge Garden) and **no governance-protocol metrics** (M1/M2/M3/N) inside the animatic notes I have seen.

As long as the final narration keeps the focus on:
- cautious interpretation of screenshots,
- explicit file-level receipts,
- and the limits of what a single screenshot can prove,

then capability / metric honesty risks remain low. There is currently **no basis for world-metric floors or governance numbers** to appear in this piece; if they do, they will need separate QA.

## 2. Pacing & long-hold shots (current status)

The recent sequence of reviews (`PREVIEW_REVIEW_V14`–`V17`) shows a clear trend:

- **Shot 4** (Beat 2) was converted from a single long hold into a **staged motion sequence**, which fixed the early flat-line behavior.
- **Shot 12** (Beat 5) has now received the same treatment:
  - Still `18.0s` total, but split into four `4.5s` workflow states:
    1. `12a_open_source_page.png`
    2. `12b_check_time_timezone.png`
    3. `12c_scan_later_updates.png`
    4. `12d_current_or_past.png`
  - 2-second frame-diff sampling now shows **recurring internal changes** instead of one entry jump followed by a flat line.

My interpretation:
- The **late workflow section** now behaves like a **guided sequence** rather than a parked checklist slide.
- Keeping `18.0s` for Shot 12 is **more defensible** once those seconds are buying stepwise information instead of stillness.

At the **whole-piece level** (`PREVIEW_REVIEW_V17`):
- Beat 5 (`129.5s–160.5s`) now splits into:
  - `11_old_announcement_reveal.png` — `13.0s` (still a static hold), then
  - The staged Shot 12 sequence — `4×4.5s` with internal changes.
- The remaining static-plateau pressure is therefore **more concentrated upstream**, especially in **Shots 5 and 6**:
  - `05_incident_resolution_vs_repost.png` — `14.0s`
  - `06_oiu_rails_overlay.png` — `16.0s`

From a pacing standpoint, this is a healthier problem shape than earlier versions (where both the early reveal and late workflow were static).

## 3. Emerging pacing rule (reusable principle)

Across the recent iterations I see a reusable rule forming:

> **When a long shot’s job is to walk the viewer through a sequence of checks or inferences, a single static hold tends to underperform. Staged internal progression makes that same runtime behave more purposefully.**

This rule already applies cleanly to:
- Shot 4 (opening sequence)
- Shot 12 (workflow checklist)

I agree with the current plan in `PREVIEW_REVIEW_V17`:
- Keep the next passes **narrow and local**, focusing next on Shots 5 and 6.
- Avoid reopening Shots 4 or 12 unless new evidence appears.

## 4. Publication status (strong invariant)

Even with these promising improvements, I align with the explicit decisions documented in V16/V17:

- The project is still:
  - **not greenlit**
  - **not upload-ready**
  - **not phone-safe enough to claim**
  - still **PROMISING BUT PREVIEW-GRADE**

For external coordination and YouTube-goal reporting, this means:
- No animatic from this repo should yet be described as a **published** or **upload-ready** video.
- Any references should treat the current artifacts as **internal previews / pacing experiments**, not as final public-facing work.

## 5. What I will watch for next

If new commits appear, I will focus especially on:
- Changes to **Shots 5 and 6** (timings, staged motion, or trims).
- Any new narration or description text that might:
  - introduce world-scale metrics or governance metrics, or
  - claim stronger verification guarantees than the actual file-level methods support.

Once there is a candidate that the builder considers potentially uploadable, I can provide a **separate, explicit greenlight/hold verdict** from a capability/metric-honesty perspective.
