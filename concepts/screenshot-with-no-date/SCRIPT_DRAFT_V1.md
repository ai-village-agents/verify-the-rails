# Script Draft V1 — The Screenshot With No Date

## Beat 1 — Apparent certainty (Hook)
This screenshot is real. The repost is real. The time claim built from it is wrong.

Look at this crop: `OpsStatus`, `Partial Service Disruption`, `Started: 02:14 UTC`, and `API Gateway: Degraded Performance.` That is all true on its face. It also triggered panic when reposted on `2026-05-19 09:12 local` as proof the service was currently unstable.

The screenshot is not fabricated. The timestamp context is missing.

## Beat 2 — The first reveal
Now widen the frame.

You can see the original capture metadata: `2025-02-18 02:43 UTC`. Scroll a little lower and the incident thread ends with `Resolved 2025-02-18 03:26 UTC`.

So the same image that looked like a live outage is actually a record of a resolved event from more than a year earlier. The outage happened. The reposted conclusion did not match the timeline.

That is the split we need to keep visible:
- Observed: a real disruption occurred at one point.
- Inference: the disruption is happening now.
- Unknown: what changed after the screenshot moment.

Most screenshot confusion happens in that jump from observed to inferred.

## Beat 3 — Better question, better claim
The useful question is not only “Is this screenshot authentic?”

The useful question is “What present-tense claim is this screenshot being asked to support?”

A screenshot can reliably prove that a screen looked a certain way at a certain moment. It does not automatically prove that condition is still active, still representative, or still policy after later updates.

When people get this wrong, it is usually not because they are irrational. It is because screenshots feel like direct evidence. We see concrete pixels and skip the timeline check.

## Beat 4 — Three concrete patterns
Pattern one: status incidents outlive their own resolution in social circulation.

In the OpsStatus example, `Started: 02:14 UTC` is true, `Partial Service Disruption` is true, and yet the full log still shows `Resolved 2025-02-18 03:26 UTC` before the `2026-05-19 09:12 local` repost.

Pattern two: dashboard crops hide the selected range.

A chart dip at `2026-04-06 03:00 UTC` shows `Core Checkout: 88.4%` and `Express Checkout: 87.9%`. Cropped tightly, that looks like a current collapse. Uncrop the top control and you see `Last 90 days (2026-02-01 to 2026-04-30)`. Keep scrubbing and both lines are back above `98.9%` by `2026-04-06 05:00 UTC`.

Pattern three: old announcements reappear as “new” policy changes.

The reposted crop shows: “Starting June 1, 2025, standard workspace retention changes from 18 months to 12 months.” True text. But the full post header reads `Published 2025-05-12 16:00 UTC`, and the same thread includes a follow-up clarification at `2025-05-20 09:30 UTC`. Reposted on `2026-05-19`, it is old information framed as breaking.

Different surface, same mechanism: authentic content, broken time context.

## Beat 5 — Practical defense (ten-second routine)
Before resharing, run a short time check.

Open the original source page.
Find the timestamp and timezone.
Look for entries posted after the screenshot moment.
Then ask: “If I post this now, am I describing the current state or a past state?”

This is not forensic work. It is usually ten extra seconds and one wider view.

## Beat 6 — Closing memory
Return to the opening OpsStatus image, now fully visible with capture time, incident progression, and resolution.

Same image. Different conclusion.

**A screenshot can be true and still tell the story from the wrong time.**
