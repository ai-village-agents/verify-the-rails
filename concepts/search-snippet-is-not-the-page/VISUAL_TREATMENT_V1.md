# Visual Treatment V1 — The Search Snippet Is Not the Page

## Status note
This is a planning document for visual direction only.
It is not a script lock, storyboard lock, greenlight note, or upload recommendation.

## Design goal
The viewer should first experience why the preview feels trustworthy, then experience the exact moment that trust becomes too broad.

This piece should make the mistake feel structural:
- the preview is real
- the page is real
- the layers are not the same thing

## Core visual principle
**Treat preview, live page, and update clue as three distinct evidence layers.**

The piece should not depend on tiny support text to explain that difference. The distinction should be visible in:
- framing
- motion
- color emphasis
- side-by-side comparisons
- explicit layer labels

## Layer roles

### 1. Preview layer
What it should communicate:
- fast confidence
- apparent clarity
- compressed authority

What it should look like:
- search-results style stack
- one highlighted snippet line
- slightly simplified interface chrome
- enough realism to feel familiar without becoming brand-specific

Viewer feeling to evoke:
- “That line looks definitive.”

### 2. Live page layer
What it should communicate:
- broader context
- exact wording
- current visible source state

What it should look like:
- opened article/help page surface
- visible heading and body block
- qualifier presented as part of the sentence, not a tiny footnote
- cleaner reading space than the preview layer

Viewer feeling to evoke:
- “The source says something narrower than the preview implied.”

### 3. Update clue layer
What it should communicate:
- time/version evidence
- why two real artifacts can disagree
- which artifact is stronger for the present-tense claim

What it should look like:
- explicit `Updated` date, revision row, or changelog marker
- visually separate cue, not buried decoration
- brief but legible absolute date

Viewer feeling to evoke:
- “Now I understand why the disagreement exists.”

## Motion strategy
Meaning should arrive through transitions between layers, not paragraphs of explanation.

Preferred motion pattern:
1. start on the preview line alone
2. hold long enough for certainty to form
3. open the result into the live page
4. pause on the qualifier that changes scope
5. reveal the update clue that explains the mismatch
6. collapse into a simple evidence hierarchy card

This should feel like a correction of frame, not a dramatic twist.

## Framing rules
- Preview layer should feel narrower and more compressed.
- Live page should feel wider and calmer.
- Update clue should feel like a decisive anchor, not a garnish.
- The audience should be able to tell when they are looking at:
  - a result preview
  - a source page
  - a date/version clue
  without needing long captions.

## Color / emphasis logic
Use emphasis to distinguish evidence roles rather than decorate.

Suggested logic:
- preview layer = warm highlight for the quoted snippet line
- live page layer = cool or neutral emphasis for the full current wording
- update clue = amber accent for date/version evidence

The color system should help answer:
- what the preview claims
- what the page currently says
- what explains the difference

## Text-density rule
This concept should aim for lighter support-text density than `The Screenshot With No Date`.

Where possible:
- put the important wording inside the artifact itself
- use short labels instead of explanatory paragraphs
- let contrast between surfaces carry meaning

If a frame requires a large side explanation block to work, the frame is probably doing too much.

## Best candidate visual chain right now
Current strongest synthetic path:
1. search result snippet shows broad rule
2. live policy page shows newly added qualifier
3. updated-date clue explains why both artifacts are real
4. evidence hierarchy card teaches the viewer what to trust for present-tense claims

This remains strongest because the mismatch is legible through visible structure rather than tiny metadata alone.

## Anti-drift rules
- Do not turn this into generic “search is bad” commentary.
- Do not make the whole piece depend on one platform's exact UI.
- Do not solve the lesson through narration-only abstraction.
- Do not bury the qualifier in microcopy that only works at desktop scale.
- Do not imply that previews are fake; the point is that they are partial and time-sensitive.

## Current judgment
This concept looks promising because the main lesson can be staged through visible layer mismatch and a dated update clue.

Current status remains:
- planning only
- not scripted
- not storyboarded
- not greenlit
