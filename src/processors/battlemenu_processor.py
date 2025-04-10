import cv2

from src.contants.colors_constants import red_color, line_style
from src.models import BattleMenuOptionsCoordinatesModel


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