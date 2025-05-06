import cv2

from models import MaskModel
from src.models import TargetsCoordinatesModel


class TargetsCoordinatesCalculator:
    @staticmethod
    def calculate_targets_coordinates(frame_width: int, frame_height: int) -> TargetsCoordinatesModel:
        targets = TargetsCoordinatesModel(
            target_left = int(frame_width * 0.339843), # 435 / 1280
            target_right = int(frame_width * 0.507812), # 650 / 1280
            target_top = int(frame_height * 0.131944), # 95 / 720
            target_bottom = int(frame_height * 0.520833), # 375 / 720
            target_x_offset = int(frame_width / 6.4),
            target_y_offset = int(frame_height / 3.2) #TODO: trova un nome per queste costanti
        )
        return targets

    @staticmethod
    def calculate_targets_mask(frame_width: int, frame_height: int) -> MaskModel:
        cover = cv2.imread("covers/cover_target.jpg")
        x_start = int(frame_width / 3.08433) # 1280 / 735
        x_end = x_start + cover.shape[1]
        y_start = int(frame_height / 36) # 720 / 36
        y_end = y_start + cover.shape[0]
        return MaskModel(
            x_start=x_start,
            x_end=x_end,
            y_start=y_start,
            y_end=y_end,
            cover=cover
        )