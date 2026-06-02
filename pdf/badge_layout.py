
from pdf.make_badge_editorial import draw_editorial_layout
from pdf.make_badge_vertical import draw_vertical_layout
from config import OPTION_PICTO_MAP


def draw_badge(c, participant, layout_mode="vertical", picto_map=None, debug=False):
    if picto_map is None:
        picto_map = OPTION_PICTO_MAP

    if layout_mode == "editorial":
        draw_editorial_layout(c, participant, picto_map, debug=debug)
    else:
        draw_vertical_layout(c, participant, picto_map, debug=debug)
