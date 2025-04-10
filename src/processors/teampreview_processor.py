import cv2

from src.contants.colors_constants import red_color, line_style
from src.models import TeamPreviewCoordinatesModel


class TeamPreviewProcessor:
    @staticmethod
    def apply_teampreview_markers(frame, teampreview: TeamPreviewCoordinatesModel):
        cv2.rectangle(
            frame,
            (teampreview.teampreviews_x, teampreview.teampreview1_y),
            (teampreview.teampreviews_x + teampreview.teampreviews_x_offset, teampreview.teampreview1_y + teampreview.teampreviews_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (teampreview.teampreviews_x, teampreview.teampreview2_y),
            (teampreview.teampreviews_x + teampreview.teampreviews_x_offset, teampreview.teampreview2_y + teampreview.teampreviews_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (teampreview.teampreviews_x, teampreview.teampreview3_y),
            (teampreview.teampreviews_x + teampreview.teampreviews_x_offset, teampreview.teampreview3_y + teampreview.teampreviews_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (teampreview.teampreviews_x, teampreview.teampreview4_y),
            (teampreview.teampreviews_x + teampreview.teampreviews_x_offset, teampreview.teampreview4_y + teampreview.teampreviews_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (teampreview.teampreviews_x, teampreview.teampreview5_y),
            (teampreview.teampreviews_x + teampreview.teampreviews_x_offset, teampreview.teampreview5_y + teampreview.teampreviews_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (teampreview.teampreviews_x, teampreview.teampreview6_y),
            (teampreview.teampreviews_x + teampreview.teampreviews_x_offset, teampreview.teampreview6_y + teampreview.teampreviews_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (teampreview.confirm_x, teampreview.confirm_y),
            (teampreview.confirm_x + teampreview.confirm_x_offset, teampreview.confirm_y + teampreview.confirm_y_offset),
            red_color,
            line_style
        )