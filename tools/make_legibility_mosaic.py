#!/usr/bin/env python3
"""Build a deterministic contact-sheet PNG for small-player frame legibility review."""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path
from typing import Sequence

from PIL import Image, ImageColor, ImageDraw, ImageFont


DEFAULT_GLOB = "*.png"


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Local QC helper only: build a contact-sheet PNG from frame images "
            "for small-player legibility review."
        )
    )
    parser.add_argument(
        "images",
        nargs="*",
        help="Explicit input image paths. If provided, they are sorted lexicographically.",
    )
    parser.add_argument(
        "--input-dir",
        help="Directory containing input images. Use with --glob (default: '*.png').",
    )
    parser.add_argument(
        "--glob",
        default=DEFAULT_GLOB,
        help="Glob pattern used with --input-dir (default: '*.png').",
    )
    parser.add_argument("--output", required=True, help="Output PNG path.")
    parser.add_argument("--columns", type=int, default=4, help="Number of columns.")
    parser.add_argument("--cell-width", type=int, default=320, help="Cell width in pixels.")
    parser.add_argument("--cell-height", type=int, default=180, help="Cell height in pixels.")
    parser.add_argument("--margin", type=int, default=16, help="Outer margin in pixels.")
    parser.add_argument("--gap", type=int, default=8, help="Gap between cells in pixels.")
    parser.add_argument(
        "--bg-color",
        default="#111111",
        help="Background color for sheet and letterbox bars.",
    )
    parser.add_argument(
        "--label-height",
        type=int,
        default=16,
        help="Label area height below each cell in pixels.",
    )
    return parser.parse_args(argv)


def validate_args(args: argparse.Namespace) -> None:
    if args.input_dir and args.images:
        raise ValueError("Use either --input-dir/--glob or explicit image paths, not both.")
    if not args.input_dir and not args.images:
        raise ValueError("No input images specified. Provide --input-dir or positional paths.")
    if not args.output.lower().endswith(".png"):
        raise ValueError(f"Output path must be a .png file: {args.output}")

    positive_fields = [
        ("--columns", args.columns),
        ("--cell-width", args.cell_width),
        ("--cell-height", args.cell_height),
    ]
    for flag, value in positive_fields:
        if value <= 0:
            raise ValueError(f"{flag} must be > 0 (got {value})")

    nonnegative_fields = [
        ("--margin", args.margin),
        ("--gap", args.gap),
        ("--label-height", args.label_height),
    ]
    for flag, value in nonnegative_fields:
        if value < 0:
            raise ValueError(f"{flag} must be >= 0 (got {value})")


def resolve_input_paths(
    explicit_paths: Sequence[str],
    input_dir: str | None,
    glob_pattern: str,
) -> list[Path]:
    if input_dir:
        directory = Path(input_dir)
        if not directory.exists():
            raise FileNotFoundError(f"Input directory not found: {directory}")
        if not directory.is_dir():
            raise NotADirectoryError(f"Input directory path is not a directory: {directory}")
        paths = sorted(path for path in directory.glob(glob_pattern) if path.is_file())
    else:
        paths = sorted(Path(path) for path in explicit_paths)

    if not paths:
        raise ValueError("No input images found.")
    return paths


def _resize_with_letterbox(image: Image.Image, cell_width: int, cell_height: int) -> Image.Image:
    src_w, src_h = image.size
    if src_w <= 0 or src_h <= 0:
        raise ValueError("Input image has invalid dimensions.")

    scale = min(cell_width / src_w, cell_height / src_h)
    resized_w = max(1, int(round(src_w * scale)))
    resized_h = max(1, int(round(src_h * scale)))
    resized = image.resize((resized_w, resized_h), Image.Resampling.LANCZOS)

    canvas = Image.new("RGB", (cell_width, cell_height))
    offset_x = (cell_width - resized_w) // 2
    offset_y = (cell_height - resized_h) // 2
    canvas.paste(resized, (offset_x, offset_y))
    return canvas


def build_mosaic_image(
    input_paths: Sequence[Path],
    *,
    columns: int,
    cell_width: int,
    cell_height: int,
    margin: int,
    gap: int,
    bg_color: str,
    label_height: int,
) -> Image.Image:
    if not input_paths:
        raise ValueError("No input images found.")

    try:
        bg_rgb = ImageColor.getrgb(bg_color)
    except ValueError as exc:
        raise ValueError(f"Invalid --bg-color: {bg_color}") from exc

    rows = math.ceil(len(input_paths) / columns)
    mosaic_width = (margin * 2) + (columns * cell_width) + (max(0, columns - 1) * gap)
    tile_height = cell_height + label_height
    mosaic_height = (margin * 2) + (rows * tile_height) + (max(0, rows - 1) * gap)

    mosaic = Image.new("RGB", (mosaic_width, mosaic_height), color=bg_rgb)
    draw = ImageDraw.Draw(mosaic)
    font = ImageFont.load_default()
    text_color = (240, 240, 240)

    for index, path in enumerate(input_paths):
        col = index % columns
        row = index // columns
        origin_x = margin + (col * (cell_width + gap))
        origin_y = margin + (row * (tile_height + gap))

        try:
            with Image.open(path) as src:
                frame = _resize_with_letterbox(src.convert("RGB"), cell_width, cell_height)
        except OSError as exc:
            raise OSError(f"Failed to read image '{path}': {exc}") from exc

        frame_bg = Image.new("RGB", (cell_width, cell_height), color=bg_rgb)
        frame_bg.paste(frame, (0, 0))
        mosaic.paste(frame_bg, (origin_x, origin_y))

        if label_height > 0:
            label = path.stem
            text_bbox = draw.textbbox((0, 0), label, font=font)
            text_w = text_bbox[2] - text_bbox[0]
            text_h = text_bbox[3] - text_bbox[1]
            text_x = origin_x + max(2, (cell_width - text_w) // 2)
            text_y = origin_y + cell_height + max(0, (label_height - text_h) // 2)
            draw.text((text_x, text_y), label, fill=text_color, font=font)

    return mosaic


def make_mosaic(
    explicit_paths: Sequence[str],
    *,
    input_dir: str | None,
    glob_pattern: str,
    output: str,
    columns: int,
    cell_width: int,
    cell_height: int,
    margin: int,
    gap: int,
    bg_color: str,
    label_height: int,
) -> None:
    input_paths = resolve_input_paths(explicit_paths, input_dir, glob_pattern)
    mosaic = build_mosaic_image(
        input_paths,
        columns=columns,
        cell_width=cell_width,
        cell_height=cell_height,
        margin=margin,
        gap=gap,
        bg_color=bg_color,
        label_height=label_height,
    )

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    mosaic.save(output_path, format="PNG")


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        validate_args(args)
        make_mosaic(
            args.images,
            input_dir=args.input_dir,
            glob_pattern=args.glob,
            output=args.output,
            columns=args.columns,
            cell_width=args.cell_width,
            cell_height=args.cell_height,
            margin=args.margin,
            gap=args.gap,
            bg_color=args.bg_color,
            label_height=args.label_height,
        )
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
