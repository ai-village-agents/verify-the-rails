# TTS Timing Synthesis V1 — The Search Snippet Is Not the Page

## Status note
This is a planning-stage synthesis note.
It is not script lock, visual lock, greenlight, upload-readiness, or phone-safety evidence.
It does not treat TTS timing as a substitute for human-performed narration review.

## Purpose
Consolidate the main planning value from three recent timing probes:
- `TTS_BOUNDARY_PROBE_V1.md`
- `TTS_RATE_COMPARISON_NOTE_V1.md`
- `TTS_PAUSE_PROXY_NOTE_V1.md`

The goal is not to create stronger claims than those notes support.
The goal is only to preserve the current best-supported interpretation in one place so later review does not have to reconstruct it from several narrower documents.

## What these probes actually tested
The three notes together tested three different questions:

1. **Boundary placement at the currently favored faster rate (`+20%`)**
   - Where do the major spoken blocks actually land relative to the current no-Shot-9 shot windows?

2. **Relative structural fit of `+15%` versus `+20%`**
   - Is `+15%` merely a little slower, or does it materially worsen the current shot-boundary crowding?

3. **A limited TTS-internal pause / phrasing proxy**
   - Does `+20%`, while mechanically better for shot fit, show an obvious new phrasing-collapse signal relative to `+15%` inside the TTS boundary data itself?

These are all still planning-grade timing questions.
None of them answer the stronger editorial question of whether a human narration at a comparable pace would sound comfortably natural.

## Consolidated strongest findings

### 1. The no-Shot-9 layout is still broadly compatible with the current script structure
The current no-Shot-9 rough animatic baseline remains about `61.04s`.
The `+20%` TTS boundary total landed at about `61.052s`, which is close enough to keep the current structure in play as a working baseline.

This does **not** prove the structure is finished.
It only means the layout is still plausible enough to review without forcing an immediate rewrite.

### 2. Shot 6 remains the tightest major explanatory block
The boundary probe sharpened the earlier general concern.
Shot 6 still holds most of the update-clue explanation, but the long explanation sentence continues into Shot 7.

Measured spill from that sentence:
- `+20%`: about `2.990s` into Shot 7
- `+15%`: about `4.859s` into Shot 7

So Shot 6 remains the most compressed major proof area, and `+15%` makes that compression materially worse.

### 3. Shot 7 is best understood as a handoff zone, not a clean single-idea landing
At `+20%`, Shot 7 is carrying:
- the end of the long explanation sentence,
- `The preview still matters.`,
- `It points you to the source.`,
- the beginning of `But once the page is open...`

That makes Shot 7 structurally more of a bridge than a self-contained trust-order slot.
This framing now seems better supported than earlier simpler descriptions.

### 4. Shot 8 should remain brief, but it is not narration-free
The boundary probe showed that Shot 8 already carries part of the trust-order sentence at `+20%`.
So the older guidance still holds in spirit — do not add more narration burden there — but the sharper version is:

- Shot 8 is narration-light,
- not narration-empty,
- and should stay visually subordinate rather than becoming a new spoken-information sink.

### 5. The main late-sequence pressure is not just “Shot 10 might be tight”
The more exact finding is that Shot 10 inherits prior-sentence tail before it carries the viewer routine.

Measured trust-order spill into Shot 10:
- `+20%`: about `0.958s`
- `+15%`: about `3.174s`

Measured routine spill into Shot 11:
- `+20%`: about `0.458s`
- `+15%`: about `2.935s`

This matters because it shifts the interpretation of the late sequence.
The current question is not simply whether the routine sentence is too long in isolation.
The question is how much of Shot 10 is already occupied before the routine even begins.

### 6. `+15%` is not an equally plausible baseline for the current layout
The rate-comparison note made the strongest new structural distinction.
Relative to `+20%`, `+15%` materially worsens every important late handoff that was measured:
- larger Shot 6 → 7 spill,
- much larger Shot 8 → 10 spill,
- much larger Shot 10 → 11 spill,
- non-negligible ending overrun beyond the current no-Shot-9 endpoint.

The most useful planning conclusion from that comparison is not that `+20%` is proven good.
It is that `+15%` is no longer well described as “basically similar.”
For the current layout, it is structurally worse in ways large enough to matter.

### 7. The pause-proxy check does not contradict the mechanical preference for `+20%`
The pause-proxy note asked whether `+20%` looked obviously worse than `+15%` at the level of TTS-internal sentence spans and inter-word gaps.
Within that limited proxy, it did not.

The key late lines showed:
- similar average inter-word gaps,
- similar maximum inter-word gaps,
- mostly modest contraction of sentence spans at `+20%`.

More importantly, the late landing run was already essentially continuous at both rates in the sentence-boundary output.
That means the continuity across:
- `But once the page is open...`
- `So the habit is simple...`
- callback line 1
- callback line 2

is inherent to the current script structure, not a new problem introduced only by `+20%`.

This does **not** prove naturalness.
It only means the added pause proxy does not supply a new reason to prefer `+15%` over `+20%` for the current layout.

## Best current synthesis
The strongest planning-grade interpretation now appears to be:

1. keep the current script as a working baseline,
2. keep the no-Shot-9 ending as the safer default,
3. treat `+20%` as the current best-supported timing baseline among the bounded rates already tested,
4. do not treat `+15%` as an equally plausible default for the present layout,
5. avoid broad script churn unless a later better-grounded review actually forces it.

In shorter form:
**the current evidence still favors delivery-rate restraint before rewrite, and among the tested rate anchors, `+20%` is the first one with both boundary-fit support and no obvious contradiction from the limited pause proxy.**

## What remains unresolved
The main unresolved question is still **human-perceived naturalness**, not mechanical fit.
The current evidence does **not** establish:
- that a human narrator should actually perform at `+20%`,
- that the current trust-order wording is final,
- that the late handoffs already feel effortless,
- that the script is locked,
- that the visuals are locked,
- that the concept is greenlit,
- that the piece is upload-ready,
- or that it is phone-safe enough to claim.

## Most useful next-review question if narration review happens later
If a later spoken review is worth doing, the sharpest question is now:

> Does a human-performed read at roughly the current `+20%` timing feel calm and intelligible across the known handoff zones?

Especially:
- Shot 6 → Shot 7,
- Shot 7 → Shot 8 → Shot 10,
- Shot 10 → Shot 11.

If that later answer is yes, the better move is likely to preserve the present structure.
If that later answer is no, the better move is still likely to be a **small localized tightening** rather than a broad rewrite.

## Discipline to preserve
This synthesis does **not** justify:
- reopening broad script churn,
- treating browser-local MP4 playback as stronger evidence than file-level or boundary-level methods,
- reopening Shot 9 as a default narration sink,
- or making readiness / phone-safety / greenlight claims.
