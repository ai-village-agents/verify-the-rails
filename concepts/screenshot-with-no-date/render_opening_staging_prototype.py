from pathlib import Path
import subprocess
from PIL import ImageDraw
import render_preview_frames as r

OUT = r.OUT
CONCAT = Path('preview_concat_v7.txt')
OUTPUT = Path('preview_animatic_v7.mp4')


def repost_frame(path: Path, count: int) -> None:
    img, d = r.base('Opening repost spread prototype', f'Shot 2 test: {count} repost' + ('' if count == 1 else 's'))
    r.status_shell(d, x=120, y=280, w=760, h=520)
    positions = [270, 430, 590]
    for i, y in enumerate(positions[:count]):
        box = (1020 + i*24, y, 1700 + i*24, y+130)
        r.panel(d, box, 'panel2')
        r.text(d, (box[0]+26, y+18), f'Repost {i+1}', 24, bold=True)
        r.text(d, (box[0]+26, y+52), '2026-05-19 09:12 local', 24, 'muted')
        r.text(d, (box[0]+26, y+80), 'Service is currently unstable.', 26)
    r.chip(d, 1080, 760, 'REPOSTED AS CURRENT', 'amber')
    if count < 3:
        r.text(d, (1080, 830), 'More reposts arrive before anyone checks the source page.', 24, 'muted')
    img.save(path)


def crop_boundary_only(path: Path) -> None:
    img, d = r.base('Opening reveal prototype', 'Shot 3 step 1: start from the crop')
    r.status_shell(d, x=220, y=250, w=980, h=620)
    d.rectangle((220, 250, 1200, 560), outline=r.PALETTE['red'], width=4)
    d.rectangle((220, 560, 1200, 870), fill='#000000CC')
    d.rectangle((980, 250, 1200, 870), fill='#000000CC')
    d.line((220, 560, 1200, 560), fill=r.PALETTE['red'], width=6)
    r.chip(d, 1280, 360, 'CROP HIDES CONTEXT', 'red')
    r.text(d, (1280, 450), 'Start with the exact area\nthat made the repost feel current.', 32)
    img.save(path)


def reveal_capture_date(path: Path) -> None:
    img, d = r.base('Opening reveal prototype', 'Shot 3 step 2: reveal the capture date first')
    x, y, w, h = 160, 220, 1100, 720
    r.status_shell(d, x=x, y=y, w=w, h=h, full=True, resolved=False)
    d.rectangle((x+40, y+420, x+w-40, y+h-30), fill='#000000D8')
    d.rectangle((x+40, y+120, x+w-40, y+220), outline=r.PALETTE['red'], width=3)
    r.chip(d, 1330, 320, 'REVEAL 1: CAPTURE DATE', 'blue')
    r.text(d, (1330, 404), 'This was captured on\n2025-02-18 at 02:43 UTC.', 32)
    r.text(d, (1330, 520), 'The repost is from\n2026-05-19.', 32, 'muted')
    r.text(d, (1330, 640), 'That alone shrinks the claim scope.', 28, 'muted')
    img.save(path)


def reveal_incident_log(path: Path) -> None:
    img, d = r.base('Opening reveal prototype', 'Shot 3 step 3: reveal the incident log next')
    x, y, w, h = 160, 220, 1100, 720
    r.status_shell(d, x=x, y=y, w=w, h=h, full=True, resolved=False)
    d.rectangle((x+52, 810, x+w-52, 886), fill='#000000D8')
    r.chip(d, 1330, 300, 'REVEAL 2: INCIDENT LOG', 'amber')
    r.text(d, (1330, 384), 'Now the viewer can see\nupdates after the first screenshot moment.', 32)
    r.text(d, (1330, 530), 'The screenshot captured one moment\ninside a longer sequence.', 28, 'muted')
    r.text(d, (1330, 648), 'One more reveal still matters.', 28, 'muted')
    img.save(path)


def reveal_resolution(path: Path) -> None:
    img, d = r.base('Opening reveal prototype', 'Shot 3 step 4: reveal the resolution state last')
    x, y, w, h = 160, 220, 1100, 720
    r.status_shell(d, x=x, y=y, w=w, h=h, full=True, resolved=True)
    d.rectangle((x+56, 810, x+w-56, 868), outline=r.PALETTE['green'], width=4)
    r.chip(d, 1330, 292, 'REVEAL 3: RESOLVED', 'green')
    r.text(d, (1330, 378), 'The missing state change is the payoff:\nresolved long before the repost.', 32)
    r.text(d, (1330, 540), 'Same screenshot.\nDifferent conclusion.', 34, 'amber', True)
    img.save(path)


def build_concat() -> list[tuple[str, float]]:
    rows = [
        ('01_open_crop.png', 2.4),
        ('02a_repost_velocity_one.png', 1.1),
        ('02b_repost_velocity_two.png', 1.1),
        ('02_repost_velocity_stack.png', 1.5),
        ('03a_hidden_ui_crop_only.png', 1.7),
        ('03b_reveal_capture_date.png', 1.8),
        ('03c_reveal_incident_log.png', 1.8),
        ('03d_reveal_resolution.png', 2.4),
    ]
    with CONCAT.open('w') as f:
        for frame, dur in rows:
            f.write(f"file '{(OUT / frame).resolve()}'\n")
            f.write(f'duration {dur}\n')
        f.write(f"file '{(OUT / rows[-1][0]).resolve()}'\n")
    return rows


def main() -> None:
    r.render_all_frames()
    repost_frame(OUT / '02a_repost_velocity_one.png', 1)
    repost_frame(OUT / '02b_repost_velocity_two.png', 2)
    crop_boundary_only(OUT / '03a_hidden_ui_crop_only.png')
    reveal_capture_date(OUT / '03b_reveal_capture_date.png')
    reveal_incident_log(OUT / '03c_reveal_incident_log.png')
    reveal_resolution(OUT / '03d_reveal_resolution.png')
    build_concat()
    subprocess.run([
        'ffmpeg', '-nostdin', '-y', '-f', 'concat', '-safe', '0', '-i', str(CONCAT),
        '-vsync', 'vfr', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', str(OUTPUT)
    ], check=True)
    print(f'Success: wrote {OUTPUT}')


if __name__ == '__main__':
    main()
