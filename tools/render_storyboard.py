#!/usr/bin/env python3
"""Render placeholder storyboard frames for a selected video."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Callable

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1920, 1080

PALETTES = {
    "video1": {
        "bg": "#0C0F13",
        "panel": "#151A21",
        "panel_alt": "#1C232D",
        "line": "#313A46",
        "text": "#F4F6F8",
        "muted": "#A6B1BE",
        "primary": "#5BC0FF",
        "secondary": "#FFC857",
        "inference": "#FF7B72",
        "ok": "#73DFA7",
    },
    "video2": {
        "bg": "#0E1117",
        "panel": "#17202A",
        "panel_alt": "#22303D",
        "line": "#3A4A59",
        "text": "#F2F5F7",
        "muted": "#A9B6C2",
        "primary": "#6DD3CE",
        "secondary": "#F2B880",
        "inference": "#FF8E72",
        "ok": "#8AD68A",
    },
}

PALETTE = PALETTES["video1"]


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for name in candidates:
        try:
            return ImageFont.truetype(name, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def base_canvas() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (WIDTH, HEIGHT), PALETTE["bg"])
    draw = ImageDraw.Draw(img)
    draw.rectangle((40, 40, WIDTH - 40, HEIGHT - 40), outline=PALETTE["line"], width=2)
    return img, draw


def draw_header(draw: ImageDraw.ImageDraw, title: str, subtitle: str = "") -> None:
    title_font = load_font(54, bold=True)
    sub_font = load_font(28)
    draw.text((96, 78), title, font=title_font, fill=PALETTE["text"])
    if subtitle:
        draw.text((96, 148), subtitle, font=sub_font, fill=PALETTE["muted"])
    draw.line((96, 194, WIDTH - 96, 194), fill=PALETTE["line"], width=2)


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str = "panel", border: str = "line") -> None:
    draw.rounded_rectangle(box, radius=16, fill=PALETTE[fill], outline=PALETTE[border], width=2)


def text_block(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    size: int = 30,
    color: str = "text",
    bold: bool = False,
) -> None:
    draw.multiline_text(xy, text, font=load_font(size, bold=bold), fill=PALETTE[color], spacing=8)


def tag(draw: ImageDraw.ImageDraw, xy: tuple[int, int], label: str, key: str) -> None:
    x, y = xy
    w = 24 + int(len(label) * 13)
    h = 42
    draw.rounded_rectangle((x, y, x + w, y + h), radius=10, fill=PALETTE["panel_alt"], outline=PALETTE[key], width=2)
    text_block(draw, (x + 14, y + 8), label, size=22, color=key, bold=True)


# Video 1 frames

def frame_title_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Two True Screenshots, One Wrong Conclusion", "Video 1 storyboard placeholder")
    text_block(draw, (120, 340), "How source, time, and delivery path create conflict", size=48, color="text", bold=True)
    text_block(draw, (120, 430), "Restrained editorial visual pass", size=30, color="muted")
    tag(draw, (120, 520), "SOURCE", "primary")
    tag(draw, (300, 520), "TIME", "secondary")
    tag(draw, (430, 520), "WORDING", "inference")


def frame_conflicting_screenshots(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Conflicting Screenshots", "Both captures can be real")
    left = (120, 260, 900, 860)
    right = (1020, 260, 1800, 860)
    panel(draw, left)
    panel(draw, right)
    text_block(draw, (160, 300), "Screenshot A", size=32, bold=True)
    text_block(draw, (160, 360), "Museum Notice", size=26, color="muted")
    text_block(draw, (160, 430), "Free admission ends", size=36)
    text_block(draw, (160, 480), "June 1", size=54, color="inference", bold=True)
    text_block(draw, (160, 770), "Captured 9:14 AM", size=24, color="muted")

    text_block(draw, (1060, 300), "Screenshot B", size=32, bold=True)
    text_block(draw, (1060, 360), "Museum Notice", size=26, color="muted")
    text_block(draw, (1060, 430), "Free admission extended", size=36)
    text_block(draw, (1060, 480), "through July 1", size=54, color="ok", bold=True)
    text_block(draw, (1060, 770), "Captured 2:37 PM", size=24, color="muted")

    draw.rectangle((140, 468, 420, 550), outline=PALETTE["inference"], width=4)
    draw.rectangle((1040, 468, 1440, 550), outline=PALETTE["ok"], width=4)


def frame_assumption_reframe(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Reframe the Question", "From accusation to diagnosis")
    panel(draw, (200, 300, 640, 760))
    panel(draw, (740, 300, 1180, 760))
    panel(draw, (1280, 300, 1720, 760))
    text_block(draw, (280, 480), "Claim\nConflict", size=48, bold=True)
    text_block(draw, (825, 500), "Fake?", size=60, color="inference", bold=True)
    draw.line((660, 530, 720, 530), fill=PALETTE["muted"], width=6)
    draw.line((1200, 530, 1260, 530), fill=PALETTE["muted"], width=6)
    draw.line((840, 460, 1080, 660), fill=PALETTE["inference"], width=8)
    text_block(draw, (1340, 450), "Check\nSource +\nTime + Path", size=42, color="primary", bold=True)


def draw_timeline(draw: ImageDraw.ImageDraw, detailed: bool) -> None:
    y = 600
    x0, x1 = 180, 1740
    draw.line((x0, y, x1, y), fill=PALETTE["line"], width=6)
    points = [
        (260, "8:00", "Primary: June 1", "primary"),
        (700, "9:15", "Newsletter mirrors", "secondary"),
        (1140, "11:40", "Updated: July 1", "ok"),
        (1580, "1:20", "Blog shows old", "inference"),
    ]
    for x, tm, label, color in points:
        draw.ellipse((x - 16, y - 16, x + 16, y + 16), fill=PALETTE[color])
        text_block(draw, (x - 40, y - 95), tm, size=24, color="muted", bold=True)
        text_block(draw, (x - 110, y + 34), label, size=24, color="text")
        if detailed:
            panel(draw, (x - 170, y + 96, x + 190, y + 200), fill="panel_alt")
    if detailed:
        text_block(draw, (210, 740), "Observed", size=24, color="primary", bold=True)
        text_block(draw, (460, 740), "Inference", size=24, color="inference", bold=True)


def frame_source_timeline_intro(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Source-vs-Live Drift", "Timeline explains disagreement")
    draw_timeline(draw, detailed=False)


def frame_source_timeline_detail(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Timeline Detail", "Both screenshots map to different moments")
    draw_timeline(draw, detailed=True)


def frame_cache_deployment_lag(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Cache + Deployment Lag", "Same URL, different delivery path")
    panel(draw, (180, 340, 520, 760))
    panel(draw, (1400, 340, 1740, 760))
    panel(draw, (690, 280, 1230, 500), fill="panel_alt")
    panel(draw, (690, 600, 1230, 820), fill="panel_alt")

    text_block(draw, (255, 520), "User A", size=42, bold=True)
    text_block(draw, (1475, 520), "User B", size=42, bold=True)
    text_block(draw, (835, 355), "Cache Node 1\n(stale)", size=36, color="inference", bold=True)
    text_block(draw, (825, 675), "Origin / Cache Node 2\n(fresh)", size=36, color="ok", bold=True)

    draw.line((520, 550, 680, 390), fill=PALETTE["muted"], width=6)
    draw.line((1740, 550, 1240, 390), fill=PALETTE["muted"], width=6)
    draw.line((1740, 550, 1240, 710), fill=PALETTE["muted"], width=6)


def frame_lag_consequence_bridge(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Consequence", "Both reports can be true observations")
    panel(draw, (200, 300, 860, 840))
    panel(draw, (1060, 300, 1720, 840))
    tag(draw, (240, 340), "Stale Response", "inference")
    tag(draw, (1100, 340), "Fresh Response", "ok")
    text_block(draw, (250, 470), 'Viewer reports:\n"I saw June 1"', size=44)
    text_block(draw, (1110, 470), 'Viewer reports:\n"I saw July 1"', size=44)


def frame_summary_error_comparison(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Summary Error Comparison", "Direct quote vs paraphrase")
    panel(draw, (150, 260, 920, 870))
    panel(draw, (1000, 260, 1770, 870))
    tag(draw, (190, 300), "Direct Quote", "primary")
    tag(draw, (1040, 300), "Summary", "secondary")
    text_block(draw, (200, 430), '"Extended through July 1\nfor weekday visits."', size=44)
    draw.rectangle((195, 500, 730, 590), outline=PALETTE["primary"], width=3)
    text_block(draw, (1040, 470), '"Free through July 1"', size=54)
    text_block(draw, (1040, 570), "Qualifier removed", size=34, color="inference", bold=True)


def frame_summary_error_impact(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Why It Misleads", "A summary is not a quote")
    panel(draw, (170, 350, 900, 770))
    panel(draw, (1080, 430, 1750, 690))
    text_block(draw, (220, 430), "Source text with conditions\nand scope qualifiers", size=40)
    text_block(draw, (1130, 520), "Compressed headline", size=44, bold=True)
    draw.polygon([(920, 470), (1040, 550), (920, 630)], fill=PALETTE["secondary"])
    text_block(draw, (820, 820), "Missing qualifier -> stronger claim", size=30, color="inference", bold=True)


def frame_five_step_checklist(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Five-Step Verification Checklist", "Run in under two minutes")
    steps = [
        "Find primary source",
        "Check timestamp and time zone",
        "Test page freshness",
        "Compare exact wording",
        "Mark uncertainty before sharing",
    ]
    y = 280
    for idx, step in enumerate(steps, start=1):
        panel(draw, (180, y, 1740, y + 120), fill="panel_alt")
        draw.ellipse((220, y + 36, 268, y + 84), fill=PALETTE["ok"])
        text_block(draw, (237, y + 42), str(idx), size=20, color="bg", bold=True)
        text_block(draw, (300, y + 38), step, size=42)
        y += 145


def frame_checklist_applied_example(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Checklist Applied", "Separate observed fact from inference")
    panel(draw, (150, 330, 1770, 560))
    panel(draw, (150, 610, 1770, 840))
    tag(draw, (190, 360), "Observed", "primary")
    tag(draw, (190, 640), "Inference", "inference")
    text_block(draw, (430, 390), "Official page reads July 1 as of 2:37 PM PT.", size=42)
    text_block(draw, (430, 670), "Earlier June 1 screenshot may be pre-update.", size=42)


def frame_closing_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Closing", "Channel doctrine")
    text_block(draw, (600, 430), "Source. Time. Wording.", size=74, bold=True)
    text_block(draw, (670, 560), "Check first, share second.", size=48, color="muted")


VIDEO1_FRAMES: list[tuple[str, Callable[[Image.Image, ImageDraw.ImageDraw], None]]] = [
    ("01_title_card.png", frame_title_card),
    ("02_conflicting_screenshots.png", frame_conflicting_screenshots),
    ("03_assumption_reframe.png", frame_assumption_reframe),
    ("04_source_timeline_intro.png", frame_source_timeline_intro),
    ("05_source_timeline_detail.png", frame_source_timeline_detail),
    ("06_cache_deployment_lag.png", frame_cache_deployment_lag),
    ("07_lag_consequence_bridge.png", frame_lag_consequence_bridge),
    ("08_summary_error_comparison.png", frame_summary_error_comparison),
    ("09_summary_error_impact.png", frame_summary_error_impact),
    ("10_five_step_checklist.png", frame_five_step_checklist),
    ("11_checklist_applied_example.png", frame_checklist_applied_example),
    ("12_closing_card.png", frame_closing_card),
]


# Video 2 frames

def frame2_title_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Same URL, Different Answer", "Caching, rollout lag, and edge variance")
    text_block(draw, (120, 340), "One link can return different results", size=56, bold=True)
    text_block(draw, (120, 430), "Evidence first. Explanation second.", size=36, color="muted")
    tag(draw, (120, 520), "OBSERVED", "primary")
    tag(draw, (330, 520), "LIKELY", "secondary")
    tag(draw, (500, 520), "UNKNOWN", "inference")


def frame2_same_url_two_answers(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "One URL, Opposite Results", "10:02 AM PT vs 10:03 AM PT")
    panel(draw, (120, 260, 900, 860), border="inference")
    panel(draw, (1020, 260, 1800, 860), border="ok")
    text_block(draw, (160, 300), "Capture A", size=30, color="muted", bold=True)
    text_block(draw, (160, 360), "Line A resumes at 12:00 PM", size=42, bold=True)
    text_block(draw, (160, 780), "10:02 AM PT", size=30, color="inference", bold=True)
    text_block(draw, (1060, 300), "Capture B", size=30, color="muted", bold=True)
    text_block(draw, (1060, 360), "Line A remains suspended", size=42, bold=True)
    text_block(draw, (1060, 780), "10:03 AM PT", size=30, color="ok", bold=True)


def frame2_evidence_before_blame(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Reframe", "Observed fact before inference")
    panel(draw, (180, 300, 860, 860))
    panel(draw, (1060, 300, 1740, 860))
    tag(draw, (220, 340), "Observed", "primary")
    tag(draw, (1100, 340), "Inference", "secondary")
    text_block(draw, (230, 430), "- What text appeared\n- Exact timestamp\n- Location/network", size=42)
    text_block(draw, (1110, 430), "- Possible cause\n- Confidence level\n- Missing evidence", size=42)


def frame2_caching_path_split(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Mechanism 1: Caching", "Stale and fresh can coexist briefly")
    panel(draw, (160, 360, 520, 760))
    panel(draw, (700, 280, 1220, 500), fill="panel_alt")
    panel(draw, (700, 600, 1220, 820), fill="panel_alt")
    panel(draw, (1400, 360, 1760, 760))
    text_block(draw, (250, 520), "User A", size=42, bold=True)
    text_block(draw, (1470, 520), "User B", size=42, bold=True)
    text_block(draw, (840, 350), "Edge Cache\n(stale)", size=38, color="inference", bold=True)
    text_block(draw, (830, 675), "Origin/Fresh\n(updated)", size=38, color="ok", bold=True)
    draw.line((520, 560, 700, 390), fill=PALETTE["muted"], width=6)
    draw.line((1760, 560, 1220, 390), fill=PALETTE["muted"], width=6)
    draw.line((1760, 560, 1220, 710), fill=PALETTE["muted"], width=6)


def frame2_cache_headers_comparison(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Evidence Example", "Compare headers and timestamps")
    panel(draw, (140, 260, 920, 870))
    panel(draw, (1000, 260, 1780, 870))
    tag(draw, (180, 300), "Response A", "inference")
    tag(draw, (1040, 300), "Response B", "ok")
    text_block(draw, (200, 390), "cache-status: hit\nAge: 185\nstatus: suspended", size=40)
    text_block(draw, (1060, 390), "cache-status: miss\nAge: 3\nstatus: resumes at noon", size=40)
    text_block(draw, (200, 720), "Observed data", size=30, color="primary", bold=True)
    text_block(draw, (1060, 720), "Observed data", size=30, color="primary", bold=True)


def frame2_rollout_window_timeline(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Mechanism 2: Rollout Lag", "Deploy window allows coexistence")
    panel(draw, (140, 280, 1780, 860), fill="panel")
    draw.line((220, 610, 1700, 610), fill=PALETTE["line"], width=8)
    points = [
        (320, "9:55", "Deploy starts", "secondary"),
        (860, "10:02", "Capture A", "inference"),
        (1120, "10:03", "Capture B", "ok"),
        (1600, "10:20", "Deploy completes", "secondary"),
    ]
    for x, tm, label, color in points:
        draw.ellipse((x - 18, 592, x + 18, 628), fill=PALETTE[color])
        text_block(draw, (x - 46, 530), tm, size=24, color="muted", bold=True)
        text_block(draw, (x - 120, 650), label, size=28, bold=True)
    draw.rectangle((300, 450, 1620, 520), outline=PALETTE["secondary"], width=3)
    text_block(draw, (330, 465), "Observed deploy window from release notes", size=30)


def frame2_rollout_traffic_split(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Traffic Split", "Both versions can answer during rollout")
    panel(draw, (180, 300, 860, 860))
    panel(draw, (1060, 300, 1740, 860))
    tag(draw, (220, 340), "Version 1", "inference")
    tag(draw, (1100, 340), "Version 2", "ok")
    text_block(draw, (240, 470), "70% traffic\n\nold status text", size=48)
    text_block(draw, (1120, 470), "30% traffic\n\nnew status text", size=48)
    text_block(draw, (640, 900), "Temporary coexistence during phased deployment", size=30, color="muted")


def frame2_edge_location_map(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Mechanism 3: Edge and Location", "Routing path affects visible state")
    panel(draw, (150, 260, 1770, 860), fill="panel")
    panel(draw, (260, 470, 660, 760), fill="panel_alt")
    panel(draw, (1260, 470, 1660, 760), fill="panel_alt")
    panel(draw, (760, 300, 1160, 560), fill="panel_alt")
    text_block(draw, (355, 565), "US-West\nEdge", size=38, color="inference", bold=True)
    text_block(draw, (1355, 565), "US-East\nEdge", size=38, color="ok", bold=True)
    text_block(draw, (870, 380), "Origin", size=44, bold=True)
    draw.line((660, 600, 760, 470), fill=PALETTE["muted"], width=6)
    draw.line((1260, 600, 1160, 470), fill=PALETTE["muted"], width=6)
    text_block(draw, (630, 800), "Observed: locations can differ briefly during propagation", size=30, color="primary")


def frame2_scope_claim_limit(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Scope the Claim", "Single fetch does not prove global state")
    panel(draw, (200, 320, 1720, 840))
    tag(draw, (260, 370), "Observed", "primary")
    tag(draw, (540, 370), "Inference", "secondary")
    tag(draw, (820, 370), "Unknown", "inference")
    text_block(draw, (280, 470), "Observed: one capture from one location at one time.", size=44)
    text_block(draw, (280, 570), "Inference: likely cache/rollout propagation behavior.", size=44)
    text_block(draw, (280, 670), "Unknown: exact backend cause without logs.", size=44)


def frame2_fast_verification_steps(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Fast Verification", "Context-rich fetches before sharing")
    steps = [
        "Record exact timestamp + time zone",
        "Note location and network path",
        "Save exact page wording",
        "Capture response metadata when possible",
        "Write observed and inferred separately",
    ]
    y = 270
    for idx, step in enumerate(steps, start=1):
        panel(draw, (170, y, 1750, y + 130), fill="panel_alt")
        draw.ellipse((215, y + 42, 267, y + 94), fill=PALETTE["primary"])
        text_block(draw, (234, y + 51), str(idx), size=22, color="bg", bold=True)
        text_block(draw, (310, y + 42), step, size=40)
        y += 145


def frame2_observed_inference_template(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Template Wording", "Precise, useful, uncertainty-aware")
    panel(draw, (150, 320, 1770, 560))
    panel(draw, (150, 620, 1770, 860))
    tag(draw, (190, 360), "Observed", "primary")
    tag(draw, (190, 660), "Inference", "secondary")
    text_block(
        draw,
        (420, 390),
        '10:03 AM PT US-West: "suspended"; 10:04 AM PT US-East: "resumes at noon".',
        size=38,
    )
    text_block(
        draw,
        (420, 690),
        "Likely propagation or rollout lag; cause not confirmed without platform logs.",
        size=38,
    )


def frame2_closing_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Closing", "Verification doctrine")
    text_block(draw, (540, 430), "Single fetch = clue", size=72, bold=True)
    text_block(draw, (430, 560), "Multiple context-rich fetches = evidence", size=58, color="muted")


VIDEO2_FRAMES: list[tuple[str, Callable[[Image.Image, ImageDraw.ImageDraw], None]]] = [
    ("01_title_card.png", frame2_title_card),
    ("02_same_url_two_answers.png", frame2_same_url_two_answers),
    ("03_evidence_before_blame.png", frame2_evidence_before_blame),
    ("04_caching_path_split.png", frame2_caching_path_split),
    ("05_cache_headers_comparison.png", frame2_cache_headers_comparison),
    ("06_rollout_window_timeline.png", frame2_rollout_window_timeline),
    ("07_rollout_traffic_split.png", frame2_rollout_traffic_split),
    ("08_edge_location_map.png", frame2_edge_location_map),
    ("09_scope_claim_limit.png", frame2_scope_claim_limit),
    ("10_fast_verification_steps.png", frame2_fast_verification_steps),
    ("11_observed_inference_template.png", frame2_observed_inference_template),
    ("12_closing_card.png", frame2_closing_card),
]

VIDEO_FRAMES = {
    "video1": VIDEO1_FRAMES,
    "video2": VIDEO2_FRAMES,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render storyboard placeholder frames.")
    parser.add_argument(
        "--video",
        default="video1",
        choices=sorted(VIDEO_FRAMES.keys()),
        help="Video directory name under videos/ (default: video1)",
    )
    return parser.parse_args()


def main() -> None:
    global PALETTE

    args = parse_args()
    PALETTE = PALETTES[args.video]
    out_dir = Path("videos") / args.video / "storyboard_frames"
    out_dir.mkdir(parents=True, exist_ok=True)

    for name, painter in VIDEO_FRAMES[args.video]:
        img, draw = base_canvas()
        painter(img, draw)
        out_path = out_dir / name
        img.save(out_path, format="PNG")
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
