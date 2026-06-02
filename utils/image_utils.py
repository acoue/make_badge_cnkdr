import os
from PIL import Image, ImageOps
import qrcode

from config import ASSETS_DIR, FLAGS_DIR, PHOTOS_DIR

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

    # ✅ 4. dernier fallback (sécurité)
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
