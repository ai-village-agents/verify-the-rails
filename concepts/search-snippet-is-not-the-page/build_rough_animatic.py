#!/usr/bin/env python3
"""
Planning-stage / rough-review tooling only; not a claim of visual lock, script lock, greenlight, or upload-readiness.
"""

import argparse
import csv
import subprocess
import sys
from pathlib import Path


EXPECTED_HEADER = ["frame", "duration_seconds"]


def resolve_path(raw: str, script_dir: Path) -> Path:
    path = Path(raw)
    if not path.is_absolute():
        path = script_dir / path
    return path.resolve()


def ffconcat_quote(path: Path) -> str:
    # Escape single quotes for ffconcat file line syntax: file '...'
    return str(path).replace("'", r"'\''")


def read_timings(timings_path: Path, frames_dir: Path) -> list[tuple[Path, float]]:
    rows: list[tuple[Path, float]] = []
    with timings_path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header != EXPECTED_HEADER:
            raise ValueError(
                f"Invalid CSV header in {timings_path}. Expected exactly: {','.join(EXPECTED_HEADER)}"
            )

        for line_number, row in enumerate(reader, start=2):
            if len(row) != 2:
                raise ValueError(f"Invalid CSV row at line {line_number}: expected 2 columns")
            frame_name = row[0].strip()
            duration_text = row[1].strip()
            if not frame_name:
                raise ValueError(f"Missing frame name at line {line_number}")
            try:
                duration = float(duration_text)
            except ValueError as exc:
                raise ValueError(
                    f"Invalid duration_seconds at line {line_number}: {duration_text}"
                ) from exc
            if duration <= 0:
                raise ValueError(
                    f"duration_seconds must be positive at line {line_number}: {duration_text}"
                )

            frame_path = (frames_dir / frame_name).resolve()
            if not frame_path.is_file():
                raise FileNotFoundError(
                    f"Referenced frame does not exist at line {line_number}: {frame_path}"
                )
            rows.append((frame_path, duration))

    if not rows:
        raise ValueError(f"No timing rows found in {timings_path}")
    return rows


def write_concat(concat_path: Path, timing_rows: list[tuple[Path, float]]) -> None:
    concat_path.parent.mkdir(parents=True, exist_ok=True)
    with concat_path.open("w", encoding="utf-8", newline="\n") as f:
        for frame_path, duration in timing_rows:
            f.write(f"file '{ffconcat_quote(frame_path)}'\n")
            f.write(f"duration {duration}\n")
        last_frame = timing_rows[-1][0]
        f.write(f"file '{ffconcat_quote(last_frame)}'\n")


def run_ffmpeg(concat_path: Path, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg",
        "-nostdin",
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(concat_path),
        "-vsync",
        "vfr",
        "-vf",
        (
            "scale=1920:1080:force_original_aspect_ratio=decrease,"
            "pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black"
        ),
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-crf",
        "23",
        "-pix_fmt",
        "yuv420p",
        "-movflags",
        "+faststart",
        str(output_path),
    ]
    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError as exc:
        raise RuntimeError("ffmpeg not found on PATH") from exc
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"ffmpeg failed with exit code {exc.returncode}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a rough MP4 animatic from rendered PNG frames and a timings CSV."
    )
    parser.add_argument("--frames-dir", required=True, help="Directory containing PNG frames.")
    parser.add_argument(
        "--timings",
        required=True,
        help="CSV with header: frame,duration_seconds",
    )
    parser.add_argument(
        "--concat-out",
        required=True,
        help="Path for ffmpeg concat demuxer text file output.",
    )
    parser.add_argument("--output", required=True, help="Path for resulting MP4 output.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    script_dir = Path(__file__).resolve().parent

    frames_dir = resolve_path(args.frames_dir, script_dir)
    timings_path = resolve_path(args.timings, script_dir)
    concat_path = resolve_path(args.concat_out, script_dir)
    output_path = resolve_path(args.output, script_dir)

    if not frames_dir.is_dir():
        print(f"Error: frames directory not found: {frames_dir}", file=sys.stderr)
        return 1
    if not timings_path.is_file():
        print(f"Error: timings CSV not found: {timings_path}", file=sys.stderr)
        return 1

    try:
        timing_rows = read_timings(timings_path, frames_dir)
        write_concat(concat_path, timing_rows)
        run_ffmpeg(concat_path, output_path)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Built rough animatic: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
