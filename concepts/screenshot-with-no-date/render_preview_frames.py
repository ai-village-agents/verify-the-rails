from pathlib import Path
import csv
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
OUT = Path('preview_frames')
OUT.mkdir(exist_ok=True)
PALETTE = {
    'bg': '#0B1320', 'panel': '#142235', 'panel2': '#1B314B', 'line': '#35506D',
    'text': '#EEF4FB', 'muted': '#A9BDCF', 'blue': '#79BFFF', 'amber': '#F0BE72',
    'red': '#E98686', 'green': '#8CD6AE', 'dim': '#09111B'
}


def font(size, bold=False):
    names = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'
    ]
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except OSError:
            pass
    return ImageFont.load_default()


def base(title, subtitle='preview frame'):
    img = Image.new('RGB', (W, H), PALETTE['bg'])
    d = ImageDraw.Draw(img)
    d.rectangle((36, 36, W-36, H-36), outline=PALETTE['line'], width=2)
    d.text((84, 74), title, font=font(54, True), fill=PALETTE['text'])
    d.text((84, 144), subtitle, font=font(24), fill=PALETTE['muted'])
    d.line((84, 188, W-84, 188), fill=PALETTE['line'], width=2)
    d.text((W-330, 84), 'PREVIEW ONLY', font=font(22, True), fill=PALETTE['amber'])
    return img, d


def panel(d, box, fill='panel'):
    d.rounded_rectangle(box, radius=18, fill=PALETTE[fill], outline=PALETTE['line'], width=2)


def text(d, xy, s, size=28, color='text', bold=False, spacing=8):
    d.multiline_text(xy, s, font=font(size, bold), fill=PALETTE[color], spacing=spacing)


