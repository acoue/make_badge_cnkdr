from reportlab.lib.utils import ImageReader

def draw_image(canvas, img, x, y, w, h):
    canvas.drawImage(ImageReader(img), x, y, w, h, mask="auto")