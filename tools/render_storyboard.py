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
    "video3": {
        "bg": "#101217",
        "panel": "#1A1F29",
        "panel_alt": "#252D3A",
        "line": "#3F4B5C",
        "text": "#F5F7FA",
        "muted": "#B3BEC9",
        "primary": "#86C8FF",
        "secondary": "#FFD38A",
        "inference": "#FF8B7C",
        "ok": "#9CE0A4",
    },
    "video4": {
        "bg": "#0F131A",
        "panel": "#18212B",
        "panel_alt": "#223140",
        "line": "#405365",
        "text": "#F5F7FA",
        "muted": "#B5C0CB",
        "primary": "#79B8FF",
        "secondary": "#F2C078",
        "inference": "#FF8F7A",
        "ok": "#95D9A6",
    },
    "video5": {
        "bg": "#0B111A",
        "panel": "#142235",
        "panel_alt": "#1D3048",
        "line": "#38506A",
        "text": "#EEF4FA",
        "muted": "#A7BACB",
        "primary": "#7EC3FF",
        "secondary": "#F2BE74",
        "inference": "#C98282",
        "ok": "#8DD6B0",
    },
    "video6": {
        "bg": "#0D121A",
        "panel": "#182433",
        "panel_alt": "#223449",
        "line": "#3A526B",
        "text": "#EEF3F8",
        "muted": "#AABAC8",
        "primary": "#74B8F8",
        "secondary": "#E4B36F",
        "inference": "#B87A7A",
        "ok": "#7FC8A1",
    },
    "video7": {
        "bg": "#0C131B",
        "panel": "#172535",
        "panel_alt": "#22384E",
        "line": "#3E5A75",
        "text": "#EEF5FB",
        "muted": "#A9BDCF",
        "primary": "#78BEFF",
        "secondary": "#E8B86E",
        "inference": "#C98989",
        "ok": "#84CFAD",
    },
    "video8": {
        "bg": "#0B121B",
        "panel": "#152435",
        "panel_alt": "#1F3348",
        "line": "#3B5875",
        "text": "#EDF4FB",
        "muted": "#A8BCCF",
        "primary": "#76C0FF",
        "secondary": "#E6B768",
        "inference": "#C88484",
        "ok": "#86CFAE",
    },
    "video9": {
        "bg": "#0B121B",
        "panel": "#162538",
        "panel_alt": "#20354C",
        "line": "#3C5A77",
        "text": "#ECF4FB",
        "muted": "#A9BDCF",
        "primary": "#78C1FF",
        "secondary": "#E7B86A",
        "inference": "#C98686",
        "ok": "#87CFAD",
    },
    "video10": {
        "bg": "#0A131C",
        "panel": "#152635",
        "panel_alt": "#21364B",
        "line": "#3D5B74",
        "text": "#ECF4FB",
        "muted": "#A7B9CB",
        "primary": "#75BFFF",
        "secondary": "#E6B66B",
        "inference": "#C78282",
        "ok": "#84CFAB",
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


# Video 3 frames

def frame3_title_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "When Summaries Drift From Sources", "Compare wording strength before sharing")
    text_block(draw, (120, 340), "Quote First. Interpret Second.", size=62, bold=True)
    text_block(draw, (120, 430), "Observed and inference labeled in every step.", size=34, color="muted")
    tag(draw, (120, 520), "OBSERVED", "primary")
    tag(draw, (340, 520), "INFERENCE", "inference")