def chip(d, x, y, label, color, size=24, pad_x=None, pad_y=None, height=None):
    scale = size / 22
    if pad_x is None:
        pad_x = int(round(12 * scale))
    if pad_y is None:
        pad_y = int(round(9 * scale))
    if height is None:
        height = int(round(42 * scale))
    f = font(size, True)
    text_box = d.textbbox((0, 0), label, font=f)
    text_w = text_box[2] - text_box[0]
    text_h = text_box[3] - text_box[1]
    w = text_w + (pad_x * 2)
    radius = max(10, int(round(12 * scale)))
    d.rounded_rectangle((x, y, x+w, y+height), radius=radius, fill=PALETTE['panel2'], outline=PALETTE[color], width=2)
    text_y = y + max(pad_y, (height - text_h) // 2 - 1)
    d.text((x + pad_x, text_y), label, font=f, fill=PALETTE[color])


def status_shell(d, x=120, y=250, w=900, h=660, full=False, resolved=False):
    panel(d, (x, y, x+w, y+h))
    text(d, (x+34, y+28), 'OpsStatus', 30, bold=True)
    text(d, (x+34, y+68), 'System Health', 22, 'muted')
    if full:
        text(d, (x+w-300, y+32), 'Captured 2025-02-18 02:43 UTC', 24, 'muted')
    d.rounded_rectangle((x+34, y+120, x+w-34, y+220), radius=18, fill='#5C491F', outline=PALETTE['amber'], width=2)
    text(d, (x+58, y+142), 'Partial Service Disruption', 34, bold=True)
    text(d, (x+58, y+182), 'Started: 02:14 UTC', 24, 'muted')
    text(d, (x+58, y+258), 'Affected components', 24, 'muted', True)
    text(d, (x+58, y+306), '- API Gateway: Degraded Performance\n- File Uploads: Intermittent Timeouts', 28)
    if full:
        text(d, (x+58, y+432), 'Incident log', 24, 'muted', True)
        rows = [
            ('02:14 UTC', 'Partial Service Disruption opened', 'amber'),
            ('02:43 UTC', 'Mitigation applied; error rate dropping.', 'blue'),
            ('03:26 UTC', 'Resolved 2025-02-18 03:26 UTC', 'green' if resolved else 'blue'),
        ]
        yy = y + 474
        for tm, msg, col in rows:
            d.line((x+72, yy+20, x+120, yy+20), fill=PALETTE[col], width=4)
            text(d, (x+136, yy), f'{tm}  {msg}', 26)
            yy += 58


def frame_01(path):
    img, d = base('The Screenshot With No Date', 'Opening crop: authentic screenshot, wrong time claim')
    status_shell(d)
    d.rectangle((120, 250, 1020, 565), outline=PALETTE['red'], width=4)
    chip(d, 1120, 320, 'REAL SCREENSHOT', 'blue')
    chip(d, 1120, 382, 'WRONG TIME CLAIM', 'red')
    text(d, (1120, 468), 'Visible crop only:\nOpsStatus\nPartial Service Disruption\nStarted: 02:14 UTC\nAPI Gateway: Degraded Performance', 30)
    img.save(path)


def frame_02(path):
    img, d = base('Repost velocity', 'How an old moment turns into a current claim')
    status_shell(d, x=120, y=280, w=760, h=520)
    for i, y in enumerate([270, 430, 590]):
        box = (1020 + i*24, y, 1700 + i*24, y+130)
        panel(d, box, 'panel2')
        text(d, (box[0]+26, y+18), f'Repost {i+1}', 24, bold=True)
        text(d, (box[0]+26, y+52), '2026-05-19 09:12 local', 24, 'muted')
        text(d, (box[0]+26, y+80), 'Service is currently unstable.', 26)
    chip(d, 1080, 760, 'REPOSTED AS CURRENT', 'amber')
    img.save(path)


def frame_03(path):
    img, d = base('Crop boundary', 'Missing context is outside the frame')
    status_shell(d, x=220, y=250, w=980, h=620)
    d.rectangle((220, 250, 1200, 560), outline=PALETTE['red'], width=4)
    d.rectangle((220, 560, 1200, 870), fill='#00000088')
    d.rectangle((980, 250, 1200, 870), fill='#00000088')
    d.line((220, 560, 1200, 560), fill=PALETTE['red'], width=6)
    text(d, (1280, 420), 'What is outside the crop?\n- capture date\n- incident log\n- resolution state', 34)
    img.save(path)


def frame_04(path):
    img, d = base('Widen the frame', 'Capture metadata changes the story')
    status_shell(d, x=120, y=230, w=1120, h=720, full=True)
    chip(d, 1320, 340, 'CAPTURED 2025-02-18 02:43 UTC', 'blue')
    text(d, (1320, 420), 'Same screenshot.\nDifferent claim scope once\nthe original capture time is visible.', 34)
    img.save(path)


def frame_05(path):
    img, d = base('Resolution vs repost', 'Timeline mismatch made visible')
    status_shell(d, x=100, y=220, w=980, h=720, full=True, resolved=True)
    panel(d, (1180, 300, 1760, 520), 'panel2')
    text(d, (1210, 334), 'Repost marker', 28, bold=True)
    text(d, (1210, 382), '2026-05-19 09:12 local', 26, 'muted')
    text(d, (1210, 426), 'Used as proof\nof a live outage', 30)
    chip(d, 1180, 582, 'RESOLVED LONG BEFORE REPOST', 'green')
    img.save(path)


def frame_06(path):
    img, d = base('Observed / Inference / Unknown', 'Keep the split visible')
    status_shell(d, x=100, y=230, w=1060, h=720, full=True, resolved=True)
    chip(d, 1240, 280, 'OBSERVED', 'blue')
    text(d, (1240, 334), 'A real disruption\noccurred at one point.', 28)
    chip(d, 1240, 470, 'INFERENCE', 'amber')
    text(d, (1240, 524), 'The disruption is\nhappening now.', 28)
    chip(d, 1240, 660, 'UNKNOWN', 'red')
    text(d, (1240, 714), 'What changed after\nthe screenshot moment?', 28)
    img.save(path)


def frame_07(path):
    img, d = base('Claim scope', 'Authentic is not the same as current')
    panel(d, (160, 250, 760, 890))
    text(d, (206, 282), 'Compose repost', 28, bold=True)
    panel(d, (206, 340, 714, 700), 'panel2')
    text(d, (234, 370), 'OpsStatus\nPartial Service Disruption\nStarted: 02:14 UTC', 28)
    panel(d, (820, 300, 1710, 830))
    text(d, (860, 340), 'Caption draft', 28, bold=True)
    text(d, (860, 394), '"Service is still down."', 36)
    chip(d, 840, 520, 'Captured 2025-02-18 02:43 UTC', 'blue')
    chip(d, 840, 590, 'Present-tense claim', 'red')
    chip(d, 840, 690, 'AUTHENTIC ≠ CURRENT', 'amber')
    img.save(path)


def frame_08(path):
    img, d = base('One moment, not all moments', 'Same evidence, two different captions')
    for i, label in enumerate(['Was disrupted', 'Is disrupted now']):
        x = 160 + i*860
        status_shell(d, x=x, y=280, w=740, h=500)
        chip(d, x+160, 808, label.upper(), 'blue' if i == 0 else 'red')
    img.save(path)


def frame_09(path):
    img, d = base('Dashboard crop', 'A hidden range selector changes meaning')
    panel(d, (140, 250, 1780, 900))
    text(d, (190, 290), 'Operations Analytics', 30, bold=True)
    text(d, (190, 336), 'Metric: Successful Transactions (%)', 24, 'muted')
    # chart
    d.rectangle((240, 420, 1560, 820), outline=PALETTE['line'], width=2)
    pts = [(280,500),(540,480),(800,470),(1060,690),(1320,450),(1520,440)]
    d.line(pts, fill=PALETTE['blue'], width=6)
    d.ellipse((1048,678,1072,702), fill=PALETTE['red'])
    panel(d, (1180, 520, 1620, 680), 'panel2')
    text(d, (1210, 548), '2026-04-06 03:00 UTC\nCore Checkout: 88.4%\nExpress Checkout: 87.9%', 24)
    text(d, (240, 850), 'Date-range selector intentionally cropped out in this frame.', 24, 'muted')
    chip(d, 240, 208, 'LOOKS LIKE NOW', 'red')
    img.save(path)


def frame_10(path):
    img, d = base('Range reveal', 'Historical window + recovery')
    panel(d, (140, 250, 1780, 900))
    text(d, (190, 290), 'Operations Analytics', 30, bold=True)
    text(d, (190, 336), 'Metric: Successful Transactions (%)', 24, 'muted')
    chip(d, 980, 282, 'Last 90 days (2026-02-01 to 2026-04-30)', 'blue', size=20)
    d.rectangle((320, 420, 1560, 820), outline=PALETTE['line'], width=2)
    for yy, label in [(440, '100'), (540, '95'), (640, '90'), (740, '85')]:
        text(d, (248, yy-14), label, 22, 'muted')
        d.line((320, yy, 1560, yy), fill='#21364E', width=1)
    pts = [(360, 500), (620, 480), (880, 470), (1140, 690), (1380, 450), (1520, 440)]
    d.line(pts, fill=PALETTE['blue'], width=6)
    d.line([(1140, 690), (1260, 520), (1380, 450), (1520, 440)], fill=PALETTE['green'], width=6)
    d.ellipse((1128, 678, 1152, 702), fill=PALETTE['red'])
    chip(d, 1000, 724, '03:00 dip', 'red', size=20)
    chip(d, 1290, 388, '05:00 recovered', 'green', size=20)
    panel(d, (1180, 560, 1700, 748), 'panel2')
    text(d, (1210, 590), 'Dip: 88.4% / 87.9%\nRecovered above 98.9%\nby 2026-04-06 05:00 UTC', 26)
    text(d, (320, 850), 'A short dip inside a 90-day window is not a live collapse.', 24, 'muted')
    chip(d, 240, 208, 'RANGE CHANGES MEANING', 'amber')
    img.save(path)


def frame_11(path):
    img, d = base('Old announcement, new panic', 'Publication date and follow-up restore context')
    panel(d, (180, 240, 1700, 900))
    text(d, (230, 284), 'Product Updates', 30, bold=True)
    text(d, (230, 332), 'Published 2025-05-12 16:00 UTC', 26, 'muted')
    chip(d, 1200, 278, 'Reposted 2026-05-19', 'red', size=22)
    chip(d, 1200, 334, 'OLD POST, NEW PANIC', 'amber', size=22)
    d.line((230, 380, 1650, 380), fill=PALETTE['line'], width=2)
    text(d, (230, 420), 'Update: Storage retention policy adjustment', 34, bold=True)
    text(d, (230, 482), 'Starting June 1, 2025, standard workspace retention\nchanges from 18 months to 12 months.', 30)
    panel(d, (230, 620, 1650, 806), 'panel2')
    text(d, (262, 650), 'Follow-up clarification', 26, 'green', True)
    text(d, (262, 692), 'Posted 2025-05-20 09:30 UTC', 24, 'muted')
    text(d, (262, 734), 'Archived exports only; active team data unchanged.', 28)
    img.save(path)


def frame_12(path):
    img, d = base('Ten-second time check', 'A practical routine before resharing')
    status_shell(d, x=100, y=260, w=860, h=580, full=True, resolved=True)
    text(d, (1080, 286), 'Pause before share', 26, 'muted', True)
    steps = [
        ('1. Open source page', 'blue'),
        ('2. Check time + timezone', 'amber'),
        ('3. Scan later updates', 'green'),
        ('4. Current or past?', 'red'),
    ]
    y = 340
    for label, col in steps:
        chip(d, 1080, y, label, col, size=22)
        y += 86
    text(d, (1080, 732), 'Usually ten extra seconds\nand one wider view.', 36)
    text(d, (1080, 828), 'Not forensic work.', 24, 'muted')
    img.save(path)


def frame_13(path):
    img, d = base('Same image. Different conclusion.', 'Closing return with resolved timeline')
    status_shell(d, x=90, y=220, w=980, h=720, full=True, resolved=True)
    y = 880
    x0, x1 = 1150, 1760
    d.line((x0, y, x1, y), fill=PALETTE['line'], width=6)
    marks = [(1180, '02:14', 'Started', 'amber'), (1370, '02:43', 'Captured', 'blue'), (1570, '03:26', 'Resolved', 'green'), (1730, '2026-05-19', 'Repost', 'red')]
    for x, tm, lab, col in marks:
        d.ellipse((x-10, y-10, x+10, y+10), fill=PALETTE[col])
        text(d, (x-48, y-96), tm, 24, 'muted', True)
        text(d, (x-52, y+20), lab, 24)
    chip(d, 1140, 300, 'CHECK THE TIME BEFORE YOU SHARE', 'amber')
    img.save(path)


FRAMES = {
    '01_open_crop.png': frame_01,
    '02_repost_velocity_stack.png': frame_02,
    '03_hidden_ui_edge_freeze.png': frame_03,
    '04_zoomout_capture_reveal.png': frame_04,
    '05_incident_resolution_vs_repost.png': frame_05,
    '06_oiu_rails_overlay.png': frame_06,
    '07_claim_scope_composer.png': frame_07,
    '08_was_vs_is_caption_swap.png': frame_08,
    '09_dashboard_crop_dip.png': frame_09,
    '10_dashboard_range_reveal.png': frame_10,
    '11_old_announcement_reveal.png': frame_11,
    '12_ten_second_timecheck_workflow.png': frame_12,
    '13_return_full_context_resolved.png': frame_13,
}

for name, fn in FRAMES.items():
    fn(OUT / name)
print(len(FRAMES))
