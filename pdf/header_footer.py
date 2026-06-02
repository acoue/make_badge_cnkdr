from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
import os
from PIL import Image
from config import SPACE_HEADER_TO_TITRE, TITLE, SUBTITLE, LOGO_HEADER_PATH, LOGO_FOOTER_PATH, HEADER_HEIGHT, TOP_MARGIN_HEADER,FONT_BOLD_NAME, FONT_NAME


def draw_header(c, width, height):
    """
    Header avec :
    - image header pleine largeur
    - texte en dessous
    """

    if os.path.exists(LOGO_HEADER_PATH):
        c.drawImage(
            ImageReader(LOGO_HEADER_PATH),
            0,
            height - HEADER_HEIGHT - TOP_MARGIN_HEADER,
            width=width,
            height=HEADER_HEIGHT,
            preserveAspectRatio=True,
            mask='auto'
        )

    # Texte sous le header
    text_y = height - HEADER_HEIGHT - SPACE_HEADER_TO_TITRE

    c.setFillColor(colors.black)
    c.setFont(FONT_BOLD_NAME, 10)
    c.drawCentredString(width / 2, text_y, TITLE)

    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.setFont(FONT_NAME, 8)
    c.drawCentredString(width / 2, text_y - 13, SUBTITLE)

def draw_footer(c, width):

    if os.path.exists(LOGO_FOOTER_PATH):
        img = Image.open(LOGO_FOOTER_PATH)

        img_width, img_height = img.size
        ratio = img_height / img_width

        footer_height = width * ratio

        c.drawImage(
            ImageReader(img),
            0,
            0,
            width=width,
            height=footer_height,
            preserveAspectRatio=False,  # OK car on calcule nous-mêmes
            mask='auto'
        )
