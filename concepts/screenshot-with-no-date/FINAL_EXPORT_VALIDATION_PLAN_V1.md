# Final Export Validation Plan V1 — The Screenshot With No Date

Date: 2026-05-20
Status: planning-only validation note

Project status remains:
- not greenlit
- not upload-ready
- not phone-safe enough to claim
- PROMISING BUT STILL PREVIEW-GRADE

## Why this note exists
The current preview packet is now more controlled than it was earlier in the project.
That is useful progress.

But the clearest remaining blocker is no longer missing concept structure.
It is missing final-export evidence.

Several existing notes already say that final-export review is required before any real lock decision:
- QUALITY_REVIEW_V3
- PRODUCTION_LOCK_CHECKLIST_V1
- POST_TRIM_LOCK_STATUS_V1
- FINAL_ANIMATION_NOTES_V1

This note turns that requirement into one explicit procedure.

## What this plan is for
Use this plan only when an actual final rendered file exists.

Its job is to answer a narrow question:
What evidence would be strong enough to judge the real export without over-trusting browser playback or preview assumptions?

## What this plan is not
This note is not:
- a greenlight
- an upload recommendation
- a phone-safety claim
- proof that the current preview already passes

It is only a method plan for a later validation stage.

## Core validation principles
1. Trust file-level evidence over browser impression.
2. Review the actual final rendered file, not only preview animatics.
3. If a browser player and extracted frames disagree, treat the extracted file-level evidence as authoritative.
4. Keep claims narrow: export review can support stronger confidence, but it should not outrun what was actually tested.
5. Re-check the known fragile areas first, not only the easiest clean-looking shots.

## Known risk areas that must be checked directly
The current review history says the most important export-sensitive checks are:

1. Shot 3 / Frame 03
- still the clearest opening caution
- risk is not just small text in general, but explanatory burden around hidden timeline evidence

2. Shot 10 / Frame 10
- strongest late-sequence discipline risk
- danger is annotation regrowth or meaning becoming dependent on tiny range text

3. Shot 12 / Frame 12
- practical routine should feel calm and readable, not lecture-like
- recent trims improved density, but the export still needs direct checking

4. Shot 13 / ending state
- callback must remain explicit
- ending must be verified at file level if any browser player looks ambiguous

## Required inputs before running the plan
Before starting, gather all of the following:

1. the actual final rendered video file
2. the final timing table or equivalent shot timing reference
3. the current strongest review notes for comparison:
   - QUALITY_REVIEW_V3
   - SMALLER_PLAYER_REVIEW_V3
   - POST_TRIM_LOCK_STATUS_V1
   - PRODUCTION_LOCK_CHECKLIST_V1
4. an output folder for validation artifacts
5. the current intended shot order and key message distinctions

## Minimum artifact set to generate
The validation pass should create a small audit packet, not only a yes or no impression.

Minimum suggested artifacts:
- ffprobe summary text for the final export
- a whole-piece midpoint sheet from the actual final file
- medium and small reduced versions of that sheet
- focused sequence sheets for Shot 3, Shot 10, Shot 12, and the ending run
- an end-sequence verification sheet from the last seconds of the export
- a short written review note summarizing what passed, what remains risky, and what status is justified

## Validation procedure

### Step 1 — Confirm export identity and technical integrity
Check the actual rendered file first.

Record at least:
- file name
- file size
- duration
- stream information
- whether audio and video streams exist as expected

Purpose:
- prevent reviewing the wrong file
- prevent accidental reliance on a stale export
- establish a reproducible baseline for later comparison

### Step 2 — Build a whole-piece midpoint review from the actual export
Using the final timing reference, extract midpoint stills from each shot or staged sub-shot in the real export.

Then assemble:
- a full-size midpoint sheet
- a medium reduced sheet
- a smaller reduced sheet

Purpose:
- compare the final export against the strongest preview structure
- quickly detect whether readability or staging changed in unexpected ways
- avoid relying on memory of the preview path

Important interpretation rule:
- this is still a structural readability check, not full phone proof
- but it is stronger than preview-only review because it comes from the actual final export

### Step 3 — Run focused checks on the four known fragile zones
Do not stop at a whole-piece sheet.
Create separate focused artifacts for the known risk areas.

#### 3A. Shot 3 opening reveal check
Verify that the opening still communicates, in sequence:
1. the crop hid lower content
2. the capture date was hidden
3. the incident log was hidden
4. the resolved state was hidden

