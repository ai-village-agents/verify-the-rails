import subprocess
import sys
from pathlib import Path

import render_preview_frames as r
from render_opening_staging_prototype import render_staged_opening_frames
from render_shot4_staging_prototype import render_staged_shot4_frames
from render_shot5_staging_prototype import render_staged_shot5_frames
from render_shot6_staging_prototype import render_staged_shot6_frames
from render_shot12_staging_prototype import render_staged_shot12_frames


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    r.render_all_frames()
    render_staged_opening_frames(r.OUT)
    render_staged_shot4_frames(r.OUT)
    render_staged_shot5_frames(r.OUT)
    render_staged_shot6_frames(r.OUT)
    render_staged_shot12_frames(r.OUT)
    subprocess.run(
        [
            sys.executable,
            str(script_dir / 'build_preview_animatic.py'),
            '--frames-dir', 'preview_frames',
            '--timings', 'SHOT_TIMINGS_V10_SHOT5_MOTION_CANDIDATE.csv',
            '--concat-out', 'preview_animatic_v15_concat.txt',
            '--output', 'preview_animatic_v15.mp4',
        ],
        check=True,
        cwd=script_dir,
    )


if __name__ == '__main__':
    main()
