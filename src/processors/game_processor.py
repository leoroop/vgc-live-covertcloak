import cv2

from src.calculators import MovesCoordinatesCalculator, TargetsCoordinatesCalculator
from src.models import MovesCoordinatesModel, TargetsCoordinatesModel


class GameProcessor:

    moves: MovesCoordinatesModel
    targets: TargetsCoordinatesModel

    def __init__(self, start_frame):
        self.frame_height = start_frame.shape[0]
        self.frame_width = start_frame.shape[1]        

        self.red_color = (0,0,255)
        self.blue_color = (255, 0,0)
        self.green_color = (0, 255,0)
        self.line_style = cv2.LINE_4

        self.moves = MovesCoordinatesCalculator.calculate_moves_positions(self.frame_width, self.frame_height)
        self.targets = TargetsCoordinatesCalculator.calculate_targets_positions(self.frame_width, self.frame_height)

    def apply_moves_markers(self, frame):
        cv2.rectangle(
            frame,
            (self.moves.moves_x, self.moves.move1_y),
            (self.moves.moves_x + self.moves.moves_x_offset, self.moves.move1_y + self.moves.moves_y_offset),
            self.red_color,
            self.line_style
        )
        cv2.rectangle(
            frame,
            (self.moves.moves_x, self.moves.move2_y),
            (self.moves.moves_x + self.moves.moves_x_offset, self.moves.move2_y + self.moves.moves_y_offset),
            self.red_color,
            self.line_style
        )
        cv2.rectangle(
            frame,
            (self.moves.moves_x, self.moves.move3_y),
            (self.moves.moves_x + self.moves.moves_x_offset, self.moves.move3_y + self.moves.moves_y_offset),
            self.red_color,
            self.line_style
        )
        cv2.rectangle(
            frame,
            (self.moves.moves_x, self.moves.move4_y),
            (self.moves.moves_x + self.moves.moves_x_offset,
            self.moves.move4_y + self.moves.moves_y_offset),
            self.red_color,
            self.line_style
        )

    def apply_targets_markers(self, frame):
        # TOP LEFT
        cv2.rectangle(
            frame,
            (self.targets.target_left, self.targets.target_top),
            (self.targets.target_left + self.targets.target_x_offset, self.targets.target_top + self.targets.target_y_offset),
            self.red_color,
            self.line_style
        )

        # TOP RIGHT
        cv2.rectangle(
            frame,
            (self.targets.target_right, self.targets.target_top),
            (self.targets.target_right + self.targets.target_x_offset, self.targets.target_top + self.targets.target_y_offset),
            self.red_color,
            self.line_style
        )

        # BOTTOM LEFT
        cv2.rectangle(
            frame,
            (self.targets.target_left, self.targets.target_bottom),
            (self.targets.target_left + self.targets.target_x_offset, self.targets.target_bottom + self.targets.target_y_offset),
            self.red_color,
            self.line_style
        )

        # BOTTOM RIGHT
        cv2.rectangle(
            frame,
            (self.targets.target_right, self.targets.target_bottom),
            (self.targets.target_right + self.targets.target_x_offset, self.targets.target_bottom + self.targets.target_y_offset),
            self.red_color,
            self.line_style
        )


