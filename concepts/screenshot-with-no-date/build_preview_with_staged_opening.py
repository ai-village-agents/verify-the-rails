import subprocess
import sys
from pathlib import Path

import render_preview_frames as r
from render_opening_staging_prototype import render_staged_opening_frames


def main() -> None:
    script_dir = Path(__file__).resolve().parent

    r.render_all_frames()
    render_staged_opening_frames(r.OUT)

    subprocess.run(
        [
            sys.executable,
            str(script_dir / 'build_preview_animatic.py'),
            '--frames-dir',
            'preview_frames',
            '--timings',
            'SHOT_TIMINGS_V3.csv',
            '--concat-out',
            'preview_concat_v8.txt',
            '--output',
            'preview_animatic_v8.mp4',
        ],
        check=True,
        cwd=script_dir,
    )


if __name__ == '__main__':
    main()
