#!/usr/bin/env python3
"""Compare repeated box crops across multiple still images for local QC."""

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
            "Local QC helper only: compare repeated box crops across multiple still "
            "images in one dark-background PNG sheet."
        )
    )
    parser.add_argument(
        "input_images",
        nargs="+",
        help="Two or more input image paths (.png/.jpg/.jpeg).",
    )
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
        help="Integer scale factor for crops (default: 2).",
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
    if len(args.input_images) < 2:
        raise ValueError("At least two input images are required.")

    for input_image in args.input_images:
        path = Path(input_image)
        if not path.exists():
            raise FileNotFoundError(f"Input image not found: {path}")
        if not path.is_file():
            raise ValueError(f"Input image path is not a file: {path}")
        if path.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
            raise ValueError(
                f"Input image must end in .png, .jpg, or .jpeg (got: {path})"
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
        return Image.Resampling.NEAREST
    except AttributeError:
        return Image.NEAREST


def _box_label(box: BoxSpec) -> str:
    return f"{box.label} ({box.x1},{box.y1})-({box.x2},{box.y2})"


def _stem_label(path: Path) -> str:
    return path.stem


def compare_crop_sheet(
    images: Sequence[tuple[Path, Image.Image]],
    boxes: Sequence[BoxSpec],
    *,
    padding: int,
    scale: int,
    font_size: int,
) -> Image.Image:
    font = load_font(font_size)
    source_images = [(path, image.convert("RGB")) for path, image in images]

    background = (18, 18, 18)
    text_color = (255, 255, 255)
    horizontal_padding = 12
    vertical_padding = 12
    section_gap = 14
    row_label_gap = 6
    stem_gap = 4
    column_gap = 10
    border_width = 2

    probe_draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))

    sections: list[tuple[str, int, list[tuple[str, Image.Image, int, int]], int, int]] = []
    max_sheet_width = 0
    total_sheet_height = 0

    for box in boxes:
        header_text = _box_label(box)
        header_bbox = probe_draw.textbbox((0, 0), header_text, font=font)
        header_height = header_bbox[3] - header_bbox[1]
        header_width = header_bbox[2] - header_bbox[0]

        cells: list[tuple[str, Image.Image, int, int]] = []
        row_width = 0
        row_height = 0

        for image_path, source in source_images:
            left = max(0, box.x1 - padding)
            top = max(0, box.y1 - padding)
            right = min(source.width, box.x2 + padding)
            bottom = min(source.height, box.y2 + padding)

            if right <= left or bottom <= top:
                raise ValueError(
                    "Invalid --box crop region after padding/clipping; no pixels remain "
                    f"for box '{box.label}' in input: {image_path}"
                )

            crop = source.crop((left, top, right, bottom))
            scaled = crop.resize(
                (crop.width * scale, crop.height * scale),
                resample=_nearest_resample(),
            )
            bordered = ImageOps.expand(scaled, border=border_width, fill=box.color_rgb)

            stem = _stem_label(image_path)
            stem_bbox = probe_draw.textbbox((0, 0), stem, font=font)
            stem_width = stem_bbox[2] - stem_bbox[0]
            stem_height = stem_bbox[3] - stem_bbox[1]

            cell_width = max(stem_width, bordered.width)
            cell_height = stem_height + stem_gap + bordered.height
            cells.append((stem, bordered, cell_width, stem_height))

            row_width += cell_width
            row_height = max(row_height, cell_height)

        if len(cells) > 1:
            row_width += column_gap * (len(cells) - 1)

        section_width = max(header_width, row_width)
        section_height = header_height + row_label_gap + row_height
        sections.append((header_text, header_height, cells, section_width, section_height))

        max_sheet_width = max(max_sheet_width, section_width)
        total_sheet_height += section_height

    if len(sections) > 1:
        total_sheet_height += section_gap * (len(sections) - 1)

    out_width = max_sheet_width + horizontal_padding * 2
    out_height = total_sheet_height + vertical_padding * 2

    sheet = Image.new("RGB", (out_width, out_height), background)
    draw = ImageDraw.Draw(sheet)

    y = vertical_padding
    for header_text, header_height, cells, _, section_height in sections:
        draw.text((horizontal_padding, y), header_text, fill=text_color, font=font)

        row_top = y + header_height + row_label_gap
        x = horizontal_padding
        for stem, bordered, cell_width, stem_height in cells:
            draw.text((x, row_top), stem, fill=text_color, font=font)
            crop_x = x + (cell_width - bordered.width) // 2
            crop_y = row_top + stem_height + stem_gap
            sheet.paste(bordered, (crop_x, crop_y))
            x += cell_width + column_gap

        y += section_height + section_gap

    return sheet


def export_file(
    input_images: Sequence[str],
    output: str,
    boxes: Sequence[BoxSpec],
    *,
    padding: int,
    scale: int,
    font_size: int,
) -> None:
    output_path = Path(output)

    opened: list[Image.Image] = []
    images: list[tuple[Path, Image.Image]] = []
    try:
        for input_image in input_images:
            path = Path(input_image)
            try:
                image = Image.open(path)
            except OSError as exc:
                raise OSError(f"Failed to read image '{path}': {exc}") from exc
            opened.append(image)
            images.append((path, image))

        sheet = compare_crop_sheet(
            images,
            boxes,
            padding=padding,
            scale=scale,
            font_size=font_size,
        )
    finally:
        for image in opened:
            image.close()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output_path, format="PNG")


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        boxes = validate_args(args)
        export_file(
            args.input_images,
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
