from pathlib import Path
import csv, subprocess

root = Path('.')
frames_dir = root / 'preview_frames'
csv_path = root / 'SHOT_TIMINGS_V1.csv'
concat_path = root / 'preview_concat.txt'
out_path = root / 'preview_animatic_v1.mp4'
rows = []
with csv_path.open() as f:
    for row in csv.DictReader(f):
        rows.append((row['frame'], float(row['duration_seconds'])))
with concat_path.open('w') as f:
    for frame, dur in rows:
        f.write(f"file '{(frames_dir / frame).resolve()}'\n")
        f.write(f'duration {dur}\n')
    f.write(f"file '{(frames_dir / rows[-1][0]).resolve()}'\n")
cmd = [
    'ffmpeg','-nostdin','-y','-f','concat','-safe','0','-i',str(concat_path),
    '-vsync','vfr','-c:v','libx264','-pix_fmt','yuv420p',str(out_path)
]
subprocess.run(cmd, check=True)
print(out_path.exists())
