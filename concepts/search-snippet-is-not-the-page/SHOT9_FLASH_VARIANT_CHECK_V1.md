# Shot 9 Flash Variant Check V1 — The Search Snippet Is Not the Page

## Status note
This is a planning-stage timing and legibility check.
It is not a script lock, visual lock, greenlight note, upload-readiness claim, or phone-safety claim.

## Why this check exists
The safest rough ending shape has been the no-Shot-9 version.
But the planning notes also left open a stricter alternative: keep Shot 9 only if it can survive as a true flash without turning into a second explainer.

So this check answers one narrow question:
- can a truncation-pattern Shot 9 be inserted into the rough animatic while staying structurally brief and visually secondary?

## Variant tested
Temporary build only; no tracked renderer changes.

A temporary source still was generated under `/tmp/search_snippet_shot9_flash_v1/frames/09_truncation_flash.png` using the already planned truncation example:

Preview flash:
- `Priority support is included for enterprise accounts on annual contracts...`

Live-page completion:
- `Priority support is included for enterprise accounts on annual contracts after account verification is complete.`

Only the limiting phrase was brightened:
- `after account verification is complete.`

## Temporary timing used
Temporary CSV:
- `/tmp/search_snippet_shot9_flash_v1/SHOT_TIMINGS_SHOT9_FLASH_V1.csv`

Late-sequence timings in that variant:
- Shot 7: `7.5s`
- Shot 8: `2.5s`
- Shot 9: `1.5s`
- Shot 10: `6.5s`
- Shot 11: `4.5s`

Nominal total:
- `62.5s`

## Build result
Temporary output:
- `/tmp/search_snippet_shot9_flash_v1/rough_animatic_shot9_flash_v1.mp4`

`ffprobe` format check:
- duration: `62.560000`
- size: `320694` bytes

Frame timestamps observed:
- `0.000000`
- `5.520000`
- `11.000000`
- `14.520000`
- `20.000000`
- `27.520000`
- `40.000000`
- `47.520000`
- `50.000000`
- `51.520000`
- `58.000000`
- `62.520000`

Late-sequence interpretation:
- Shot 8 encoded hold: about `47.52–50.00s`
- Shot 9 encoded hold: about `50.00–51.52s`
- Shot 10 encoded hold: about `51.52–58.00s`
- Shot 11 encoded hold: about `58.00–62.52s`

This means the temporary Shot 9 behaves like a real inserted flash beat, not an accidental rebuild of the ending.

## Visual review artifacts
Temporary source-based review artifacts:
- `/tmp/search_snippet_shot9_flash_v1/late_sequence_source_hold_strip_with_shot9_small.png`
- `/tmp/search_snippet_shot9_flash_v1/shot9_source_legibility_pressure_view.png`

What they support:
1. the ending still reads in the same broad order
   - Shot 7 anchors the proof
   - Shot 8 stays brief
   - Shot 9 appears as a quick confirming interruption
   - Shot 10 resumes the viewer routine
   - Shot 11 remains the callback landing
2. the inserted Shot 9 is visibly denser than Shots 8, 10, and 11
3. Shot 9 seems readable enough at larger source-based review sizes to function as a quick pattern echo
4. Shot 9 degrades quickly as the frame is reduced
5. therefore Shot 9 does **not** become evidence for small-player robustness, much less a phone-safety claim

## Main judgment
This bounded test gives **practical build-level support** for a very narrow claim:

> A truncation-pattern Shot 9 can fit into the rough ending as a roughly `1.5s` flash without obviously breaking the taper shape.

But the same test also supports a restraint conclusion:
- Shot 9 remains too dense to carry explanatory burden
- it only survives as a brief category-broadening flash
- it should not receive extra labels, extra narration, or extra timing

## What this changes
- It slightly strengthens the case that Shot 9 is **possible**.
- It does **not** overturn the safer default that the no-Shot-9 ending is easier to defend.
- It does **not** change the project status:
  - not script-locked
  - not visually locked
  - not greenlit
  - not upload-ready

## Bottom line
If Shot 9 is used at all, this check suggests the safest form is still:
- one truncation-pattern flash
- about `1.5s` of visual dwell
- no extra explanatory load
- immediate handoff back to Shot 10

If later passes need more explanation than that, the better move is still to cut Shot 9 rather than let the ending thicken.
