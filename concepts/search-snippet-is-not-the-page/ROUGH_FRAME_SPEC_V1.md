# Rough Frame Spec V1 — The Search Snippet Is Not the Page

## Status note
This is a planning-stage rough frame spec.
It is not a render lock, storyboard lock, greenlight note, or upload-readiness claim.

## Purpose
Turn the concept into a small set of concrete frame targets with exact on-screen wording.
This is meant to reduce ambiguity before any prototype rendering work.

## Prototype scope
Limit the first prototype pass to six frames that test the main contradiction:
1. search preview
2. confidence formed from preview
3. opened live page
4. qualifier emphasis
5. update clue
6. evidence hierarchy

If those six frames do not work, the concept should not expand yet.

## Shared synthetic source details
Search result title:
- `Refund policy — Help Center`

Search result URL line:
- `help.example.com › billing › refund-policy`

Live page heading:
- `Refund policy`

Live page support line:
- `Billing and plan changes`

Update clue:
- `Updated March 14, 2026`

## Frame 1 — Search preview as apparent proof
### Visual role
Make the viewer feel why somebody would stop at the preview.

### On-screen text
Top search line:
- `Refund policy — Help Center`

URL line:
- `help.example.com › billing › refund-policy`

Snippet line:
- `Refunds are available for all annual plans.`

Optional small label:
- `Search preview`

### Emphasis rule
- Highlight only the snippet sentence.
- Keep surrounding interface quiet.

### Test question
Does the frame feel quotable without extra explanation?

## Frame 2 — Claim formed from preview
### Visual role
Show the leap from preview text to confident conclusion.

### On-screen text
Carry over the snippet line:
- `Refunds are available for all annual plans.`

Short overlay:
- `So refunds apply to every annual plan.`

### Emphasis rule
- The overlay should feel like a conclusion drawn from the preview, not a narrator lecture.
- Keep it short enough to read instantly.

### Test question
Can the viewer feel the certainty before the correction arrives?

## Frame 3 — Open the live page
### Visual role
Create the expectation that the page will simply confirm the preview.

### On-screen text
Page heading:
- `Refund policy`

Support line:
- `Billing and plan changes`

Body sentence:
- `Refunds are available for annual plans within 14 days of purchase.`

Optional page chrome:
- `Help Center`

### Emphasis rule
- Do not emphasize the whole sentence equally.
- Save strongest emphasis for the qualifier in the next frame.

### Test question
Does this still look calm and source-like rather than confrontational?

## Frame 4 — Qualifier changes scope
### Visual role
Make the narrowing phrase feel decisive.

### On-screen text
Main sentence again:
- `Refunds are available for annual plans within 14 days of purchase.`

Qualifier highlight:
- `within 14 days of purchase`

Optional short label:
- `Current page wording`

### Emphasis rule
- Shared wording should dim.
- The qualifier phrase should be the brightest element in the frame.
- Avoid extra bullets.

### Test question
Can the viewer understand the meaning shift even with the sound off?

## Frame 5 — Update clue explains the mismatch
### Visual role
Explain why preview and page can both be real.

### On-screen text
Update chip or header line:
- `Updated March 14, 2026`

Live page sentence retained in smaller role:
- `Refunds are available for annual plans within 14 days of purchase.`

Optional short label:
- `Why the layers disagree`

### Emphasis rule
- Date cue should be isolated and strong.
- This frame should not imply certainty about search indexing mechanics.

### Test question
Does the date feel causal rather than decorative?

## Frame 6 — Evidence hierarchy
### Visual role
Land the reusable viewer habit.

### On-screen text
Stack labels:
- `Preview: points to the source`
- `Live page: current wording`
- `Update clue: explains mismatch`

Bottom habit line:
- `Open the page. Compare the wording. Check one update clue.`

### Emphasis rule
- Keep the hierarchy labels short.
- The bottom habit line should read like a routine, not a scolding.

### Test question
Does the viewer leave with a trust order for present-tense claims?

## Prototype success conditions
The first rough visual pass is promising only if:
1. Frame 1 feels sufficient on purpose
2. Frame 4 makes the qualifier unmistakable
3. Frame 5 makes the date explanatory
4. Frame 6 lands without text overload
5. the sequence still works at reduced size better than dense screenshot-style layouts would

## Current judgment
Useful bridge between planning docs and any actual prototype render.
Still planning only.

Current status remains:
- not visually locked
- not script-locked
- not greenlit
