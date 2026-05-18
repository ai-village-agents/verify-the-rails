#!/usr/bin/env python3
"""Build a narration-length rough cut from storyboard frames."""

from __future__ import annotations

import argparse
import csv
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_shot_timings(csv_path: Path, frames_dir: Path) -> list[tuple[str, float]]:
    if not csv_path.exists():
        raise FileNotFoundError(f"Missing rough cut timings file: {csv_path}")

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

            frame_path = frames_dir / frame
            if not frame_path.exists():
                raise FileNotFoundError(f"Row {row_num}: missing frame file {frame_path}")

            shots.append((frame, duration))

    if not shots:
        raise ValueError("No shots found in ROUGH_CUT_TIMINGS.csv")

    return shots


def write_concat_file(concat_path: Path, shots: list[tuple[str, float]], frames_dir: Path) -> None:
    # Repeat the final frame without duration so ffmpeg holds it for prior duration.
    lines: list[str] = []
    for frame, duration in shots:
        abs_frame_path = (frames_dir / frame).resolve()
        escaped = str(abs_frame_path).replace("'", "'\\''")
        lines.append(f"file '{escaped}'")
        lines.append(f"duration {duration:.3f}")

    final_frame = str((frames_dir / shots[-1][0]).resolve()).replace("'", "'\\''")
    lines.append(f"file '{final_frame}'")

    concat_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a narration-length rough cut.")
    parser.add_argument(
        "--video",
        default="video1",
        help="Video directory name under videos/ to use (default: video1)",
    )
    return parser.parse_args()


def build_rough_cut() -> None:
    args = parse_args()

    ffmpeg_bin = shutil.which("ffmpeg")
    if not ffmpeg_bin:
        raise RuntimeError("ffmpeg not found in PATH. Please install ffmpeg and retry.")

    video_dir = ROOT / "videos" / args.video
    frames_dir = video_dir / "storyboard_frames"
    rough_cut_timings_csv = video_dir / "ROUGH_CUT_TIMINGS.csv"
    narration_audio = video_dir / f"{args.video}_narration.mp3"
    output_path = video_dir / f"{args.video}_rough_cut.mp4"

    if not narration_audio.exists():
        raise FileNotFoundError(f"Missing narration audio file: {narration_audio}")

    shots = load_shot_timings(rough_cut_timings_csv, frames_dir)
    total_shot_duration = sum(duration for _, duration in shots)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(prefix=f"{args.video}_rough_cut_", suffix=".txt", delete=False) as tmp:
        concat_path = Path(tmp.name)

    try:
        write_concat_file(concat_path, shots, frames_dir)

        cmd = [
            ffmpeg_bin,
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_path),
            "-i",
            str(narration_audio),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-vsync",
            "vfr",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-movflags",
            "+faststart",
            "-shortest",
            str(output_path),
        ]
        subprocess.run(cmd, check=True)
    finally:
        concat_path.unlink(missing_ok=True)

    print(f"Built {output_path}")
    print(f"Shots: {len(shots)}")
    print(f"Total still-frame duration: {total_shot_duration:.1f}s")
    print(f"Audio source: {narration_audio}")


if __name__ == "__main__":
    build_rough_cut()
