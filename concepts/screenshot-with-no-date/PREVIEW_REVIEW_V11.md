# Preview Review V11 — Shot 4 Trim Candidate Check

Date: 2026-05-20
Artifact reviewed: `preview_animatic_v10.mp4`
Candidate timings: `SHOT_TIMINGS_V5_CANDIDATE.csv`
Related notes:
- `PREVIEW_REVIEW_V10.md`
- `SHOT4_REBALANCE_NOTE_V1.md`

## Why this review exists
`PREVIEW_REVIEW_V10.md` established that the previous timing candidate fixed the old opening sprint but turned **Shot 4 / Beat 2** into the clearest pacing bottleneck.

The narrow next test was intentionally small:
- keep all other timings the same
- trim only `04_zoomout_capture_reveal`
- move it from `34.0s` to `30.0s`

So the question for this pass is not whether the whole piece is now final.
It is simply whether that `4s` trim is enough to make Beat 2 stop feeling sticky **without** undoing the gains in Beat 1 or reintroducing Beat 2 narration-compression risk.

## Review method
For this concept, I still do **not** want to trust browser playback or quick stream-copy beat clips as the primary evidence.

Primary review method used here:
- inspect the timing table directly
- generate timestamped contact sheets directly from `preview_animatic_v10.mp4`
- measure sampled frame-to-frame visual change from extracted source frames

Artifacts used in this pass:
- `/tmp/v10_review/review_beat1_v10_sheet.png`
- `/tmp/v10_review/review_beat2_v10_sheet.png`
- `/tmp/v10_review/review_beat6_v10_sheet.png`

## Targeted timing context
### Beat 1 — Hook (`01` through `03d`)
- unchanged from V10 review baseline
- total: `25.0s`
- approximate density: `77 / 25.0 = 3.08 wps`

### Beat 2 — First reveal (`04`)
- changed from `34.0s` to `30.0s`
- total: `30.0s`
- approximate density: `107 / 30.0 = 3.57 wps`

### Beat 6 — Closing memory (`13`)
- unchanged from V10 review baseline
- total: `14.0s`
- approximate density: `39 / 14.0 = 2.79 wps`

## Frame-change evidence
### Beat 1 sampled change
Using 2-second extracted-frame intervals across the opening, the sampled frame-to-frame mean absolute differences were:

`[12.3693, 1.6581, 4.0897, 17.4947, 11.5084, 0.0, 7.2092, 5.1863, 0.0, 12.2506, 0.0, 0.0]`

Interpretation:
- the opening still contains multiple meaningful state changes
- some 2-second pairs are naturally identical because a shot is holding for comprehension
- but the beat as a whole clearly behaves like a reveal chain rather than a single parked still

### Beat 2 sampled change
Using 2-second extracted-frame intervals across the `30.0s` Shot 4 hold, the sampled frame-to-frame mean absolute differences were:

`[12.1043, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`

Interpretation:
- the first non-zero jump is just the entry into Shot 4 from the preceding shot
- after that, every sampled 2-second comparison was effectively unchanged
- in practical terms, the beat still behaves like one static frame held for almost the entire `30s`

A useful external heuristic from GPT-5.2 was to aim for **no more than about `6–8s` between visible state changes** if Shot 4 is going to stay long.
This candidate does **not** meet that bar:
- once Shot 4 begins, the sampled evidence shows no meaningful internal state change across roughly `28s` of the hold

### Beat 6 sampled change
Using 2-second extracted-frame intervals across the closing frame, the sampled frame-to-frame mean absolute differences were:

`[0.0146, 0.0, 0.0, 0.0, 0.0, 0.0]`

Interpretation:
- this is expected for a static callback ending
- the key question there is proportion, not motion density
- nothing here suggests the existing `14.0s` ending needs to be reopened

## Findings
### 1) Beat 1 still keeps the gains from the prior redistribution
The good news is that this narrower Shot 4 trim did **not** damage the stronger opening achieved in the prior pass.

Practical judgment:
- Beat 1 still looks materially healthier than the old `v8` timing baseline
- the hook still functions as a staged reveal rather than a sprint
- no new evidence here suggests reopening Beat 1

### 2) Beat 2 is improved on paper, but still visually too static
This candidate absolutely moves in the right direction numerically.

What improved on paper:
- Shot 4 is shorter than the `34.0s` version
- Beat 2 density improves from about `3.15 wps` to about `3.57 wps`
- the candidate remains much safer for narration than the old `20.0s` baseline

But the stronger practical finding is that the **visual problem mostly remains**.

What the beat-2 sheet and sampled diffs show:
- the same zoomed-out evidence frame still repeats through the whole sampled span
- the extra `4s` trim reduces the overhold somewhat, but does **not** create new internal visual events
- the beat still reads as a long static explanation pause rather than a mini-reveal

Practical judgment:
- **`30.0s` is better than `34.0s`, but not enough to fully solve the Shot 4 stickiness if the shot stays visually static**
- this candidate avoids the earlier narration-compression problem better than a hard snap back to `20.0s`
- however, it does not yet justify keeping Beat 2 long in a motionless form

### 3) Beat 6 still looks proportionate
Nothing in this pass changes the earlier closing judgment.

Practical judgment:
- `14.0s` still does not look too abrupt
- the ending remains stable, legible, and proportionate
- Shot 4 remains the only pacing question this pass materially changes

## Overall interpretation
This `30.0s` Shot 4 candidate is a **useful midpoint test**, but it does not fully clear the bottleneck.

Best current interpretation:
- it preserves the opening gains
- it preserves the acceptable trimmed ending
- it is safer for narration than collapsing all the way back to the old short Beat 2
- **but it still leaves Beat 2 visually under-differentiated for too long**

So the story shifts from:
- `34.0s` = clearly overheld static frame

to:
- `30.0s` = less overheld, but still too static to feel convincingly solved

## Recommended next move
Keep the next pass narrow.

Most likely paths now:
1. **add internal staged motion to Shot 4** if Beat 2 is meant to stay around this length
2. **trim Shot 4 further** into the lower part of the previously suggested band if it will remain static

Current lean:
- if no staged motion is added, the evidence now points toward trying a value **closer to `28s` than `30s` or `34s`**
- if Beat 2 needs to remain around `30s`, it should earn that time with visible progression rather than one parked frame

What still should **not** happen next:
- broad script rewriting
- reopening opening geometry churn
- claiming the piece is greenlit because the runtime now sits in a more comfortable band

## Decision
- **Status:** informative narrow test, not a lock
- **Beat 1:** gains preserved
- **Beat 2:** improved numerically, but still visually sticky in static form
- **Beat 6:** still acceptable at `14.0s`
- project status remains:
  - **not greenlit**
  - **not upload-ready**
  - **not phone-safe enough to claim**
  - still **PROMISING BUT STILL PREVIEW-GRADE**
