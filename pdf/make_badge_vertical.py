from reportlab.lib.pagesizes import A5

from config import (
    HEADER_SPACE,
    FOOTER_SPACE,
    BANDEAU_H,
    FONT_BOLD_NAME,
    FONT_NAME,
    VERTICAL,
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


# def draw_vertical_layout(c, participant, picto_map):
#     width, height = A5
#     center_x = width / 2
#     cfg = VERTICAL

#     # ------------------------------------------------------------------
#     # current_y = HAUT du prochain bloc à dessiner
#     # ------------------------------------------------------------------
#     current_y = height - HEADER_SPACE

#     # =====================
#     # PHOTO
#     # =====================
#     photo_w = cfg["PHOTO_W"]
#     photo_h = cfg["PHOTO_H"]
#     photo_x = center_x - (photo_w / 2)
#     photo_bottom_y = current_y - photo_h

#     render_photo(
#         c,
#         participant,
#         photo_x,
#         photo_bottom_y,
#         photo_w,
#         photo_h,
#     )

#     current_y = photo_bottom_y - cfg["SPACE_PHOTO_TO_NAME"]

#     # =====================
#     # NOM
#     # =====================
#     name_w = cfg["NAME_BOX_W"]
#     name_h = cfg["NAME_BOX_H"]
#     name_x = center_x - (name_w / 2)
#     name_bottom_y = current_y - name_h

#     render_text_box_centered(
#         c,
#         f"{participant.prenom} {participant.nom}",
#         name_x,
#         name_bottom_y,
#         name_w,
#         name_h,
#         FONT_BOLD_NAME,
#         font_size=18,
#         line_height=20,
#         max_chars=20,
#         debug_label="name",
#     )

#     current_y = name_bottom_y - cfg["SPACE_NAME_TO_TEXT"]

#     # =====================
#     # TEXTE LIBRE
#     # =====================
#     free_w = cfg["FREE_TEXT_BOX_W"]
#     free_h = cfg["FREE_TEXT_BOX_H"]
#     free_x = center_x - (free_w / 2)
#     free_bottom_y = current_y - free_h

#     render_text_box_centered(
#         c,
#         getattr(participant, "ligne_libre", ""),
#         free_x,
#         free_bottom_y,
#         free_w,
#         free_h,
#         FONT_NAME,
#         font_size=13,
#         line_height=15,
#         max_chars=28,
#         debug_label="text",
#     )

#     current_y = free_bottom_y - cfg["SPACE_TEXT_TO_FLAG"]

#     # =====================
#     # DRAPEAU
#     # =====================
#     flag_w = cfg["FLAG_W"]
#     flag_h = cfg["FLAG_H"]
#     flag_x = center_x - (flag_w / 2)
#     flag_bottom_y = current_y - flag_h

#     render_flag(
#         c,
#         participant,
#         flag_x,
#         flag_bottom_y,
#         flag_w,
#         flag_h,
#     )

#     current_y = flag_bottom_y - cfg["SPACE_FLAG_TO_COUNTRY"]

#     # =====================
#     # PAYS
#     # =====================
#     country_w = cfg["COUNTRY_BOX_W"]
#     country_h = cfg["COUNTRY_BOX_H"]
#     country_x = center_x - (country_w / 2)
#     country_bottom_y = current_y - country_h

#     render_text_box_centered(
#         c,
#         participant.pays or "",
#         country_x,
#         country_bottom_y,
#         country_w,
#         country_h,
#         FONT_NAME,
#         font_size=20,
#         line_height=22,
#         max_chars=18,
#         debug_label="country",
#     )

#     current_y = country_bottom_y - cfg["SPACE_COUNTRY_TO_PICTOS"]

#     # =====================
#     # PICTOS
#     # =====================
#     picto_box_w = cfg["PICTO_BOX_W"]
#     picto_box_x = center_x - (picto_box_w / 2)

#     # IMPORTANT :
#     # render_pictos attend un y "haut du bloc"
#     # et renvoie le y disponible suivant
#     current_y = render_pictos(
#         c,
#         participant,
#         picto_box_x,
#         current_y,
#         picto_box_w,
#         cfg["PICTO_SIZE"],
#         cfg["PICTO_SPACING"],
#         picto_map,
#     )

#     # =====================
#     # ROLE
#     # =====================
#     label, color = get_style_role(participant.fonction)

#     # current_y est maintenant le y dispo SOUS les pictos
#     role_bottom_y = current_y - cfg["SPACE_PICTOS_TO_ROLE"] - BANDEAU_H

#     # sécurité : éviter de passer sous le footer
#     role_bottom_y = max(role_bottom_y, FOOTER_SPACE + 4)

#     render_role_bandeau(
#         c,
#         label,
#         color,
#         0,
#         role_bottom_y,
#         width,
#         BANDEAU_H,
#     )
def draw_vertical_layout(c, participant, picto_map, debug=False):
    width, height = A5
    center_x = width / 2
    cfg = VERTICAL

    # ✅ point de départ unique
    current_y = height - HEADER_SPACE

    # =====================
    # PHOTO
    # =====================
    photo_w = cfg["PHOTO_W"]
    photo_h = cfg["PHOTO_H"]
    photo_x = center_x - photo_w / 2

    render_photo(
        c,
        participant,
        photo_x,
        current_y - photo_h,
        photo_w,
        photo_h,
        debug= debug,
    )

    current_y -= photo_h
    current_y -= cfg["SPACE_PHOTO_TO_NAME"]

    # =====================
    # NOM
    # =====================
    name_w = cfg["NAME_BOX_W"]
    name_h = cfg["NAME_BOX_H"]

    render_text_box_centered(
        c,
        f"{participant.prenom} {participant.nom}",
        center_x - name_w / 2,
        current_y - name_h,
        name_w,
        name_h,
        FONT_BOLD_NAME,
        font_size=18,
        line_height=20,
        max_chars=20,
        debug= debug,
        debug_label="name",
    )

    current_y -= name_h
    current_y -= cfg["SPACE_NAME_TO_TEXT"]

    # =====================
    # TEXTE LIBRE
    # =====================
    free_w = cfg["FREE_TEXT_BOX_W"]
    free_h = cfg["FREE_TEXT_BOX_H"]

    render_text_box_centered(
        c,
        getattr(participant, "ligne_libre", ""),
        center_x - free_w / 2,
        current_y - free_h,
        free_w,
        free_h,
        FONT_NAME,
        font_size=13,
        line_height=15,
        max_chars=28,
        debug= debug,
        debug_label="text",
    )

    current_y -= free_h
    current_y -= cfg["SPACE_TEXT_TO_FLAG"]

    # =====================
    # DRAPEAU
    # =====================
    flag_w = cfg["FLAG_W"]
    flag_h = cfg["FLAG_H"]
    flag_x = center_x - flag_w / 2

    render_flag(
        c,
        participant,
        flag_x,
        current_y - flag_h,
        flag_w,
        flag_h,
        debug= debug,
    )

    current_y -= flag_h
    current_y -= cfg["SPACE_FLAG_TO_COUNTRY"]

    # =====================
    # PAYS
    # =====================
    country_w = cfg["COUNTRY_BOX_W"]
    country_h = cfg["COUNTRY_BOX_H"]

    render_text_box_centered(
        c,
        participant.pays or "",
        center_x - country_w / 2,
        current_y - country_h,
        country_w,
        country_h,
        FONT_NAME,
        font_size=20,
        line_height=22,
        max_chars=18,
        debug=debug,
        debug_label="country",
    )

    current_y -= country_h
    current_y -= cfg["SPACE_COUNTRY_TO_PICTOS"]

    # =====================
    # PICTOS
    # =====================
    current_y = render_pictos(
        c,
        participant,
        center_x - cfg["PICTO_BOX_W"] / 2,
        current_y,
        cfg["PICTO_BOX_W"],
        cfg["PICTO_SIZE"],
        cfg["PICTO_SPACING"],
        picto_map,
        debug= debug,
    )

    current_y -= cfg["SPACE_PICTOS_TO_ROLE"]

    # =====================
    # ROLE
    # =====================
    label, color = get_style_role(participant.fonction)

    render_role_bandeau(
        c,
        label,
        color,
        0,
        current_y - BANDEAU_H,
        width,
        BANDEAU_H,
        debug= debug,
    )