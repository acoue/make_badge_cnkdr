
from config import FONT_NAME

def debug_box(c, x, y, w, h, label="block"):
    c.saveState()
    c.setStrokeColor('black')
    c.setLineWidth(0.8)
    c.rect(x, y, w, h, fill=0, stroke=1)

    c.setFont(FONT_NAME, 6)
    c.drawString(x + 2, y + h - 8, label)
    c.restoreState()