Pass condition:
- the sequence still teaches hidden timeline evidence even if every tiny word is not read perfectly

Fail condition:
- the shot mainly reads as crop geometry plus dense explanation

#### 3B. Shot 10 range-reveal check
Verify that the dashboard section still communicates that the visible dip sits inside a larger date range and later recovery.

Pass condition:
- the meaning shift is legible as a range-context reveal
- motion or visual hierarchy does more work than annotation clutter

Fail condition:
- tiny range text becomes the only real carrier of the point
- the frame regrows into a label-heavy explainer block

#### 3C. Shot 12 checklist check
Verify that the practical routine still feels ordinary and quick.

Pass condition:
- the staged routine reads as a usable habit
- recent microcopy trims remain directionally helpful in the final export

Fail condition:
- the checklist feels crowded, lecture-like, or dependent on patient reading

#### 3D. Ending verification check
Inspect the last seconds of the export directly.
If needed, extract multiple late frames across the final hold.

Pass condition:
- the callback remains explicit
- resolved-versus-reposted contrast is visibly present
- the actual file really ends where the intended ending says it should end

Fail condition:
- browser playback looks ambiguous and no file-level check is done
- the end state loses the final contrast or callback clarity

### Step 4 — Verify critical distinctions and final copy discipline
The export does not need to preserve every preview word exactly.
But it must preserve the critical distinctions the piece depends on.

Check that the final export still clearly communicates:
- original capture time versus later repost time
- resolved past state versus present-tense repost claim
- narrow chart crop versus wider date-range truth
- old announcement versus reposted panic framing
- pause-and-check habit as the viewer-facing takeaway

If key wording changed, judge the distinction, not just the literal sentence.

Fail if a wording change makes any major reveal more vague, more generic, or more annotation-dependent.

### Step 5 — Re-run reduced-view review on the real export
Reduce the final-export midpoint sheet to at least the same medium and small review sizes already used in prior checks.

Purpose:
- test whether the actual export preserves the same shot-role clarity that the strongest preview path showed
- detect regressions introduced by final polish, motion, or copy changes

Interpretation discipline:
- passing this still does not justify a phone-safe claim by itself
- it only supports a stronger smaller-player confidence statement if the evidence really holds

### Step 6 — Write the result as a gate decision, not a vibes summary
The final review note should explicitly answer:
- what was reviewed
- what artifacts were generated
- which gates passed
- which risk areas remain
- whether the best justified label is:
  - GREENLIT FOR FINAL PRODUCTION
  - NOT GREENLIT — REVISE BEFORE PRODUCTION
  - PROMISING BUT STILL PREVIEW-GRADE

## Red flags that should block any stronger claim
Do not advance status if any of the following happen:
- the review is based mainly on browser-local playback impression
- the file under review is not clearly identified
- the ending has not been checked at file level after any ambiguity
- Shot 3 still depends on dense explanatory support to carry the meaning
- Shot 10 regains clutter or depends on tiny range labels alone
- Shot 12 becomes more crowded in the export than in the improved preview path
- the reduced-view export check materially regresses from the current V15 baseline
- the review language starts claiming phone safety without direct supporting evidence

## Minimum standard for a meaningful status upgrade
A stronger status than the current preview-grade label would require all of the following:
1. actual final-export evidence exists
2. the known risk areas have been checked directly
3. the export preserves the current reveal logic rather than flattening it
4. reduced-view review on the actual export does not introduce new obvious failures
5. the final written judgment remains narrower than the strongest evidence available

If any of those are missing, the safest honest label remains preview-grade.

## Recommended output naming
If this plan is run later, keep the artifacts easy to audit.
Suggested directory pattern:
- tmp/final_export_validation_v1

Suggested artifact naming pattern:
- ffprobe_summary.txt
- full_piece_midpoint_sheet.png
- full_piece_midpoint_sheet_medium.png
- full_piece_midpoint_sheet_small.png
- shot03_sequence_sheet.png
- shot10_sequence_sheet.png
- shot12_sequence_sheet.png
- ending_sequence_sheet.png
- final_export_review.md

## Bottom line
The current strongest next move is not broader script churn or a premature readiness claim.
It is to make the eventual final-export gate explicit enough that the project can later be judged by file-level evidence instead of hopeful interpretation.
