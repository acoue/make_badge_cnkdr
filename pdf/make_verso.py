from reportlab.lib.pagesizes import A5
from reportlab.lib.utils import ImageReader

from config import QR_BACK, BACK_QR_ROWS, FONT_BOLD_NAME
from utils.image_utils import generate_qr_with_logo
from utils.utils_pdf import participant_context, safe_format, debug_box, split_text


def draw_multiline_centered(c, center_x, top_y, text, font_name, font_size, line_height, max_chars):
    lines = split_text(text, max_chars)
    c.setFont(font_name, font_size)

    y = top_y
    for line in lines:
        c.drawCentredString(center_x, y, line)
        y -= line_height

    return y


def draw_back_qr_layout(c, participant, debug=False):
    width, height = A5
    cfg = QR_BACK
    ctx = participant_context(participant)

    top_y = height - cfg["TOP_MARGIN"]
    bottom_limit = cfg["BOTTOM_MARGIN"]

    # -------------------------
    # Titre verso
    # -------------------------
    if cfg.get("TITLE"):
        c.setFont(FONT_BOLD_NAME, 14)
        c.drawCentredString(width / 2, top_y, cfg["TITLE"])
        top_y -= 24

    available_width = width - cfg["LEFT_MARGIN"] - cfg["RIGHT_MARGIN"]

    for row in BACK_QR_ROWS:
        if not row:
            continue

        count = len(row)
        qr_size = cfg["QR_SIZE"]
        col_gap = cfg["COL_GAP"]

        row_total_width = count * qr_size + (count - 1) * col_gap
        start_x = cfg["LEFT_MARGIN"] + (available_width - row_total_width) / 2

        # hauteur de la ligne = QR + zone label
        label_zone_h = 26
        row_height = qr_size + label_zone_h

        row_bottom_y = top_y - row_height

        for idx, qr_def in enumerate(row):
            qr_x = start_x + idx * (qr_size + col_gap)
            qr_y = top_y - qr_size

            qr_data = safe_format(qr_def.get("data", ""), ctx)
            qr_label = safe_format(qr_def.get("label", ""), ctx)

            qr_img = generate_qr_with_logo(
                qr_data,
                size=qr_size,
                logo_path=cfg.get("QR_LOGO_PATH"),
                logo_ratio=cfg.get("QR_LOGO_RATIO", 0.22),
                logo_padding=cfg.get("QR_LOGO_PADDING", 4),
                border=cfg.get("QR_BORDER", 2),
                box_size=cfg.get("QR_BOX_SIZE", 10),
                error_correction=cfg.get("QR_ERROR_CORRECTION", "H"),
            )

            c.drawImage(
                ImageReader(qr_img),
                qr_x,
                qr_y,
                width=qr_size,
                height=qr_size,
                mask="auto",
            )

            label_top_y = qr_y - 6
            draw_multiline_centered(
                c,
                qr_x + qr_size / 2,
                label_top_y,
                qr_label,
                cfg["LABEL_FONT_NAME"],
                cfg["LABEL_FONT_SIZE"],
                cfg["LABEL_LINE_HEIGHT"],
                cfg["LABEL_MAX_CHARS"],
            )

            if debug :
                debug_box(c, qr_x, qr_y, qr_size, qr_size, "qr")

        top_y = row_bottom_y - cfg["ROW_GAP"]

        if top_y < bottom_limit:
            break
