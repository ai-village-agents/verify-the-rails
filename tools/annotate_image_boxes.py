#!/usr/bin/env python3
"""Draw labeled rectangles on a still image for local geometry/coverage QC."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import NamedTuple, Sequence

from PIL import Image, ImageColor, ImageDraw, ImageFont


class BoxSpec(NamedTuple):
    x1: int
    y1: int
    x2: int
    y2: int
    label: str
    color: str
    color_rgb: tuple[int, int, int]


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Local QC helper only: draw labeled rectangle overlays on a still image "
            "for geometry/coverage review."
        )
    )
    parser.add_argument("input_image", help="Input image path (.png/.jpg/.jpeg).")
    parser.add_argument("--output", required=True, help="Output PNG path.")
    parser.add_argument(
        "--box",
        action="append",
        default=[],
        help=(
            "Repeatable box spec: x1,y1,x2,y2,label,color "
            "(example: 10,20,130,90,title,#00ff00)"
        ),
    )
    parser.add_argument(
        "--line-width",
        type=int,
        default=3,
        help="Rectangle outline width in pixels (default: 3).",
    )
    parser.add_argument(
        "--font-size",
        type=int,
        default=14,
        help=(
            "Preferred label font size (default: 14). "
            "Best effort with Pillow default font."
        ),
    )
    return parser.parse_args(argv)


def parse_box_spec(spec: str) -> BoxSpec:
    parts = spec.split(",", 5)
    if len(parts) != 6:
        raise ValueError(
            "Invalid --box format; expected x1,y1,x2,y2,label,color "
            f"(got: {spec})"
        )

    x1_text, y1_text, x2_text, y2_text, label, color = parts

    try:
        x1 = int(x1_text)
        y1 = int(y1_text)
        x2 = int(x2_text)
        y2 = int(y2_text)
    except ValueError as exc:
        raise ValueError(f"Invalid --box coordinates; expected integers (got: {spec})") from exc

    if not label:
        raise ValueError(f"Invalid --box label; label must be non-empty (got: {spec})")

    if x2 <= x1:
        raise ValueError(f"Invalid --box coordinates; x2 must be > x1 (got: {spec})")
    if y2 <= y1:
        raise ValueError(f"Invalid --box coordinates; y2 must be > y1 (got: {spec})")

    try:
        color_rgb = ImageColor.getrgb(color)
    except ValueError as exc:
        raise ValueError(f"Invalid --box color: {color}") from exc

    return BoxSpec(x1=x1, y1=y1, x2=x2, y2=y2, label=label, color=color, color_rgb=color_rgb)


def parse_box_specs(specs: Sequence[str]) -> list[BoxSpec]:
    return [parse_box_spec(spec) for spec in specs]


def validate_args(args: argparse.Namespace) -> list[BoxSpec]:
    input_path = Path(args.input_image)
    if not input_path.exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")
    if not input_path.is_file():
        raise ValueError(f"Input image path is not a file: {input_path}")

    if not args.output.lower().endswith(".png"):
        raise ValueError(f"Output path must be a .png file: {args.output}")

    if args.line_width <= 0:
        raise ValueError(f"--line-width must be > 0 (got {args.line_width})")
    if args.font_size <= 0:
        raise ValueError(f"--font-size must be > 0 (got {args.font_size})")

    if not args.box:
        raise ValueError("At least one --box is required.")

    return parse_box_specs(args.box)


def load_font(font_size: int) -> ImageFont.ImageFont:
    font = ImageFont.load_default()
    if hasattr(font, "font_variant"):
        try:
            return font.font_variant(size=font_size)
        except (TypeError, OSError, ValueError):
            return font
    return font


def annotate_image(
    image: Image.Image,
    boxes: Sequence[BoxSpec],
    *,
    line_width: int,
    font_size: int,
) -> Image.Image:
    annotated = image.convert("RGB")
    draw = ImageDraw.Draw(annotated)
    font = load_font(font_size)

    for box in boxes:
        draw.rectangle((box.x1, box.y1, box.x2, box.y2), outline=box.color_rgb, width=line_width)

        text_bbox = draw.textbbox((0, 0), box.label, font=font)
        text_w = text_bbox[2] - text_bbox[0]
        text_h = text_bbox[3] - text_bbox[1]

        text_x = max(0, box.x1 + 2)
        text_y = max(0, box.y1 + 2)
        bg_left = max(0, text_x - 1)
        bg_top = max(0, text_y - 1)
        bg_right = min(annotated.width, text_x + text_w + 1)
        bg_bottom = min(annotated.height, text_y + text_h + 1)

        if bg_right > bg_left and bg_bottom > bg_top:
            draw.rectangle((bg_left, bg_top, bg_right, bg_bottom), fill=box.color_rgb)
        draw.text((text_x, text_y), box.label, fill=(255, 255, 255), font=font)

    return annotated


def annotate_file(
    input_image: str,
    output: str,
    boxes: Sequence[BoxSpec],
    *,
    line_width: int,
    font_size: int,
) -> None:
    input_path = Path(input_image)
    output_path = Path(output)

    try:
        with Image.open(input_path) as image:
            annotated = annotate_image(
                image,
                boxes,
                line_width=line_width,
                font_size=font_size,
            )
    except OSError as exc:
        raise OSError(f"Failed to read image '{input_path}': {exc}") from exc

    output_path.parent.mkdir(parents=True, exist_ok=True)
    annotated.save(output_path, format="PNG")


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        boxes = validate_args(args)
        annotate_file(
            args.input_image,
            args.output,
            boxes,
            line_width=args.line_width,
            font_size=args.font_size,
        )
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
