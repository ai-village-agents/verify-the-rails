#!/usr/bin/env python3
"""Render a restrained editorial thumbnail for a selected video."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1280, 720

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


def draw_editorial_background(draw: ImageDraw.ImageDraw, palette: dict[str, str]) -> None:
    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=palette["bg"])
    draw.rectangle((36, 36, WIDTH - 36, HEIGHT - 36), outline=palette["line"], width=2)
    draw.line((84, 124, WIDTH - 84, 124), fill=palette["line"], width=2)


def draw_video1_thumbnail(draw: ImageDraw.ImageDraw, palette: dict[str, str]) -> None:
    left = (84, 188, 608, 610)
    right = (672, 188, 1196, 610)
    draw.rounded_rectangle(left, radius=18, fill=palette["panel"], outline=palette["inference"], width=3)
    draw.rounded_rectangle(right, radius=18, fill=palette["panel"], outline=palette["ok"], width=3)

    label_font = load_font(29, bold=True)
    body_font = load_font(34, bold=True)
    meta_font = load_font(23)

    draw.text((120, 220), "Screenshot A", font=label_font, fill=palette["muted"])
    draw.text((120, 280), "Free admission ends", font=body_font, fill=palette["text"])
    draw.text((120, 328), "June 1", font=load_font(56, bold=True), fill=palette["inference"])
    draw.text((120, 560), "Captured 9:14 AM", font=meta_font, fill=palette["muted"])

    draw.text((708, 220), "Screenshot B", font=label_font, fill=palette["muted"])
    draw.text((708, 280), "Free admission extended", font=body_font, fill=palette["text"])
    draw.text((708, 328), "through July 1", font=load_font(56, bold=True), fill=palette["ok"])
    draw.text((708, 560), "Captured 2:37 PM", font=meta_font, fill=palette["muted"])

    draw.text((84, 34), "Two True Screenshots", font=load_font(84, bold=True), fill=palette["text"])
    draw.text(
        (87, 636),
        "Same claim, different source timing and delivery path.",
        font=load_font(34),
        fill=palette["muted"],
    )


def draw_video2_thumbnail(draw: ImageDraw.ImageDraw, palette: dict[str, str]) -> None:
    left = (84, 188, 608, 610)
    right = (672, 188, 1196, 610)
    draw.rounded_rectangle(left, radius=18, fill=palette["panel"], outline=palette["inference"], width=3)
    draw.rounded_rectangle(right, radius=18, fill=palette["panel"], outline=palette["ok"], width=3)

    draw.text((120, 220), "10:02 AM PT", font=load_font(30, bold=True), fill=palette["inference"])
    draw.text((120, 282), "Line A resumes", font=load_font(42, bold=True), fill=palette["text"])
    draw.text((120, 336), "at 12:00 PM", font=load_font(54, bold=True), fill=palette["inference"])
    draw.text((120, 560), "US-West edge", font=load_font(24), fill=palette["muted"])

    draw.text((708, 220), "10:03 AM PT", font=load_font(30, bold=True), fill=palette["ok"])
    draw.text((708, 282), "Line A remains", font=load_font(42, bold=True), fill=palette["text"])
    draw.text((708, 336), "suspended", font=load_font(54, bold=True), fill=palette["ok"])
    draw.text((708, 560), "US-East edge", font=load_font(24), fill=palette["muted"])

    draw.text((84, 34), "Same URL, Different Answer", font=load_font(72, bold=True), fill=palette["text"])
    draw.text(
        (87, 636),
        "Cache, rollout, and edge timing can disagree briefly.",
        font=load_font(34),
        fill=palette["muted"],
    )


def draw_video3_thumbnail(draw: ImageDraw.ImageDraw, palette: dict[str, str]) -> None:
    left = (84, 188, 608, 610)
    right = (672, 188, 1196, 610)
    draw.rounded_rectangle(left, radius=18, fill=palette["panel"], outline=palette["primary"], width=3)
    draw.rounded_rectangle(right, radius=18, fill=palette["panel"], outline=palette["inference"], width=3)

    draw.text((120, 220), "Source wording", font=load_font(29, bold=True), fill=palette["muted"])
    draw.text((120, 278), '"associated with"', font=load_font(52, bold=True), fill=palette["primary"])
    draw.text((120, 346), "higher complaints", font=load_font(38, bold=True), fill=palette["text"])
    draw.text((120, 560), "Cautious claim", font=load_font(24), fill=palette["muted"])

    draw.text((708, 220), "Summary wording", font=load_font(29, bold=True), fill=palette["muted"])
    draw.text((708, 278), '"proves" / "causes"', font=load_font(52, bold=True), fill=palette["inference"])
    draw.text((708, 346), "stronger certainty", font=load_font(38, bold=True), fill=palette["text"])
    draw.text((708, 560), "Stronger claim", font=load_font(24), fill=palette["muted"])

    draw.text((84, 34), "When Summaries Drift", font=load_font(80, bold=True), fill=palette["text"])
    draw.text(
        (87, 636),
        "Compare exact phrases before you share.",
        font=load_font(34),
        fill=palette["muted"],
    )


def draw_video4_thumbnail(draw: ImageDraw.ImageDraw, palette: dict[str, str]) -> None:
    left = (84, 188, 608, 610)
    right = (672, 188, 1196, 610)
    draw.rounded_rectangle(left, radius=18, fill=palette["panel"], outline=palette["inference"], width=3)
    draw.rounded_rectangle(right, radius=18, fill=palette["panel"], outline=palette["ok"], width=3)

    draw.text((120, 220), "Scholarship Page", font=load_font(29, bold=True), fill=palette["muted"])
    draw.text((120, 276), "Applications close", font=load_font(40, bold=True), fill=palette["text"])
    draw.text((120, 334), "May 1", font=load_font(72, bold=True), fill=palette["inference"])
    draw.text((120, 560), "Authentic capture", font=load_font(24), fill=palette["secondary"])

    draw.text((708, 220), "Scholarship Page", font=load_font(29, bold=True), fill=palette["muted"])
    draw.text((708, 276), "Applications close", font=load_font(40, bold=True), fill=palette["text"])
    draw.text((708, 334), "May 15", font=load_font(72, bold=True), fill=palette["ok"])
    draw.text((708, 560), "Authentic capture", font=load_font(24), fill=palette["secondary"])

    draw.text((84, 34), "This Was True Yesterday", font=load_font(78, bold=True), fill=palette["text"])
    draw.text(
        (87, 636),
        "A real screenshot can still be outdated.",
        font=load_font(34),
        fill=palette["muted"],
    )


def draw_video5_thumbnail(draw: ImageDraw.ImageDraw, palette: dict[str, str]) -> None:
    crop_box = (84, 188, 560, 610)
    reveal_box = (600, 188, 1196, 610)
    draw.rounded_rectangle(crop_box, radius=18, fill=palette["panel"], outline=palette["secondary"], width=3)
    draw.rounded_rectangle(reveal_box, radius=18, fill=palette["panel"], outline=palette["primary"], width=3)

    draw.text((114, 220), "Inside crop", font=load_font(28, bold=True), fill=palette["secondary"])
    draw.text((114, 310), "24,000 users", font=load_font(72, bold=True), fill=palette["secondary"])

    draw.text((632, 220), "Outside crop", font=load_font(28, bold=True), fill=palette["primary"])
    draw.text((632, 296), "24,000 users", font=load_font(58, bold=True), fill=palette["text"])
    draw.rounded_rectangle((632, 392, 1132, 478), radius=12, fill=palette["panel_alt"], outline=palette["primary"], width=2)
    draw.text((660, 414), "Filter: Last 24 hours", font=load_font(40, bold=True), fill=palette["primary"])

    draw.text((84, 34), "The Crop Hides the Clue", font=load_font(78, bold=True), fill=palette["text"])
    draw.text((87, 636), "Real screenshot. Missing context.", font=load_font(34), fill=palette["muted"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a video thumbnail.")
    parser.add_argument(
        "--video",
        default="video1",
        choices=sorted(PALETTES.keys()),
        help="Video directory name under videos/ (default: video1)",
    )
    return parser.parse_args()


def render_thumbnail(video: str) -> Path:
    palette = PALETTES[video]
    out_path = Path("videos") / video / f"{video}_thumbnail.png"

    image = Image.new("RGB", (WIDTH, HEIGHT), palette["bg"])
    draw = ImageDraw.Draw(image)

    draw_editorial_background(draw, palette)
    if video == "video1":
        draw_video1_thumbnail(draw, palette)
    elif video == "video2":
        draw_video2_thumbnail(draw, palette)
    elif video == "video3":
        draw_video3_thumbnail(draw, palette)
    elif video == "video4":
        draw_video4_thumbnail(draw, palette)
    elif video == "video5":
        draw_video5_thumbnail(draw, palette)
    else:
        raise ValueError(f"Unsupported video: {video}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(out_path)
    return out_path


if __name__ == "__main__":
    args = parse_args()
    output = render_thumbnail(args.video)
    print(f"Wrote {output}")
