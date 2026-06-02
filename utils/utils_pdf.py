
from config import (FONT_NAME, ROLE_STYLES, DEFAULT_ROLE_STYLE,OPTION_PICTO_MAP,DEFAULT_PICTO_SIZE, DEFAULT_PICTO_SPACING)
from utils.debug import debug_box


def get_style_role(fonction):
    return ROLE_STYLES.get((fonction or "").lower(), DEFAULT_ROLE_STYLE)

def split_text(text, max_chars):
    paragraphs = (text or "").split("\n")
    lines = []

    for paragraph in paragraphs:
        words = paragraph.split()
        current = ""

        for word in words:
            candidate = f"{current} {word}".strip()
            if len(candidate) <= max_chars:
                current = candidate
            else:
                if current:
                    lines.append(current)
                current = word

        if current:
            lines.append(current)

        # ligne vide entre paragraphes si retour manuel
        if paragraph != paragraphs[-1]:
            lines.append("")

    return lines

def render_text_box_centered(
    c,
    text,
    x,
    y,
    w,
    h,
    font_name=FONT_NAME,
    font_size=14,
    line_height=16,
    max_chars=20,
    debug=False,
    debug_label="text"
):
    lines = split_text(text, max_chars)

    c.setFont(font_name, font_size)

    # hauteur totale du bloc texte
    text_block_h = len(lines) * line_height

    # y de départ centré dans la boîte
    start_y = y + (h / 2) + (text_block_h / 2) - line_height

    for line in lines:
        c.drawCentredString(x + w / 2, start_y, line)
        start_y -= line_height

    if debug:
        debug_box(c, x, y, w, h, debug_label)

# def draw_pictos(c, participant, y, center_x):
#     options = getattr(participant, "options", "")

#     if not options:
#         return y

#     keys = [o.strip() for o in options.split(",") if o.strip()]

#     images = [OPTION_PICTO_MAP.get(k) for k in keys if OPTION_PICTO_MAP.get(k)]

#     if not images:
#         return y

#     total_width = len(images) * DEFAULT_PICTO_SIZE + (len(images) - 1) * DEFAULT_PICTO_SPACING

#     start_x = center_x - total_width / 2

#     for i, img_path in enumerate(images):
#         if os.path.exists(img_path):
#             c.drawImage(
#                 img_path,
#                 start_x + i * (DEFAULT_PICTO_SIZE + DEFAULT_PICTO_SPACING),
#                 y - DEFAULT_PICTO_SIZE,
#                 width=DEFAULT_PICTO_SIZE,
#                 height=DEFAULT_PICTO_SIZE,
#                 preserveAspectRatio=True,
#                 mask='auto'
#             )

#     return y - DEFAULT_PICTO_SIZE - 10