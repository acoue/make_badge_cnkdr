
from reportlab.lib.pagesizes import A5
from utils.canvas_utils import draw_image
from pdf.make_badge_editorial import draw_editorial_layout
from pdf.make_badge_vertical import draw_vertical_layout
from utils.image_utils import generate_qr_code
from reportlab.lib.pagesizes import A5
from config import OPTION_PICTO_MAP

def draw_back_qr_layout(c, participant, lines_count=2, debug=False):
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

def draw_badge(c, participant, layout_mode="vertical", picto_map=None, debug=False):
    if picto_map is None:
        picto_map = OPTION_PICTO_MAP

    if layout_mode == "editorial":
        draw_editorial_layout(c, participant, picto_map, debug=debug)
    else:
        draw_vertical_layout(c, participant, picto_map, debug=debug)
