from reportlab.lib import colors
from pathlib import Path

# ============================================================
# 🧾 METADATA PROJET
# ============================================================
# Informations générales sur le projet (utilisables pour PDF, footer, etc.)

PROJECT_NAME = "Badge Generator CNKDR"
AUTHOR = "Anthony Coué"
LICENSE = "MIT"

# ============================================================
# 🌍 GLOBAL / DOCUMENT
# ============================================================

# Titre principal affiché sur le badge (header texte)
TITLE = "MERIGNAC 26 et 27 Septembre 2026"

# Sous-titre (optionnel)
SUBTITLE = ""

# Permet d'activer une logique recto / verso (non utilisé actuellement)
DOCUMENT_RECTO_VERSO = True

# Polices utilisées dans le PDF
FONT_NAME = "Helvetica"
FONT_BOLD_NAME = "Helvetica-Bold"

# Couleur de fond du badge
BACKGROUND_COLOR = colors.HexColor("#FFFFFF")

BORDER_PHOTO_WIDTH = 1
BORDER_FLAG_WIDTH = 1

BORDER_PHOTO_COLOR = colors.HexColor("#333333")
BORDER_FLAG_COLOR = colors.HexColor("#000000")

# ============================================================
# 📁 CHEMINS (ASSETS)
# ============================================================

BASE_DIR = Path(__file__).parent

ASSETS_DIR = BASE_DIR / "assets"

PHOTOS_DIR = ASSETS_DIR / "photos"
FLAGS_DIR = ASSETS_DIR / "flags"
PICTOS_DIR = ASSETS_DIR / "pictos"


# ============================================================
# 🖼️ ASSETS (images)
# ============================================================

# Logo en haut du badge
LOGO_HEADER_PATH = ASSETS_DIR / "logo.png"

# Image du footer (élément graphique bas)
LOGO_FOOTER_PATH = ASSETS_DIR / "footer.png"

# Mapping des pictogrammes (utilisé avec la colonne "options" du CSV)
OPTION_PICTO_MAP = {
    "bus": PICTOS_DIR / "bus.png",
    "sayo": PICTOS_DIR / "fete.png",
    "lunch": PICTOS_DIR / "lunch.png",
}

# ============================================================
# 🎯 ROLES (bandeau bas)
# ============================================================

# Style par défaut si la fonction n’est pas reconnue
DEFAULT_ROLE_STYLE = ("PARTICIPANT", colors.HexColor("#7C7D80"))

# Mapping rôle → (libellé, couleur)
ROLE_STYLES = {
    "coach": ("COACH", colors.HexColor("#0E7490")),
    "competiteur": ("COMPÉTITEUR", colors.HexColor("#B91C1C")),
    "commissaire": ("COMMISSAIRE", colors.HexColor("#77670C")),
    "referee": ("ARBITRE", colors.HexColor("#4F46E5")),
    "bénévole": ("BÉNÉVOLE", colors.HexColor("#15803D")),
    "delegation": ("DÉLÉGATION", colors.HexColor("#7C3AED")),
}

# Hauteur du bandeau rôle
BANDEAU_H = 35


# ============================================================
# 📄 PAGE / ZONES
# ============================================================

# Hauteur réelle du header (image)
HEADER_HEIGHT = 80

# Espace réservé sous le header avant le contenu
HEADER_SPACE = 100

# Hauteur réservée au footer (zone interdite pour le contenu)
FOOTER_SPACE = 100

# Marge au-dessus du header
TOP_MARGIN_HEADER = 0

# Espace entre le header et le titre
SPACE_HEADER_TO_TITRE = 15


# ============================================================
# 🎯 PICTOS (DEFAULT GLOBAL)
# ============================================================

# Taille par défaut d'un pictogramme
DEFAULT_PICTO_SIZE = 40

# Espacement horizontal entre pictos
DEFAULT_PICTO_SPACING = 20

# ============================================================
# 📋 LAYOUT VERTICAL
# ============================================================

VERTICAL = {

    # --------------------
    # 📏 Tailles des blocs
    # --------------------
    "PHOTO_W": 110,
    "PHOTO_H": 140,

    "FLAG_W": 70,
    "FLAG_H": 42,

    "NAME_BOX_W": 500,
    "NAME_BOX_H": 25,

    "FREE_TEXT_BOX_W": 500,
    "FREE_TEXT_BOX_H": 25,

    "COUNTRY_BOX_W": 300,
    "COUNTRY_BOX_H": 25,

    "PICTO_BOX_W": 200,
    "PICTO_BOX_H": 40,

    # --------------------
    # 🎯 Pictos
    # --------------------
    "PICTO_SIZE": 30,        # taille des icônes
    "PICTO_SPACING": 10,     # espace entre icônes

    # --------------------
    # 📐 Espacements verticaux
    # --------------------
    "SPACE_PHOTO_TO_NAME": 5,
    "SPACE_NAME_TO_TEXT": 5,
    "SPACE_TEXT_TO_FLAG": 5,
    "SPACE_FLAG_TO_COUNTRY": 5,
    "SPACE_COUNTRY_TO_PICTOS": 10,
    "SPACE_PICTOS_TO_ROLE": 5,
}


