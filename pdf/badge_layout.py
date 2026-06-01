from reportlab.lib.pagesizes import A5
from reportlab.lib import colors
from config import FONT_NAME, FONT_BOLD_NAME, ROLE_STYLES, DEFAULT_ROLE_STYLE,HEADER_SPACE,FOOTER_SPACE,PHOTO_W, PHOTO_H,FLAG_W, FLAG_H, BANDEAU_H,LEFT_MARGIN, RIGHT_MARGIN, GUTTER,OPTION_PICTO_MAP,SIZE_PICTO, SPACING_PICTO
from utils.image_utils import load_photo, load_flag
from pdf.canvas_utils import draw_image
from reportlab.lib import colors
from utils.image_utils import generate_qr_code
import os

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

def draw_multiline_left(c, x, y, text, font_name=FONT_NAME, font_size=12, line_height=16, max_chars=20):
    lines = split_text(text, max_chars)
    c.setFont(font_name, font_size)

    for line in lines:
        c.drawString(x, y, line)
        y -= line_height

    return y

def draw_multiline_centered(c, x, y, text, font_name=FONT_NAME, font_size=12, line_height=16, max_chars=22):
    """
    Dessine un texte multilignes centré.
    Retourne le nouveau y après dessin.
    """
    lines = split_text(text, max_chars)
    c.setFont(font_name, font_size)

    for line in lines:
        c.drawCentredString(x, y, line)
        y -= line_height

    return y

def draw_text_in_box_centered(c, box_x, box_y, box_w, box_h, text,
                              font_name=FONT_NAME, font_size=14, line_height=16, max_chars=18):
    """
    Dessine un texte multilignes centré dans une boîte.
    """
    lines = split_text(text, max_chars)
    total_h = len(lines) * line_height
    start_y = box_y + (box_h / 2) + (total_h / 2) - line_height

    c.setFont(font_name, font_size)
    for line in lines:
        c.drawCentredString(box_x + box_w / 2, start_y, line)
        start_y -= line_height

def draw_vertical_layout(c, participant):
    """
    Layout vertical :
    header
    photo
    nom
    drapeau
    ligne
    pays
    bandeau fonction
    footer
    """
    width, height = A5
    y = height - HEADER_SPACE

    # PHOTO
    photo = load_photo(participant.photo, PHOTO_W, PHOTO_H, getattr(participant, "genre", ""))
    draw_image(
        c,
        photo,
        width / 2 - PHOTO_W / 2,
        y - PHOTO_H,
        PHOTO_W,
        PHOTO_H
    )
    y -= PHOTO_H+ 20 # espace après photo

    # NOM
    c.setFillColor(colors.black)
    y = draw_multiline_centered(
        c,
        width / 2,
        y,
        f"{participant.prenom} {participant.nom}",
        font_name=FONT_BOLD_NAME,
        font_size=18,
        line_height=18,
        max_chars=20
    )

    y -= 5 # espace après nom

    # =====================
    # 📝 LIGNE LIBRE (optionnelle)
    # =====================

    ligne_libre = getattr(participant, "ligne_libre", "")

    if ligne_libre:
        # texte multilignes
        y = draw_multiline_centered(
            c,
            width / 2,
            y,
            ligne_libre,
            font_name=FONT_NAME,
            font_size=13,
            line_height=14,
            max_chars=30
        )

    # DRAPEAU
    flag = load_flag(participant.drapeau, FLAG_W, FLAG_H)
    draw_image(
        c,
        flag,
        width / 2 - FLAG_W / 2,
        y - FLAG_H,
        FLAG_W,
        FLAG_H
    )

    y -= FLAG_H
    y -= 20 # espace après drapeau

    # PAYS
    c.setFont(FONT_NAME, 18)
    c.drawCentredString(width / 2, y, participant.pays or "")

    # =====================
    # LIGNE 3 : PICTOS
    # =====================
    y -=  30
    y = draw_pictos(c, participant, y, width/2)

    # BANDEAU FONCTION
    label, color = get_style_role(participant.fonction)
    bandeau_y = FOOTER_SPACE + 80 # position au-dessus du footer

    c.setFillColor(color)
    c.rect(0, bandeau_y, width, BANDEAU_H, fill=1)

    c.setFillColorRGB(1, 1, 1)
    c.setFont(FONT_BOLD_NAME, 15)

    c.drawCentredString(
        width / 2,
        bandeau_y + BANDEAU_H / 2 - 5,
        label
    )

