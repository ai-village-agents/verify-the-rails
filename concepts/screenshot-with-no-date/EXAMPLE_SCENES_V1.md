# EXAMPLE SCENES V1

All examples below are synthetic and platform-neutral. They are designed as believable training scenarios, not depictions of real incidents.

## Example A: Status incident

1. **Scenario summary (1 sentence)**
A cropped status screenshot shows an outage banner that is real, but the missing date makes it look like an active incident.

2. **Exact synthetic on-screen text (screenshot/mock UI)**
```text
OpsStatus
System Health

[Amber dot] Partial Service Disruption
Started: 02:14 UTC

Affected components
- API Gateway: Degraded Performance
- File Uploads: Intermittent Timeouts

Latest update
"Mitigation applied; error rate dropping."

Incident ID: INC-7421
```

3. **Exact timestamps and/or date ranges to use**
- Full-page timestamp in original capture: `2025-02-18 02:43 UTC`
- Incident start shown in event log: `2025-02-18 02:14 UTC`
- Resolution entry lower on page: `Resolved 2025-02-18 03:26 UTC`
- Repost timestamp (separate feed UI): `2026-05-19 09:12 local`

4. **What the cropped repost makes viewers assume**
Viewers assume the disruption is happening now and services are currently unstable.

5. **What the wider context reveals**
The full page and event log show the incident was fully resolved in 72 minutes on February 18, 2025, more than a year before the repost.

6. **How the example should appear in storyboard/animatic terms**
- Shot A1 (0:00-0:04): Tight crop on amber banner and “Partial Service Disruption.”
- Shot A2 (0:04-0:07): Slight punch-in on “Degraded Performance” to increase urgency.
- Shot A3 (0:07-0:11): Frame expands downward to reveal incident log with `Resolved 2025-02-18 03:26 UTC`.
- Shot A4 (0:11-0:14): Split-frame adds repost time `2026-05-19 09:12 local` beside original capture date.

7. **Why this works (short note)**
It demonstrates a true screenshot becoming misleading through omitted temporal metadata, not fabricated content.

## Example B: Dashboard/date-range crop

1. **Scenario summary (1 sentence)**
A performance dashboard crop hides the selected date range, making a normal short dip look like a current system-wide collapse.

2. **Exact synthetic on-screen text (screenshot/mock UI)**
```text
Operations Analytics
Metric: Successful Transactions (%)

[Line chart visible, date selector cropped out]
Y-axis labels: 100, 95, 90, 85

Legend
- Core Checkout
- Express Checkout

Tooltip (visible at dip)
2026-04-06 03:00 UTC
Core Checkout: 88.4%
Express Checkout: 87.9%
```

3. **Exact timestamps and/or date ranges to use**
- Actual dashboard date range (hidden in cropped version): `Last 90 days (2026-02-01 to 2026-04-30)`
- Dip timestamp in tooltip: `2026-04-06 03:00 UTC`
- Recovery by: `2026-04-06 05:00 UTC` (both lines back above `98.9%`)
- Repost overlay label: `Posted 2026-05-19`

4. **What the cropped repost makes viewers assume**
Viewers assume the dip reflects today’s live performance and that transactions are still failing.

5. **What the wider context reveals**
The full dashboard shows a historical 90-day view with one brief maintenance-window dip that recovered within two hours.

6. **How the example should appear in storyboard/animatic terms**
- Shot B1 (0:00-0:03): Show chart crop with dramatic dip centered; hide top date selector.
- Shot B2 (0:03-0:06): Add claim text card: “System is collapsing right now.”
- Shot B3 (0:06-0:10): Vertical reveal upward to expose `Last 90 days (2026-02-01 to 2026-04-30)`.
- Shot B4 (0:10-0:14): Animate scrub across line to show rapid recovery by `05:00 UTC`.

7. **Why this works (short note)**
It isolates a common failure mode where missing range controls invert the meaning of otherwise accurate chart data.

## Example C: Resurfaced old announcement

1. **Scenario summary (1 sentence)**
An old product-announcement screenshot is reposted without its publish date, making a past policy change look newly introduced.

2. **Exact synthetic on-screen text (screenshot/mock UI)**
```text
Product Updates

Update: Storage retention policy adjustment

Starting June 1, 2025, standard workspace retention changes from
18 months to 12 months.

What this affects
- Archived exports
- Team backups

Published by: Product Communications
```

3. **Exact timestamps and/or date ranges to use**
- Original announcement publish date (visible in full view): `Published 2025-05-12 16:00 UTC`
- Effective date stated in body: `June 1, 2025`
- Follow-up clarification post (same thread): `2025-05-20 09:30 UTC`
- Repost date in external feed mock: `2026-05-19`

4. **What the cropped repost makes viewers assume**
Viewers assume a new retention cut is being imposed now.

5. **What the wider context reveals**
The announcement is a year old, already implemented in 2025, and accompanied by a follow-up clarification that was cropped out.

6. **How the example should appear in storyboard/animatic terms**
- Shot C1 (0:00-0:04): Crop only headline and policy sentence; no header metadata.
- Shot C2 (0:04-0:07): Overlay social-style caption: “New change announced today.”
- Shot C3 (0:07-0:11): Pull back to reveal `Published 2025-05-12 16:00 UTC` above headline.
- Shot C4 (0:11-0:15): Scroll down to `2025-05-20 09:30 UTC` clarification entry and highlight it.

7. **Why this works (short note)**
It shows how true archival content can be reframed as breaking news when publication timing is hidden.

## Specificity rules

1. Always include at least two absolute timestamps: one from the original capture and one from the repost context.
2. Use realistic UI microcopy (labels, legends, status names, IDs) instead of generic placeholders like “Alert” or “Important update.”
3. Define the exact crop boundary in words (what is visible and what is hidden) so scene framing is reproducible.
4. Keep timeline math explicit and check consistency (start, update, resolution, repost) before finalizing the example.
5. Pair every misleading cropped claim with a concrete reveal artifact (date badge, range selector, resolved log row, or follow-up entry).
