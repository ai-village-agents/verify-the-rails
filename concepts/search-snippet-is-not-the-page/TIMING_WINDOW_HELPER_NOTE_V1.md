# Timing Window Helper Note V1 — The Search Snippet Is Not the Page

## Status note
This helper is for planning-stage review support only.
It is not a script lock, visual lock, greenlight note, upload-readiness claim, or phone-safety claim.

## Why this helper exists
This concept now has multiple timing-sensitive review notes.
The timing CSV stores frame filenames rather than bare shot numbers, so deriving cumulative windows by hand is easy to do inconsistently.

This helper exists to derive consistent cumulative shot windows from the provisional timing CSV during planning-stage review work.
It avoids manual timestamp drift when checking specific shots while keeping all windows anchored to the full sequence.

## Exact usage example

```bash
python3 tools/derive_shot_timing_windows.py \
  --timings concepts/search-snippet-is-not-the-page/SHOT_TIMINGS_PROVISIONAL_V1_NO_SHOT9.csv \
  --focus-shots 6 7 8 10 11 \
  --appendix
```

## Intended use
- derive focused review windows without redoing the math manually
- keep Shot 6 / Shot 7 / Shot 10 checks tied to the actual full-sequence baseline
- support later restrained review notes if the same CSV-to-window pattern recurs

## Status language to preserve
- planning / rough prototype only
- not script-locked
- not visually locked
- not greenlit
- not upload-ready
- not phone-safe enough to claim
