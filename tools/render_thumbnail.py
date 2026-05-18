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
    else:
        draw_video2_thumbnail(draw, palette)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(out_path)
    return out_path


if __name__ == "__main__":
    args = parse_args()
    output = render_thumbnail(args.video)
    print(f"Wrote {output}")
