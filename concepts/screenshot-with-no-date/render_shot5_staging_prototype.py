from pathlib import Path

import render_preview_frames as r

OUT = r.OUT


def _shot5_base(subtitle: str):
    img, d = r.base('Resolution vs repost', subtitle)
    x, y, w, h = 100, 220, 980, 720
    r.status_shell(d, x=x, y=y, w=w, h=h, full=True, resolved=True)
    return img, d, x, y, w, h


def _draw_resolution_focus(d, x: int, y: int, w: int) -> None:
    row_top = y + 588
    row_bottom = row_top + 48
    d.rounded_rectangle(
        (x + 126, row_top, x + w - 34, row_bottom),
        radius=12,
        outline=r.PALETTE['green'],
        width=3,
    )
    r.chip(d, 128, 956, 'RESOLVED 2025-02-18 03:26 UTC', 'green', size=20)


def _draw_repost_panel(d) -> None:
    r.panel(d, (1180, 300, 1760, 520), 'panel2')
    r.text(d, (1210, 334), 'Repost marker', 28, bold=True)
    r.text(d, (1210, 382), '2026-05-19 09:12 local', 26, 'muted')
    r.text(d, (1210, 426), 'Used as proof\nof a live outage', 30)


def shot5_state1_resolution_visible(path: Path) -> None:
    img, d, x, y, w, h = _shot5_base('Shot 5 state 1: reveal incident resolution timing')
    _draw_resolution_focus(d, x, y, w)
    img.save(path)


def shot5_state2_repost_marker_added(path: Path) -> None:
    img, d, x, y, w, h = _shot5_base('Shot 5 state 2: keep resolution visible and add repost marker')
    _draw_resolution_focus(d, x, y, w)
    _draw_repost_panel(d)
    img.save(path)


def shot5_state3_timeline_gap_locked(path: Path) -> None:
    img, d, x, y, w, h = _shot5_base('Shot 5 state 3: lock the timeline mismatch conclusion')
    _draw_resolution_focus(d, x, y, w)
    _draw_repost_panel(d)
    r.chip(d, 1180, 582, 'RESOLVED LONG BEFORE REPOST', 'green')
    img.save(path)


def render_staged_shot5_frames(out_dir: Path = OUT) -> None:
    out_dir.mkdir(exist_ok=True)
    shot5_state1_resolution_visible(out_dir / '05a_resolution_visible.png')
    shot5_state2_repost_marker_added(out_dir / '05b_repost_marker_added.png')
    shot5_state3_timeline_gap_locked(out_dir / '05c_timeline_gap_locked.png')


if __name__ == '__main__':
    r.render_all_frames()
    render_staged_shot5_frames(OUT)
    print(f'Rendered staged Shot 5 prototype frames into {OUT.resolve()}')
