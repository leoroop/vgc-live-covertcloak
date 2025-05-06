import cv2

from src.contants.colors_constants import red_color, line_style
from src.models import BattleMenuOptionsCoordinatesModel
from utils import Utils


class BattleMenuOptionsProcessor:
    @staticmethod
    def apply_battlemenuoptions_markers(frame, battlemenuoptions: BattleMenuOptionsCoordinatesModel):
        cv2.rectangle(
            frame,
            (battlemenuoptions.options_x, battlemenuoptions.option1_y),
            (battlemenuoptions.options_x + battlemenuoptions.options_x_offset, battlemenuoptions.option1_y + battlemenuoptions.options_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (battlemenuoptions.options_x, battlemenuoptions.option2_y),
            (battlemenuoptions.options_x + battlemenuoptions.options_x_offset, battlemenuoptions.option2_y + battlemenuoptions.options_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (battlemenuoptions.options_x, battlemenuoptions.option3_y),
            (battlemenuoptions.options_x + battlemenuoptions.options_x_offset, battlemenuoptions.option3_y + battlemenuoptions.options_y_offset),
            red_color,
            line_style
        )

    @staticmethod
    def check_if_option_selection(masked_frame, battlemenuoptions: BattleMenuOptionsCoordinatesModel) -> bool:
        marker_area = Utils.get_marker_area(battlemenuoptions.options_x_offset, battlemenuoptions.options_y_offset)
        option_1 = masked_frame[
                 battlemenuoptions.option1_y: battlemenuoptions.option1_y + battlemenuoptions.options_y_offset,
                 battlemenuoptions.options_x: battlemenuoptions.options_x + battlemenuoptions.options_x_offset,
                 ]
        option_2 = masked_frame[
                 battlemenuoptions.option2_y: battlemenuoptions.option2_y + battlemenuoptions.options_y_offset,
                 battlemenuoptions.options_x: battlemenuoptions.options_x + battlemenuoptions.options_x_offset,
                 ]
        option_3 = masked_frame[
                 battlemenuoptions.option3_y: battlemenuoptions.option3_y + battlemenuoptions.options_y_offset,
                 battlemenuoptions.options_x: battlemenuoptions.options_x + battlemenuoptions.options_x_offset,
                 ]

        option1_pixels = cv2.countNonZero(option_1)
        option2_pixels = cv2.countNonZero(option_2)
        option3_pixels = cv2.countNonZero(option_3)

        return (
                option1_pixels >= (marker_area * 0.85) or
                option2_pixels >= (marker_area * 0.85) or
                option3_pixels >= (marker_area * 0.85)
        )