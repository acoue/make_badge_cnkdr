from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5

from pdf.header_footer import draw_header, draw_footer
from pdf.make_badge_vertical import draw_vertical_layout
from pdf.make_badge_editorial import draw_editorial_layout
from pdf.make_verso import draw_back_qr_layout
from config import DOCUMENT_RECTO_VERSO, OPTION_PICTO_MAP, PROJECT_NAME, AUTHOR


def generate_pdf(participants, output, layout_mode="vertical", debug=False):
    c = canvas.Canvas(output, pagesize=A5)
    c.setTitle(PROJECT_NAME)
    c.setAuthor(AUTHOR)
    c.setPageCompression(1)
    width, height = A5

    for p in participants:
        # RECTO
        draw_header(c, width, height)

        if layout_mode == "editorial":
            draw_editorial_layout(c, p, OPTION_PICTO_MAP, debug=debug)
        else:
            draw_vertical_layout(c, p, OPTION_PICTO_MAP, debug=debug)

        draw_footer(c, width)
        c.showPage()

        # VERSO
        if DOCUMENT_RECTO_VERSO:
            draw_back_qr_layout(c, p, debug=debug)
            c.showPage()

    c.save()