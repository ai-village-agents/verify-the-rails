#!/usr/bin/env python3
"""Planning-stage rough frame renderer for concept validation, not final production rendering."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 1920
HEIGHT = 1080

OUT_DIR = Path(__file__).resolve().parent / "rough_frames"

TEXT = {
    "title": "Refund policy — Help Center",
    "url": "help.example.com \u203a billing \u203a refund-policy",
    "page_heading": "Refund policy",
    "support_line": "Billing and plan changes",
    "preview_sentence": "Refunds are available for all annual plans.",
    "live_sentence": "Refunds are available for annual plans within 14 days of purchase.",
    "update_clue": "Updated March 14, 2026",
}

PALETTE = {
    "bg": (13, 18, 27),
    "panel": (22, 30, 44),
    "panel_soft": (28, 38, 56),
    "line": (65, 86, 120),
    "text": (224, 232, 246),
    "muted": (145, 163, 192),
    "highlight_bg": (45, 87, 134),
    "highlight_text": (236, 245, 255),
    "accent": (255, 196, 103),
    "accent_soft": (106, 83, 45),
}


def font(size, bold=False):
    names = ["DejaVuSans-Bold.ttf", "DejaVuSans.ttf"] if bold else ["DejaVuSans.ttf", "DejaVuSans-Bold.ttf"]
    for name in names:
        try:
            return ImageFont.truetype(name, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def make_canvas():
    img = Image.new("RGB", (WIDTH, HEIGHT), PALETTE["bg"])
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, WIDTH, 92), fill=(9, 14, 22))
    draw.text((72, 30), "Verify the Rails \u2022 rough frame", font=font(30, bold=True), fill=PALETTE["muted"])
    return img, draw


def rrect(draw, box, fill, outline=None, radius=22, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def wrap_text(draw, text, text_font, max_width):
    words = text.split()
    lines = []
    current = []
    for word in words:
        trial = " ".join(current + [word])
        if current and draw.textlength(trial, font=text_font) > max_width:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return lines


def frame_01(path):
    img, d = make_canvas()
    rrect(d, (180, 190, 1740, 840), PALETTE["panel"], outline=PALETTE["line"])
    d.text((230, 230), "Search preview", font=font(30, bold=True), fill=PALETTE["muted"])
    d.line((230, 280, 1690, 280), fill=PALETTE["line"], width=2)
    d.text((230, 320), TEXT["title"], font=font(48, bold=True), fill=PALETTE["text"])
    d.text((230, 388), TEXT["url"], font=font(30), fill=PALETTE["muted"])
    rrect(d, (218, 455, 1702, 565), PALETTE["highlight_bg"], radius=14)
    d.text((244, 484), TEXT["preview_sentence"], font=font(44, bold=True), fill=PALETTE["highlight_text"])
    d.text((230, 630), "Other search details are intentionally quiet in this rough pass.", font=font(28), fill=(113, 130, 158))
    img.save(path)


def frame_02(path):
    img, d = make_canvas()
    rrect(d, (180, 190, 1740, 840), PALETTE["panel"], outline=PALETTE["line"])
    d.text((230, 230), "Search preview", font=font(30, bold=True), fill=PALETTE["muted"])
    d.text((230, 320), TEXT["title"], font=font(46, bold=True), fill=PALETTE["text"])
    d.text((230, 386), TEXT["url"], font=font(30), fill=PALETTE["muted"])
    rrect(d, (218, 450, 1702, 558), PALETTE["highlight_bg"], radius=14)
    d.text((244, 480), TEXT["preview_sentence"], font=font(44, bold=True), fill=PALETTE["highlight_text"])
    rrect(d, (640, 630, 1670, 760), (35, 55, 82), outline=(94, 123, 167), radius=20)
    d.text((680, 675), "So refunds apply to every annual plan.", font=font(44, bold=True), fill=PALETTE["text"])
    img.save(path)


def frame_03(path):
    img, d = make_canvas()
    # Browser/page setup: calm, source-like, and intentionally low-drama.
    rrect(d, (220, 150, 1700, 920), PALETTE["panel_soft"], outline=PALETTE["line"])
    rrect(d, (220, 150, 1700, 230), (19, 27, 39), outline=PALETTE["line"], radius=22, width=2)
    for i, c in enumerate([(99, 121, 155), (91, 113, 146), (83, 105, 136)]):
        d.ellipse((264 + i * 34, 180, 284 + i * 34, 200), fill=c)
    rrect(d, (390, 172, 1580, 208), (26, 36, 52), outline=(74, 96, 130), radius=10, width=1)
    d.text((424, 179), "help.example.com / billing / refund-policy", font=font(24), fill=(148, 167, 196))

    rrect(d, (280, 270, 1640, 860), PALETTE["panel"], outline=(73, 96, 131), radius=18, width=2)
    d.text((340, 320), "Help Center", font=font(30, bold=True), fill=(156, 176, 206))
    d.text((340, 374), TEXT["page_heading"], font=font(58, bold=True), fill=PALETTE["text"])
    d.text((340, 444), TEXT["support_line"], font=font(31), fill=PALETTE["muted"])
    d.line((340, 494, 1584, 494), fill=(70, 92, 125), width=2)

    sentence_font = font(42)
    max_text_width = 1180
    lines = wrap_text(d, TEXT["live_sentence"], sentence_font, max_text_width)
    y = 548
    for line in lines[:2]:
        d.text((340, y), line, font=sentence_font, fill=(205, 217, 236))
        y += 58
    d.text((340, 700), TEXT["update_clue"], font=font(29), fill=(138, 158, 188))
    img.save(path)


def frame_04(path):
    img, d = make_canvas()
    rrect(d, (220, 250, 1700, 840), PALETTE["panel"], outline=PALETTE["line"])
    d.text((270, 300), "Current page wording", font=font(34, bold=True), fill=PALETTE["muted"])

    shared = "Refunds are available for annual plans"
    qualifier = "within 14 days of purchase"
    suffix = "."

    base_x = 270
    shared_y = 430
    qual_y = 520
    shared_font = font(54, bold=True)
    qual_font = font(74, bold=True)

    d.text((base_x, shared_y), shared, font=shared_font, fill=(120, 137, 163))
    d.text((base_x, qual_y), f"{qualifier}{suffix}", font=qual_font, fill=PALETTE["accent"])
    qual_w = d.textlength(f"{qualifier}{suffix}", font=qual_font)
    d.line((base_x, qual_y + 88, base_x + qual_w, qual_y + 88), fill=PALETTE["accent"], width=4)
    img.save(path)


def frame_05(path):
    img, d = make_canvas()
    rrect(d, (170, 150, 1750, 930), PALETTE["panel_soft"], outline=PALETTE["line"])
    d.text((250, 220), "Direct wording compare", font=font(34, bold=True), fill=PALETTE["muted"])

    shared_font = font(46, bold=True)
    diff_font_preview = font(68, bold=True)
    diff_font_live = font(60, bold=True)
    shared_fill = (130, 149, 178)

    # Top card: preview sentence split so the differing phrase becomes the visual event.
    rrect(d, (250, 300, 1670, 550), PALETTE["panel"], outline=PALETTE["line"], radius=18)
    d.text((310, 338), "Preview", font=font(34, bold=True), fill=PALETTE["muted"])
    d.text((310, 398), "Refunds are available for", font=shared_font, fill=shared_fill)
    d.text((310, 452), "all annual plans.", font=diff_font_preview, fill=PALETTE["accent"])

    # Bottom card: live sentence split the same way for easy side-by-side comparison.
    rrect(d, (250, 590, 1670, 860), PALETTE["panel"], outline=PALETTE["line"], radius=18)
    d.text((310, 628), "Live page", font=font(34, bold=True), fill=PALETTE["muted"])
    d.text((310, 688), "Refunds are available for", font=shared_font, fill=shared_fill)
    d.text((310, 742), "annual plans within 14 days of purchase.", font=diff_font_live, fill=PALETTE["accent"])
    img.save(path)


def frame_06(path):
    img, d = make_canvas()
    rrect(d, (250, 170, 1670, 900), PALETTE["panel_soft"], outline=PALETTE["line"])
    d.text((320, 240), "Live page + update clue", font=font(34, bold=True), fill=PALETTE["muted"])

    # Live page surface.
    rrect(d, (320, 300, 1600, 790), PALETTE["panel"], outline=PALETTE["line"], radius=18)
    d.text((370, 345), TEXT["page_heading"], font=font(50, bold=True), fill=PALETTE["text"])
    d.text((370, 407), TEXT["support_line"], font=font(30), fill=PALETTE["muted"])
    d.line((370, 456, 1548, 456), fill=PALETTE["line"], width=2)

    lines = wrap_text(d, TEXT["live_sentence"], font(48, bold=True), 1090)
    y = 500
    for line in lines[:2]:
        d.text((370, y), line, font=font(48, bold=True), fill=(174, 191, 219))
        y += 60

    # Isolated update chip, visually anchored to the page surface.
    rrect(d, (1170, 264, 1550, 356), PALETTE["accent_soft"], outline=PALETTE["accent"], radius=14, width=3)
    d.text((1200, 296), TEXT["update_clue"], font=font(30, bold=True), fill=PALETTE["accent"])
    d.line((1360, 356, 1360, 456), fill=PALETTE["accent"], width=3)

    # Compact subdued preview reference for contrast.
    rrect(d, (370, 690, 980, 760), (24, 34, 49), outline=(58, 79, 112), radius=12, width=2)
    d.text((396, 714), "Preview: \"...all annual plans.\"", font=font(28), fill=(132, 151, 181))
    img.save(path)


def frame_07(path):
    img, d = make_canvas()
    rrect(d, (420, 190, 1500, 860), PALETTE["panel"], outline=PALETTE["line"])
    d.text((500, 270), "Evidence hierarchy", font=font(42, bold=True), fill=PALETTE["text"])
    labels = [
        "Preview: points to the source",
        "Live page: current wording",
        "Update clue: explains mismatch",
    ]
    y = 360
    for label in labels:
        rrect(d, (500, y, 1420, y + 96), (31, 46, 68), outline=(83, 109, 151), radius=14, width=2)
        d.text((540, y + 28), label, font=font(38, bold=True), fill=PALETTE["text"])
        y += 122
    d.line((500, 760, 1420, 760), fill=PALETTE["line"], width=2)
    d.text((500, 790), "Open the page. Compare the wording. Check one update clue.", font=font(34, bold=True), fill=PALETTE["accent"])
    img.save(path)


def frame_08(path):
    img, d = make_canvas()
    rrect(d, (520, 230, 1400, 760), PALETTE["panel"], outline=PALETTE["line"])
    d.text((590, 286), "Pattern label", font=font(36, bold=True), fill=PALETTE["muted"])

    labels = [
        "Preview: points to the source",
        "Live page: current wording",
        "Update clue: explains mismatch",
    ]
    y = 360
    for label in labels:
        rrect(d, (590, y, 1330, y + 72), (31, 46, 68), outline=(83, 109, 151), radius=12, width=2)
        d.text((622, y + 22), label, font=font(28, bold=True), fill=PALETTE["text"])
        y += 90

    d.line((590, 648, 1330, 648), fill=PALETTE["line"], width=2)
    d.text(
        (590, 680),
        "The mistake was treating the preview as the page.",
        font=font(36, bold=True),
        fill=PALETTE["accent"],
    )
    img.save(path)


def frame_10(path):
    img, d = make_canvas()
    rrect(d, (420, 240, 1500, 820), PALETTE["panel"], outline=PALETTE["line"])
    d.text((500, 320), "Viewer routine", font=font(36, bold=True), fill=PALETTE["muted"])

    lines = [
        "Open the page.",
        "Compare the wording.",
        "Check one update clue.",
    ]
    y = 430
    for line in lines:
        d.text((500, y), line, font=font(56, bold=True), fill=PALETTE["text"])
        y += 120
    img.save(path)


def frame_11(path):
    img, d = make_canvas()
    rrect(d, (180, 190, 1740, 840), PALETTE["panel"], outline=PALETTE["line"])
    d.text((230, 230), "Search preview", font=font(30, bold=True), fill=PALETTE["muted"])
    d.line((230, 280, 1690, 280), fill=PALETTE["line"], width=2)
    d.text((230, 320), TEXT["title"], font=font(48, bold=True), fill=PALETTE["text"])
    d.text((230, 388), TEXT["url"], font=font(30), fill=PALETTE["muted"])
    rrect(d, (218, 455, 1702, 565), (34, 52, 75), radius=14, outline=(82, 108, 149), width=2)
    d.text((244, 486), TEXT["preview_sentence"], font=font(42, bold=True), fill=(177, 194, 221))
    d.text(
        (230, 640),
        "A preview can point you to a source. It is not the source.",
        font=font(44, bold=True),
        fill=PALETTE["accent"],
    )
    img.save(path)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for old_png in OUT_DIR.glob("*.png"):
        old_png.unlink()
    targets = [
        ("01_search_preview.png", frame_01),
        ("02_preview_claim.png", frame_02),
        ("03_live_page.png", frame_03),
        ("04_qualifier_focus.png", frame_04),
        ("05_wording_compare.png", frame_05),
        ("06_update_clue.png", frame_06),
        ("07_evidence_hierarchy.png", frame_07),
        ("08_pattern_label.png", frame_08),
        ("10_viewer_routine.png", frame_10),
        ("11_closing_callback.png", frame_11),
    ]
    for name, fn in targets:
        fn(OUT_DIR / name)
    print(f"Wrote {len(targets)} rough frames to: {OUT_DIR}")


if __name__ == "__main__":
    main()
