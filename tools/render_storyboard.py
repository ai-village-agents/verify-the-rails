#!/usr/bin/env python3
"""Render placeholder storyboard frames for Video 1.

Outputs 1920x1080 PNG files to videos/video1/storyboard_frames/.
"""

from __future__ import annotations

from pathlib import Path
from typing import Callable

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1920, 1080
OUT_DIR = Path("videos/video1/storyboard_frames")

PALETTE = {
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
}


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
    points = [(260, "8:00", "Primary: June 1", "primary"), (700, "9:15", "Newsletter mirrors", "secondary"), (1140, "11:40", "Updated: July 1", "ok"), (1580, "1:20", "Blog shows old", "inference")]
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
    text_block(draw, (250, 470), "Viewer reports:\n\"I saw June 1\"", size=44)
    text_block(draw, (1110, 470), "Viewer reports:\n\"I saw July 1\"", size=44)


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


FRAMES: list[tuple[str, Callable[[Image.Image, ImageDraw.ImageDraw], None]]] = [
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


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, painter in FRAMES:
        img, draw = base_canvas()
        painter(img, draw)
        out_path = OUT_DIR / name
        img.save(out_path, format="PNG")
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
