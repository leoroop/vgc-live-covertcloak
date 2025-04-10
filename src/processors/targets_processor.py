import cv2

from src.contants.colors_constants import red_color, line_style
from src.models import TargetsCoordinatesModel


class TargetsProcessor:
    @classmethod
    def apply_targets_markers(cls, frame, targets: TargetsCoordinatesModel):
       cls.__apply_top_left_marker(frame, targets)
       cls.__apply_top_right_marker(frame, targets)
       cls.__apply_bottom_left_marker(frame, targets)
       cls.__apply_bottom_right_marker(frame, targets)

    @staticmethod
    def __apply_top_left_marker(frame, targets: TargetsCoordinatesModel):
        cv2.rectangle(
            frame,
            (targets.target_left, targets.target_top),
            (targets.target_left + targets.target_x_offset, targets.target_top + targets.target_y_offset),
            red_color,
            line_style
        )

    @staticmethod
    def __apply_top_right_marker(frame, targets: TargetsCoordinatesModel):
        cv2.rectangle(
            frame,
            (targets.target_right, targets.target_top),
            (targets.target_right + targets.target_x_offset, targets.target_top + targets.target_y_offset),
            red_color,
            line_style
        )

    @staticmethod
    def __apply_bottom_left_marker(frame, targets: TargetsCoordinatesModel):
        cv2.rectangle(
            frame,
            (targets.target_left, targets.target_bottom),
            (targets.target_left + targets.target_x_offset, targets.target_bottom + targets.target_y_offset),
            red_color,
            line_style
        )

    @staticmethod
    def __apply_bottom_right_marker(frame, targets: TargetsCoordinatesModel):
        cv2.rectangle(
            frame,
            (targets.target_right, targets.target_bottom),
            (targets.target_right + targets.target_x_offset, targets.target_bottom + targets.target_y_offset),
            red_color,
            line_style
        )