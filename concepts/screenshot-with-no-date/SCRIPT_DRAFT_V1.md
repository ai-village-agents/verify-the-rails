# Script Draft V1 — The Screenshot With No Date

## Beat 1 — Apparent certainty (Hook)
This screenshot is real. The repost is real. The conclusion people drew from it was wrong.

Here’s the post: a status page, bright red banner, `Major Outage — Investigating.` No date in the crop. No clock. Just the scary part. It spreads fast, people cancel plans, support teams get flooded, and someone says, “See? Still down.”

At first glance, that sounds responsible. But it only works if this image is current. The screenshot can be authentic and still be the wrong moment.

## Beat 2 — Small crack in the story
Now zoom out.

Top-right corner: `Updated 8:12 AM UTC.`
Timeline underneath:
- 8:12 AM UTC: Investigating
- 8:27 AM UTC: Identified
- 8:41 AM UTC: Monitoring
- 9:03 AM UTC: Resolved
- 1:46 PM local time: screenshot reposted as “service is down”

Nothing in the screenshot was fake. The problem is simpler: people treated a captured moment as a live state.

This is where a useful split helps:
- Observed: the service was down at one point.
- Inference: the service is down right now.
- Unknown: what changed after capture.

That gap between observed and inferred is where most screenshot confusion lives.

## Beat 3 — Reframing the claim
So the question is not “Is this screenshot real?”
The better question is “What claim is this screenshot being used to make?”

A real image proves one thing really happened. It does not automatically prove that thing is still true at 1:46 PM, still representative, or shown with full context.

When people get fooled here, it is usually not because they are careless. It is because screenshots look like receipts. You see pixels, not process. A post that says `Investigating` reads like a current status unless you deliberately check when it was captured and what happened next.

## Beat 4 — Pattern set (three concrete cases)
Pattern one: status incidents that outlive resolution.
A single `Investigating` screenshot travels longer than the actual outage. The dramatic frame survives; the resolved update does not.

Pattern two: cropped dashboard windows.
You see a chart with a huge spike and the caption says “traffic collapsed.” The crop hides the date-range control. Zoom out and it’s set to `Last 1 hour` during a deployment test. Switch to `Last 30 days` and the “collapse” is a tiny dip in a normal pattern.

Pattern three: resurfaced old announcements.
A screenshot of a policy post reappears with “breaking” language. The post is real, but it is from months ago, and a follow-up announcement changed the rule two weeks later. The old screenshot keeps circulating because it is emotionally sharper than the boring update.

Different domains, same mechanism: the missing or hidden timeline does the persuading.

## Beat 5 — Practical defense (small habit)
Use one short routine before you reshare: do a ten-second time check.

Open the original post or page.
Find the timestamp and timezone.
Scan for updates posted after the screenshot moment.
Then ask one question: if I shared this now, would I be describing the current state or a past state?

You do not need a forensic toolkit. Most of the time, you just need ten extra seconds and a wider frame.

## Beat 6 — Closing memory
Return to that opening outage screenshot, now fully visible with the full update thread and timeline.

Same image. Different conclusion.

**A screenshot can be true and still tell the story from the wrong time.**
