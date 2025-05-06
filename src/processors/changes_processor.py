import cv2

from src.contants.colors_constants import red_color, line_style
from src.models import ChangesCoordinatesModel
from utils import Utils


class ChangesProcessor:
    @staticmethod
    def apply_changes_markers(frame, changes: ChangesCoordinatesModel):
        cv2.rectangle(
            frame,
            (changes.changes_x, changes.change1_y),
            (changes.changes_x + changes.changes_x_offset, changes.change1_y + changes.changes_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (changes.changes_x, changes.change2_y),
            (changes.changes_x + changes.changes_x_offset, changes.change2_y + changes.changes_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (changes.changes_x, changes.change3_y),
            (changes.changes_x + changes.changes_x_offset, changes.change3_y + changes.changes_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (changes.changes_x, changes.change4_y),
            (changes.changes_x + changes.changes_x_offset,
             changes.change4_y + changes.changes_y_offset),
            red_color,
            line_style
        )

    @staticmethod
    def check_if_change_pokemon_selection(masked_frame, changes_coordinates: ChangesCoordinatesModel) -> bool:
        marker_area = Utils.get_marker_area(changes_coordinates.changes_x_offset, changes_coordinates.changes_y_offset)
        change_1 = masked_frame[
                 changes_coordinates.change1_y: changes_coordinates.change1_y + changes_coordinates.changes_y_offset,
                 changes_coordinates.changes_x: changes_coordinates.changes_x + changes_coordinates.changes_x_offset,
                 ]
        change_2 = masked_frame[
                 changes_coordinates.change2_y: changes_coordinates.change2_y + changes_coordinates.changes_y_offset,
                 changes_coordinates.changes_x: changes_coordinates.changes_x + changes_coordinates.changes_x_offset,
                 ]
        change_3 = masked_frame[
                 changes_coordinates.change3_y: changes_coordinates.change3_y + changes_coordinates.changes_y_offset,
                 changes_coordinates.changes_x: changes_coordinates.changes_x + changes_coordinates.changes_x_offset,
                 ]
        change_4 = masked_frame[
                 changes_coordinates.change4_y: changes_coordinates.change4_y + changes_coordinates.changes_y_offset,
                 changes_coordinates.changes_x: changes_coordinates.changes_x + changes_coordinates.changes_x_offset,
                 ]


        change1_pixels = cv2.countNonZero(change_1)
        change2_pixels = cv2.countNonZero(change_2)
        change3_pixels = cv2.countNonZero(change_3)
        change4_pixels = cv2.countNonZero(change_4)

        return (
                change1_pixels >= (marker_area * 0.70) or
                change2_pixels >= (marker_area * 0.70) or
                change3_pixels >= (marker_area * 0.70) or
                change4_pixels >= (marker_area * 0.70)
        )