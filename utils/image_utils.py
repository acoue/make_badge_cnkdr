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

def load_photo(path, width, height, genre):
    full_path = PHOTOS_DIR / path
    default_men = PHOTOS_DIR / "men.png"
    default_women = PHOTOS_DIR / "women.png"

    img_path = None

    if path and os.path.exists(full_path):
        img_path = full_path
    else:
        if not path or not os.path.exists(path):
            if genre.lower() == "f":
                img_path = default_women
            else:
                img_path = default_men

    if img_path:
        img = Image.open(img_path).convert("RGB")
        return ImageOps.fit(img, (width, height))

    return Image.new("RGB", (width, height), (220, 220, 220))


def load_flag(path, width, height):
    full_path = FLAGS_DIR / path
    try:
        img = Image.open(full_path).convert("RGB")
        return ImageOps.contain(img, (width, height))
    except:
        return Image.new("RGB", (width, height), (240, 240, 240))


def generate_qr_code(data, size=200):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=2
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    return img.resize((size, size))


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
    qr = qrcode.QRCode(
        version=None,
        error_correction=QR_EC_MAP.get(error_correction, ERROR_CORRECT_H),
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    qr_img = qr_img.resize((size, size), Image.Resampling.LANCZOS)

    if logo_path:
        logo_path = Path(logo_path)
        if logo_path.exists():
            logo = Image.open(logo_path).convert("RGBA")

            logo_size = int(size * logo_ratio)
            logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)

            # petit fond blanc sous le logo pour préserver la lisibilité du QR
            bg_size = (logo.width + logo_padding * 2, logo.height + logo_padding * 2)
            bg = Image.new("RGBA", bg_size, (255, 255, 255, 255))

            logo_x = (bg.width - logo.width) // 2
            logo_y = (bg.height - logo.height) // 2
            bg.paste(logo, (logo_x, logo_y), logo)

            bg_x = (size - bg.width) // 2
            bg_y = (size - bg.height) // 2

            qr_img.paste(bg, (bg_x, bg_y), bg)

    return qr_img
