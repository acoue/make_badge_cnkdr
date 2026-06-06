from utils.utils_pdf import split_text
from utils.canvas_utils import draw_image
from utils.debug import debug_box
from utils.image_utils import load_photo, load_flag
from config import (BORDER_FLAG_COLOR, BORDER_FLAG_WIDTH, BORDER_PHOTO_COLOR, BORDER_PHOTO_WIDTH, FONT_NAME, FONT_BOLD_NAME, FONT_SIZE_BLOCK_BANDEAU,FONT_SIZE_BLOCK_NAME,FONT_SIZE_BLOCK_FREE_TEXT,FONT_SIZE_BLOCK_PAYS)

def render_photo(c, participant, x, y, w, h, debug=False):
    photo = load_photo(participant.photo, w, h, getattr(participant, "genre", ""))
    draw_image(c, photo, x, y, w, h)

    # bordure photo
    c.setLineWidth(1)
    c.setLineWidth(BORDER_PHOTO_WIDTH)
    c.setStrokeColor(BORDER_PHOTO_COLOR)
    c.rect(x, y, w, h, stroke=1, fill=0)

    if debug:
        debug_box(c, x, y, w, h, "photo")

def render_name(c, text, x, y, w,  line_height=18, max_chars=20, debug=False):
    lines = split_text(text, max_chars)
    text_height = len(lines) * line_height
    box_top_y = y
    start_y = box_top_y - ((line_height - FONT_SIZE_BLOCK_NAME) / 2)
    start_y -= (text_height / 2) - (line_height / 2)

    c.setFont(FONT_NAME, FONT_SIZE_BLOCK_NAME)

    for line in lines:
        c.drawCentredString(
            x + w / 2,
            start_y,
            line
        )
        start_y -= line_height

    if debug:
        debug_box(
            c,
            x,
            y - text_height,
            w,
            text_height,
        "name"
    )

    return y - text_height

def render_free_text(c, text, x, y, w, line_height=16, max_chars=24, debug=False):
    if not text:
        return y

    lines = split_text(text, max_chars)
    text_height = len(lines) * line_height
    start_y = y
    start_y -= (text_height / 2) - (line_height / 2)

    c.setFont(FONT_NAME, FONT_SIZE_BLOCK_FREE_TEXT)

    for line in lines:
        c.drawCentredString(x + w / 2, start_y, line)
        start_y -= line_height

    if debug:
        debug_box(
            c,
            x,
            y - text_height,
            w,
            text_height,
            "text"
        )

    return y - text_height

def render_flag(c, participant, x, y, w, h, debug=False):
    flag = load_flag(participant.drapeau, w, h)
    draw_image(c, flag, x, y, w, h)

    # bordure drapeau
    c.setLineWidth(BORDER_FLAG_WIDTH)
    c.setStrokeColor(BORDER_FLAG_COLOR)
    c.rect(x, y, w, h, stroke=1, fill=0)

    if debug:
        debug_box(c, x, y, w, h, "flag")

def render_country(c, text, x, y, w, debug=False):
    c.setFont(FONT_BOLD_NAME, FONT_SIZE_BLOCK_PAYS)
    c.drawCentredString(x + w / 2, y, text)
    if debug:
        debug_box(c, x, y - FONT_SIZE_BLOCK_PAYS, w, FONT_SIZE_BLOCK_PAYS + 8, "country")

import os

def render_pictos(c, participant, x, y, w, size, spacing, picto_map, debug=False):

    options = getattr(participant, "options", "")

    if not options:
        return y

    keys = [o.strip() for o in options.split(",") if o.strip()]

    images = []
    for k in keys:
        img_path = picto_map.get(k)
        if img_path and os.path.exists(img_path):
            images.append(img_path)

    if not images:
        return y

    total_width = len(images) * size + (len(images) - 1) * spacing
    start_x = x + (w - total_width) / 2

    for i, img_path in enumerate(images):
        c.drawImage(
            str(img_path),
            start_x + i * (size + spacing),
            y - size,
            width=size,
            height=size,
            preserveAspectRatio=True,
            mask='auto'
        )

    if debug:
        debug_box(c, x, y - size, w, size, "pictos")
    return y - size - 10

def render_role_bandeau(c, text, color, x, y, w, h, debug=False):
    c.setFillColor(color)
    c.rect(x, y, w, h, fill=1, stroke=0)

    c.setFillColorRGB(1, 1, 1)
    c.setFont(FONT_NAME, FONT_SIZE_BLOCK_BANDEAU)
    c.drawCentredString(x + w / 2, y + h / 2 - 5, text)

    if debug:
        debug_box(c, x, y, w, h, "role")