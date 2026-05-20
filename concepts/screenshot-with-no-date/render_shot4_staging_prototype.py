from pathlib import Path
import render_preview_frames as r

OUT = r.OUT


def _shot4_base(subtitle: str):
    img, d = r.base('Widen the frame', subtitle)
    x, y, w, h = 120, 230, 1120, 720
    r.status_shell(d, x=x, y=y, w=w, h=h, full=True, resolved=True)
    return img, d, x, y, w, h


def shot4_step1_capture_visible(path: Path) -> None:
    img, d, x, y, w, h = _shot4_base('Shot 4 step 1: anchor the original capture moment')
    d.rectangle((x + w - 360, y + 18, x + w - 30, y + 70), outline=r.PALETTE['blue'], width=3)
    d.rectangle((x + 30, y + 430, x + w - 30, y + h - 26), fill='#000000D0')
    r.chip(d, 1320, 318, 'STEP 1: CAPTURE TIME', 'blue')
    r.text(d, (1320, 404), 'Start with the original\nscreenshot moment:\n2025-02-18 02:43 UTC.', 32)
    r.text(d, (1320, 560), 'This is real evidence,\nbut only from that moment.', 28, 'muted')
    img.save(path)


def shot4_step2_repost_gap(path: Path) -> None:
    img, d, x, y, w, h = _shot4_base('Shot 4 step 2: compare capture time against repost time')
    d.rectangle((x + w - 360, y + 18, x + w - 30, y + 70), outline=r.PALETTE['blue'], width=3)
    r.chip(d, 1320, 286, 'CAPTURED 2025-02-18 02:43 UTC', 'blue', size=22)
    r.chip(d, 1320, 346, 'REPOSTED 2026-05-19 09:12 local', 'red', size=22)
    r.panel(d, (1320, 438, 1770, 708), 'panel2')
    r.text(d, (1350, 472), 'The repost arrived\nabout 15 months later.', 32)
    r.text(d, (1350, 592), 'Same screenshot.\nDifferent present-tense risk.', 28, 'muted')
    img.save(path)


def shot4_step3_claim_scope(path: Path) -> None:
    img, d, x, y, w, h = _shot4_base('Shot 4 step 3: shift from authenticity to claim scope')
    r.chip(d, 1320, 284, 'AUTHENTIC', 'blue', size=24)
    r.chip(d, 1476, 284, '≠', 'amber', size=24)
    r.chip(d, 1536, 284, 'CURRENT', 'red', size=24)
    r.panel(d, (1320, 380, 1770, 770), 'panel2')
    r.text(d, (1352, 418), 'What the image supports:', 28, 'muted', True)
    r.text(d, (1352, 468), '• there was a disruption\n• this page was captured\n  at 02:43 UTC', 31)
    r.text(d, (1352, 606), 'What it does not prove:', 28, 'muted', True)
    r.text(d, (1352, 656), '• that the disruption\n  was still happening\n  when reposted', 31)
    img.save(path)


def shot4_step4_timeline_math(path: Path) -> None:
    img, d, x, y, w, h = _shot4_base('Shot 4 step 4: make the timeline mismatch explicit')
    r.chip(d, 1316, 286, 'TIMELINE MISMATCH', 'green')
    y0 = 536
    d.line((1318, y0, 1760, y0), fill=r.PALETTE['line'], width=4)
    pts = [
        (1336, '02:14', 'started', 'amber'),
        (1458, '02:43', 'captured', 'blue'),
        (1578, '03:26', 'resolved', 'green'),
        (1710, '2026-05-19', 'reposted', 'red'),
    ]
    for px, top, bottom, col in pts:
        d.ellipse((px-9, y0-9, px+9, y0+9), fill=r.PALETTE[col])
        r.text(d, (px-28, y0-62), top, 22, 'muted')
        r.text(d, (px-36, y0+20), bottom, 22)
    r.text(d, (1320, 640), 'The screenshot captured a real point\ninside the incident. The repost treated\nit as proof of the present.', 31)
    r.text(d, (1320, 780), 'That is the claim-scope error.', 34, 'amber', True)
    img.save(path)


def render_staged_shot4_frames(out_dir: Path = OUT) -> None:
    shot4_step1_capture_visible(out_dir / '04a_capture_time_visible.png')
    shot4_step2_repost_gap(out_dir / '04b_repost_gap.png')
    shot4_step3_claim_scope_shift(out_dir / '04c_claim_scope_shift.png')
    shot4_step4_timeline_math(out_dir / '04d_timeline_mismatch.png')


# Backwards-compatible function name used above.
def shot4_step3_claim_scope_shift(path: Path) -> None:
    shot4_step3_claim_scope(path)


if __name__ == '__main__':
    r.render_all_frames()
    render_staged_shot4_frames(OUT)
    print(f'Rendered staged Shot 4 prototype frames into {OUT.resolve()}')
