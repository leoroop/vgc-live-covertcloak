import cv2

from models import MaskModel
from src.calculators import MovesCoordinatesCalculator, TargetsCoordinatesCalculator, ChangesCoordinatesCalculator, \
    TeamPreviewCoordinatesCalculator
from src.calculators.battlemenuoptions_coordinates_calculator import BattleMenuOptionsCoordinatesCalculator
from src.calculators.pkmninfo_coordinates_calculator import PkmnInfoCoordinatesCalculator
from src.models import MovesCoordinatesModel, TargetsCoordinatesModel, ChangesCoordinatesModel, \
    TeamPreviewCoordinatesModel, PkmnInfoCoordinatesModel
from src.models.battlemenuoptions_coordinates_model import BattleMenuOptionsCoordinatesModel
from src.processors.battlemenu_processor import BattleMenuOptionsProcessor
from src.processors.changes_processor import ChangesProcessor
from src.processors.moves_processor import MovesProcessor
from src.processors.pkmninfo_processor import PkmnInfoProcessor
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
    pkmninfo: PkmnInfoCoordinatesModel

    moves_buffer_frames: int = 10
    actual_moves_buffer_frames: int = 0

    battle_menu_buffer_frames: int = 10
    actual_battle_menu_buffer_frames: int = 0

    change_pkmn_buffer_frames: int = 10
    actual_change_pkmn_buffer_frames: int = 0

    teampreview_buffer_frames: int = 10
    actual_teampreview_buffer_frames: int = 0

    targets_buffer_frames: int = 10
    actual_targets_buffer_frames: int = 0

    pkmninfo_buffer_frames: int = 10
    actual_pkmninfo_buffer_frames: int = 0

    covers = {
        "teampreview": cv2.imread("covers/team_preview.jpg")
    }
    moves_mask: MaskModel

    def __init__(self, start_frame):
        self.frame_height = start_frame.shape[0]
        self.frame_width = start_frame.shape[1]

        self.moves = MovesCoordinatesCalculator.calculate_moves_coordinates(self.frame_width, self.frame_height)
        self.battlemenuoptions = BattleMenuOptionsCoordinatesCalculator.calculate_battlemenuoptions_coordinates(self.frame_width, self.frame_height)
        self.moves_mask = MovesCoordinatesCalculator.calculate_moves_mask(self.frame_width, self.frame_height)

        self.targets = TargetsCoordinatesCalculator.calculate_targets_coordinates(self.frame_width, self.frame_height)
        self.targets_mask = TargetsCoordinatesCalculator.calculate_targets_mask(self.frame_width, self.frame_height)

        self.changes = ChangesCoordinatesCalculator.calculate_changes_coordinates(self.frame_width, self.frame_height)
        self.changes_mask = ChangesCoordinatesCalculator.calculate_changes_mask(self.frame_width, self.frame_height)

        self.teampreview = TeamPreviewCoordinatesCalculator.calculate_teampreview_coordinates(self.frame_width, self.frame_height)

        self.pkmninfo = PkmnInfoCoordinatesCalculator.calculate_pkmninfo_coordinates(self.frame_width, self.frame_height)
        self.pkmninfo_mask = PkmnInfoCoordinatesCalculator.calculate_pkmninfo_mask(self.frame_width, self.frame_height)


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

    def apply_pkmninfo_markers(self, frame):
        PkmnInfoProcessor.apply_pkmninfo_markers(frame, self.pkmninfo)

    def move_selection_screen_is_active(self, frame) -> bool:
        return MovesProcessor.check_if_move_selection(frame, self.moves)

    def target_selection_screen_is_active(self, frame) -> bool:
        return TargetsProcessor.check_if_target_selection(frame, self.targets)

    def battlemenu_is_active(self, frame) -> bool:
        return BattleMenuOptionsProcessor.check_if_option_selection(frame, self.battlemenuoptions)

    def changepokemon_is_active(self, frame) -> bool:
        return ChangesProcessor.check_if_change_pokemon_selection(frame, self.changes)

    def teampreview_is_active(self, frame) -> bool:
        return TeamPreviewProcessor.check_if_teampreview_selection(frame, self.teampreview)

    def pkmninfo_is_active(self, frame) -> bool:
        return PkmnInfoProcessor.pkmninfo_is_active(frame, self.pkmninfo)

    def apply_masks(self, frame, mask_yellow, mask_blue):
        self.apply_moves_mask(frame, mask_yellow)
        self.apply_target_mask(frame, mask_yellow)
        self.apply_battlemenu_mask(frame, mask_yellow)
        self.apply_change_pkmn_mask(frame, mask_yellow)
        self.apply_teampreview_mask(frame, mask_yellow)
        self.apply_pkmninfo_mask(frame, mask_blue)

    def apply_moves_mask(self, frame, masked_frame):
        if self.move_selection_screen_is_active(masked_frame):
            self.actual_moves_buffer_frames = self.moves_buffer_frames
        elif  self.actual_moves_buffer_frames > 0:
            self.actual_moves_buffer_frames -= 1
        if  self.actual_moves_buffer_frames > 0:
            frame[
                self.moves_mask.y_start:self.moves_mask.y_end,
                self.moves_mask.x_start:self.moves_mask.x_end
            ] = self.moves_mask.cover

    def apply_target_mask(self, frame, masked_frame):
        if self.target_selection_screen_is_active(masked_frame):
            self.actual_targets_buffer_frames = self.targets_buffer_frames
        elif self.actual_targets_buffer_frames > 0:
            self.actual_targets_buffer_frames -= 1
        if self.actual_targets_buffer_frames > 0:
            frame[
                self.targets_mask.y_start:self.targets_mask.y_end,
                self.targets_mask.x_start:self.targets_mask.x_end
            ] = self.targets_mask.cover

    def apply_battlemenu_mask(self, frame, masked_frame):
        if self.battlemenu_is_active(masked_frame):
            self.actual_battle_menu_buffer_frames = self.battle_menu_buffer_frames
        elif self.actual_battle_menu_buffer_frames > 0:
            self.actual_battle_menu_buffer_frames -= 1
        if self.actual_battle_menu_buffer_frames > 0:
            frame[
                self.moves_mask.y_start:self.moves_mask.y_end,
                self.moves_mask.x_start:self.moves_mask.x_end
            ] = self.moves_mask.cover

    def apply_change_pkmn_mask(self, frame, masked_frame):
        if self.changepokemon_is_active(masked_frame):
            self.actual_change_pkmn_buffer_frames = self.change_pkmn_buffer_frames
        elif self.actual_change_pkmn_buffer_frames > 0:
            self.actual_change_pkmn_buffer_frames -= 1
        if self.actual_change_pkmn_buffer_frames > 0:
            frame[
                self.changes_mask.y_start:self.changes_mask.y_end,
                self.changes_mask.x_start:self.changes_mask.x_end
            ] = self.changes_mask.cover

    def apply_teampreview_mask(self, frame, masked_frame):
        if self.teampreview_is_active(masked_frame):
            self.actual_teampreview_buffer_frames = self.teampreview_buffer_frames
        elif self.actual_teampreview_buffer_frames > 0:
            self.actual_teampreview_buffer_frames -= 1
        if self.actual_teampreview_buffer_frames > 0:
            frame[80:640, 85:555] = self.covers["teampreview"]

    def apply_pkmninfo_mask(self, frame, masked_frame):
        if self.pkmninfo_is_active(masked_frame):
            self.actual_pkmninfo_buffer_frames = self.pkmninfo_buffer_frames
        elif self.actual_pkmninfo_buffer_frames > 0:
            self.actual_pkmninfo_buffer_frames -= 1
        if self.actual_pkmninfo_buffer_frames > 0:
            frame[
                self.pkmninfo_mask.y_start:self.pkmninfo_mask.y_end,
                self.pkmninfo_mask.x_start:self.pkmninfo_mask.x_end
            ] = self.pkmninfo_mask.cover
