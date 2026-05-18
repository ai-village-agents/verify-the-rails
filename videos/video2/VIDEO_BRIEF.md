# Video 2 Brief

## Working Goal

Explain, in plain English, how the same URL can show different answers at the same moment because of cache state, rollout/deployment lag, and edge/location routing.

## Title Options

1. **Same Link, Different Answer: What Changed?**
2. **Why One URL Can Tell Two Different Stories**
3. **Same Page, Different Result: Caches, Rollouts, and Location**

## Viewer Promise

By the end, viewers can recognize three normal infrastructure reasons for conflicting page results and run a quick check before concluding that someone is lying.

## Core Examples to Show

1. **Caching:** Viewer A gets an older cached response, Viewer B gets a fresh one after expiry/invalidation.
2. **Rollout lag:** A gradual deploy sends new code to part of traffic while the old version is still live for others.
3. **Edge/location differences:** Requests served from different regions/edges briefly disagree while updates propagate.
4. **Fast verification demo:** Same URL checked from two networks/regions plus timestamped headers/screenshot notes.

## Risks to Avoid

- Do not claim every disagreement is "just cache" or "just CDN."
- Do not imply malicious intent without evidence.
- Do not overstate certainty when logs/headers are unavailable.
- Do not bury timing context; always show exact check time and location/network context.
- Do not overload with jargon; define terms once and keep plain language.

## Target Length

5-7 minutes
