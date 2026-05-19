import argparse
import csv
import subprocess
from pathlib import Path


def resolve_from_script(path_str: str, script_dir: Path) -> Path:
    path = Path(path_str)
    return path if path.is_absolute() else (script_dir / path).resolve()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--frames-dir', default='preview_frames')
    parser.add_argument('--timings', default='SHOT_TIMINGS_V1.csv')
    parser.add_argument('--concat-out', default='preview_concat.txt')
    parser.add_argument('--output', default='preview_animatic_v1.mp4')
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    frames_dir = resolve_from_script(args.frames_dir, script_dir)
    csv_path = resolve_from_script(args.timings, script_dir)
    concat_path = resolve_from_script(args.concat_out, script_dir)
    out_path = resolve_from_script(args.output, script_dir)

    rows = []
    with csv_path.open() as f:
        for row in csv.DictReader(f):
            rows.append((row['frame'], float(row['duration_seconds'])))
    if not rows:
        raise ValueError(f'No frame timing rows found in CSV: {csv_path}')

    with concat_path.open('w') as f:
        for frame, dur in rows:
            f.write(f"file '{(frames_dir / frame).resolve()}'\n")
            f.write(f'duration {dur}\n')
        f.write(f"file '{(frames_dir / rows[-1][0]).resolve()}'\n")

    cmd = [
        'ffmpeg',
        '-nostdin',
        '-y',
        '-f',
        'concat',
        '-safe',
        '0',
        '-i',
        str(concat_path),
        '-vsync',
        'vfr',
        '-c:v',
        'libx264',
        '-pix_fmt',
        'yuv420p',
        str(out_path),
    ]
    subprocess.run(cmd, check=True)
    print(f'Success: wrote {out_path}')


if __name__ == '__main__':
    main()
