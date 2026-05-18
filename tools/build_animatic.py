#!/usr/bin/env python3
"""Build a simple storyboard animatic for Video 1 using ffmpeg concat demuxer."""

from __future__ import annotations

import csv
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEO_DIR = ROOT / "videos" / "video1"
FRAMES_DIR = VIDEO_DIR / "storyboard_frames"
SHOT_TIMINGS_CSV = VIDEO_DIR / "SHOT_TIMINGS.csv"
OUTPUT_PATH = VIDEO_DIR / "video1_animatic.mp4"


def load_shot_timings(csv_path: Path) -> list[tuple[str, float]]:
    if not csv_path.exists():
        raise FileNotFoundError(f"Missing shot timings file: {csv_path}")

    shots: list[tuple[str, float]] = []
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected = ["frame", "duration_seconds"]
        if reader.fieldnames != expected:
            raise ValueError(f"Expected CSV header {expected}, got {reader.fieldnames}")

        for row_num, row in enumerate(reader, start=2):
            frame = (row.get("frame") or "").strip()
            duration_raw = (row.get("duration_seconds") or "").strip()

            if not frame:
                raise ValueError(f"Row {row_num}: frame is required")

            try:
                duration = float(duration_raw)
            except ValueError as exc:
                raise ValueError(f"Row {row_num}: invalid duration_seconds '{duration_raw}'") from exc

            if duration <= 0:
                raise ValueError(f"Row {row_num}: duration_seconds must be > 0")

            frame_path = FRAMES_DIR / frame
            if not frame_path.exists():
                raise FileNotFoundError(f"Row {row_num}: missing frame file {frame_path}")

            shots.append((frame, duration))

    if not shots:
        raise ValueError("No shots found in SHOT_TIMINGS.csv")

    return shots


def write_concat_file(concat_path: Path, shots: list[tuple[str, float]]) -> None:
    # Repeat the final frame without duration so ffmpeg holds it for the prior duration.
    lines: list[str] = []
    for frame, duration in shots:
        abs_frame_path = (FRAMES_DIR / frame).resolve()
        escaped = str(abs_frame_path).replace("'", "'\\''")
        lines.append(f"file '{escaped}'")
        lines.append(f"duration {duration:.3f}")

    final_frame = str((FRAMES_DIR / shots[-1][0]).resolve()).replace("'", "'\\''")
    lines.append(f"file '{final_frame}'")

    concat_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_animatic() -> None:
    ffmpeg_bin = shutil.which("ffmpeg")
    if not ffmpeg_bin:
        raise RuntimeError("ffmpeg not found in PATH. Please install ffmpeg and retry.")

    shots = load_shot_timings(SHOT_TIMINGS_CSV)
    total_duration = sum(duration for _, duration in shots)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(prefix="video1_animatic_", suffix=".txt", delete=False) as tmp:
        concat_path = Path(tmp.name)

    try:
        write_concat_file(concat_path, shots)

        cmd = [
            ffmpeg_bin,
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_path),
            "-vsync",
            "vfr",
            "-pix_fmt",
            "yuv420p",
            str(OUTPUT_PATH),
        ]
        subprocess.run(cmd, check=True)
    finally:
        concat_path.unlink(missing_ok=True)

    print(f"Built {OUTPUT_PATH}")
    print(f"Shots: {len(shots)}")
    print(f"Rough total duration: {total_duration:.1f}s")


if __name__ == "__main__":
    build_animatic()