def draw_editorial_layout(c, participant):
    width, height = A5

    # =====================
    # ZONE PRINCIPALE
    # =====================
    top_y = height - HEADER_SPACE

    left_col_x = LEFT_MARGIN
    left_col_w = PHOTO_W
    right_col_x = left_col_x + left_col_w + GUTTER
    right_col_w = width - right_col_x - RIGHT_MARGIN

    # =====================
    # LIGNE 1 : PHOTO + NOM/TEXTE LIBRE
    # =====================
    y = top_y

    # PHOTO
    photo = load_photo(participant.photo, PHOTO_W, PHOTO_H, getattr(participant, "genre", ""))
    draw_image(
        c,
        photo,
        left_col_x,
        y - PHOTO_H,
        PHOTO_W,
        PHOTO_H
    )

    # NOM + TEXTE LIBRE
    text_y = y - 10

    c.setFillColor(colors.black)

    full_name = f"\n\n{participant.prenom} {participant.nom}"
    text_y = draw_multiline_left(
        c,
        right_col_x,
        text_y,
        full_name,
        font_name=FONT_BOLD_NAME,
        font_size=22,
        line_height=24,
        max_chars=16
    )

    ligne_libre = getattr(participant, "ligne_libre", "") or ""
    if ligne_libre:
        c.setFillColor(colors.HexColor("#333333"))
        text_y = draw_multiline_left(
            c,
            right_col_x,
            text_y -15,
            ligne_libre,
            font_name=FONT_NAME,
            font_size=18,
            line_height=20,
            max_chars=18
        )

    # =====================
    # LIGNE 2 : DRAPEAU + PAYS
    # =====================
    row2_y = y - PHOTO_H - 45

    # Drapeau à gauche
    flag = load_flag(participant.drapeau, FLAG_W, FLAG_H)
    draw_image(
        c,
        flag,
        left_col_x,
        row2_y - FLAG_H,
        FLAG_W,
        FLAG_H
    )

    # Pays à droite
    c.setFillColor(colors.black)
    c.setFont(FONT_NAME, 24)
    pays_text = f"\n{participant.pays or ''}"
    draw_multiline_left(
        c,
        right_col_x,
        row2_y - 20,
        pays_text,
        font_name=FONT_BOLD_NAME,
        font_size=22,
        line_height=24,
        max_chars=16
    )

    # =====================
    # LIGNE 3 : PICTOS
    # =====================
    y -= row2_y - 30
    y = draw_pictos(c, participant, y, width/2)

    # =====================
    # LIGNE 4 : ROLE (bandeau coloré)
    # =====================
    label, color = get_style_role(participant.fonction)

    bandeau_y = FOOTER_SPACE + 80 # position au-dessus du footer

    c.setFillColor(color)
    c.rect(0, bandeau_y, width, BANDEAU_H, fill=1, stroke=0)

    c.setFillColor(colors.white)
    c.setFont(FONT_BOLD_NAME, 15)
    c.drawCentredString(width / 2, bandeau_y + 11, label)

def draw_back_qr_layout(c, participant, lines_count=2):
    width, height = A5

    # Zone de travail
    top_y = height - 100
    bottom_y = 100

    usable_height = top_y - bottom_y

    # Nombre de lignes
    rows = lines_count

    # marge et espacement
    col_count = 3
    margin_x = 40
    gutter_x = 20
    gutter_y = 20

    col_width = (width - 2 * margin_x - (col_count - 1) * gutter_x) / col_count
    row_height = (usable_height - (rows - 1) * gutter_y) / rows

    # Exemple des infos QR (à adapter)
    qr_data_list = [
        f"ID:{participant.nom}",
        f"PAYS:{participant.pays}",
        f"ROLE:{participant.fonction}",
        f"EVENT:EJC2026",
        f"CHECKIN:{participant.nom}",
        f"CATEGORY:{participant.fonction}"
    ]

    index = 0

    for row in range(rows):
        y = top_y - row * (row_height + gutter_y) - row_height

        for col in range(col_count):
            if index >= len(qr_data_list):
                break

            x = margin_x + col * (col_width + gutter_x)

            # QR
            qr_img = generate_qr_code(qr_data_list[index], size=80)

            draw_image(
                c,
                qr_img,
                x + col_width/2 - 40,
                y + row_height/2,
                80,
                80
            )

            # Texte sous QR
            c.setFont("Helvetica", 9)
            c.drawCentredString(
                x + col_width/2,
                y + row_height/2 - 10,
                qr_data_list[index]
            )

            index += 1

def draw_pictos(c, participant, y, center_x):
    options = getattr(participant, "options", "")

    if not options:
        return y

    keys = [o.strip() for o in options.split(",") if o.strip()]

    images = [OPTION_PICTO_MAP.get(k) for k in keys if OPTION_PICTO_MAP.get(k)]

    if not images:
        return y

    total_width = len(images) * SIZE_PICTO + (len(images) - 1) * SPACING_PICTO

    start_x = center_x - total_width / 2

    for i, img_path in enumerate(images):
        if os.path.exists(img_path):
            c.drawImage(
                img_path,
                start_x + i * (SIZE_PICTO + SPACING_PICTO),
                y - SIZE_PICTO,
                width=SIZE_PICTO,
                height=SIZE_PICTO,
                preserveAspectRatio=True,
                mask='auto'
            )

    return y - SIZE_PICTO - 10


def draw_badge(c, participant, layout_mode="vertical"):
    """
    layout_mode:
    - vertical
    - editorial
    """
    if layout_mode == "editorial":
        draw_editorial_layout(c, participant)
    else:
        draw_vertical_layout(c, participant)