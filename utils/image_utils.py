import os
from PIL import Image, ImageOps
import qrcode

ASSETS_PATH = "assets"


def load_photo(path, width, height, genre):
    default_men = os.path.join(ASSETS_PATH, "men.png")
    default_women = os.path.join(ASSETS_PATH, "women.png")

    img_path = None

    if path and os.path.exists(path):
        img_path = path
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
    try:
        img = Image.open(path).convert("RGB")
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
