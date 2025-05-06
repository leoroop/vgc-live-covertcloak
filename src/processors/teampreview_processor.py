import cv2

from src.contants.colors_constants import red_color, line_style
from src.models import TeamPreviewCoordinatesModel
from utils import Utils


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

    @staticmethod
    def check_if_teampreview_selection(masked_frame, teampreview_coordinates: TeamPreviewCoordinatesModel) -> bool:
        marker_area = Utils.get_marker_area(teampreview_coordinates.teampreviews_x_offset, teampreview_coordinates.teampreviews_y_offset)
        teampreview_1 = masked_frame[
                 teampreview_coordinates.teampreview1_y: teampreview_coordinates.teampreview1_y + teampreview_coordinates.teampreviews_y_offset,
                 teampreview_coordinates.teampreviews_x: teampreview_coordinates.teampreviews_x + teampreview_coordinates.teampreviews_x_offset,
                 ]
        teampreview_2 = masked_frame[
                 teampreview_coordinates.teampreview2_y: teampreview_coordinates.teampreview2_y + teampreview_coordinates.teampreviews_y_offset,
                 teampreview_coordinates.teampreviews_x: teampreview_coordinates.teampreviews_x + teampreview_coordinates.teampreviews_x_offset,
                 ]
        teampreview_3 = masked_frame[
                 teampreview_coordinates.teampreview3_y: teampreview_coordinates.teampreview3_y + teampreview_coordinates.teampreviews_y_offset,
                 teampreview_coordinates.teampreviews_x: teampreview_coordinates.teampreviews_x + teampreview_coordinates.teampreviews_x_offset,
                 ]
        teampreview_4 = masked_frame[
                 teampreview_coordinates.teampreview4_y: teampreview_coordinates.teampreview4_y + teampreview_coordinates.teampreviews_y_offset,
                 teampreview_coordinates.teampreviews_x: teampreview_coordinates.teampreviews_x + teampreview_coordinates.teampreviews_x_offset,
                 ]
        teampreview_5 = masked_frame[
            teampreview_coordinates.teampreview5_y: teampreview_coordinates.teampreview5_y + teampreview_coordinates.teampreviews_y_offset,
            teampreview_coordinates.teampreviews_x: teampreview_coordinates.teampreviews_x + teampreview_coordinates.teampreviews_x_offset,
        ]
        teampreview_6 = masked_frame[
            teampreview_coordinates.teampreview6_y: teampreview_coordinates.teampreview6_y + teampreview_coordinates.teampreviews_y_offset,
            teampreview_coordinates.teampreviews_x: teampreview_coordinates.teampreviews_x + teampreview_coordinates.teampreviews_x_offset,
        ]
        confirm = masked_frame[
            teampreview_coordinates.confirm_y: teampreview_coordinates.confirm_y + teampreview_coordinates.confirm_y_offset,
            teampreview_coordinates.confirm_x: teampreview_coordinates.confirm_x + teampreview_coordinates.confirm_x_offset
        ]

        teampreview1_pixels = cv2.countNonZero(teampreview_1)
        teampreview2_pixels = cv2.countNonZero(teampreview_2)
        teampreview3_pixels = cv2.countNonZero(teampreview_3)
        teampreview4_pixels = cv2.countNonZero(teampreview_4)
        teampreview5_pixels = cv2.countNonZero(teampreview_5)
        teampreview6_pixels = cv2.countNonZero(teampreview_6)
        confirm_pixels = cv2.countNonZero(confirm)

        return (
                teampreview1_pixels >= (marker_area * 0.85) or
                teampreview2_pixels >= (marker_area * 0.85) or
                teampreview3_pixels >= (marker_area * 0.85) or
                teampreview4_pixels >= (marker_area * 0.85) or
                teampreview5_pixels >= (marker_area * 0.85) or
                teampreview6_pixels >= (marker_area * 0.85) or
                confirm_pixels >= (marker_area * 0.85)
        )