#!/usr/bin/env python3
"""Render a restrained editorial thumbnail for Video 1."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1280, 720
OUT_PATH = Path("videos/video1/video1_thumbnail.png")

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


def draw_editorial_background(draw: ImageDraw.ImageDraw) -> None:
    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=PALETTE["bg"])
    draw.rectangle((36, 36, WIDTH - 36, HEIGHT - 36), outline=PALETTE["line"], width=2)
    draw.line((84, 124, WIDTH - 84, 124), fill=PALETTE["line"], width=2)


def draw_split_cards(draw: ImageDraw.ImageDraw) -> None:
    left = (84, 188, 608, 610)
    right = (672, 188, 1196, 610)
    draw.rounded_rectangle(left, radius=18, fill=PALETTE["panel"], outline=PALETTE["inference"], width=3)
    draw.rounded_rectangle(right, radius=18, fill=PALETTE["panel"], outline=PALETTE["ok"], width=3)

    label_font = load_font(29, bold=True)
    body_font = load_font(34, bold=True)
    meta_font = load_font(23)

    draw.text((120, 220), "Screenshot A", font=label_font, fill=PALETTE["muted"])
    draw.text((120, 280), "Free admission ends", font=body_font, fill=PALETTE["text"])
    draw.text((120, 328), "June 1", font=load_font(56, bold=True), fill=PALETTE["inference"])
    draw.text((120, 560), "Captured 9:14 AM", font=meta_font, fill=PALETTE["muted"])

    draw.text((708, 220), "Screenshot B", font=label_font, fill=PALETTE["muted"])
    draw.text((708, 280), "Free admission extended", font=body_font, fill=PALETTE["text"])
    draw.text((708, 328), "through July 1", font=load_font(56, bold=True), fill=PALETTE["ok"])
    draw.text((708, 560), "Captured 2:37 PM", font=meta_font, fill=PALETTE["muted"])


def draw_type(draw: ImageDraw.ImageDraw) -> None:
    headline_font = load_font(84, bold=True)
    support_font = load_font(34)

    headline = "Two True Screenshots"
    support = "Same claim, different source timing and delivery path."

    draw.text((84, 34), headline, font=headline_font, fill=PALETTE["text"])
    draw.text((87, 636), support, font=support_font, fill=PALETTE["muted"])


def render_thumbnail() -> Path:
    image = Image.new("RGB", (WIDTH, HEIGHT), PALETTE["bg"])
    draw = ImageDraw.Draw(image)

    draw_editorial_background(draw)
    draw_split_cards(draw)
    draw_type(draw)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUT_PATH)
    return OUT_PATH


if __name__ == "__main__":
    output = render_thumbnail()
    print(f"Wrote {output}")