# ============================================================
# 📰 LAYOUT EDITORIAL (row / column)
# ============================================================

EDITORIAL = {

    # --------------------
    # 📐 Marges globales
    # --------------------
    "TOP_CONTENT_MARGIN": 20,   # espace sous le header

    "LEFT_MARGIN": 30,
    "RIGHT_MARGIN": 30,

    "COLUMN_GUTTER": 20,  # espace entre colonne photo et texte

    # --------------------
    # 📏 Tailles des blocs
    # --------------------
    "PHOTO_W": 130,
    "PHOTO_H": 170,

    "FLAG_W": 90,
    "FLAG_H": 50,

    "NAME_BOX_W": 250,
    "NAME_BOX_H": 60,

    "FREE_TEXT_BOX_W": 250,
    "FREE_TEXT_BOX_H": 60,

    "COUNTRY_BOX_W": 250,
    "COUNTRY_BOX_H": 50,

    "PICTO_BOX_W": 250,
    "PICTO_BOX_H": 50,

    # --------------------
    # 🎯 Pictos
    # --------------------
    "PICTO_SIZE": 40,
    "PICTO_SPACING": 10,

    # --------------------
    # 📐 Layout interne
    # --------------------
    "NAME_TOP_MARGIN": 10,
    "TEXT_LIBRE_MARGIN": 10,
    "ROW_FLAG_COUNTRY_MARGIN": 10,

    # --------------------
    # 📐 Espacements
    # --------------------
    "SPACE_NAME_TO_TEXT": 10,
    "SPACE_TEXT_TO_FLAGROW": 10,
    "SPACE_FLAG_TO_COUNTRY": 10,
    "SPACE_COUNTRY_TO_PICTOS": 20,
    "SPACE_PICTOS_TO_ROLE": 10,

    # --------------------
    # 🛡️ Sécurité visuelle
    # --------------------
    "FOOTER_SAFE_MARGIN": 10,   # évite chevauchement avec footer
}

# ============================================================
# 🔳 VERSO / QR CODE
# ============================================================
QR_BACK = {
    # Titre optionnel du verso
    "TITLE": "Informations & accès",

    # Mise en page générale
    "TOP_MARGIN": 45,
    "BOTTOM_MARGIN": 45,
    "LEFT_MARGIN": 25,
    "RIGHT_MARGIN": 25,
    "ROW_GAP": 22,
    "COL_GAP": 18,

    # QR
    "QR_SIZE": 90,
    "QR_BORDER": 2,
    "QR_BOX_SIZE": 10,
    "QR_ERROR_CORRECTION": "H",

    # Logo au centre du QR (petit logo)
    "QR_LOGO_PATH": ASSETS_DIR / "qr_center_logo.png",
    "QR_LOGO_RATIO": 0.22,   # 22% de la largeur du QR
    "QR_LOGO_PADDING": 4,    # fond blanc autour du logo

    # Texte sous chaque QR
    "LABEL_FONT_NAME": "Helvetica",
    "LABEL_FONT_SIZE": 9,
    "LABEL_LINE_HEIGHT": 11,
    "LABEL_MAX_CHARS": 22,
}

# ============================================================
# 🔳 LIGNES DE QR À GÉNÉRER SUR LE VERSO
# Chaque élément de la liste = une ligne
# Chaque ligne = une liste de QR
# ============================================================
BACK_QR_ROWS = [
    [
        {
            "label": "Location",
            "data": "https://www.ejc2026.fr/location/"
        },
        {
            "label": "Schedule",
            "data": "https://www.ejc2026.fr/schedule/"
        },
        {
            "label": "Rules and Regulations",
            "data": "https://www.ejc2026.fr/rules-and-regulations/"
        },

    ],
    [
        {
            "label": "Transport",
            "data": "https://ejc2026.fr/transport"
        },
        {
            "label": "Competitors Lunch",
            "data": "https://www.ejc2026.fr/competitors-lunch/"
        },
        {
            "label": "Official’s Lunch",
            "data": "https://www.ejc2026.fr/officiels-lunch/"
        },
    ],
    [
        {
            "label": "Contact",
            "data": "https://www.ejc2026.fr/contact/"
        },
    ]
]
