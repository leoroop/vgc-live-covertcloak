import cv2

from src.contants.colors import red_color, line_style
from src.models import MovesCoordinatesModel


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