from src.calculators import MovesCoordinatesCalculator, TargetsCoordinatesCalculator, ChangesCoordinatesCalculator, \
    TeamPreviewCoordinatesCalculator
from src.calculators.battlemenuoptions_coordinates_calculator import BattleMenuOptionsCoordinatesCalculator
from src.models import MovesCoordinatesModel, TargetsCoordinatesModel, ChangesCoordinatesModel, \
    TeamPreviewCoordinatesModel
from src.models.battlemenuoptions_coordinates_model import BattleMenuOptionsCoordinatesModel
from src.processors.battlemenu_processor import BattleMenuOptionsProcessor
from src.processors.changes_processor import ChangesProcessor
from src.processors.moves_processor import MovesProcessor
from src.processors.targets_processor import TargetsProcessor
from src.processors.teampreview_processor import TeamPreviewProcessor


class GameProcessor:
    frame_height: int
    frame_width: int
    moves: MovesCoordinatesModel
    targets: TargetsCoordinatesModel
    battlemenuoptions: BattleMenuOptionsCoordinatesModel
    changes: ChangesCoordinatesModel
    teampreview: TeamPreviewCoordinatesModel

    def __init__(self, start_frame):
        self.frame_height = start_frame.shape[0]
        self.frame_width = start_frame.shape[1]
        self.moves = MovesCoordinatesCalculator.calculate_moves_coordinates(self.frame_width, self.frame_height)
        self.targets = TargetsCoordinatesCalculator.calculate_targets_coordinates(self.frame_width, self.frame_height)
        self.battlemenuoptions = BattleMenuOptionsCoordinatesCalculator.calculate_battlemenuoptions_coordinates(self.frame_width, self.frame_height)
        self.changes = ChangesCoordinatesCalculator.calculate_changes_coordinates(self.frame_width, self.frame_height)
        self.teampreview = TeamPreviewCoordinatesCalculator.calculate_teampreview_coordinates(self.frame_width, self.frame_height)

    def apply_moves_markers(self, frame):
        MovesProcessor.apply_moves_markers(frame, self.moves)

    def apply_targets_markers(self, frame):
        TargetsProcessor.apply_targets_markers(frame, self.targets)

    def apply_battlemenuoptions_markers(self, frame):
        BattleMenuOptionsProcessor.apply_battlemenuoptions_markers(frame, self.battlemenuoptions)

    def apply_changes_markers(self, frame):
        ChangesProcessor.apply_changes_markers(frame, self.changes)

    def apply_teampreview_markers(self, frame):
        TeamPreviewProcessor.apply_teampreview_markers(frame, self.teampreview)