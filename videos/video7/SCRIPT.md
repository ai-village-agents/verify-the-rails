# Script - Video 7

## Title

Same Label, Different Metric

## Promise

A number can be accurate and still be non-comparable if the counting rule changed underneath the same label.

This episode shows how to detect definition drift before treating two values as evidence of change.

## Cold Open

A dashboard says `Active users: 24,000` in January.
The same dashboard says `Active users: 31,000` in April.
The label did not change.
The number rose sharply.

Many people stop there.

But there is a hidden question:
**Did behavior change, or did the definition change?**

## Reframe

Most metric confusion online is not fake data.
It is definition drift.

That means the same word is reused while the inclusion rule changes.
When that happens, both numbers can be real, and the comparison can still be wrong.

So we separate three rails every time:

- `Observed`: what the source directly reports
- `Inference`: what someone concludes from it
- `Unknown`: what is still missing about scope or method

## Main Point

Before comparing two values with the same label, verify that they counted the same thing.

If the counting rule changed, the values are not directly comparable, even if each value is correctly reported.

## Example 1: Active Users Dashboard Rule Change

Suppose a product dashboard shows:

- January: `Active users = 24,000`
- April: `Active users = 31,000`

In April, a methodology note appears:
`Active users now includes web sessions, mobile sessions, and API token activity. Previously web + mobile only.`

Now the interpretation changes.

`Observed`: the dashboard reports 24,000 then 31,000.
`Observed`: the inclusion rule expanded in April.
`Inference`: "usage growth alone caused the full jump" is not established.
`Unknown`: how much of the increase came from behavior versus newly included activity.

The number can be real.
The comparison can still be mixed.

## Example 2: Resolved Cases Category Expansion

Now a policy tracker labeled `Resolved cases`.
For months, it counted only fully resolved cases.
Then a release note says `Resolved now includes fully resolved + partially resolved + administratively closed`.
The next report shows a large increase.

Again, no fabrication is required.
The count may be accurate under the new rule.

`Observed`: the category definition expanded.
`Observed`: the reported count increased after expansion.
`Inference`: "operations suddenly got much better" may overstate what the data proves.
`Unknown`: trend under a consistent definition across both periods.

Same label.
Different bucket contents.

## Example 3: Incidents Metric Broadens Scope

Third case: an `Incidents` metric in a city or school report.
Earlier reports counted only high-severity incidents.
A newer report includes low-severity reports and near-miss submissions under the same `Incidents` label.
The total rises.

`Observed`: the new report includes broader incident types.
`Observed`: the incident total is higher.
`Inference`: "risk conditions sharply worsened" is not proven by that comparison alone.
`Unknown`: what the trend looks like when severity thresholds are held constant.

A broadened scope can create an honest increase in measured count without an equal increase in underlying harm.

## Practical Verification Routine

Use this checklist before sharing a before-and-after number claim:

1. Confirm the exact metric label in both sources.
2. Read the definition or methodology note in both periods.
3. Compare inclusion and exclusion rules side by side.
4. Locate change date, release note, or footnote that documents rule changes.
5. Mark comparability explicitly: `comparable`, `partially comparable`, or `not comparable`.
6. Write claim boundaries using `Observed / Inference / Unknown`.

## Reusable Note Template

`Observed`: Source A reports X using definition D1.
`Observed`: Source B reports Y using definition D2.
`Inference`: the metric level changed.
`Unknown`: how much reflects real-world change versus definition drift.

This keeps confidence proportional to evidence.

## Close

Definition drift is quiet.
The label stays the same, so the numbers feel directly comparable.

But if the counting rule moved, the comparison moved with it.

Before you share the trend line, check the definition line.

**Same label does not guarantee same metric.**
