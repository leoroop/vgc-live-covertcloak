import cv2

from models import MaskModel
from src.models import ChangesCoordinatesModel


class ChangesCoordinatesCalculator:

    @staticmethod
    def calculate_changes_coordinates(frame_width: int, frame_height: int) -> ChangesCoordinatesModel:
        moves_coordinates = ChangesCoordinatesModel(
            changes_x=int(frame_width * 0.070313), # 90 / 1280
            change1_y=int(frame_height * 0.197222), # 140 / 720
            change2_y=int(frame_height * 0.311111), # 224 / 720
            change3_y=int(frame_height * 0.427778), # 308 / 720
            change4_y=int(frame_height * 0.544444), # 392 / 720
            changes_x_offset = int(frame_width / 11),
            changes_y_offset = int(frame_height / 56) #TODO: trova un nome per queste costanti
        )
        return moves_coordinates

    @staticmethod
    def calculate_changes_mask(frame_width: int, frame_height: int) -> MaskModel:
        cover = cv2.imread("covers/cover_change.jpg")
        x_start = int(frame_width / 42.666667) # 1280 / 30
        x_end = x_start + cover.shape[1]
        y_start = int(frame_height / 10.285714) # 720 / 70
        y_end = y_start + cover.shape[0]
        return MaskModel(
            x_start=x_start,
            x_end=x_end,
            y_start=y_start,
            y_end=y_end,
            cover=cover
        )