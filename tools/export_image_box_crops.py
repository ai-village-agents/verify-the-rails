#!/usr/bin/env python3
"""Export labeled box crops into a local QC contact sheet."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import NamedTuple, Sequence

from PIL import Image, ImageColor, ImageDraw, ImageFont, ImageOps


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
            "Local QC helper only: export box crops as a dark-background contact "
            "sheet for box-by-box geometry checks."
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
        "--padding",
        type=int,
        default=0,
        help="Extra pixels around each box before cropping (default: 0).",
    )
    parser.add_argument(
        "--scale",
        type=int,
        default=2,
        help="Integer scale factor for crop rows (default: 2).",
    )
    parser.add_argument(
        "--font-size",
        type=int,
        default=14,
        help="Preferred label font size (default: 14).",
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
    if input_path.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
        raise ValueError(
            f"Input image must end in .png, .jpg, or .jpeg (got: {input_path})"
        )

    if not args.output.lower().endswith(".png"):
        raise ValueError(f"Output path must be a .png file: {args.output}")

    if not args.box:
        raise ValueError("At least one --box is required.")

    if args.padding < 0:
        raise ValueError(f"--padding must be >= 0 (got {args.padding})")
    if args.scale <= 0:
        raise ValueError(f"--scale must be > 0 (got {args.scale})")
    if args.font_size <= 0:
        raise ValueError(f"--font-size must be > 0 (got {args.font_size})")

    return parse_box_specs(args.box)


def load_font(font_size: int) -> ImageFont.ImageFont:
    font = ImageFont.load_default()
    if hasattr(font, "font_variant"):
        try:
            return font.font_variant(size=font_size)
        except (TypeError, OSError, ValueError):
            return font
    return font


def _nearest_resample() -> int:
    try:
        return Image.Resampling.NEAREST  # Pillow >= 9
    except AttributeError:
        return Image.NEAREST


def _label_text(box: BoxSpec) -> str:
    return f"{box.label} ({box.x1},{box.y1})-({box.x2},{box.y2})"


def export_crop_sheet(
    image: Image.Image,
    boxes: Sequence[BoxSpec],
    *,
    padding: int,
    scale: int,
    font_size: int,
) -> Image.Image:
    source = image.convert("RGB")
    font = load_font(font_size)

    background = (18, 18, 18)
    text_color = (255, 255, 255)
    horizontal_padding = 12
    vertical_padding = 12
    label_to_image_gap = 6
    row_gap = 12
    border_width = 2

    rows: list[tuple[str, Image.Image, int, int]] = []
    max_row_width = 0
    total_row_height = 0

    for box in boxes:
        left = max(0, box.x1 - padding)
        top = max(0, box.y1 - padding)
        right = min(source.width, box.x2 + padding)
        bottom = min(source.height, box.y2 + padding)

        if right <= left or bottom <= top:
            raise ValueError(
                "Invalid --box crop region after padding/clipping; no pixels remain "
                f"for box: {box.label}"
            )

        crop = source.crop((left, top, right, bottom))
        scaled = crop.resize(
            (crop.width * scale, crop.height * scale),
            resample=_nearest_resample(),
        )
        bordered = ImageOps.expand(scaled, border=border_width, fill=box.color_rgb)

        row_label = _label_text(box)
        temp_draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))
        label_bbox = temp_draw.textbbox((0, 0), row_label, font=font)
        label_height = label_bbox[3] - label_bbox[1]
        label_width = label_bbox[2] - label_bbox[0]

        row_width = max(label_width, bordered.width)
        row_height = label_height + label_to_image_gap + bordered.height

        rows.append((row_label, bordered, label_height, row_height))
        max_row_width = max(max_row_width, row_width)
        total_row_height += row_height

    if len(rows) > 1:
        total_row_height += row_gap * (len(rows) - 1)

    out_width = max_row_width + (horizontal_padding * 2)
    out_height = total_row_height + (vertical_padding * 2)

    sheet = Image.new("RGB", (out_width, out_height), background)
    draw = ImageDraw.Draw(sheet)

    y = vertical_padding
    for row_label, bordered, label_height, row_height in rows:
        x = horizontal_padding
        draw.text((x, y), row_label, fill=text_color, font=font)
        image_y = y + label_height + label_to_image_gap
        sheet.paste(bordered, (x, image_y))
        y += row_height + row_gap

    return sheet


def export_file(
    input_image: str,
    output: str,
    boxes: Sequence[BoxSpec],
    *,
    padding: int,
    scale: int,
    font_size: int,
) -> None:
    input_path = Path(input_image)
    output_path = Path(output)

    try:
        with Image.open(input_path) as image:
            sheet = export_crop_sheet(
                image,
                boxes,
                padding=padding,
                scale=scale,
                font_size=font_size,
            )
    except OSError as exc:
        raise OSError(f"Failed to read image '{input_path}': {exc}") from exc

    output_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output_path, format="PNG")


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        boxes = validate_args(args)
        export_file(
            args.input_image,
            args.output,
            boxes,
            padding=args.padding,
            scale=args.scale,
            font_size=args.font_size,
        )
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
