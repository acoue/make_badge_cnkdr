from reportlab.lib.pagesizes import A5

from config import (
    HEADER_SPACE,
    FOOTER_SPACE,
    BANDEAU_H,
    FONT_BOLD_NAME,
    FONT_NAME,
    EDITORIAL,
)

from pdf.build_bloc import (
    render_flag,
    render_photo,
    render_pictos,
    render_role_bandeau,
)

from utils.utils_pdf import (
    get_style_role,
    render_text_box_centered,
)


def draw_editorial_layout(c, participant, picto_map, debug=False):
    width, height = A5
    cfg = EDITORIAL

    # =====================
    # POINT DE DÉPART
    # =====================
    top_y = height - HEADER_SPACE - cfg.get("TOP_CONTENT_MARGIN", 0)

    # =====================
    # COLONNES
    # =====================
    left_x = cfg["LEFT_MARGIN"]
    right_x = left_x + cfg["PHOTO_W"] + cfg["COLUMN_GUTTER"]
    right_w = width - right_x - cfg["RIGHT_MARGIN"]

    # ============================================================
    # ROW 1 : PHOTO + NOM + TEXTE
    # ============================================================
    photo_h = cfg["PHOTO_H"]
    photo_y = top_y - photo_h

    render_photo(
        c, participant,
        left_x, photo_y,
        cfg["PHOTO_W"], photo_h,
        debug=debug
    )

    # NOM
    name_h = cfg["NAME_BOX_H"]
    name_y = top_y - cfg["NAME_TOP_MARGIN"] - name_h

    render_text_box_centered(
        c,
        f"{participant.prenom} {participant.nom}",
        right_x,
        name_y,
        right_w,
        name_h,
        FONT_BOLD_NAME,
        font_size=20,
        line_height=22,
        max_chars=18,
        debug=debug,
        debug_label="name"
    )

    # TEXTE
    free_h = cfg["FREE_TEXT_BOX_H"]
    free_y = name_y - cfg["TEXT_LIBRE_MARGIN"] - free_h

    render_text_box_centered(
        c,
        getattr(participant, "ligne_libre", ""),
        right_x,
        free_y,
        right_w,
        free_h,
        FONT_NAME,
        font_size=15,
        line_height=17,
        max_chars=18,
        debug=debug,
        debug_label="text"
    )

    # =====================
    # BASE COMMUNE
    # =====================
    content_bottom = min(photo_y, free_y)

    # ============================================================
    # ROW 2 : FLAG + COUNTRY (même ligne)
    # ============================================================
    row2_top = content_bottom - cfg["ROW_FLAG_COUNTRY_MARGIN"]
    row2_height = max(cfg["FLAG_H"], cfg["COUNTRY_BOX_H"])
    row2_bottom = row2_top - row2_height

    # FLAG centré dans la colonne gauche
    flag_x = left_x + (cfg["PHOTO_W"] - cfg["FLAG_W"]) / 2
    flag_y = row2_bottom + (row2_height - cfg["FLAG_H"]) / 2

    render_flag(
        c,
        participant,
        flag_x,
        flag_y,
        cfg["FLAG_W"],
        cfg["FLAG_H"],
        debug=debug,
    )

    # COUNTRY centré
    render_text_box_centered(
        c,
        participant.pays or "",
        right_x,
        row2_bottom,
        right_w,
        row2_height,
        FONT_NAME,
        font_size=22,
        line_height=24,
        max_chars=18,
        debug=debug,
        debug_label="country",
    )

    # ============================================================
    # ROW 3 : PICTOS (pleine largeur)
    # ============================================================
    pictos_y = row2_bottom - cfg["SPACE_COUNTRY_TO_PICTOS"]

    render_pictos(
        c,
        participant,
        cfg["LEFT_MARGIN"],
        pictos_y,
        width - cfg["LEFT_MARGIN"] - cfg["RIGHT_MARGIN"],
        cfg["PICTO_SIZE"],
        cfg["PICTO_SPACING"],
        picto_map,
        debug=debug,
    )

    # ✅ IMPORTANT : vrai bas des pictos
    pictos_bottom = pictos_y - cfg["PICTO_SIZE"]

    # ============================================================
    # ROW 4 : ROLE
    # ============================================================
    label, color = get_style_role(participant.fonction)

    role_y = pictos_bottom - cfg["SPACE_PICTOS_TO_ROLE"] - BANDEAU_H

    # sécurité footer
    role_y = max(role_y, FOOTER_SPACE + cfg.get("FOOTER_SAFE_MARGIN", 10))

    render_role_bandeau(
        c,
        label,
        color,
        0,
        role_y,
        width,
        BANDEAU_H,
        debug=debug,
    )