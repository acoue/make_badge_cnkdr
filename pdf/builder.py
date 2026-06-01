from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5

from pdf.badge_layout import draw_badge, draw_back_qr_layout
from pdf.header_footer import draw_header, draw_footer
from config import LAYOUT_MODE, BACKGROUND_COLOR,VERSO

def generate_pdf(participants, output):
    c = canvas.Canvas(output, pagesize=A5)
    width, height = A5
    c.setFillColor(BACKGROUND_COLOR)
    c.rect(0, 0, width, height, fill=1, stroke=0)

    for p in participants:
        # RECTO
        draw_header(c, width, height)
        draw_badge(c, p, layout_mode=LAYOUT_MODE)
        draw_footer(c, width)
        c.showPage()

        if VERSO:
            # VERSO (QR)
            draw_back_qr_layout(c, p, lines_count=3)
            c.showPage()

    c.save()