# Narration - Video 7

A dashboard says, "Active users: twenty-four thousand" in January.
The same dashboard says, "Active users: thirty-one thousand" in April.
Same label. Bigger number. Easy conclusion.

But we need one more check:
Did behavior change, or did the counting rule change?

On Verify the Rails, we use evidence before interpretation.
So we ask two questions:
Is the number real?
Is this comparison valid?

Because a number can be accurate and still non-comparable.
That is definition drift: the same label is reused while the metric underneath changes.
When that happens, both reports can be honest, and the trend claim can still overreach.

Throughout this video, keep three rails visible: Observed, Inference, Unknown.
Observed is what the source states. Inference is the conclusion. Unknown is what we still need.

First example: active users.
In January, the dashboard reports twenty-four thousand active users.
In April, it reports thirty-one thousand.
A post says, "Usage exploded by seven thousand users."

Then the methodology note says:
"Active users now includes web sessions, mobile sessions, and API token activity. Previously web plus mobile only."

Observed: January is twenty-four thousand.
Observed: April is thirty-one thousand.
Observed: the rule expanded to include API activity.
Inference: "all of this rise is behavior growth" does not follow.
Unknown: how much is real behavioral change versus newly counted activity.

Each value may be correct under its own rule.
But if the rule changed, the two values are not a clean apples-to-apples comparison.

Second example: resolved cases.
A tracker uses a monthly metric labeled resolved cases.
For months, that means fully resolved only.
Then an update note says resolved now includes fully resolved, partially resolved, and administratively closed.
The next report shows a sharp increase.

Again, this can be honest reporting.

Observed: category definition expanded.
Observed: count rose right after expansion.
Inference: "the team suddenly solved far more cases at the same standard" may be too strong.
Unknown: what the trend would look like under one stable definition.

When the bucket gets bigger, counts often rise even if process quality is flat.

Third example: incidents with broader scope.
A city or school report publishes incidents.
Earlier reports count high-severity events only.
A newer report includes low-severity reports and near-miss submissions under the same incidents label.
Total incidents rise.

That increase may be real under the newer scope and useful for prevention planning.
But comparability is the issue.

Observed: scope broadened to include more event types.
Observed: total incident count increased.
Inference: "conditions became dramatically more dangerous" is not proven by that comparison alone.
Unknown: the trend under a constant severity threshold.

When scope broadens, measured volume can rise without an equal rise in underlying harm.
So the number is not necessarily wrong; interpretation can still drift past evidence.

Across all three examples, the pattern is identical.
Active users changed what activity qualifies.
Resolved cases changed what outcomes qualify.
Incidents changed what event types qualify.

Same label.
Different metric.

Use this six-step checklist before sharing a trend claim.

One: match the exact metric label in both sources.
Do not assume same label means same definition.

Two: read the metric definition or methodology note for each period.
If one period has a footnote and the other does not, treat that as unresolved.

Three: compare inclusion and exclusion rules side by side.
List what is newly included, newly excluded, or reclassified.

Four: find the change date.
Check release notes, changelogs, methodology updates, or footnotes.

Five: assign comparability status in plain language:
comparable, partially comparable, or not comparable.

Six: write one short evidence note using the three rails.

Observed: source A reports X under definition D1.
Observed: source B reports Y under definition D2.
Inference: the reported level changed between periods.
Unknown: how much change reflects underlying reality versus definition drift.

This discipline does not weaken analysis.
It keeps confidence proportional to evidence.
You are not saying, "Ignore the number."
You are saying, "Use the number within its definition."

Definition drift is quiet.
The label looks familiar, so comparison feels automatic.
But when the counting rule moves, the conclusion must slow down.

Before sharing a before-and-after claim, check the definition line, not just the trend.

Same label does not guarantee same metric.
