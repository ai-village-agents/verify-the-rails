from pathlib import Path

import render_preview_frames as r

SCRIPT_DIR = Path(__file__).resolve().parent
OUT = SCRIPT_DIR / 'preview_frames'
OUT.mkdir(exist_ok=True)


def _shot6_base():
    img, d = r.base('Observed / Inference / Unknown', 'Keep the split visible')
    r.status_shell(d, x=100, y=230, w=1060, h=720, full=True, resolved=True)
    return img, d


def shot6_step1_observed_only(path: Path) -> None:
    img, d = _shot6_base()
    r.chip(d, 1240, 280, 'OBSERVED', 'blue')
    r.text(d, (1240, 334), 'A real disruption\noccurred at one point.', 28)
    img.save(path)


def shot6_step2_inference_added(path: Path) -> None:
    img, d = _shot6_base()
    r.chip(d, 1240, 280, 'OBSERVED', 'muted')
    r.text(d, (1240, 334), 'A real disruption\noccurred at one point.', 28, 'muted')
    r.chip(d, 1240, 470, 'INFERENCE', 'amber')
    r.text(d, (1240, 524), 'The disruption is\nhappening now.', 28)
    img.save(path)


def shot6_step3_unknown_added(path: Path) -> None:
    img, d = _shot6_base()
    r.chip(d, 1240, 280, 'OBSERVED', 'muted')
    r.text(d, (1240, 334), 'A real disruption\noccurred at one point.', 28, 'muted')
    r.chip(d, 1240, 470, 'INFERENCE', 'amber')
    r.text(d, (1240, 524), 'The disruption is\nhappening now.', 28)
    r.chip(d, 1240, 660, 'UNKNOWN', 'red')
    r.text(d, (1240, 714), 'What changed after\nthe screenshot moment?', 28)
    img.save(path)


def render_staged_shot6_frames(out_dir: Path = OUT) -> None:
    out_dir.mkdir(exist_ok=True)
    shot6_step1_observed_only(out_dir / '06a_observed_only.png')
    shot6_step2_inference_added(out_dir / '06b_inference_added.png')
    shot6_step3_unknown_added(out_dir / '06c_unknown_added.png')


if __name__ == '__main__':
    r.render_all_frames()
    render_staged_shot6_frames(OUT)
    print(f'Rendered staged Shot 6 prototype frames into {OUT.resolve()}')
