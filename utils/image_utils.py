import os
from PIL import Image, ImageOps
import qrcode
from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H

QR_EC_MAP = {
    "L": ERROR_CORRECT_L,
    "M": ERROR_CORRECT_M,
    "Q": ERROR_CORRECT_Q,
    "H": ERROR_CORRECT_H,
}

from config import FLAGS_DIR, PHOTOS_DIR

from PIL import Image, ImageOps, ImageFilter, ImageEnhance

def load_photo(path, width, height, genre, upsample_factor=2):
    full_path = PHOTOS_DIR / path
    default_men = PHOTOS_DIR / "men.png"
    default_women = PHOTOS_DIR / "women.png"

    img_path = None

    if path and os.path.exists(full_path):
        img_path = full_path
    elif genre.lower() == "f":
        img_path = default_women
    else:
        img_path = default_men

    if img_path:
        img = Image.open(img_path).convert("RGB")

        # 1. Travailler en haute résolution puis downscaler (meilleure qualité)
        target_size = (width * upsample_factor, height * upsample_factor)
        img = ImageOps.fit(img, target_size, method=Image.LANCZOS)

        # 2. Légère netteté après redimensionnement
        img = img.filter(ImageFilter.UnsharpMask(radius=1, percent=120, threshold=3))

        # 3. Downscale final avec LANCZOS
        img = img.resize((width, height), Image.LANCZOS)

        return img

    return Image.new("RGB", (width, height), (220, 220, 220))

def load_flag(path, width, height, upsample_factor=2):
    full_path = FLAGS_DIR / path
    try:
        img = Image.open(full_path).convert("RGBA")  # RGBA pour préserver la transparence des PNG

        # 1. Upscale intermédiaire pour un meilleur rendu
        target_size = (width * upsample_factor, height * upsample_factor)
        img = ImageOps.contain(img, target_size, method=Image.LANCZOS)

        # 2. Légère netteté (plus douce que pour les photos — les drapeaux ont des aplats)
        img = img.filter(ImageFilter.UnsharpMask(radius=0.8, percent=100, threshold=2))

        # 3. Downscale final
        img = img.resize((width, height), Image.LANCZOS)

        # 4. Recomposite sur fond blanc si transparence
        background = Image.new("RGB", (width, height), (255, 255, 255))
        if img.mode == "RGBA":
            background.paste(img, mask=img.split()[3])
        else:
            background.paste(img)

        return background

    except Exception as e:
        return Image.new("RGB", (width, height), (240, 240, 240))


def generate_qr_code(
    data,
    size=200,
    border=2,
    box_size=10,
    error_correction="H",
):
    EC_MAP = {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H,
    }

    qr = qrcode.QRCode(
        version=None,
        error_correction=EC_MAP.get(error_correction.upper(), qrcode.constants.ERROR_CORRECT_H),
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # 1. Générer à haute résolution, downscaler ensuite
    hr_size = size * 2
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    qr_img = qr_img.resize((hr_size, hr_size), Image.Resampling.NEAREST)  # NEAREST : QR = pixels binaires

    # 2. Downscale final avec LANCZOS pour lisser les bords
    qr_img = qr_img.resize((size, size), Image.Resampling.LANCZOS)

    return qr_img

def generate_qr_with_logo(
    data,
    size=200,
    logo_path=None,
    logo_ratio=0.22,
    logo_padding=4,
    border=2,
    box_size=10,
    error_correction="H",
):
    EC_MAP = {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H,
    }

    qr = qrcode.QRCode(
        version=None,
        error_correction=EC_MAP.get(error_correction.upper(), qrcode.constants.ERROR_CORRECT_H),
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # 1. Générer à haute résolution, downscaler ensuite
    hr_size = size * 2
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    qr_img = qr_img.resize((hr_size, hr_size), Image.Resampling.NEAREST)  # NEAREST : QR = pixels binaires

    if logo_path:
        logo_path = Path(logo_path)
        if logo_path.exists():
            logo = Image.open(logo_path).convert("RGBA")

            logo_size = int(hr_size * logo_ratio)
            logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)

            # Fond blanc arrondi sous le logo
            bg_size = (logo.width + logo_padding * 2 * 2, logo.height + logo_padding * 2 * 2)
            bg = Image.new("RGBA", bg_size, (0, 0, 0, 0))

            # Coins arrondis sur le fond blanc
            from PIL import ImageDraw
            draw = ImageDraw.Draw(bg)
            radius = logo_padding * 2
            draw.rounded_rectangle([(0, 0), (bg.width - 1, bg.height - 1)], radius=radius, fill=(255, 255, 255, 255))

            logo_x = (bg.width - logo.width) // 2
            logo_y = (bg.height - logo.height) // 2
            bg.paste(logo, (logo_x, logo_y), logo)

            bg_x = (hr_size - bg.width) // 2
            bg_y = (hr_size - bg.height) // 2
            qr_img.paste(bg, (bg_x, bg_y), bg)

    # 2. Downscale final avec LANCZOS pour lisser les bords
    qr_img = qr_img.resize((size, size), Image.Resampling.LANCZOS)

    return qr_img