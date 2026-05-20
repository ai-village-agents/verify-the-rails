#!/usr/bin/env python3
import argparse
import csv
import math
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FULL_SIZE = (1760, 2100)
MEDIUM_SIZE = (880, 1050)
SMALL_SIZE = (586, 700)
COLS = 4
THUMB_W = 420
THUMB_H = 236
LABEL_H = 32
MARGIN_X = 16
MARGIN_Y = 28
GAP_X = 16
GAP_Y = 28
ROWS = 7
BG = (11, 18, 28)
TEXT = (225, 232, 238)
SUBTEXT = (150, 170, 190)
BOX = (18, 28, 40)


def load_font(size):
    candidates = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
    ]
    for path in candidates:
        p = Path(path)
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


FONT = load_font(18)
SMALL_FONT = load_font(14)


def parse_timings(path):
    rows = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        total = 0.0
        for idx, row in enumerate(reader, start=1):
            frame = row['frame']
            duration = float(row['duration_seconds'])
            start = total
            end = start + duration
            mid = start + duration / 2.0
            rows.append({
                'index': idx,
                'frame': frame,
                'duration': duration,
                'start': start,
                'mid': mid,
                'end': end,
            })
            total = end
    return rows


def ffmpeg_extract(video, timestamp, outpath):
    cmd = [
        'ffmpeg', '-nostdin', '-y',
        '-ss', f'{timestamp:.3f}',
        '-i', str(video),
        '-frames:v', '1',
        str(outpath),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def run_ffprobe(video, outpath):
    cmd = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', 'format=filename,duration,size,bit_rate:stream=index,codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels',
        '-of', 'default=noprint_wrappers=1',
        str(video),
    ]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    outpath.write_text(result.stdout)


def fit_image(image, size):
    target_w, target_h = size
    src_w, src_h = image.size
    src_ratio = src_w / src_h
    target_ratio = target_w / target_h
    if src_ratio > target_ratio:
        new_h = target_h
        new_w = round(new_h * src_ratio)
    else:
        new_w = target_w
        new_h = round(new_w / src_ratio)
    resized = image.resize((new_w, new_h), Image.LANCZOS)
    left = max(0, (new_w - target_w) // 2)
    top = max(0, (new_h - target_h) // 2)
    return resized.crop((left, top, left + target_w, top + target_h))


def make_sheet(frame_paths, timing_rows, outpath):
    sheet = Image.new('RGB', FULL_SIZE, BG)
    draw = ImageDraw.Draw(sheet)
    for i, (frame_path, info) in enumerate(zip(frame_paths, timing_rows)):
        row = i // COLS
        col = i % COLS
        x = MARGIN_X + col * (THUMB_W + GAP_X)
        y = MARGIN_Y + row * (LABEL_H + THUMB_H + GAP_Y)
        draw.rounded_rectangle((x, y, x + THUMB_W, y + LABEL_H + THUMB_H), radius=12, fill=BOX)
        label = f"{info['index']:02d}  {info['frame']}  mid {info['mid']:.2f}s"
        draw.text((x + 10, y + 7), label, font=FONT, fill=TEXT)
        img = Image.open(frame_path).convert('RGB')
        thumb = fit_image(img, (THUMB_W, THUMB_H))
        sheet.paste(thumb, (x, y + LABEL_H))
        duration_label = f"start {info['start']:.2f}s  dur {info['duration']:.2f}s"
        draw.text((x + 10, y + LABEL_H + THUMB_H - 24), duration_label, font=SMALL_FONT, fill=SUBTEXT)
    sheet.save(outpath)
    return sheet


def resize_and_save(image, size, outpath):
    image.resize(size, Image.LANCZOS).save(outpath)


def save_row_crops(image, size, outdir, prefix):
    outdir.mkdir(parents=True, exist_ok=True)
    scaled = image.resize(size, Image.LANCZOS)
    row_height = round(size[1] / ROWS)
    for row in range(ROWS):
        top = row * row_height
        bottom = size[1] if row == ROWS - 1 else (row + 1) * row_height
        crop = scaled.crop((0, top, size[0], bottom))
        crop.save(outdir / f'{prefix}_row_{row + 1:02d}.png')


def write_summary(outdir, rows):
    total = rows[-1]['end'] if rows else 0.0
    lines = [
        f'rows: {len(rows)}',
        f'total_duration_seconds: {total:.3f}',
        f'full_sheet: full_piece_midpoint_sheet.png',
        f'medium_sheet: full_piece_midpoint_sheet_medium.png',
        f'small_sheet: full_piece_midpoint_sheet_small.png',
        f'medium_rows_dir: full_piece_midpoint_sheet_medium_rows',
        f'small_rows_dir: full_piece_midpoint_sheet_small_rows',
        '',
    ]
    for info in rows:
        lines.append(
            f"{info['index']:02d}	{info['frame']}	start={info['start']:.3f}	mid={info['mid']:.3f}	end={info['end']:.3f}	dur={info['duration']:.3f}"
        )
    (outdir / 'summary.txt').write_text(chr(10).join(lines) + chr(10))
    (outdir / 'timing_summary.txt').write_text(chr(10).join(lines) + chr(10))


def main():
    parser = argparse.ArgumentParser(description='Generate midpoint review artifacts from a video and timing CSV.')
    parser.add_argument('--video', required=True)
    parser.add_argument('--timings', required=True)
    parser.add_argument('--outdir', required=True)
    args = parser.parse_args()

    video = Path(args.video)
    timings = Path(args.timings)
    outdir = Path(args.outdir)
    frames_dir = outdir / 'midpoints'
    frames_dir.mkdir(parents=True, exist_ok=True)

    run_ffprobe(video, outdir / 'ffprobe_summary.txt')

    rows = parse_timings(timings)
    frame_paths = []
    for info in rows:
        outpath = frames_dir / f"{info['index']:02d}_{info['frame']}.png"
        ffmpeg_extract(video, info['mid'], outpath)
        frame_paths.append(outpath)

    sheet_path = outdir / 'full_piece_midpoint_sheet.png'
    sheet = make_sheet(frame_paths, rows, sheet_path)
    resize_and_save(sheet, MEDIUM_SIZE, outdir / 'full_piece_midpoint_sheet_medium.png')
    resize_and_save(sheet, SMALL_SIZE, outdir / 'full_piece_midpoint_sheet_small.png')
    save_row_crops(sheet, MEDIUM_SIZE, outdir / 'full_piece_midpoint_sheet_medium_rows', 'medium')
    save_row_crops(sheet, SMALL_SIZE, outdir / 'full_piece_midpoint_sheet_small_rows', 'small')
    write_summary(outdir, rows)


if __name__ == '__main__':
    main()
