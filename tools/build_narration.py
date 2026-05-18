#!/usr/bin/env python3
"""Build Video 1 narration audio from markdown using edge-tts."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

DEFAULT_VOICE = "en-US-AriaNeural"


def strip_headings(markdown_text: str) -> str:
    lines = []
    for raw_line in markdown_text.splitlines():
        line = raw_line.strip()
        if not line:
            lines.append("")
            continue
        if line.startswith("#"):
            continue
        if line == "---":
            continue
        lines.append(line)

    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate videos/video1/video1_narration.mp3 from NARRATION.md."
    )
    parser.add_argument(
        "--voice",
        default=DEFAULT_VOICE,
        help=f"edge-tts voice name (default: {DEFAULT_VOICE})",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    input_path = repo_root / "videos" / "video1" / "NARRATION.md"
    output_path = repo_root / "videos" / "video1" / "video1_narration.mp3"

    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 1

    if shutil.which("edge-tts") is None:
        print(
            "edge-tts is not installed or not on PATH. Install it with: pip install edge-tts",
            file=sys.stderr,
        )
        return 1

    narration_text = strip_headings(input_path.read_text(encoding="utf-8"))
    if not narration_text:
        print(f"No narration text found after stripping headings: {input_path}", file=sys.stderr)
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "edge-tts",
        "--voice",
        args.voice,
        "--text",
        narration_text,
        "--write-media",
        str(output_path),
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as exc:
        print(f"edge-tts failed with exit code {exc.returncode}", file=sys.stderr)
        return exc.returncode or 1

    print(f"Wrote narration: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
