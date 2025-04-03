import cv2

from src.calculators import MovesCoordinatesCalculator, TargetsCoordinatesCalculator
from src.calculators.battlemenuoptions_coordinates_calculator import BattleMenuOptionsCoordinatesCalculator
from src.models import MovesCoordinatesModel, TargetsCoordinatesModel
from src.models.battlemenuoptions_coordinates_model import BattleMenuOptionsCoordinatesModel
from src.processors.battlemenu_processor import BattleMenuOptionsProcessor
from src.processors.moves_processor import MovesProcessor
from src.processors.targets_processor import TargetsProcessor


class GameProcessor:
    frame_height: int
    frame_width: int
    moves: MovesCoordinatesModel
    targets: TargetsCoordinatesModel
    battlemenuoptions: BattleMenuOptionsCoordinatesModel

    def __init__(self, start_frame):
        self.frame_height = start_frame.shape[0]
        self.frame_width = start_frame.shape[1]
        self.moves = MovesCoordinatesCalculator.calculate_moves_coordinates(self.frame_width, self.frame_height)
        self.targets = TargetsCoordinatesCalculator.calculate_targets_coordinates(self.frame_width, self.frame_height)
        self.battlemenuoptions = BattleMenuOptionsCoordinatesCalculator.calculate_battlemenuoptions_coordinates(self.frame_width, self.frame_height)

    def apply_moves_markers(self, frame):
        MovesProcessor.apply_moves_markers(frame, self.moves)

    def apply_targets_markers(self, frame):
        TargetsProcessor.apply_targets_markers(frame, self.targets)

    def apply_battlemenuoptions_markers(self, frame):
        BattleMenuOptionsProcessor.apply_battlemenuoptions_markers(frame, self.battlemenuoptions)

