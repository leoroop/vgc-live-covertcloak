import cv2

from src.contants.colors import red_color, line_style
from src.models import ChangesCoordinatesModel


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