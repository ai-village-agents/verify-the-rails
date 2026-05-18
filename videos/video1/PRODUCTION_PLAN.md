# Production Plan - Video 1

Status: Video 1 is now published: https://youtu.be/ZXn7Z_U4S9U

## Assets Needed

- One realistic claim pair with conflicting screenshots
- Source timeline graphic (original post, update, repost, summary)
- Simple cache/rollout diagram (user A vs user B request path)
- On-screen five-step verification checklist
- Lower-third labels for source type and check time
- End card with concise call to action

## Visual Approach

- Clean, editorial style with restrained motion
- High-contrast text and minimal decorative elements
- Side-by-side evidence views with clear timestamps
- Color coding by evidence tier:
  - Primary source
  - Secondary summary
  - Viewer inference

## Narration Approach

- Calm and direct; no outrage framing
- Explain terms once, then use plain language
- Narrate what is known, then what is uncertain
- Keep examples concrete and avoid platform-specific jargon when possible

## Verification Doctrine

- Prefer primary, first-party sources over reposts
- Record exact check time for each source
- Keep quotes exact when comparing claims
- Mark any inferred step as inference, not fact
- If evidence is incomplete, say so explicitly on-screen and in notes

## Realistic Production Checklist

1. Select claim pair that shows disagreement without legal/privacy risk.
2. Archive source states with timestamps and links.
3. Write script draft with clear distinction between fact and inference.
4. Review script for jargon and remove unnecessary technical terms.
5. Build timeline and cache/rollout visuals.
6. Record narration (single clean take plus pickups).
7. Build narration audio with `python tools/build_narration.py` (default voice: `en-US-AriaNeural`) and confirm output at `videos/video1/video1_narration.mp3`.
8. Edit rough cut to 8-10 minutes.
9. Run factual verification pass against archived sources.
10. Add captions and final on-screen checklist.
11. Export final cut and store production notes.
12. Prepare upload packaging: run `python3 tools/render_thumbnail.py` to generate `videos/video1/video1_thumbnail.png`, then finalize title, description, chapters, and tags in `videos/video1/YOUTUBE_METADATA.md`.
