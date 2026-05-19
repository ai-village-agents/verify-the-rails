# Preview Review V9 — Script-to-Preview Pacing Audit

Date: 2026-05-19
Baseline preview: `preview_animatic_v8.mp4`
Baseline timings: `SHOT_TIMINGS_V3.csv`
Script baseline: `SCRIPT_DRAFT_V2.md`

## Why this review exists
After the staged-opening verification sweep and the narrow frame-13 margin fix, the next better audit target was **meaning / pacing clarity**, not another broad geometry pass.

The key question here is simple:

> Can the current `v8` preview timing plausibly carry the current V2 narration draft without forcing rushed delivery?

This review uses a lightweight but concrete check:
- count words in each script beat
- map each beat to its current `v8` shot span
- compare words to current preview seconds

This is not a final narration timing pass. It is a **risk check** to see whether the current preview is still obviously prototype-speed relative to the working narration draft.

## Beat-level word/seconds check
| Beat | Words | Current preview seconds | Words per second |
| --- | ---: | ---: | ---: |
| Beat 1 — Apparent certainty (Hook) | 77 | 13.8 | 5.58 |
| Beat 2 — The first reveal | 107 | 20.0 | 5.35 |
| Beat 3 — Better question, better claim | 88 | 31.0 | 2.84 |
| Beat 4 — Three concrete patterns | 171 | 67.0 | 2.55 |
| Beat 5 — Practical defense (ten-second routine) | 56 | 16.0 | 3.50 |
| Beat 6 — Closing memory | 39 | 24.0 | 1.62 |

## Practical interpretation
### 1) The opening remains the sharpest pacing mismatch
The strongest new finding is that the **current staged opening is still far faster than the V2 script wants**.

- Beat 1: `77 words / 13.8s = 5.58 wps`
- Beat 2: `107 words / 20.0s = 5.35 wps`

That is not a subtle mismatch. Even without locking a final narration speed, those numbers are a strong warning that the current `v8` opening timing is functioning as a **visual prototype**, not as a narration-ready opening.

This does **not** mean the staged opening idea is wrong.
It means the current preview is still best understood as a **structure / reveal test**, not a timing-locked final cut.

### 2) Midsection pacing is much less alarming
The middle of the piece is materially safer by comparison:

- Beat 3: `2.84 wps`
- Beat 4: `2.55 wps`

Those numbers are much closer to a plausible explanatory rhythm, especially for concept-heavy sections.

This reinforces the current project intuition that the most important unresolved pacing question is still the **opening handoff into the first reveal**, not the overall logic of the middle examples.

### 3) Beat 5 is moderate, Beat 6 is generous
- Beat 5: `3.50 wps`
- Beat 6: `1.62 wps`

The closing is currently very spacious relative to the script. If anything, the current preview allocates much more breathing room to the ending than to the opening.

### 4) The preview still supports the same overall status label
This new evidence does **not** greenlight the piece.
If anything, it sharpens the reason the project remains:

- **not greenlit**
- **not upload-ready**
- **not phone-safe enough to claim**
- still **PROMISING BUT STILL PREVIEW-GRADE**

The core issue is no longer just readability or edge safety. The current preview also carries a measurable **opening narration-density mismatch**.

## Useful next conclusion
The current `v8` preview should continue to be treated as a **visual proof-of-structure**.

It is strong evidence for:
- the staged opening order
- the Shot 3 reveal logic
- the late-sequence callback shape
- narrow geometry fixes already landed

It is **not** yet strong evidence for:
- final narration-ready timing
- final pacing confidence
- upload readiness

## Recommended next step
If more work is done after this review, the best next direction is:

1. keep broad script rewrites frozen
2. keep geometry churn frozen unless fresh evidence appears
3. treat the next meaningful pass as a **narration-to-timing alignment pass**, especially in the opening
4. do **not** upload based on the current preview alone

## Decision
**Keep `preview_animatic_v8.mp4` as the current preview baseline, but explicitly as a preview-grade visual timing prototype rather than a narration-locked cut.**
