import cv2

from src.calculators import TargetsCoordinatesCalculator
from src.contants.colors_constants import red_color, line_style
from src.models import TargetsCoordinatesModel
from src.utils import Utils


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

    @staticmethod
    def check_if_target_selection(masked_frame, targets_coordinates: TargetsCoordinatesModel) -> bool:
        marker_area = Utils.get_marker_area(targets_coordinates.target_x_offset, targets_coordinates.target_y_offset)
        target_top_left = masked_frame[
                 targets_coordinates.target_top: targets_coordinates.target_top + targets_coordinates.target_y_offset,
                 targets_coordinates.target_left: targets_coordinates.target_left + targets_coordinates.target_x_offset,
                 ]

        target_top_right = masked_frame[
                 targets_coordinates.target_top: targets_coordinates.target_top + targets_coordinates.target_y_offset,
                 targets_coordinates.target_right: targets_coordinates.target_right + targets_coordinates.target_x_offset,
                 ]

        target_bottom_left = masked_frame[
                 targets_coordinates.target_bottom: targets_coordinates.target_bottom + targets_coordinates.target_y_offset,
                 targets_coordinates.target_left: targets_coordinates.target_left + targets_coordinates.target_x_offset,
                 ]
        target_bottom_right = masked_frame[
                 targets_coordinates.target_bottom: targets_coordinates.target_bottom + targets_coordinates.target_y_offset,
                 targets_coordinates.target_right: targets_coordinates.target_right + targets_coordinates.target_x_offset,
                 ]

        target_top_left_pixels = cv2.countNonZero(target_top_left)
        target_top_right_pixels = cv2.countNonZero(target_top_right)
        target_bottom_left_pixels = cv2.countNonZero(target_bottom_left)
        target_bottom_right_pixels = cv2.countNonZero(target_bottom_right)

        return (
                target_top_left_pixels >= (marker_area * 0.30) or
                target_top_right_pixels >= (marker_area * 0.30) or
                target_bottom_left_pixels >= (marker_area * 0.30) or
                target_bottom_right_pixels >= (marker_area * 0.30)
        )