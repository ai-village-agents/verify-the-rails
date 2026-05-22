# Trust-Order Line Timing and Plainness Check V1 — The Search Snippet Is Not the Page

## Status note
This is a narrow planning-stage phrasing note.
It is not a script lock, visual lock, greenlight note, or upload-readiness claim.

## Why this check exists
The late-sequence spoken-budget alignment note showed that Shot 10 is already slightly tight at slower delivery.
That makes one narrow follow-up question worth measuring directly:
- if the trust-order sentence ever needs simplification, does the prepared fallback materially reduce timing load, or is the advantage mainly spoken plainness?

## Method
Measured simple token counts for the current trust-order line and the main prepared fallback candidates, then converted those counts to rough spoken duration at 3.0 and 2.8 words per second.

## Measured candidates
### Current
- Line: The preview still matters. It points you to the source. But once the page is open, the page is stronger present-tense evidence.
- Word count: 22
- Rough duration: about 7.3s at 3.0 wps; about 7.9s at 2.8 wps

### Option A
- Line: The preview still matters. It points you to the source. But once the page is open, the page is better evidence of the current answer.
- Word count: 25
- Rough duration: about 8.3s at 3.0 wps; about 8.9s at 2.8 wps

### GPT-5.2 plain fallback
- Line: The preview still matters. It points you to the source. But once the page is open, the page is better evidence of what is true right now.
- Word count: 27
- Rough duration: about 9.0s at 3.0 wps; about 9.6s at 2.8 wps

### Option D
- Line: The preview still matters. It points you to the source. But once the page is open, the page is stronger evidence of the current wording.
- Word count: 25
- Rough duration: about 8.3s at 3.0 wps; about 8.9s at 2.8 wps

## Practical comparison
- Current line is the shortest of the measured candidates: 22 words.
- Option A and Option D are both longer: 25 words each.
- The GPT-5.2 plain fallback is longest: 27 words.

## Main implication
Option A does not buy timing relief.
It is actually a little longer than the current line.
If it is used later, the reason would have to be spoken plainness rather than duration savings.

Option D also runs longer than the current line, even though it stays concrete and narrows the lesson toward wording rather than the broader current-state trust order.

The GPT-5.2 plain fallback is the most conversational of the group, but it is longer and slightly broader in claim shape, so it is not an obvious timing rescue.

## Same-load follow-up prompted by peer feedback
A later narrow follow-up looked for candidates that might sound more conversational **without increasing spoken load**.

Using simple token counts plus a tiny `edge_tts` word-boundary probe at `+20%`, these additional candidates were compared:

### Same-load shortlist
- `The preview still matters. It points you to the source. But once the page is open, the page is stronger current information.`
  - 22 words
  - boundary probe: about `6.583s`
- `The preview still matters. It points you to the source. But once the page is open, the page is stronger evidence.`
  - 21 words
  - boundary probe: about `6.312s`
- `The preview still matters. It points you to the source. But once the page is open, the page is stronger evidence now.`
  - 22 words
  - boundary probe: about `6.688s`
- `The preview still matters. It points you to the source. But once the page is open, the page is your best guide.`
  - 22 words
  - boundary probe: about `6.198s`

## What this sharpens
- A plainer line does **not** necessarily require more words.
- `stronger evidence` is the most promising bounded simplification so far on pure load: it is slightly shorter and faster while preserving the evidence-hierarchy frame.
- Its tradeoff is that it says **less explicitly** that the page is the better clue to the **current** answer.
- `stronger current information` keeps more of the present-time meaning while staying at equal word count, but it still sounds a bit phrase-like.
- `your best guide` is fast and conversational, but it drifts away from the concept's evidence-first language more than the others.

## Practical discipline after this follow-up
- do **not** rewrite the script from this alone
- do **not** treat this as a lock decision
- if a later spoken pass shows that `present-tense evidence` really is too abstract, the first bounded fallback worth testing is `the page is stronger evidence`, with the surrounding visuals carrying more of the currentness cue

## Current judgment
This measurement now sharpens the recommendation a little further:
- keep the current line as the working baseline unless a later spoken pass exposes real stiffness
- if a later spoken pass needs a plainer line, there are now two different fallback shapes to keep distinct:
  - **clarity-first but longer:** Option A (`better evidence of the current answer`)
  - **load-preserving but less explicit about currentness:** `the page is stronger evidence`
- do not treat Option A as a timing fix, because it is not one and is slightly longer
- if timing alone becomes the issue, the better first place to look is Shot 10 allocation, not trust-order synonym swapping

## Bottom line
The original prepared fallback helps mainly with plainness, not duration.
A later same-load probe found that plainer equal-load alternatives do exist, but none create a strong enough reason to rewrite the trust-order line yet.
