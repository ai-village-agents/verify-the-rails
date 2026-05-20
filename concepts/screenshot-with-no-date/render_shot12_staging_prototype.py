from pathlib import Path
import render_preview_frames as r

OUT = r.OUT


STEPS = [
    ('1. Open source page', 'blue'),
    ('2. Check time + timezone', 'amber'),
    ('3. Scan later updates', 'green'),
    ('4. Current or past?', 'red'),
]


def _draw_steps(d, active_idx: int) -> None:
    r.text(d, (1080, 286), 'Pause before share', 26, 'muted', True)
    y = 340
    for idx, (label, col) in enumerate(STEPS):
        active = idx == active_idx
        r.chip(d, 1080, y, label, col if active else 'muted', size=22)
        y += 86


def _shot12_base(subtitle: str, active_idx: int):
    img, d = r.base('Ten-second time check', subtitle)
    x, y, w, h = 100, 260, 860, 580
    r.status_shell(d, x=x, y=y, w=w, h=h, full=True, resolved=True)
    _draw_steps(d, active_idx)
    return img, d, x, y, w, h


def shot12_step1_open_source(path: Path) -> None:
    img, d, x, y, w, h = _shot12_base('Shot 12 step 1: start by opening the original source page', 0)
    d.rectangle((x + 8, y + 8, x + w - 8, y + h - 8), outline=r.PALETTE['blue'], width=4)
    r.panel(d, (1080, 548, 1770, 804), 'panel2')
    r.text(d, (1114, 586), 'Step 1 anchors you in the original page\ninstead of the reposted crop.', 30)
    r.text(d, (1114, 704), 'Start from source, then verify time.', 28, 'muted')
    r.text(d, (1080, 828), 'Usually ten extra seconds\nand one wider view.', 36)
    r.text(d, (1080, 920), 'Not forensic work.', 24, 'muted')
    img.save(path)


def shot12_step2_check_time(path: Path) -> None:
    img, d, x, y, w, h = _shot12_base('Shot 12 step 2: check the visible timestamp and timezone', 1)
    d.rectangle((x + w - 326, y + 18, x + w - 18, y + 66), outline=r.PALETTE['amber'], width=4)
    r.panel(d, (1080, 548, 1770, 804), 'panel2')
    r.text(d, (1114, 586), 'Step 2 asks a simple question:\nwhat moment does this image actually show?', 30)
    r.text(d, (1114, 704), 'Captured 2025-02-18 02:43 UTC\nis not the same as reposted today.', 28, 'muted')
    r.text(d, (1080, 828), 'Usually ten extra seconds\nand one wider view.', 36)
    r.text(d, (1080, 920), 'Not forensic work.', 24, 'muted')
    img.save(path)


def shot12_step3_scan_updates(path: Path) -> None:
    img, d, x, y, w, h = _shot12_base('Shot 12 step 3: scan for later updates before resharing', 2)
    d.rectangle((x + 32, y + 426, x + w - 32, y + h - 24), outline=r.PALETTE['green'], width=4)
    r.panel(d, (1080, 548, 1770, 804), 'panel2')
    r.text(d, (1114, 586), 'Step 3 checks whether the page itself\ncontains a later correction or resolution.', 30)
    r.text(d, (1114, 704), 'The update log often tells you whether\nthe scary screenshot is already outdated.', 28, 'muted')
    r.text(d, (1080, 828), 'Usually ten extra seconds\nand one wider view.', 36)
    r.text(d, (1080, 920), 'Not forensic work.', 24, 'muted')
    img.save(path)


def shot12_step4_current_or_past(path: Path) -> None:
    img, d, x, y, w, h = _shot12_base('Shot 12 step 4: decide whether the claim is current or historical', 3)
    r.panel(d, (1080, 548, 1770, 838), 'panel2')
    r.chip(d, 1114, 586, 'PAST MOMENT', 'blue', size=22)
    r.chip(d, 1270, 586, '≠', 'amber', size=22)
    r.chip(d, 1332, 586, 'CURRENT STATE', 'red', size=22)
    r.text(d, (1114, 658), 'Step 4 converts the check into the actual\nquestion that matters before you share.', 30)
    r.text(d, (1114, 776), 'Same image. Different conclusion.', 30, 'muted', True)
    r.text(d, (1080, 920), 'Not forensic work.', 24, 'muted')
    img.save(path)


def render_staged_shot12_frames(out_dir: Path = OUT) -> None:
    shot12_step1_open_source(out_dir / '12a_open_source_page.png')
    shot12_step2_check_time(out_dir / '12b_check_time_timezone.png')
    shot12_step3_scan_updates(out_dir / '12c_scan_later_updates.png')
    shot12_step4_current_or_past(out_dir / '12d_current_or_past.png')


if __name__ == '__main__':
    r.render_all_frames()
    render_staged_shot12_frames(OUT)
    print(f'Rendered staged Shot 12 prototype frames into {OUT.resolve()}')
