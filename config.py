from reportlab.lib import colors

FONT_NAME = "Helvetica"
FONT_BOLD_NAME = "Helvetica-Bold"

TITLE = "MERIGNAC 26 et 27 Septembre 2026"
SUBTITLE = ""
VERSO=True

DEFAULT_ROLE_STYLE = ("PARTICIPANT", colors.HexColor("#7C7D80"))
BACKGROUND_COLOR = colors.HexColor("#FFFFFF")
LAYOUT_MODE = "vertical"  # Options: vertical / editorial
LEFT_MARGIN = 50
RIGHT_MARGIN = 40
GUTTER = 30

LOGO_HEADER_PATH = "assets/logo.png"
LOGO_FOOTER_PATH = "assets/footer.png"
TOP_MARGIN_HEADER = 0
HEADER_SPACE = 100
HEADER_HEIGHT = 80
FOOTER_SPACE = 50
PHOTO_W = 120
PHOTO_H = 140
FLAG_W = 120
FLAG_H = 80
BANDEAU_H = 35
SIZE_PICTO = 40
SPACING_PICTO = 20

ROLE_STYLES = {
    "coach": ("COACH", colors.HexColor("#0E7490")),
    "competiteur": ("COMPÉTITEUR", colors.HexColor("#B91C1C")),
    "commissaire": ("COMMISSAIRE", colors.HexColor("#77670C")),
    "arbitre": ("ARBITRE", colors.HexColor("#4F46E5")),
    "bénévole": ("BÉNÉVOLE", colors.HexColor("#15803D")),
}

OPTION_PICTO_MAP = {
    "bus": "assets/bus.png",
    "sayo": "assets/fete.png",
    "lunch": "assets/lunch.png",
}