def frame3_source_vs_summary(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Same Topic, Stronger Retelling", "Source wording vs summary wording")
    panel(draw, (120, 260, 900, 860), border="primary")
    panel(draw, (1020, 260, 1800, 860), border="inference")
    tag(draw, (160, 300), "Source", "primary")
    tag(draw, (1060, 300), "Summary", "inference")
    text_block(draw, (170, 430), '"associated with"', size=64, color="primary", bold=True)
    text_block(draw, (170, 530), "higher sleep complaints", size=40)
    text_block(draw, (1070, 430), '"proves" / "causes"', size=64, color="inference", bold=True)
    text_block(draw, (1070, 530), "stronger certainty claim", size=40)
    tag(draw, (160, 760), "Observed", "primary")
    text_block(draw, (350, 768), "wording differs exactly", size=28, color="muted")


def frame3_compare_claims_not_tone(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Compare Claims, Not Tone", "Summary utility is not the issue")
    panel(draw, (180, 300, 860, 860))
    panel(draw, (1060, 300, 1740, 860))
    tag(draw, (220, 340), "Observed", "primary")
    tag(draw, (1100, 340), "Inference", "inference")
    text_block(draw, (230, 440), "- Source claim text\n- Summary claim text\n- Exact verb differences", size=42)
    text_block(draw, (1110, 440), "- Drift likely from speed\n- Certainty pressure\n- Not proof of intent", size=42)
    text_block(draw, (640, 900), "Useful summary != stronger claim", size=34, color="secondary", bold=True)


def frame3_source_hierarchy(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Source Hierarchy", "Start at strongest evidence layer")
    panel(draw, (260, 280, 1660, 860), fill="panel")
    draw.polygon([(960, 320), (520, 760), (1400, 760)], fill=PALETTE["panel_alt"], outline=PALETTE["line"])
    text_block(draw, (860, 410), "Primary", size=44, color="primary", bold=True)
    text_block(draw, (810, 520), "Summary", size=44, color="secondary", bold=True)
    text_block(draw, (760, 640), "Commentary", size=44, color="muted", bold=True)
    text_block(draw, (550, 800), "Distance from primary source increases drift risk", size=32, color="inference", bold=True)


def frame3_drift_mechanisms_table(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Five Drift Mechanisms", "Visible wording shifts")
    panel(draw, (120, 250, 1800, 900), fill="panel")
    rows = [
        ("Compression", "long sentence", "short slogan"),
        ("Omission", '"in this sample"', "removed"),
        ("Simplification", '"associated with"', '"causes"'),
        ("Version drift", "older draft", "reused summary"),
        ("Status shift", '"proposes"', '"approved"'),
    ]
    y = 300
    for label, left_text, right_text in rows:
        panel(draw, (160, y, 1760, y + 104), fill="panel_alt")
        text_block(draw, (190, y + 28), label, size=32, color="secondary", bold=True)
        text_block(draw, (540, y + 30), left_text, size=30, color="text")
        text_block(draw, (1020, y + 30), "->", size=30, color="muted", bold=True)
        text_block(draw, (1100, y + 30), right_text, size=30, color="inference", bold=True)
        y += 118


def frame3_health_report_comparison(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Worked Example: Health Report", "Verb and scope comparison")
    panel(draw, (140, 260, 920, 880))
    panel(draw, (1000, 260, 1780, 880))
    tag(draw, (180, 300), "Source", "primary")
    tag(draw, (1040, 300), "Summary", "inference")
    text_block(draw, (190, 430), '"associated with"\n"in surveyed adults"', size=42)
    text_block(draw, (1050, 430), '"proves"\n"causes"\n(scope removed)', size=42)
    draw.rectangle((180, 418, 700, 585), outline=PALETTE["secondary"], width=3)
    draw.rectangle((1040, 418, 1450, 660), outline=PALETTE["inference"], width=3)
    tag(draw, (180, 770), "Observed", "primary")
    text_block(draw, (370, 780), "summary is stronger than source text", size=30, color="muted")


def frame3_budget_memo_comparison(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Worked Example: Budget Memo", "Status wording changes claim")
    panel(draw, (140, 260, 920, 880))
    panel(draw, (1000, 260, 1780, 880))
    tag(draw, (180, 300), "Source", "primary")
    tag(draw, (1040, 300), "Summary", "inference")
    text_block(draw, (190, 430), '"proposes"\n"pilot subsidy"\n"next fiscal year"', size=40)
    text_block(draw, (1050, 430), '"approved"\n"free transit"\n"next year"', size=40)
    text_block(draw, (190, 760), "Observed: proposal language", size=30, color="primary", bold=True)
    text_block(draw, (1050, 760), "Observed: decision language", size=30, color="inference", bold=True)


def frame3_verbs_scope_status(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Check Verbs, Scope, Status", "Three fast drift checks")
    cards = [
        (220, "Verb", '"associated" vs "causes"', "secondary"),
        (720, "Scope", '"surveyed adults" vs omitted', "primary"),
        (1220, "Status", '"proposes" vs "approved"', "inference"),
    ]
    for x, title, body, color in cards:
        panel(draw, (x, 310, x + 420, 850), fill="panel_alt")
        text_block(draw, (x + 36, 370), title, size=44, color=color, bold=True)
        text_block(draw, (x + 36, 500), body, size=33)
    text_block(draw, (560, 900), "Observed terms first, interpretation second", size=32, color="muted")


def frame3_date_version_context(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Date + Version Context", "Older wording can persist in reposts")
    panel(draw, (160, 280, 1760, 860))
    draw.line((260, 620, 1660, 620), fill=PALETTE["line"], width=8)
    points = [
        (340, "Mar 4", "Draft v1", "secondary"),
        (820, "Mar 11", "Source revised", "ok"),
        (1320, "Mar 14", "Old summary reposted", "inference"),
    ]
    for x, dt, label, color in points:
        draw.ellipse((x - 18, 602, x + 18, 638), fill=PALETTE[color])
        text_block(draw, (x - 72, 540), dt, size=24, color="muted", bold=True)
        text_block(draw, (x - 120, 662), label, size=30, bold=True)
    tag(draw, (250, 730), "Observed", "primary")
    text_block(draw, (440, 740), "date mismatch can explain apparent contradiction", size=30, color="muted")


def frame3_fast_verification_steps(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Fast Verification Steps", "Use before sharing")
    steps = [
        "Capture source sentence and summary sentence",
        "Mark date and version for both",
        "Circle claim verbs and status words",
        "Check scope words and missing qualifiers",
        "Write observed vs inference lines",
    ]
    y = 270
    for idx, step in enumerate(steps, start=1):
        panel(draw, (170, y, 1750, y + 130), fill="panel_alt")
        draw.ellipse((215, y + 42, 267, y + 94), fill=PALETTE["ok"])
        text_block(draw, (234, y + 50), str(idx), size=22, color="bg", bold=True)
        text_block(draw, (310, y + 42), step, size=38)
        y += 145


def frame3_observed_inference_template(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Reusable Template", "Explicitly separate fact from meaning")
    panel(draw, (150, 320, 1770, 560))
    panel(draw, (150, 620, 1770, 860))
    tag(draw, (190, 360), "Observed", "primary")
    tag(draw, (190, 660), "Inference", "inference")
    text_block(
        draw,
        (420, 390),
        'Source: "associated with" | Summary: "causes" | Scope changed.',
        size=38,
    )
    text_block(
        draw,
        (420, 690),
        "Inference: summary likely overstates certainty (confidence: likely).",
        size=38,
    )


def frame3_closing_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Closing", "Verification doctrine")
    text_block(draw, (520, 430), "Read the source.", size=74, bold=True)
    text_block(draw, (470, 540), "Measure the drift.", size=74, bold=True)
    text_block(draw, (590, 650), "Share with context.", size=58, color="muted")


VIDEO3_FRAMES: list[tuple[str, Callable[[Image.Image, ImageDraw.ImageDraw], None]]] = [
    ("01_title_card.png", frame3_title_card),
    ("02_source_vs_summary.png", frame3_source_vs_summary),
    ("03_compare_claims_not_tone.png", frame3_compare_claims_not_tone),
    ("04_source_hierarchy.png", frame3_source_hierarchy),
    ("05_drift_mechanisms_table.png", frame3_drift_mechanisms_table),
    ("06_health_report_comparison.png", frame3_health_report_comparison),
    ("07_budget_memo_comparison.png", frame3_budget_memo_comparison),
    ("08_verbs_scope_status.png", frame3_verbs_scope_status),
    ("09_date_version_context.png", frame3_date_version_context),
    ("10_fast_verification_steps.png", frame3_fast_verification_steps),
    ("11_observed_inference_template.png", frame3_observed_inference_template),
    ("12_closing_card.png", frame3_closing_card),
]


# Video 4 frames

def frame4_title_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "This Was True Yesterday", "How date and version drift breaks online claims")
    panel(draw, (120, 260, 900, 860), border="inference")
    panel(draw, (1020, 260, 1800, 860), border="ok")
    tag(draw, (160, 300), "Authentic capture", "secondary")
    tag(draw, (1060, 300), "Authentic capture", "secondary")
    text_block(draw, (170, 400), "Scholarship Page", size=34, color="muted", bold=True)
    text_block(draw, (170, 460), "Applications close", size=40, bold=True)
    text_block(draw, (170, 520), "May 1", size=76, color="inference", bold=True)
    text_block(draw, (170, 770), "Captured Monday", size=28, color="muted")
    text_block(draw, (1070, 400), "Scholarship Page", size=34, color="muted", bold=True)
    text_block(draw, (1070, 460), "Applications close", size=40, bold=True)
    text_block(draw, (1070, 520), "May 15", size=76, color="ok", bold=True)
    text_block(draw, (1070, 770), "Current Wednesday page", size=28, color="muted")
    panel(draw, (600, 900, 1320, 1020), fill="panel_alt", border="primary")
    text_block(draw, (670, 938), "When was this true?", size=52, color="text", bold=True)


def frame4_two_real_captures(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Two Real Captures", "Authentic evidence can still disagree")
    panel(draw, (120, 260, 900, 860), border="inference")
    panel(draw, (1020, 260, 1800, 860), border="ok")
    tag(draw, (160, 300), "Authentic capture", "secondary")
    tag(draw, (1060, 300), "Authentic capture", "secondary")
    text_block(draw, (180, 470), "Applications close May 1", size=56, color="inference", bold=True)
    text_block(draw, (1080, 470), "Applications close May 15", size=56, color="ok", bold=True)
    panel(draw, (700, 900, 1220, 1010), fill="panel_alt", border="secondary")
    text_block(draw, (740, 934), "Fake? Or different moments?", size=38, bold=True)


def frame4_when_was_this_true(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Reframe", "Ask the timing question first")
    panel(draw, (380, 300, 1540, 780), fill="panel_alt", border="primary")
    text_block(draw, (660, 470), "When was this true?", size=72, bold=True)
    tag(draw, (540, 840), "wording", "primary")
    tag(draw, (840, 840), "timestamp", "secondary")
    tag(draw, (1180, 840), "version", "inference")


def frame4_source_time_version(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Source + Time + Version", "Three checks before interpretation")
    panel(draw, (260, 280, 1660, 860), fill="panel")
    panel(draw, (460, 370, 900, 760), fill="panel_alt", border="primary")
    panel(draw, (1010, 370, 1450, 760), fill="panel_alt", border="secondary")
    panel(draw, (735, 560, 1185, 920), fill="panel_alt", border="ok")
    text_block(draw, (540, 500), "exact wording", size=44, color="primary", bold=True)
    text_block(draw, (1080, 500), "visible timestamp", size=42, color="secondary", bold=True)
    text_block(draw, (800, 700), "version/update state", size=42, color="ok", bold=True)
    draw.line((900, 560, 1010, 560), fill=PALETTE["line"], width=5)
    draw.line((900, 610, 1010, 650), fill=PALETTE["line"], width=5)


def frame4_deadline_update_timeline(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Deadline Update Timeline", "Historical capture vs current page")
    panel(draw, (160, 280, 1760, 860))
    draw.line((260, 620, 1660, 620), fill=PALETTE["line"], width=8)
    points = [
        (420, "Monday", "Capture: May 1", "inference"),
        (1380, "Wednesday", "Current page: May 15", "ok"),
    ]
    for x, day, label, color in points:
        draw.ellipse((x - 20, 600, x + 20, 640), fill=PALETTE[color])
        text_block(draw, (x - 70, 530), day, size=30, color="muted", bold=True)
        text_block(draw, (x - 180, 670), label, size=42, color=color, bold=True)
    panel(draw, (610, 420, 1310, 515), fill="panel_alt", border="secondary")
    text_block(draw, (690, 448), "Historical != current", size=44, color="secondary", bold=True)


def frame4_status_page_updates(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Status Page Updates", "Time context changes meaning")
    panel(draw, (240, 280, 1680, 860), border="line")
    panel(draw, (300, 380, 1620, 530), fill="panel_alt", border="inference")
    panel(draw, (300, 570, 1620, 720), fill="panel_alt", border="ok")
    text_block(draw, (360, 430), "10:15 AM", size=40, color="inference", bold=True)
    text_block(draw, (610, 430), "Investigating elevated error rates", size=44, bold=True)
    text_block(draw, (360, 620), "11:40 AM", size=40, color="ok", bold=True)
    text_block(draw, (610, 620), "Resolved", size=44, bold=True)
    tag(draw, (300, 760), "time context changes meaning", "secondary")


def frame4_draft_vs_final(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Draft vs Final", "Version stage changes claim strength")
    panel(draw, (120, 260, 900, 860), border="secondary")
    panel(draw, (1020, 260, 1800, 860), border="ok")
    tag(draw, (160, 300), "Draft", "secondary")
    tag(draw, (1060, 300), "Final", "ok")
    text_block(draw, (180, 470), '"recommends"', size=72, color="secondary", bold=True)
    text_block(draw, (1080, 470), '"approved"', size=72, color="ok", bold=True)
    text_block(draw, (180, 760), "Not a final decision", size=34, color="muted")
    text_block(draw, (1080, 760), "Final adopted state", size=34, color="muted")


def frame4_moving_dashboard(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Moving Dashboard", "Snapshot and live state can both be valid")
    panel(draw, (120, 260, 900, 860), border="secondary")
    panel(draw, (1020, 260, 1800, 860), border="ok")
    text_block(draw, (180, 390), "24,000 users", size=84, color="secondary", bold=True)
    text_block(draw, (1080, 390), "29,000 users", size=84, color="ok", bold=True)
    tag(draw, (180, 700), "Historical snapshot", "secondary")
    tag(draw, (1080, 700), "Current dashboard", "ok")


def frame4_claim_classification(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Claim Classification", "Label claims before sharing")
    panel(draw, (120, 280, 620, 880), border="ok")
    panel(draw, (710, 280, 1210, 880), border="secondary")
    panel(draw, (1300, 280, 1800, 880), border="inference")
    text_block(draw, (290, 340), "Current", size=48, color="ok", bold=True)
    text_block(draw, (860, 340), "Historical", size=48, color="secondary", bold=True)
    text_block(draw, (1460, 340), "Unclear", size=48, color="inference", bold=True)
    text_block(draw, (160, 460), "Live page now\nsays May 15", size=38)
    text_block(draw, (750, 460), "Monday screenshot\nshows May 1", size=38)
    text_block(draw, (1340, 460), "No timestamp or\nversion shown", size=38)


def frame4_fast_verification_steps(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Fast Verification Steps", "Use before reposting claims")
    steps = [
        "Capture the exact claim being made",
        "Look for visible time markers",
        "Check the current source",
        "Look for version history",
        "Classify: current / historical / unclear",
    ]
    y = 270
    for idx, step in enumerate(steps, start=1):
        panel(draw, (170, y, 1750, y + 130), fill="panel_alt")
        draw.ellipse((215, y + 42, 267, y + 94), fill=PALETTE["primary"])
        text_block(draw, (234, y + 50), str(idx), size=22, color="bg", bold=True)
        text_block(draw, (310, y + 42), step, size=40)
        y += 145


def frame4_observed_inference_template(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Observed / Inference Template", "Reusable note format")
    rows = [
        ("Observed", "this screenshot shows the page saying X at the visible date or version.", "primary"),
        ("Observed", "the current page now says Y.", "primary"),
        ("Inference", "the source changed between those two checks.", "inference"),
        ("Unknown", "exactly when the change happened, unless a log confirms it.", "secondary"),
    ]
    y = 290
    for label, content, color in rows:
        panel(draw, (140, y, 1780, y + 160), fill="panel_alt")
        tag(draw, (180, y + 56), label, color)
        text_block(draw, (430, y + 64), content, size=36)
        y += 185


def frame4_closing_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Closing", "Keep time attached to claims")
    draw.line((260, 760, 1660, 760), fill=PALETTE["line"], width=6)
    for x, color in [(420, "secondary"), (860, "primary"), (1280, "ok"), (1560, "inference")]:
        draw.ellipse((x - 14, 746, x + 14, 774), fill=PALETTE[color])
    text_block(draw, (460, 430), "Read the date. Check the version.", size=72, bold=True)
    text_block(draw, (660, 560), "Share with time attached.", size=54, color="muted", bold=True)


VIDEO4_FRAMES: list[tuple[str, Callable[[Image.Image, ImageDraw.ImageDraw], None]]] = [
    ("01_title_card.png", frame4_title_card),
    ("02_two_real_captures.png", frame4_two_real_captures),
    ("03_when_was_this_true.png", frame4_when_was_this_true),
    ("04_source_time_version.png", frame4_source_time_version),
    ("05_deadline_update_timeline.png", frame4_deadline_update_timeline),
    ("06_status_page_updates.png", frame4_status_page_updates),
    ("07_draft_vs_final.png", frame4_draft_vs_final),
    ("08_moving_dashboard.png", frame4_moving_dashboard),
    ("09_claim_classification.png", frame4_claim_classification),
    ("10_fast_verification_steps.png", frame4_fast_verification_steps),
    ("11_observed_inference_template.png", frame4_observed_inference_template),
    ("12_closing_card.png", frame4_closing_card),
]


# Video 5 frames

def frame5_title_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "The Crop Hides the Clue", "How missing context changes screenshot claims")
    panel(draw, (180, 290, 960, 900), border="secondary")
    panel(draw, (860, 250, 1740, 880), fill="panel_alt", border="primary")
    tag(draw, (230, 340), "Inside crop", "secondary")
    tag(draw, (910, 300), "Outside crop", "primary")
    text_block(draw, (270, 500), "24,000 users", size=70, color="secondary", bold=True)
    text_block(draw, (980, 500), "Last 24 hours", size=58, color="primary", bold=True)
    text_block(draw, (360, 930), "Real screenshot. Smaller certainty.", size=38, color="muted")


def frame5_real_crop_wrong_conclusion(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Real Crop, Wrong Conclusion?", "Authentic image does not guarantee full context")
    panel(draw, (210, 290, 950, 840), border="secondary")
    panel(draw, (980, 250, 1710, 880), border="primary")
    tag(draw, (250, 330), "Inside crop", "secondary")
    tag(draw, (1020, 290), "Outside crop", "primary")
    text_block(draw, (280, 480), "24,000 users", size=68, color="secondary", bold=True)
    text_block(draw, (1040, 470), "Filter: Last 24 hours", size=44, color="primary", bold=True)
    panel(draw, (520, 900, 1410, 1015), fill="panel_alt", border="inference")
    text_block(draw, (570, 938), "Real image, wrong conclusion?", size=52, color="inference", bold=True)


def frame5_what_is_outside_frame(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "What Is Outside the Frame?", "Missing clues often set claim limits")
    panel(draw, (180, 270, 1740, 840))
    text_block(draw, (520, 360), "What is outside the frame?", size=76, bold=True)
    clues = [
        (300, 610, "date", "primary"),
        (560, 610, "domain", "primary"),
        (860, 610, "filter", "secondary"),
        (1140, 610, "banner", "secondary"),
        (1410, 610, "version", "inference"),
    ]
    for x, y, label, color in clues:
        tag(draw, (x, y), label, color)


def frame5_context_rails_grid(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Context Rails", "Check each rail before drawing conclusions")
    cards = [
        (180, 300, "Date", "Captured Mar 8, 9:12 AM PT", "primary"),
        (560, 300, "Domain", "mirror.example.net", "inference"),
        (940, 300, "Filter", "Last 24 hours", "secondary"),
        (1320, 300, "Status Banner", "Resolved 20 min later", "ok"),
        (750, 620, "Document Label", "Draft for review", "inference"),
    ]
    for x, y, title, body, color in cards:
        panel(draw, (x, y, x + 360, y + 240), fill="panel_alt", border=color)
        text_block(draw, (x + 26, y + 36), title, size=38, color=color, bold=True)
        text_block(draw, (x + 26, y + 116), body, size=30)


def frame5_chart_filter_reveal(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Chart Filter Reveal", "Crop hides what the metric counts")
    panel(draw, (170, 280, 860, 860), border="secondary")
    panel(draw, (940, 240, 1760, 890), border="primary")
    tag(draw, (210, 320), "Inside crop", "secondary")
    tag(draw, (980, 280), "Outside crop", "primary")
    text_block(draw, (220, 500), "24,000 users", size=76, color="secondary", bold=True)
    text_block(draw, (1000, 360), "Filter: Last 24 hours", size=44, color="primary", bold=True)
    text_block(draw, (1000, 470), "Observed: number is real", size=36, color="primary")
    text_block(draw, (1000, 560), "Inference: total users", size=36, color="inference")


def frame5_status_banner_reveal(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Status Banner Reveal", "Current-state claims need full page context")
    panel(draw, (170, 280, 860, 860), border="secondary")
    panel(draw, (940, 240, 1760, 890), border="primary")
    tag(draw, (210, 320), "Inside crop", "secondary")
    tag(draw, (980, 280), "Outside crop", "primary")
    text_block(draw, (220, 430), "Investigating elevated", size=42, bold=True)
    text_block(draw, (220, 490), "error rates", size=42, bold=True)
    panel(draw, (980, 360, 1720, 500), fill="panel_alt", border="ok")
    text_block(draw, (1020, 406), "Resolved - 20 minutes later", size=42, color="ok", bold=True)


def frame5_draft_header_reveal(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Draft Header Reveal", "Quoted text can be real but pre-final")
    panel(draw, (170, 280, 860, 860), border="secondary")
    panel(draw, (940, 240, 1760, 890), border="primary")
    tag(draw, (210, 320), "Inside crop", "secondary")
    tag(draw, (980, 280), "Outside crop", "primary")
    text_block(draw, (220, 430), '"Policy update takes', size=40)
    text_block(draw, (220, 490), 'effect July 1."', size=40)
    panel(draw, (980, 360, 1680, 480), fill="panel_alt", border="inference")
    text_block(draw, (1020, 400), "Header: Draft for review", size=44, color="inference", bold=True)
    text_block(draw, (1020, 550), "Claim limit: not final policy", size=36, color="secondary", bold=True)


def frame5_domain_context_reveal(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Domain Context Reveal", "Source claim changes with full frame")
    panel(draw, (170, 280, 860, 860), border="secondary")
    panel(draw, (940, 240, 1760, 890), border="primary")
    tag(draw, (210, 320), "Inside crop", "secondary")
    tag(draw, (980, 280), "Outside crop", "primary")
    text_block(draw, (220, 430), "Official-looking notice", size=44, bold=True)
    panel(draw, (980, 360, 1720, 490), fill="panel_alt", border="inference")
    text_block(draw, (1020, 398), "Domain: mirror.example.net", size=42, color="inference", bold=True)
    text_block(draw, (1020, 560), "Observed: copied text", size=34, color="primary")
    text_block(draw, (1020, 630), "Unknown: source provenance", size=34, color="secondary")


def frame5_claim_limit_template(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Claim Limit Template", "Inside crop vs outside crop vs claim limit")
    panel(draw, (120, 280, 620, 900), border="secondary")
    panel(draw, (710, 280, 1210, 900), border="primary")
    panel(draw, (1300, 280, 1800, 900), border="inference")
    text_block(draw, (200, 340), "Inside crop", size=46, color="secondary", bold=True)
    text_block(draw, (770, 340), "Outside crop", size=46, color="primary", bold=True)
    text_block(draw, (1380, 340), "Claim limit", size=46, color="inference", bold=True)
    text_block(draw, (150, 460), "24,000 users", size=40)
    text_block(draw, (740, 460), "Last 24 hours", size=40)
    text_block(draw, (1340, 460), "Not total users", size=40)
    text_block(draw, (150, 620), "Investigating", size=40)
    text_block(draw, (740, 620), "Resolved banner", size=40)
    text_block(draw, (1340, 620), "Incident now closed", size=40)


def frame5_fast_verification_steps(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Fast Verification Steps", "Routine for cropped screenshot claims")
    steps = [
        "Write the exact claim the screenshot supports",
        "List clues missing outside the crop",
        "Find uncropped source view if possible",
        "Separate direct evidence from context gaps",
        "Lower confidence when context is unresolved",
    ]
    y = 270
    for idx, step in enumerate(steps, start=1):
        panel(draw, (170, y, 1750, y + 130), fill="panel_alt")
        draw.ellipse((215, y + 42, 267, y + 94), fill=PALETTE["primary"])
        text_block(draw, (234, y + 50), str(idx), size=22, color="bg", bold=True)
        text_block(draw, (310, y + 42), step, size=38)
        y += 145


def frame5_observed_unknown_inference(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Observed / Unknown / Inference", "Reusable uncertainty-aware note")
    rows = [
        ("Observed", "Cropped screenshot shows '24,000 users'.", "primary"),
        ("Unknown", "Whether this is total users or a filtered window.", "secondary"),
        ("Inference", "Repost may overclaim without uncropped context.", "inference"),
    ]
    y = 300
    for label, content, color in rows:
        panel(draw, (150, y, 1770, y + 180), fill="panel_alt")
        tag(draw, (190, y + 68), label, color)
        text_block(draw, (440, y + 72), content, size=38)
        y += 205


def frame5_closing_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Closing", "Verification doctrine")
    text_block(draw, (470, 460), "Ask what is outside the frame.", size=72, bold=True)
    text_block(draw, (640, 580), "Real screenshot. Smaller certainty.", size=46, color="muted", bold=True)


VIDEO5_FRAMES: list[tuple[str, Callable[[Image.Image, ImageDraw.ImageDraw], None]]] = [
    ("01_title_card.png", frame5_title_card),
    ("02_real_crop_wrong_conclusion.png", frame5_real_crop_wrong_conclusion),
    ("03_what_is_outside_frame.png", frame5_what_is_outside_frame),
    ("04_context_rails_grid.png", frame5_context_rails_grid),
    ("05_chart_filter_reveal.png", frame5_chart_filter_reveal),
    ("06_status_banner_reveal.png", frame5_status_banner_reveal),
    ("07_draft_header_reveal.png", frame5_draft_header_reveal),
    ("08_domain_context_reveal.png", frame5_domain_context_reveal),
    ("09_claim_limit_template.png", frame5_claim_limit_template),
    ("10_fast_verification_steps.png", frame5_fast_verification_steps),
    ("11_observed_unknown_inference.png", frame5_observed_unknown_inference),
    ("12_closing_card.png", frame5_closing_card),
]


# Video 6 frames

def frame6_title_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "A Real Number, Incomplete Conclusion", "Missing denominator, baseline, or window can mislead")
    panel(draw, (170, 300, 1750, 860), fill="panel_alt")
    text_block(draw, (260, 430), "The number may be real.", size=62, color="primary", bold=True)
    text_block(draw, (260, 530), "The conclusion can still overreach.", size=62, color="inference", bold=True)
    tag(draw, (260, 700), "Observed", "primary")
    tag(draw, (500, 700), "Missing context", "secondary")
    tag(draw, (840, 700), "Overreach risk", "inference")
    tag(draw, (1140, 700), "Clarifying context", "ok")


def frame6_big_number_hook(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Big Number Hook", "Dramatic count, unclear meaning")
    panel(draw, (180, 260, 920, 880), border="secondary")
    panel(draw, (990, 260, 1740, 880), border="primary")
    tag(draw, (220, 300), "Count card", "secondary")
    text_block(draw, (250, 430), "24,000\nreports filed", size=88, color="secondary", bold=True)
    text_block(draw, (250, 760), "Observed: number appears in source", size=30, color="primary")
    tag(draw, (1030, 300), "Context card", "primary")
    text_block(draw, (1070, 430), "But what does\nit mean?", size=72, color="text", bold=True)
    text_block(draw, (1070, 730), "Need denominator, baseline,\nand time window.", size=34, color="muted")


def frame6_out_of_how_many(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Out of How Many?", "Denominator changes interpretation")
    panel(draw, (150, 300, 1770, 860), fill="panel")
    panel(draw, (220, 380, 860, 780), fill="panel_alt", border="secondary")
    panel(draw, (1030, 380, 1700, 780), fill="panel_alt", border="ok")
    text_block(draw, (270, 470), "24,000 reports", size=64, color="secondary", bold=True)
    text_block(draw, (1080, 470), "18,000,000 users", size=64, color="ok", bold=True)
    draw.line((860, 580, 1030, 580), fill=PALETTE["line"], width=6)
    text_block(draw, (650, 530), "/", size=64, color="text", bold=True)
    panel(draw, (520, 800, 1400, 930), fill="panel_alt", border="primary")
    text_block(draw, (610, 842), "24,000 / 18,000,000 = 1.3 per 1,000", size=42, color="primary", bold=True)


def frame6_count_vs_rate(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Count vs Rate", "Use the metric that matches the claim")
    panel(draw, (160, 300, 900, 860), border="secondary")
    panel(draw, (1020, 300, 1760, 860), border="primary")
    tag(draw, (200, 340), "Count", "secondary")
    tag(draw, (1060, 340), "Rate", "primary")
    text_block(draw, (220, 460), "Answers volume", size=46, color="secondary", bold=True)
    text_block(draw, (220, 550), "City A: 12,000", size=54, color="text", bold=True)
    text_block(draw, (220, 650), "City B: 8,000", size=54, color="text", bold=True)
    text_block(draw, (1080, 460), "Answers prevalence", size=46, color="primary", bold=True)
    text_block(draw, (1080, 550), "City A: 3 per 1,000", size=54, color="text", bold=True)
    text_block(draw, (1080, 650), "City B: 8 per 1,000", size=54, color="text", bold=True)
    text_block(draw, (540, 910), "Observed metric first, conclusion second", size=34, color="muted")


def frame6_small_base_rate(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Small Base Rate", "Correct math can still overstate scope")
    panel(draw, (210, 300, 1710, 860), fill="panel")
    panel(draw, (300, 380, 820, 760), fill="panel_alt", border="inference")
    panel(draw, (900, 380, 1620, 760), fill="panel_alt", border="secondary")
    text_block(draw, (360, 470), '"Up 100%"', size=72, color="inference", bold=True)
    text_block(draw, (960, 470), "3 -> 6 cases", size=80, color="secondary", bold=True)
    text_block(draw, (960, 620), "Observed: doubling", size=34, color="primary")
    text_block(draw, (350, 620), "Inference risk:\n'widespread now'", size=34, color="inference")
    tag(draw, (700, 800), "Correct math, limited scope", "ok")


def frame6_time_window_reveal(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Time Window Reveal", "Totals need a timeframe")
    panel(draw, (170, 300, 1750, 860))
    panel(draw, (240, 390, 860, 770), fill="panel_alt", border="secondary")
    panel(draw, (980, 390, 1680, 770), fill="panel_alt", border="ok")
    text_block(draw, (300, 500), "1,200 incidents", size=72, color="secondary", bold=True)
    text_block(draw, (1040, 480), "Over 5 years", size=66, color="ok", bold=True)
    text_block(draw, (1040, 600), "~20 per month avg", size=52, color="primary", bold=True)
    tag(draw, (760, 800), "Window changes urgency claims", "secondary")


def frame6_rank_vs_population(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Rank vs Population", "Per-capita adjustment can reverse rankings")
    panel(draw, (120, 270, 900, 900), border="secondary")
    panel(draw, (1020, 270, 1800, 900), border="primary")
    tag(draw, (160, 310), "Raw count ranking", "secondary")
    tag(draw, (1060, 310), "Per-capita ranking", "primary")
    text_block(draw, (170, 430), "City A: 12,000 (4M)", size=44, bold=True)
    text_block(draw, (170, 520), "City B: 8,000 (1M)", size=44, bold=True)
    text_block(draw, (170, 650), "Count rank: A > B", size=50, color="secondary", bold=True)
    text_block(draw, (1070, 430), "A: 3 per 1,000", size=48, bold=True)
    text_block(draw, (1070, 520), "B: 8 per 1,000", size=48, bold=True)
    text_block(draw, (1070, 650), "Rate rank: B > A", size=50, color="primary", bold=True)
    text_block(draw, (660, 940), "Metric mismatch causes reversal", size=34, color="muted")


def frame6_baseline_shift(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Baseline Shift", "Compared with what baseline?")
    panel(draw, (160, 300, 1760, 860), fill="panel")
    panel(draw, (230, 380, 1730, 760), fill="panel_alt")
    labels = [
        (290, "Last month", "secondary"),
        (760, "Last year", "secondary"),
        (1210, "Typical range", "ok"),
    ]
    for x, text, color in labels:
        panel(draw, (x, 430, x + 380, 700), fill="panel", border=color)
        text_block(draw, (x + 48, 500), text, size=44, color=color, bold=True)
    text_block(draw, (530, 840), "Same value, different baselines -> different claims", size=36, color="primary")


def frame6_claim_limit_template(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Claim Limit Template", "Observed, Inference, Unknown")
    panel(draw, (140, 290, 1780, 450), fill="panel_alt")
    panel(draw, (140, 490, 1780, 650), fill="panel_alt")
    panel(draw, (140, 690, 1780, 850), fill="panel_alt")
    panel(draw, (140, 890, 1780, 1020), fill="panel_alt")
    tag(draw, (190, 348), "Observed", "primary")
    tag(draw, (190, 548), "Inference", "inference")
    tag(draw, (190, 748), "Unknown", "secondary")
    tag(draw, (190, 918), "Claim limit", "ok")
    text_block(draw, (470, 352), "Source shows 24,000 reports.", size=42)
    text_block(draw, (470, 552), "Count alone may sound severe.", size=42)
    text_block(draw, (470, 752), "Need denominator, baseline, and window.", size=42)
    text_block(draw, (470, 920), "Use scoped wording until missing context is found.", size=40, color="ok")


def frame6_fast_verification_steps(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Fast Verification Steps", "Four rails before sharing")
    steps = [
        "1 Out of how many?",
        "2 Compared with what baseline?",
        "3 Over what time window?",
        "4 Count or rate?",
    ]
    y = 300
    for idx, step in enumerate(steps, start=1):
        panel(draw, (190, y, 1730, y + 150), fill="panel_alt")
        draw.ellipse((240, y + 50, 292, y + 102), fill=PALETTE["primary"])
        text_block(draw, (258, y + 58), str(idx), size=22, color="bg", bold=True)
        text_block(draw, (340, y + 50), step, size=46)
        y += 170


def frame6_observed_inference_template(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Observed / Inference / Unknown", "Reusable note format")
    rows = [
        ("Observed", "Source says: 24,000 reports were filed.", "primary"),
        ("Inference", "May imply elevated activity, but severity is not confirmed.", "inference"),
        ("Unknown", "Denominator, baseline trend, and window-specific spike data.", "secondary"),
    ]
    y = 300
    for label, content, color in rows:
        panel(draw, (160, y, 1760, y + 190), fill="panel_alt")
        tag(draw, (210, y + 72), label, color)
        text_block(draw, (500, y + 76), content, size=38)
        y += 215


def frame6_closing_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Verify the Rails", "Real number, incomplete conclusion.")
    text_block(draw, (470, 420), "Check denominator, baseline, window.", size=62, bold=True)
    text_block(draw, (660, 560), "Then match count vs rate.", size=50, color="muted")
    tag(draw, (540, 700), "Observed", "primary")
    tag(draw, (760, 700), "Unknown", "secondary")
    tag(draw, (980, 700), "Inference", "inference")
    tag(draw, (1220, 700), "Context", "ok")


VIDEO6_FRAMES: list[tuple[str, Callable[[Image.Image, ImageDraw.ImageDraw], None]]] = [
    ("01_title_card.png", frame6_title_card),
    ("02_big_number_hook.png", frame6_big_number_hook),
    ("03_out_of_how_many.png", frame6_out_of_how_many),
    ("04_count_vs_rate.png", frame6_count_vs_rate),
    ("05_small_base_rate.png", frame6_small_base_rate),
    ("06_time_window_reveal.png", frame6_time_window_reveal),
    ("07_rank_vs_population.png", frame6_rank_vs_population),
    ("08_baseline_shift.png", frame6_baseline_shift),
    ("09_claim_limit_template.png", frame6_claim_limit_template),
    ("10_fast_verification_steps.png", frame6_fast_verification_steps),
    ("11_observed_inference_template.png", frame6_observed_inference_template),
    ("12_closing_card.png", frame6_closing_card),
]


# Video 7 frames

def frame7_title_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Same Label, Different Metric", "Definition drift can break comparisons")
    panel(draw, (170, 290, 1750, 860), fill="panel_alt")
    text_block(draw, (250, 390), "Same label, different metric.", size=74, bold=True)
    tag(draw, (250, 560), "Label unchanged", "primary")
    tag(draw, (560, 560), "Rule set A", "secondary")
    tag(draw, (760, 560), "Rule set B", "inference")
    panel(draw, (250, 640, 820, 770), fill="panel", border="primary")
    panel(draw, (910, 640, 1480, 770), fill="panel", border="inference")
    text_block(draw, (300, 684), "Active users", size=46, color="text", bold=True)
    text_block(draw, (960, 684), "Active users", size=46, color="text", bold=True)


def frame7_metric_jump_hook(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Metric Jump Hook", "Unchanged label does not guarantee comparability")
    panel(draw, (170, 270, 900, 880), border="secondary")
    panel(draw, (1020, 270, 1750, 880), border="inference")
    tag(draw, (210, 310), "Dashboard card", "secondary")
    tag(draw, (1060, 310), "Dashboard card", "inference")
    text_block(draw, (240, 430), "Active users", size=56, bold=True)
    text_block(draw, (240, 540), "Jan: 24,000", size=78, color="secondary", bold=True)
    text_block(draw, (240, 790), "Same label", size=36, color="primary")
    text_block(draw, (1090, 430), "Active users", size=56, bold=True)
    text_block(draw, (1090, 540), "Apr: 31,000", size=78, color="inference", bold=True)
    text_block(draw, (1090, 790), "Same label", size=36, color="primary")


def frame7_reality_or_definition(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Reality or Definition?", "Diagnostic split before trend claims")
    panel(draw, (220, 300, 1700, 860), fill="panel")
    panel(draw, (290, 390, 860, 760), fill="panel_alt", border="ok")
    panel(draw, (1060, 390, 1630, 760), fill="panel_alt", border="secondary")
    text_block(draw, (350, 470), "Did reality\nchange?", size=62, color="ok", bold=True)
    text_block(draw, (1120, 470), "Or did definition\nchange?", size=62, color="secondary", bold=True)
    draw.line((860, 570, 980, 570), fill=PALETTE["line"], width=8)
    draw.polygon([(980, 540), (1035, 570), (980, 600)], fill=PALETTE["line"])
    text_block(draw, (630, 810), "Same label, different metric.", size=40, color="muted", bold=True)


def frame7_definition_drift_rails(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Definition Drift Rails", "Observed / Inference / Unknown")
    rows = [
        ("Observed", "Label stayed the same while inclusion rules changed.", "primary"),
        ("Inference", "Part of the jump may be definition drift.", "inference"),
        ("Unknown", "How much is true behavior vs rule change.", "secondary"),
    ]
    y = 300
    for label, content, color in rows:
        panel(draw, (150, y, 1770, y + 190), fill="panel_alt")
        tag(draw, (200, y + 74), label, color)
        text_block(draw, (520, y + 78), content, size=38)
        y += 215


def frame7_active_users_note_reveal(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Active Users Note Reveal", "Methodology changed under the same heading")
    panel(draw, (170, 270, 1750, 860), border="primary")
    text_block(draw, (250, 360), "Active users", size=64, bold=True)
    text_block(draw, (250, 470), "24,000 -> 31,000", size=82, color="secondary", bold=True)
    panel(draw, (250, 610, 1670, 790), fill="panel_alt", border="inference")
    text_block(draw, (290, 650), "Methodology note: Now includes API token activity", size=44, color="inference", bold=True)
    text_block(draw, (290, 712), "Previously web + mobile only", size=38, color="muted")
    tag(draw, (1300, 350), "Label unchanged", "primary")


def frame7_resolved_cases_expansion(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Resolved Cases Expansion", "Bucket widened while label stayed fixed")
    panel(draw, (180, 280, 1740, 860), fill="panel")
    panel(draw, (240, 360, 1680, 760), fill="panel_alt", border="primary")
    text_block(draw, (280, 410), "Resolved cases", size=58, bold=True)
    panel(draw, (300, 510, 760, 700), fill="panel", border="ok")
    text_block(draw, (330, 565), "Before:\nfully resolved only", size=40, color="ok")
    panel(draw, (860, 510, 1620, 700), fill="panel", border="secondary")
    text_block(draw, (890, 555), "Now:\nfully + partial + admin closed", size=40, color="secondary")
    draw.line((760, 605, 860, 605), fill=PALETTE["line"], width=8)
    tag(draw, (1320, 410), "Label unchanged", "primary")


def frame7_incidents_scope_broadening(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Incidents Scope Broadening", "Headline identical, severity scope expanded")
    panel(draw, (180, 280, 1740, 860), fill="panel")
    panel(draw, (240, 360, 1680, 760), fill="panel_alt", border="primary")
    text_block(draw, (280, 410), "Incidents", size=58, bold=True)
    panel(draw, (300, 500, 760, 690), fill="panel", border="secondary")
    text_block(draw, (330, 555), "Before:\nhigh severity", size=44, color="secondary")
    panel(draw, (860, 500, 1620, 690), fill="panel", border="inference")
    text_block(draw, (890, 535), "Now:\nhigh + low + near-miss", size=44, color="inference")
    text_block(draw, (300, 735), "Severity legend expanded; label did not.", size=36, color="muted")
    tag(draw, (1320, 410), "Label unchanged", "primary")


def frame7_number_real_not_comparable(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Number Real, Not Comparable", "Counting rule changed")
    panel(draw, (170, 300, 900, 860), border="ok")
    panel(draw, (1020, 300, 1750, 860), border="secondary")
    tag(draw, (210, 340), "Authenticity", "ok")
    tag(draw, (1060, 340), "Comparability", "secondary")
    text_block(draw, (240, 470), "Number can be real", size=62, color="ok", bold=True)
    text_block(draw, (240, 600), "Source is authentic", size=38)
    text_block(draw, (1090, 470), "Comparison can fail", size=62, color="secondary", bold=True)
    text_block(draw, (1090, 600), "Counting rule changed", size=42, color="inference", bold=True)
    draw.line((900, 570, 1020, 570), fill=PALETTE["line"], width=8)


def frame7_claim_boundary_template(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Claim Boundary Template", "Reusable language for definition drift")
    panel(draw, (150, 290, 1770, 490), fill="panel_alt")
    panel(draw, (150, 520, 1770, 720), fill="panel_alt")
    panel(draw, (150, 750, 1770, 950), fill="panel_alt")
    tag(draw, (200, 370), "Observed", "primary")
    tag(draw, (200, 600), "Inference", "inference")
    tag(draw, (200, 830), "Unknown", "secondary")
    text_block(draw, (500, 376), "Definition changed while headline label stayed the same.", size=38)
    text_block(draw, (500, 606), "Trend claim is limited until like-for-like counts are rebuilt.", size=38)
    text_block(draw, (500, 836), "True behavior change share vs definition change share.", size=38)


def frame7_verification_checklist(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Verification Checklist", "Six steps for same-label metric changes")
    steps = [
        "1 Label",
        "2 Definition",
        "3 Inclusion rules",
        "4 Change date",
        "5 Comparability",
        "6 O-I-U note",
    ]
    y = 260
    for step in steps:
        panel(draw, (230, y, 1690, y + 112), fill="panel_alt")
        draw.ellipse((278, y + 34, 326, y + 82), fill=PALETTE["ok"])
        text_block(draw, (292, y + 40), "✓", size=24, color="bg", bold=True)
        text_block(draw, (360, y + 34), step, size=42)
        y += 126


def frame7_reusable_note_example(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Reusable Note Example", "Plain-language worksheet")
    panel(draw, (170, 290, 1750, 910), fill="panel")
    panel(draw, (250, 370, 1670, 860), fill="panel_alt", border="line")
    text_block(draw, (300, 440), "Observed: A uses D1, B uses D2", size=48, color="primary", bold=True)
    text_block(draw, (300, 570), "Inference: metric changed", size=48, color="inference", bold=True)
    text_block(draw, (300, 700), "Unknown: behavior vs definition share", size=46, color="secondary", bold=True)
    text_block(draw, (300, 810), "Same label, different metric.", size=34, color="muted")


def frame7_closing_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Closing", "Definition line before trend line")
    panel(draw, (220, 320, 1700, 860), fill="panel_alt")
    text_block(draw, (300, 450), "Same label does not guarantee same metric.", size=62, bold=True)
    text_block(draw, (330, 570), "Check the definition line before the trend line.", size=50, color="muted", bold=True)
    tag(draw, (620, 700), "Observed", "primary")
    tag(draw, (840, 700), "Unknown", "secondary")
    tag(draw, (1060, 700), "Inference", "inference")
    tag(draw, (1280, 700), "Context", "ok")


VIDEO7_FRAMES: list[tuple[str, Callable[[Image.Image, ImageDraw.ImageDraw], None]]] = [
    ("01_title_card.png", frame7_title_card),
    ("02_metric_jump_hook.png", frame7_metric_jump_hook),
    ("03_reality_or_definition.png", frame7_reality_or_definition),
    ("04_definition_drift_rails.png", frame7_definition_drift_rails),
    ("05_active_users_note_reveal.png", frame7_active_users_note_reveal),
    ("06_resolved_cases_expansion.png", frame7_resolved_cases_expansion),
    ("07_incidents_scope_broadening.png", frame7_incidents_scope_broadening),
    ("08_number_real_not_comparable.png", frame7_number_real_not_comparable),
    ("09_claim_boundary_template.png", frame7_claim_boundary_template),
    ("10_verification_checklist.png", frame7_verification_checklist),
    ("11_reusable_note_example.png", frame7_reusable_note_example),
    ("12_closing_card.png", frame7_closing_card),
]


# Video 8 frames

def frame8_title_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Three Posts Are Not a Trend", "How Sample Bias Misleads")
    panel(draw, (170, 290, 1750, 860), fill="panel_alt")
    text_block(draw, (250, 410), "Evidence of existence is not\nevidence of prevalence.", size=66, bold=True)
    tag(draw, (250, 640), "Observed", "primary")
    tag(draw, (470, 640), "Unknown", "secondary")
    tag(draw, (680, 640), "Overreach", "inference")


def frame8_viral_feed_hook(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Viral Feed Hook", "A ranked feed can feel like a trend")
    panel(draw, (220, 260, 920, 900), border="inference")
    panel(draw, (1000, 260, 1700, 900), border="primary")
    text_block(draw, (270, 320), "My feed is full of this", size=48, bold=True)
    panel(draw, (270, 420, 870, 530), fill="panel_alt")
    panel(draw, (270, 560, 870, 670), fill="panel_alt")
    panel(draw, (270, 700, 870, 810), fill="panel_alt")
    text_block(draw, (310, 452), "3 viral posts in a row", size=40, color="inference", bold=True)
    text_block(draw, (310, 594), "Feels like a trend", size=40, color="inference", bold=True)
    text_block(draw, (1030, 380), "Top slots favor\nhigh engagement", size=50, color="primary", bold=True)
    text_block(draw, (1030, 620), "Ordinary posts\nbelow fold", size=44, color="muted")


def frame8_existence_vs_prevalence(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Existence vs Prevalence", "Different claims need different proof")
    panel(draw, (160, 280, 900, 860), border="primary")
    panel(draw, (1020, 280, 1760, 860), border="secondary")
    tag(draw, (200, 320), "Evidence of existence", "primary")
    tag(draw, (1060, 320), "Evidence of prevalence", "secondary")
    panel(draw, (220, 420, 840, 760), fill="panel_alt")
    text_block(draw, (280, 520), "One verified\nexample", size=60, color="primary", bold=True)
    bars = [(1140, 700), (1260, 620), (1380, 760), (1500, 540), (1620, 660)]
    for x, y in bars:
        draw.rounded_rectangle((x, y, x + 70, 780), radius=12, fill=PALETTE["secondary"])
    text_block(draw, (1110, 810), "Population distribution data", size=30, color="muted")


def frame8_sampling_bias_rails(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Sampling Bias Rails", "Observed / Inference / Unknown")
    rows = [
        ("Observed", "Examples shown are authentic captures.", "primary"),
        ("Inference", "Feed snapshot suggests a widespread trend.", "inference"),
        ("Unknown", "How representative the visible sample is.", "secondary"),
    ]
    y = 300
    for label, content, color in rows:
        panel(draw, (160, y, 1760, y + 200), fill="panel_alt")
        tag(draw, (210, y + 78), label, color)
        text_block(draw, (500, y + 82), content, size=40)
        y += 220


def frame8_feed_selection_pressure(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Feed Selection Pressure", "Visible does not mean common")
    panel(draw, (150, 270, 1770, 880), fill="panel")
    panel(draw, (220, 360, 760, 780), fill="panel_alt", border="secondary")
    panel(draw, (1080, 360, 1620, 780), fill="panel_alt", border="primary")
    text_block(draw, (280, 420), "Ranked for\nattention", size=54, color="secondary", bold=True)
    text_block(draw, (1140, 420), "Amplified\nsample", size=54, color="primary", bold=True)
    draw.polygon([(780, 460), (1040, 560), (780, 660)], fill=PALETTE["line"])
    text_block(draw, (820, 810), "Visible ≠ common", size=44, color="inference", bold=True)


def frame8_screenshot_thread_claim(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Screenshot Thread Claim", "Thread collage vs denominator")
    panel(draw, (170, 280, 980, 880), border="secondary")
    panel(draw, (1050, 280, 1750, 880), border="inference")
    text_block(draw, (230, 340), "5 real screenshots", size=56, color="secondary", bold=True)
    for i in range(5):
        y0 = 430 + i * 78
        panel(draw, (230, y0, 920, y0 + 62), fill="panel_alt")
    text_block(draw, (1100, 420), "Claim:\neveryone is saying this", size=54, color="inference", bold=True)
    panel(draw, (1100, 670, 1690, 790), fill="panel_alt", border="secondary")
    text_block(draw, (1160, 708), "Out of how many?", size=48, color="secondary", bold=True)


def frame8_reporting_intensity_dashboard(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Reporting Intensity Dashboard", "Reported incidents up")
    panel(draw, (160, 270, 1760, 880), fill="panel")
    panel(draw, (230, 350, 1220, 820), fill="panel_alt", border="primary")
    points = [(280, 760), (430, 730), (580, 700), (730, 620), (880, 540), (1030, 470), (1180, 430)]
    draw.line(tuple(v for p in points for v in p), fill=PALETTE["primary"], width=8)
    text_block(draw, (270, 390), "Reported incidents up", size=44, color="primary", bold=True)
    panel(draw, (1280, 390, 1710, 550), fill="panel_alt", border="secondary")
    panel(draw, (1280, 590, 1710, 750), fill="panel_alt", border="inference")
    text_block(draw, (1320, 440), "Reporting\ncampaign active", size=34, color="secondary", bold=True)
    text_block(draw, (1320, 640), "Visibility\npressure", size=34, color="inference", bold=True)


def frame8_visibility_not_prevalence(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Visibility Is Not Prevalence", "Accurate count, limited claim")
    panel(draw, (170, 300, 900, 860), border="ok")
    panel(draw, (1020, 300, 1750, 860), border="secondary")
    tag(draw, (210, 340), "Accurate report count", "ok")
    tag(draw, (1060, 340), "Uncertain prevalence claim", "secondary")
    text_block(draw, (230, 480), "Count integrity:\nverified", size=58, color="ok", bold=True)
    text_block(draw, (1090, 480), "Need stable\ndenominator", size=58, color="secondary", bold=True)
    text_block(draw, (520, 900), "Evidence of existence is not evidence of prevalence.", size=36, color="muted")


def frame8_observed_inference_unknown_template(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Observed / Inference / Unknown", "Reusable O-I-U template")
    panel(draw, (150, 290, 1770, 500), fill="panel_alt")
    panel(draw, (150, 530, 1770, 740), fill="panel_alt")
    panel(draw, (150, 770, 1770, 980), fill="panel_alt")
    tag(draw, (200, 374), "Observed", "primary")
    tag(draw, (200, 614), "Inference", "inference")
    tag(draw, (200, 854), "Unknown", "secondary")
    text_block(draw, (490, 382), "Examples are real.", size=44)
    text_block(draw, (490, 622), "Trend may be widespread.", size=44)
    text_block(draw, (490, 862), "Representativeness not established.", size=44)


def frame8_verification_checklist(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Verification Checklist", "Six steps for sample-bias claims")
    steps = [
        "1 Population",
        "2 X out of Y",
        "3 Collection method",
        "4 Visibility pressure",
        "5 Missing context",
        "6 O-I-U note",
    ]
    y = 250
    for step in steps:
        panel(draw, (220, y, 1700, y + 118), fill="panel_alt")
        draw.ellipse((264, y + 38, 312, y + 86), fill=PALETTE["ok"])
        text_block(draw, (278, y + 44), "✓", size=24, color="bg", bold=True)
        text_block(draw, (350, y + 36), step, size=44)
        y += 128


def frame8_checklist_applied_walkthrough(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Checklist Applied Walkthrough", "Thread case with claim boundary")
    panel(draw, (170, 300, 1750, 900), fill="panel")
    panel(draw, (250, 380, 1670, 840), fill="panel_alt", border="line")
    text_block(draw, (300, 450), "Population: platform posts this week", size=44, color="primary", bold=True)
    text_block(draw, (300, 560), "Sample: 5 shown, Y unknown", size=44, color="secondary", bold=True)
    text_block(draw, (300, 670), "Status: existence shown, prevalence unproven", size=44, color="inference", bold=True)
    tag(draw, (1260, 450), "Claim limited", "ok")


def frame8_closing_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Closing", "Real examples, weak population claim")
    panel(draw, (230, 330, 1690, 840), fill="panel_alt")
    text_block(draw, (300, 470), "Separate examples from prevalence claims.", size=60, bold=True)
    text_block(draw, (420, 600), "Evidence of existence is not evidence of prevalence.", size=40, color="muted")
    tag(draw, (640, 710), "Observed", "primary")
    tag(draw, (860, 710), "Unknown", "secondary")
    tag(draw, (1080, 710), "Inference", "inference")


VIDEO8_FRAMES: list[tuple[str, Callable[[Image.Image, ImageDraw.ImageDraw], None]]] = [
    ("01_title_card.png", frame8_title_card),
    ("02_viral_feed_hook.png", frame8_viral_feed_hook),
    ("03_existence_vs_prevalence.png", frame8_existence_vs_prevalence),
    ("04_sampling_bias_rails.png", frame8_sampling_bias_rails),
    ("05_feed_selection_pressure.png", frame8_feed_selection_pressure),
    ("06_screenshot_thread_claim.png", frame8_screenshot_thread_claim),
    ("07_reporting_intensity_dashboard.png", frame8_reporting_intensity_dashboard),
    ("08_visibility_not_prevalence.png", frame8_visibility_not_prevalence),
    ("09_observed_inference_unknown_template.png", frame8_observed_inference_unknown_template),
    ("10_verification_checklist.png", frame8_verification_checklist),
    ("11_checklist_applied_walkthrough.png", frame8_checklist_applied_walkthrough),
    ("12_closing_card.png", frame8_closing_card),
]


# Video 9 frames

def frame9_title_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "The Winners Are Not the Whole Field", "How Survivorship Bias Misleads")
    panel(draw, (170, 280, 1750, 900), fill="panel_alt")
    for x, y, r, color in [
        (360, 500, 16, "muted"),
        (470, 610, 14, "muted"),
        (620, 470, 15, "muted"),
        (760, 640, 14, "muted"),
        (910, 520, 14, "muted"),
        (1040, 660, 14, "muted"),
        (1180, 500, 13, "muted"),
        (1330, 620, 15, "muted"),
        (1510, 540, 14, "muted"),
        (570, 740, 14, "muted"),
        (1240, 760, 14, "muted"),
    ]:
        draw.ellipse((x - r, y - r, x + r, y + r), fill=PALETTE[color])
    for x, y in [(640, 560), (980, 430), (1380, 470)]:
        draw.ellipse((x - 22, y - 22, x + 22, y + 22), fill=PALETTE["primary"])
    text_block(draw, (250, 790), "Survivors show possibility, not prevalence.", size=40, color="secondary", bold=True)


def frame9_winner_list_hook(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Winner-Heavy Inputs", "Common sources that hide missing cases")
    panel(draw, (240, 260, 1680, 900), fill="panel")
    cards = [
        (320, 330, "Founder success thread"),
        (320, 500, "Current winners list"),
        (320, 670, "Creator growth advice"),
    ]
    for x, y, label in cards:
        panel(draw, (x, y, 1520, y + 130), fill="panel_alt", border="primary")
        text_block(draw, (380, y + 42), label, size=48, color="text", bold=True)
    for y in [360, 530, 700]:
        panel(draw, (1120, y, 1600, y + 90), fill="panel", border="line")
    text_block(draw, (1138, 386), "missing field", size=32, color="secondary", bold=True)
    text_block(draw, (1138, 556), "hidden failures", size=32, color="secondary", bold=True)
    text_block(draw, (1138, 726), "denominator unknown", size=32, color="secondary", bold=True)


def frame9_possibility_vs_prevalence(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Possibility vs Prevalence", "Different claims need different evidence")
    panel(draw, (160, 280, 900, 880), border="primary")
    panel(draw, (1020, 280, 1760, 880), border="secondary")
    text_block(draw, (220, 360), "Proves possibility", size=54, color="primary", bold=True)
    draw.line((280, 700, 420, 520, 560, 610, 700, 460, 840, 540), fill=PALETTE["primary"], width=10)
    text_block(draw, (230, 760), "One working path exists", size=34, color="muted")
    text_block(draw, (1080, 360), "Does not prove typicality", size=52, color="inference", bold=True)
    bars = [(1120, 760), (1240, 700), (1360, 640), (1480, 780), (1600, 680)]
    for x, top in bars:
        draw.rounded_rectangle((x, top, x + 80, 800), radius=12, fill=PALETTE["secondary"])
    text_block(draw, (1080, 840), "Need full field for prevalence", size=34, color="secondary", bold=True)


def frame9_survivorship_mechanism_rails(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Survivorship Mechanism", "Observed / Inference / Unknown")
    panel(draw, (170, 280, 1750, 700), fill="panel")
    panel(draw, (300, 390, 860, 600), fill="panel_alt", border="secondary")
    panel(draw, (1100, 390, 1620, 600), fill="panel_alt", border="primary")
    text_block(draw, (390, 455), "starting\npopulation", size=44, color="secondary", bold=True)
    text_block(draw, (1190, 455), "visible\nsurvivors", size=44, color="primary", bold=True)
    draw.polygon([(900, 410), (1080, 495), (900, 580)], fill=PALETTE["line"])
    rows = [
        ("Observed", "Visible winners are real examples.", "primary"),
        ("Inference", "Winner traits explain most outcomes.", "inference"),
        ("Unknown", "How many similar attempts disappeared.", "secondary"),
    ]
    y = 740
    for label, body, color in rows:
        panel(draw, (170, y, 1750, y + 96), fill="panel_alt")
        tag(draw, (220, y + 26), label, color)
        text_block(draw, (500, y + 30), body, size=36)
        y += 106


def frame9_founder_thread_example(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Founder Thread Example", "One winner story plus missing attempts")
    panel(draw, (180, 280, 1740, 900), fill="panel")
    panel(draw, (260, 340, 1180, 840), fill="panel_alt", border="primary")
    text_block(draw, (310, 390), "One founder won", size=52, color="primary", bold=True)
    text_block(draw, (310, 470), "Tactics documented", size=42, color="text")
    draw.line((340, 620, 1080, 620), fill=PALETTE["line"], width=6)
    for x in [380, 560, 740, 920, 1060]:
        draw.ellipse((x - 14, 606, x + 14, 634), fill=PALETTE["primary"])
    for x, y in [(1280, 420), (1400, 520), (1520, 620), (1380, 740), (1600, 460), (1660, 680)]:
        draw.ellipse((x - 12, y - 12, x + 12, y + 12), fill=PALETTE["muted"])
    text_block(draw, (1240, 780), "How many similar attempts failed?", size=36, color="secondary", bold=True)


def frame9_founder_oiu_breakout(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Founder O-I-U Breakout", "Apply rails before broad advice")
    panel(draw, (170, 300, 1750, 520), fill="panel_alt", border="primary")
    draw.line((290, 430, 1630, 430), fill=PALETTE["line"], width=6)
    for x in [360, 620, 880, 1140, 1400, 1560]:
        draw.ellipse((x - 12, 418, x + 12, 442), fill=PALETTE["primary"])
    rows = [
        ("Observed", "one success path", "primary"),
        ("Inference", "broadly reliable method", "inference"),
        ("Unknown", "denominator of failures", "secondary"),
    ]
    y = 580
    for label, body, color in rows:
        panel(draw, (170, y, 1750, y + 120), fill="panel_alt")
        tag(draw, (220, y + 38), label, color)
        text_block(draw, (500, y + 42), body, size=42)
        y += 132


def frame9_current_tools_example(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Current Tools Example", "Leader map can omit sunset peers")
    panel(draw, (170, 280, 1750, 900), fill="panel")
    panel(draw, (240, 350, 1120, 840), fill="panel_alt", border="primary")
    text_block(draw, (280, 390), "Current leaders shown", size=48, color="primary", bold=True)
    for x, y, label in [(300, 500, "Tool A"), (520, 600, "Tool B"), (760, 520, "Tool C"), (920, 680, "Tool D")]:
        panel(draw, (x, y, x + 180, y + 82), fill="panel", border="primary")
        text_block(draw, (x + 28, y + 24), label, size=30, bold=True)
    text_block(draw, (1240, 410), "Traits look predictive", size=44, color="text", bold=True)
    panel(draw, (1240, 560, 1680, 760), fill="panel_alt", border="secondary")
    text_block(draw, (1290, 610), "sunset archive", size=40, color="secondary", bold=True)
    text_block(draw, (1290, 672), "Discontinued peers omitted", size=30, color="muted")


def frame9_tools_oiu_breakout(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Tools O-I-U Breakout", "Survivor set vs hidden graveyard set")
    panel(draw, (170, 280, 940, 650), fill="panel_alt", border="primary")
    panel(draw, (980, 280, 1750, 650), fill="panel_alt", border="secondary")
    text_block(draw, (240, 340), "active survivors", size=44, color="primary", bold=True)
    text_block(draw, (1060, 340), "faded graveyard", size=44, color="secondary", bold=True)
    for x, y in [(260, 430), (430, 500), (600, 440), (760, 530)]:
        panel(draw, (x, y, x + 140, y + 70), fill="panel", border="primary")
    for x, y in [(1070, 430), (1230, 510), (1390, 450), (1550, 540)]:
        panel(draw, (x, y, x + 140, y + 70), fill="panel", border="line")
    rows = [
        ("Observed", "active survivors", "primary"),
        ("Inference", "trait causes success", "inference"),
        ("Unknown", "similar failed products", "secondary"),
    ]
    y = 700
    for label, body, color in rows:
        panel(draw, (170, y, 1750, y + 104), fill="panel_alt")
        tag(draw, (220, y + 30), label, color)
        text_block(draw, (500, y + 34), body, size=38)
        y += 116


def frame9_creator_advice_example(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Creator Advice Example", "Visible channels can hide silent attrition")
    panel(draw, (170, 280, 1750, 900), fill="panel")
    panel(draw, (240, 350, 980, 840), fill="panel_alt", border="primary")
    text_block(draw, (280, 390), "Visible channels analyzed", size=44, color="primary", bold=True)
    for i, label in enumerate(["Channel A", "Channel B", "Channel C"]):
        y0 = 490 + i * 110
        panel(draw, (290, y0, 920, y0 + 86), fill="panel", border="primary")
        text_block(draw, (330, y0 + 26), label, size=36, bold=True)
    panel(draw, (1060, 350, 1680, 840), fill="panel_alt", border="secondary")
    text_block(draw, (1120, 420), "Habits extracted", size=44, color="text", bold=True)
    text_block(draw, (1120, 520), "Silent failures missing", size=40, color="secondary", bold=True)
    for y in [610, 690, 770]:
        draw.line((1120, y, 1600, y), fill=PALETTE["muted"], width=5)


def frame9_creator_oiu_and_checklist(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Creator O-I-U and Checklist", "Turn example into verification routine")
    panel(draw, (160, 280, 940, 900), fill="panel")
    rows = [
        ("Observed", "visible channels analyzed", "primary"),
        ("Inference", "habits drive most outcomes", "inference"),
        ("Unknown", "non-survivor channel outcomes", "secondary"),
    ]
    y = 340
    for label, body, color in rows:
        panel(draw, (220, y, 880, y + 150), fill="panel_alt")
        tag(draw, (260, y + 52), label, color)
        text_block(draw, (500, y + 58), body, size=30)
        y += 170
    panel(draw, (980, 280, 1760, 900), fill="panel")
    steps = ["1 Start population", "2 Attrition", "3 Non-survivor source", "4 Possible vs typical", "5 O-I-U note"]
    y = 350
    for idx, step in enumerate(steps):
        fill = "primary" if idx == 0 else "secondary" if idx in (1, 2) else "inference" if idx == 3 else "ok"
        panel(draw, (1040, y, 1700, y + 90), fill="panel_alt", border=fill)
        text_block(draw, (1080, y + 28), step, size=34, bold=True)
        y += 106


def frame9_apply_checklist_fast(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Apply Checklist Fast", "One worksheet across founder / tools / creator")
    panel(draw, (170, 280, 1750, 900), fill="panel")
    panel(draw, (230, 350, 1690, 830), fill="panel_alt", border="line")
    headers = ["Case", "Status", "Boundary"]
    x_positions = [280, 760, 1210]
    for x, label in zip(x_positions, headers):
        text_block(draw, (x, 390), label, size=36, color="muted", bold=True)
    rows = [
        ("Case: winner-heavy claim", "Status: possibility shown", "Typicality unproven"),
        ("Founder / tools / creator", "Observed: survivors visible", "Need full denominator"),
    ]
    y = 470
    for row in rows:
        panel(draw, (260, y, 1660, y + 140), fill="panel")
        text_block(draw, (280, y + 34), row[0], size=34, color="primary", bold=True)
        text_block(draw, (760, y + 34), row[1], size=34, color="ok", bold=True)
        text_block(draw, (1210, y + 34), row[2], size=34, color="secondary", bold=True)
        y += 170
    text_block(draw, (300, 850), "Survivors show possibility, not prevalence.", size=38, color="inference", bold=True)


def frame9_closing_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Closing", "Bounded claim doctrine")
    panel(draw, (220, 320, 1700, 860), fill="panel_alt")
    text_block(draw, (300, 430), "Visible survivors are real evidence.", size=64, bold=True)
    text_block(draw, (340, 545), "They are not the whole distribution.", size=58, color="muted", bold=True)
    for x in [450, 760, 1080, 1390]:
        draw.ellipse((x - 20, 725, x + 20, 765), fill=PALETTE["primary"])
    for x in [330, 560, 650, 860, 960, 1180, 1270, 1510]:
        draw.ellipse((x - 12, 745, x + 12, 769), fill=PALETTE["muted"])
    text_block(draw, (530, 805), "Survivors show possibility, not prevalence.", size=34, color="secondary", bold=True)


VIDEO9_FRAMES: list[tuple[str, Callable[[Image.Image, ImageDraw.ImageDraw], None]]] = [
    ("01_title_card.png", frame9_title_card),
    ("02_winner_list_hook.png", frame9_winner_list_hook),
    ("03_possibility_vs_prevalence.png", frame9_possibility_vs_prevalence),
    ("04_survivorship_mechanism_rails.png", frame9_survivorship_mechanism_rails),
    ("05_founder_thread_example.png", frame9_founder_thread_example),
    ("06_founder_oiu_breakout.png", frame9_founder_oiu_breakout),
    ("07_current_tools_example.png", frame9_current_tools_example),
    ("08_tools_oiu_breakout.png", frame9_tools_oiu_breakout),
    ("09_creator_advice_example.png", frame9_creator_advice_example),
    ("10_creator_oiu_and_checklist.png", frame9_creator_oiu_and_checklist),
    ("11_apply_checklist_fast.png", frame9_apply_checklist_fast),
    ("12_closing_card.png", frame9_closing_card),
]


# Video 10 frames

def frame10_title_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "One Chart Is Not the Whole Story", "How Axis and Framing Choices Mislead")
    panel(draw, (170, 290, 1750, 860), fill="panel_alt")
    text_block(draw, (250, 410), "One chart can be accurate\nand still mislead by framing.", size=62, bold=True)
    tag(draw, (250, 650), "Observed", "primary")
    tag(draw, (470, 650), "Impression", "inference")
    tag(draw, (710, 650), "Unknown", "secondary")


def frame10_framework_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Observed / Impression / Unknown", "Use the same structure for each chart")
    rows = [
        ("Observed", "What the chart directly shows.", "primary"),
        ("Impression", "What the framing makes you feel is happening.", "inference"),
        ("Unknown", "Missing context before a stronger claim is justified.", "secondary"),
    ]
    y = 290
    for label, body, color in rows:
        panel(draw, (170, y, 1750, y + 210), fill="panel_alt")
        tag(draw, (220, y + 82), label, color)
        text_block(draw, (520, y + 84), body, size=40)
        y += 228


def frame10_example1_raw_values(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Example 1: Raw Values", "Month A 4.8% vs Month B 5.2%")
    panel(draw, (170, 270, 1750, 900), fill="panel")
    panel(draw, (230, 330, 1240, 860), fill="panel_alt", border="primary")
    draw.line((300, 780, 1140, 780), fill=PALETTE["line"], width=5)
    draw.line((300, 420, 300, 780), fill=PALETTE["line"], width=5)
    draw.rounded_rectangle((470, 492, 620, 780), radius=12, fill=PALETTE["primary"])
    draw.rounded_rectangle((780, 468, 930, 780), radius=12, fill=PALETTE["primary"])
    text_block(draw, (480, 812), "Month A\n4.8%", size=28, color="text", bold=True)
    text_block(draw, (790, 812), "Month B\n5.2%", size=28, color="text", bold=True)
    panel(draw, (1300, 380, 1700, 560), fill="panel_alt", border="secondary")
    text_block(draw, (1340, 430), "Difference:", size=38, color="muted", bold=True)
    text_block(draw, (1340, 486), "0.4 points", size=48, color="secondary", bold=True)
    tag(draw, (1300, 620), "Observed", "primary")
    tag(draw, (1520, 620), "Unknown", "secondary")


def frame10_example1_truncated_axis(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Same Values, Different Axis Start", "Axis Start: 4.6")
    left = (140, 280, 920, 900)
    right = (1000, 280, 1780, 900)
    panel(draw, left, fill="panel_alt", border="primary")
    panel(draw, right, fill="panel_alt", border="inference")

    draw.line((230, 810, 840, 810), fill=PALETTE["line"], width=4)
    draw.line((230, 370, 230, 810), fill=PALETTE["line"], width=4)
    draw.rounded_rectangle((390, 458, 510, 810), radius=10, fill=PALETTE["primary"])
    draw.rounded_rectangle((600, 428, 720, 810), radius=10, fill=PALETTE["primary"])
    text_block(draw, (250, 320), "Axis 0-6", size=30, color="primary", bold=True)

    draw.line((1090, 810, 1700, 810), fill=PALETTE["line"], width=4)
    draw.line((1090, 450, 1090, 810), fill=PALETTE["line"], width=4)
    draw.rounded_rectangle((1240, 650, 1360, 810), radius=10, fill=PALETTE["inference"])
    draw.rounded_rectangle((1450, 500, 1570, 810), radius=10, fill=PALETTE["inference"])
    text_block(draw, (1110, 400), "Axis 4.6-5.4", size=30, color="inference", bold=True)
    draw.ellipse((1410, 450, 1620, 840), outline=PALETTE["inference"], width=5)
    tag(draw, (1180, 318), "Axis Start", "secondary")
    text_block(draw, (1270, 322), "4.6", size=26, color="secondary", bold=True)


def frame10_example1_oiu_callout(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Example 1 O-I-U", "Axis choice changes impression, not values")
    rows = [
        ("Observed", "4.8% to 5.2%; Month B is higher.", "primary"),
        ("Impression", "Huge jump or collapse signal.", "inference"),
        ("Unknown", "Practical significance and normal variation.", "secondary"),
    ]
    y = 300
    for label, body, color in rows:
        panel(draw, (170, y, 1750, y + 200), fill="panel_alt")
        tag(draw, (220, y + 74), label, color)
        text_block(draw, (520, y + 80), body, size=42)
        y += 218


def frame10_example2_same_series(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Example 2: Same Weekly Series", "100, 101, 99, 102, 100, 101, 100, 102")
    panel(draw, (160, 280, 1760, 900), fill="panel")
    panel(draw, (230, 350, 1230, 840), fill="panel_alt", border="primary")
    draw.line((300, 780, 1160, 780), fill=PALETTE["line"], width=4)
    draw.line((300, 420, 300, 780), fill=PALETTE["line"], width=4)
    points = [(340, 640), (450, 610), (560, 670), (670, 580), (780, 640), (890, 610), (1000, 640), (1110, 580)]
    draw.line(tuple(v for p in points for v in p), fill=PALETTE["primary"], width=7)
    for x, y in points:
        draw.ellipse((x - 8, y - 8, x + 8, y + 8), fill=PALETTE["primary"])
    panel(draw, (1290, 390, 1710, 610), fill="panel_alt", border="secondary")
    text_block(draw, (1335, 450), "Same source\nvalues", size=44, color="secondary", bold=True)
    tag(draw, (1290, 660), "Observed", "primary")
    tag(draw, (1510, 660), "Unknown", "secondary")


def frame10_example2_time_window_pair(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Time Window Framing", "Short Window: urgent / Long Window: steady")
    left = (140, 280, 920, 900)
    right = (1000, 280, 1780, 900)
    panel(draw, left, fill="panel_alt", border="inference")
    panel(draw, right, fill="panel_alt", border="primary")

    draw.line((220, 810, 840, 810), fill=PALETTE["line"], width=4)
    draw.line((220, 420, 220, 810), fill=PALETTE["line"], width=4)
    short_pts = [(420, 700), (560, 620), (700, 520)]
    draw.line(tuple(v for p in short_pts for v in p), fill=PALETTE["inference"], width=9)
    for x, y in short_pts:
        draw.ellipse((x - 8, y - 8, x + 8, y + 8), fill=PALETTE["inference"])
    text_block(draw, (250, 350), "Short Window:\nurgent", size=36, color="inference", bold=True)
    tag(draw, (250, 742), "Time Window", "secondary")

    draw.line((1080, 810, 1700, 810), fill=PALETTE["line"], width=4)
    draw.line((1080, 420, 1080, 810), fill=PALETTE["line"], width=4)
    long_pts = [(1120, 670), (1210, 640), (1300, 700), (1390, 610), (1480, 670), (1570, 640), (1660, 670), (1710, 610)]
    draw.line(tuple(v for p in long_pts for v in p), fill=PALETTE["primary"], width=7)
    text_block(draw, (1110, 350), "Long Window:\nsteady", size=36, color="primary", bold=True)
    tag(draw, (1110, 742), "Time Window", "secondary")


def frame10_example2_scale_pair(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Scale Range Framing", "Tight Scale / Wide Scale / Same points")
    left = (140, 280, 920, 900)
    right = (1000, 280, 1780, 900)
    panel(draw, left, fill="panel_alt", border="inference")
    panel(draw, right, fill="panel_alt", border="primary")
    pts_left = [(260, 740), (360, 680), (460, 800), (560, 620), (660, 740), (760, 680), (860, 740), (900, 620)]
    pts_right = [(1120, 700), (1210, 690), (1300, 710), (1390, 685), (1480, 700), (1570, 690), (1660, 700), (1710, 685)]

    draw.line((220, 810, 840, 810), fill=PALETTE["line"], width=4)
    draw.line((220, 450, 220, 810), fill=PALETTE["line"], width=4)
    draw.line(tuple(v for p in pts_left for v in p), fill=PALETTE["inference"], width=8)
    text_block(draw, (250, 356), "Tight Scale\n99-102", size=34, color="inference", bold=True)
    tag(draw, (250, 742), "Scale Range", "secondary")

    draw.line((1080, 810, 1700, 810), fill=PALETTE["line"], width=4)
    draw.line((1080, 450, 1080, 810), fill=PALETTE["line"], width=4)
    draw.line(tuple(v for p in pts_right for v in p), fill=PALETTE["primary"], width=8)
    text_block(draw, (1110, 356), "Wide Scale\n0-120", size=34, color="primary", bold=True)
    tag(draw, (1110, 742), "Scale Range", "secondary")
    text_block(draw, (760, 930), "Same points", size=34, color="muted", bold=True)


def frame10_example3_cumulative_vs_rate(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Example 3: Cumulative vs Daily Rate", "Cumulative Total / Daily New Rate / ~40/day")
    left = (140, 280, 920, 900)
    right = (1000, 280, 1780, 900)
    panel(draw, left, fill="panel_alt", border="primary")
    panel(draw, right, fill="panel_alt", border="secondary")

    draw.line((220, 810, 840, 810), fill=PALETTE["line"], width=4)
    draw.line((220, 430, 220, 810), fill=PALETTE["line"], width=4)
    cumulative = [(260, 760), (360, 720), (460, 675), (560, 620), (660, 560), (760, 500), (860, 430)]
    draw.line(tuple(v for p in cumulative for v in p), fill=PALETTE["primary"], width=8)
    text_block(draw, (250, 360), "Cumulative Total", size=34, color="primary", bold=True)

    draw.line((1080, 810, 1700, 810), fill=PALETTE["line"], width=4)
    draw.line((1080, 430, 1080, 810), fill=PALETTE["line"], width=4)
    bars = [(1140, 690), (1220, 676), (1300, 698), (1380, 670), (1460, 686), (1540, 674), (1620, 692), (1700, 668)]
    for x, top in bars:
        draw.rounded_rectangle((x - 28, top, x + 28, 810), radius=8, fill=PALETTE["secondary"])
    text_block(draw, (1110, 360), "Daily New Rate\n~40/day", size=34, color="secondary", bold=True)
    tag(draw, (1120, 742), "Chart Type", "secondary")


def frame10_example3_oiu_callout(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Example 3 O-I-U", "Chart type can drive acceleration impression")
    rows = [
        ("Observed", "Cumulative total increases steadily.", "primary"),
        ("Impression", "Growth is speeding up.", "inference"),
        ("Unknown", "Underlying per-period rate trend.", "secondary"),
    ]
    y = 300
    for label, body, color in rows:
        panel(draw, (170, y, 1750, y + 200), fill="panel_alt")
        tag(draw, (220, y + 74), label, color)
        text_block(draw, (520, y + 80), body, size=42)
        y += 218
    tag(draw, (220, 912), "Chart Type", "secondary")


def frame10_verification_checklist(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Verification Checklist", "Five checks before accepting chart-level claims")
    steps = ["1 Axis", "2 Window", "3 Scale", "4 Chart Type", "5 O-I-U note"]
    y = 280
    for step in steps:
        panel(draw, (250, y, 1670, y + 132), fill="panel_alt")
        draw.ellipse((300, y + 44, 348, y + 92), fill=PALETTE["ok"])
        text_block(draw, (314, y + 48), "✓", size=24, color="bg", bold=True)
        text_block(draw, (390, y + 42), step, size=48)
        y += 144


def frame10_closing_card(img: Image.Image, draw: ImageDraw.ImageDraw) -> None:
    draw_header(draw, "Closing", "Framing check before interpretation")
    panel(draw, (220, 330, 1700, 860), fill="panel_alt")
    text_block(
        draw,
        (270, 500),
        "Real data can still support a distorted visual impression.",
        size=56,
        bold=True,
    )
    tag(draw, (620, 700), "Observed", "primary")
    tag(draw, (840, 700), "Impression", "inference")
    tag(draw, (1090, 700), "Unknown", "secondary")


VIDEO10_FRAMES: list[tuple[str, Callable[[Image.Image, ImageDraw.ImageDraw], None]]] = [
    ("01_title_card.png", frame10_title_card),
    ("02_framework_card.png", frame10_framework_card),
    ("03_example1_raw_values.png", frame10_example1_raw_values),
    ("04_example1_truncated_axis.png", frame10_example1_truncated_axis),
    ("05_example1_oiu_callout.png", frame10_example1_oiu_callout),
    ("06_example2_same_series.png", frame10_example2_same_series),
    ("07_example2_time_window_pair.png", frame10_example2_time_window_pair),
    ("08_example2_scale_pair.png", frame10_example2_scale_pair),
    ("09_example3_cumulative_vs_rate.png", frame10_example3_cumulative_vs_rate),
    ("10_example3_oiu_callout.png", frame10_example3_oiu_callout),
    ("11_verification_checklist.png", frame10_verification_checklist),
    ("12_closing_card.png", frame10_closing_card),
]

VIDEO_FRAMES = {
    "video1": VIDEO1_FRAMES,
    "video2": VIDEO2_FRAMES,
    "video3": VIDEO3_FRAMES,
    "video4": VIDEO4_FRAMES,
    "video5": VIDEO5_FRAMES,
    "video6": VIDEO6_FRAMES,
    "video7": VIDEO7_FRAMES,
    "video8": VIDEO8_FRAMES,
    "video9": VIDEO9_FRAMES,
    "video10": VIDEO10_FRAMES,
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
