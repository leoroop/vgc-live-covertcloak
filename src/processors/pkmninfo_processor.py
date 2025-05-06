import cv2

from src.contants.colors_constants import red_color, line_style
from src.models import PkmnInfoCoordinatesModel
from utils import Utils


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

    @staticmethod
    def pkmninfo_is_active(masked_frame, pkmninfo_coordinates: PkmnInfoCoordinatesModel) -> bool:
        marker1_area = Utils.get_marker_area(pkmninfo_coordinates.pkmninfo1_x_offset, pkmninfo_coordinates.pkmninfo1_y_offset)
        marker2_area = Utils.get_marker_area(pkmninfo_coordinates.pkmninfo2_x_offset, pkmninfo_coordinates.pkmninfo2_y_offset)
        marker3_area = Utils.get_marker_area(pkmninfo_coordinates.pkmninfo3_x_offset, pkmninfo_coordinates.pkmninfo3_y_offset)
        marker4_area = Utils.get_marker_area(pkmninfo_coordinates.pkmninfo4_x_offset, pkmninfo_coordinates.pkmninfo4_y_offset)

        bluearea_1 = masked_frame[
             pkmninfo_coordinates.pkmninfo1_y: pkmninfo_coordinates.pkmninfo1_y + pkmninfo_coordinates.pkmninfo1_y_offset,
             pkmninfo_coordinates.pkmninfo1_x: pkmninfo_coordinates.pkmninfo1_x + pkmninfo_coordinates.pkmninfo1_x_offset,
        ]
        bluearea_2 = masked_frame[
             pkmninfo_coordinates.pkmninfo2_y: pkmninfo_coordinates.pkmninfo2_y + pkmninfo_coordinates.pkmninfo2_y_offset,
             pkmninfo_coordinates.pkmninfo2_x: pkmninfo_coordinates.pkmninfo2_x + pkmninfo_coordinates.pkmninfo2_x_offset,
        ]
        bluearea_3 = masked_frame[
             pkmninfo_coordinates.pkmninfo3_y: pkmninfo_coordinates.pkmninfo3_y + pkmninfo_coordinates.pkmninfo3_y_offset,
             pkmninfo_coordinates.pkmninfo3_x: pkmninfo_coordinates.pkmninfo3_x + pkmninfo_coordinates.pkmninfo3_x_offset,
        ]
        bluearea_4 = masked_frame[
             pkmninfo_coordinates.pkmninfo4_y: pkmninfo_coordinates.pkmninfo4_y + pkmninfo_coordinates.pkmninfo4_y_offset,
             pkmninfo_coordinates.pkmninfo4_x: pkmninfo_coordinates.pkmninfo4_x + pkmninfo_coordinates.pkmninfo4_x_offset,
        ]

        bluearea1_pixels = cv2.countNonZero(bluearea_1)
        bluearea2_pixels = cv2.countNonZero(bluearea_2)
        bluearea3_pixels = cv2.countNonZero(bluearea_3)
        bluearea4_pixels = cv2.countNonZero(bluearea_4)

        return (
                bluearea1_pixels >= (marker1_area * 0.60) and
                bluearea2_pixels >= (marker2_area * 0.60) and
                bluearea3_pixels >= (marker3_area * 0.60) and
                bluearea4_pixels >= (marker4_area * 0.60)
        )