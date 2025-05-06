import cv2

from src.contants.colors_constants import red_color, line_style
from src.models import MovesCoordinatesModel
from src.utils import Utils


class MovesProcessor:
    @staticmethod
    def apply_moves_markers(frame, moves: MovesCoordinatesModel):
        cv2.rectangle(
            frame,
            (moves.moves_x, moves.move1_y),
            (moves.moves_x + moves.moves_x_offset, moves.move1_y + moves.moves_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (moves.moves_x, moves.move2_y),
            (moves.moves_x + moves.moves_x_offset, moves.move2_y + moves.moves_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (moves.moves_x, moves.move3_y),
            (moves.moves_x + moves.moves_x_offset, moves.move3_y + moves.moves_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (moves.moves_x, moves.move4_y),
            (moves.moves_x + moves.moves_x_offset,
             moves.move4_y + moves.moves_y_offset),
            red_color,
            line_style
        )
        cv2.rectangle(
            frame,
            (moves.teracristal_x, moves.teracristal_y),
            (moves.teracristal_x + moves.teracristal_x_offset,
             moves.teracristal_y + moves.teracristal_y_offset),
            red_color,
            line_style
        )

    @staticmethod
    def check_if_move_selection(masked_frame, moves_coordinates: MovesCoordinatesModel) -> bool:
        marker_area = Utils.get_marker_area(moves_coordinates.moves_x_offset, moves_coordinates.moves_y_offset)
        move_1 = masked_frame[
            moves_coordinates.move1_y: moves_coordinates.move1_y + moves_coordinates.moves_y_offset,
            moves_coordinates.moves_x: moves_coordinates.moves_x + moves_coordinates.moves_x_offset,
        ]
        move_2 = masked_frame[
            moves_coordinates.move2_y: moves_coordinates.move2_y + moves_coordinates.moves_y_offset,
            moves_coordinates.moves_x: moves_coordinates.moves_x + moves_coordinates.moves_x_offset,
        ]
        move_3 = masked_frame[
            moves_coordinates.move3_y: moves_coordinates.move3_y + moves_coordinates.moves_y_offset,
            moves_coordinates.moves_x: moves_coordinates.moves_x + moves_coordinates.moves_x_offset,
        ]
        move_4 = masked_frame[
            moves_coordinates.move4_y: moves_coordinates.move4_y + moves_coordinates.moves_y_offset,
            moves_coordinates.moves_x: moves_coordinates.moves_x + moves_coordinates.moves_x_offset,
        ]

        teracristal = masked_frame[
            moves_coordinates.teracristal_y: moves_coordinates.teracristal_y + moves_coordinates.teracristal_y_offset,
            moves_coordinates.teracristal_x: moves_coordinates.teracristal_x + moves_coordinates.teracristal_x_offset,
        ]

        move1_pixels = cv2.countNonZero(move_1)
        move2_pixels = cv2.countNonZero(move_2)
        move3_pixels = cv2.countNonZero(move_3)
        move4_pixels = cv2.countNonZero(move_4)
        teracristal_pixels = cv2.countNonZero(teracristal)

        return (
                move1_pixels >= (marker_area * 0.85) or
                move2_pixels >= (marker_area * 0.85) or
                move3_pixels >= (marker_area * 0.85) or
                move4_pixels >= (marker_area * 0.85) or
                225 <= teracristal_pixels <= 300
        )
