# Example Scenes V1 — The Search Snippet Is Not the Page

All examples are synthetic, platform-neutral, and provisional.

## Example A
- Example name
  Policy qualifier added after indexing
- Surface setup
  A help-center policy article appears in search results. The preview line is shown under the page title in a standard results list view.
- Original wording / earlier state
  Page body on `January 8, 2026, 10:05 UTC`: “Account credits can be transferred between teams.”
- Later page state / qualifier
  Page updated on `March 14, 2026, 18:40 UTC`: “Account credits can be transferred between teams that share the same billing owner.”
- What the preview layer still shows
  Search preview continues to show: “Account credits can be transferred between teams.”
- Why people could argue past each other
  One person cites the preview as proof of an unrestricted rule; another person cites the opened page showing a restriction. Both are reading real text from different states.
- What the viewer should check
  Open the page, find the last-updated line, and compare the preview sentence against the current paragraph wording.

## Example B
- Example name
  Truncated snippet drops the limiting clause
- Surface setup
  A results snippet shows a clipped sentence ending in an ellipsis. The full sentence exists on the live guidance page.
- Original wording / earlier state
  Earlier full sentence on `February 2, 2026`: “Priority support is included for enterprise accounts on annual contracts.”
- Later page state / qualifier
  Current sentence on `April 21, 2026, 09:15 UTC`: “Priority support is included for enterprise accounts on annual contracts after account verification is complete.”
- What the preview layer still shows
  Snippet displays: “Priority support is included for enterprise accounts on annual contracts...”
- Why people could argue past each other
  The preview preserves the strongest promise while clipping the condition. One person reads “included,” another reads the qualifier on-page and interprets a gate.
- What the viewer should check
  Open the result, read the full sentence without truncation, and verify whether any condition sits after the clipped segment.

## Example C
- Example name
  Shared card preview lags behind revised page
- Surface setup
  A team chat card embeds a page title and one-line summary from a knowledge article. The card was generated when the link was first pasted.
- Original wording / earlier state
  Article summary at `May 1, 2026, 16:20 UTC`: “Data exports remain available for 30 days.”
- Later page state / qualifier
  Article revised at `May 12, 2026, 07:55 UTC`: “Data exports remain available for 30 days for active workspaces; suspended workspaces have a 7-day export window.”
- What the preview layer still shows
  The chat embed card still reads: “Data exports remain available for 30 days.”
- Why people could argue past each other
  People citing the card believe the 30-day rule is universal; people opening the live page see a conditional rule by workspace status.
- What the viewer should check
  Open the underlying page from the card, confirm the revision date, and compare embed summary text to the current rule sentence.

## Selection guidance
Example A currently looks strongest for visual storytelling because the disagreement is easiest to stage through a clean layer stack: search preview sentence, opened page qualifier, and explicit dated update clue.
