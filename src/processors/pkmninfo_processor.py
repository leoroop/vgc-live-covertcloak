import cv2

from src.contants.colors_constants import red_color, line_style
from src.models import PkmnInfoCoordinatesModel


class PkmnInfoProcessor:
    @staticmethod
    def apply_pkmninfo_markers(frame, pkmninfo: PkmnInfoCoordinatesModel):
        cv2.rectangle(
            frame,
            (pkmninfo.pkmninfo1_x, pkmninfo.pkmninfo1_y),
            (pkmninfo.pkmninfo1_x + pkmninfo.pkmninfo1_x_offset, pkmninfo.pkmninfo1_y + pkmninfo.pkmninfo1_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (pkmninfo.pkmninfo2_x, pkmninfo.pkmninfo2_y),
            (pkmninfo.pkmninfo2_x + pkmninfo.pkmninfo2_x_offset, pkmninfo.pkmninfo2_y + pkmninfo.pkmninfo2_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (pkmninfo.pkmninfo3_x, pkmninfo.pkmninfo3_y),
            (pkmninfo.pkmninfo3_x + pkmninfo.pkmninfo3_x_offset, pkmninfo.pkmninfo3_y + pkmninfo.pkmninfo3_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (pkmninfo.pkmninfo4_x, pkmninfo.pkmninfo4_y),
            (pkmninfo.pkmninfo4_x + pkmninfo.pkmninfo4_x_offset, pkmninfo.pkmninfo4_y + pkmninfo.pkmninfo4_y_offset),
            red_color,
            line_style
        )