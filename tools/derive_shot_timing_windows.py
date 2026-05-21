#!/usr/bin/env python3
"""
Planning-stage / review helper only: derive shot timing windows from a provisional
timings CSV for focused review and discussion.
"""

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


EXPECTED_HEADER = ["frame", "duration_seconds"]
SHOT_PREFIX_RE = re.compile(r"^(\d+)_")


@dataclass(frozen=True)
class TimingRow:
    shot_number: int
    frame_name: str
    duration: float
    start: float
    end: float


def format_seconds(seconds: float) -> str:
    minutes = int(seconds // 60)
    sec = seconds - (minutes * 60)
    return f"{minutes}:{sec:04.1f}"


def parse_shot_number(frame_name: str, line_number: int) -> int:
    match = SHOT_PREFIX_RE.match(frame_name)
    if not match:
        raise ValueError(
            f"Invalid frame filename at line {line_number}: '{frame_name}' "
            "must start with a numeric shot prefix like '06_update_clue.png'."
        )
    return int(match.group(1))


def read_timing_rows(csv_path: Path) -> list[TimingRow]:
    if not csv_path.exists():
        raise FileNotFoundError(f"Timing CSV not found: {csv_path}")
    if not csv_path.is_file():
        raise FileNotFoundError(f"Timing CSV path is not a file: {csv_path}")

    rows: list[TimingRow] = []
    cursor = 0.0

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header != EXPECTED_HEADER:
            raise ValueError(
                f"Invalid CSV header in {csv_path}. "
                f"Expected exactly: {','.join(EXPECTED_HEADER)}"
            )

        for line_number, row in enumerate(reader, start=2):
            if len(row) != 2:
                raise ValueError(
                    f"Invalid CSV row at line {line_number}: expected exactly 2 columns"
                )
            frame_name = row[0].strip()
            duration_text = row[1].strip()

            if not frame_name:
                raise ValueError(f"Missing frame value at line {line_number}")
            if not duration_text:
                raise ValueError(f"Missing duration_seconds value at line {line_number}")

            shot_number = parse_shot_number(frame_name, line_number)

            try:
                duration = float(duration_text)
            except ValueError as exc:
                raise ValueError(
                    f"Invalid duration_seconds at line {line_number}: '{duration_text}'"
                ) from exc
            if duration <= 0:
                raise ValueError(
                    f"duration_seconds must be positive at line {line_number}: '{duration_text}'"
                )

            start = cursor
            end = cursor + duration
            rows.append(
                TimingRow(
                    shot_number=shot_number,
                    frame_name=frame_name,
                    duration=duration,
                    start=start,
                    end=end,
                )
            )
            cursor = end

    if not rows:
        raise ValueError(f"No timing rows found in {csv_path}")
    return rows


def filter_rows(rows: Iterable[TimingRow], focus_shots: set[int] | None) -> list[TimingRow]:
    if not focus_shots:
        return list(rows)
    return [row for row in rows if row.shot_number in focus_shots]


def print_markdown_table(rows: list[TimingRow]) -> None:
    print("| Shot | Duration | Window |")
    print("| --- | --- | --- |")
    for row in rows:
        shot_label = f"Shot {row.shot_number}"
        duration_label = f"{row.duration:.1f}s"
        window_label = f"`{format_seconds(row.start)}–{format_seconds(row.end)}`"
        print(f"| {shot_label} | {duration_label} | {window_label} |")


def print_appendix(rows: list[TimingRow]) -> None:
    print()
    print("Appendix:")
    for row in rows:
        shot_label = f"Shot {row.shot_number}"
        window_label = f"`{format_seconds(row.start)}–{format_seconds(row.end)}`"
        print(
            f"- {shot_label} (`{row.frame_name}`): {window_label} ({row.duration:.1f}s)"
        )


def parse_args() -> argparse.Namespace:
    def positive_int(value: str) -> int:
        try:
            parsed = int(value)
        except ValueError as exc:
            raise argparse.ArgumentTypeError(f"invalid int value: '{value}'") from exc
        if parsed <= 0:
            raise argparse.ArgumentTypeError(
                f"invalid positive int value: '{value}'"
            )
        return parsed

    parser = argparse.ArgumentParser(
        description=(
            "Planning-stage / review helper: derive cumulative shot timing windows "
            "from a CSV with header frame,duration_seconds."
        )
    )
    parser.add_argument(
        "--timings",
        required=True,
        help="Path to timing CSV with exact header: frame,duration_seconds",
    )
    parser.add_argument(
        "--focus-shots",
        nargs="+",
        type=positive_int,
        help=(
            "Optional list of shot numbers to show in the table; windows are still "
            "derived from the full CSV."
        ),
    )
    parser.add_argument(
        "--appendix",
        action="store_true",
        help="Also print a markdown bullet appendix with every derived window.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    csv_path = Path(args.timings).resolve()
    focus_shots = set(args.focus_shots) if args.focus_shots else None

    try:
        all_rows = read_timing_rows(csv_path)
        available_shots = sorted({row.shot_number for row in all_rows})
        available_shots_set = set(available_shots)
        if focus_shots:
            missing_shots = sorted(focus_shots - available_shots_set)
            if missing_shots:
                requested = ", ".join(str(shot) for shot in sorted(focus_shots))
                missing = ", ".join(str(shot) for shot in missing_shots)
                available = ", ".join(str(shot) for shot in available_shots)
                print(
                    "Error: Some requested --focus-shots were not found in the CSV. "
                    f"Requested: [{requested}]. Missing: [{missing}]. "
                    f"Available: [{available}]",
                    file=sys.stderr,
                )
                return 1
        visible_rows = filter_rows(all_rows, focus_shots)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print_markdown_table(visible_rows)
    if args.appendix:
        print_appendix(all_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
