import cv2

from src.models import MovesCoordinatesModel, MaskModel


class MovesCoordinatesCalculator:

    @staticmethod
    def calculate_moves_coordinates(frame_width: int, frame_height: int) -> MovesCoordinatesModel:
        moves_coordinates = MovesCoordinatesModel(
            moves_x=int(frame_width * 0.734375), # 940 / 1280
            move1_y=int(frame_height * 0.618056), # 445 / 720
            move2_y=int(frame_height * 0.722222), # 520 / 720
            move3_y=int(frame_height * 0.826389), # 595 / 720
            move4_y=int(frame_height * 0.930556), # 670 / 720
            moves_x_offset = int(frame_width / 32),
            moves_y_offset = int(frame_height / 36), #TODO: trova un nome per queste costanti
            teracristal_x = int(frame_width * 0.613281), # 785 / 1280
            teracristal_y = int(frame_height * 0.631944), # 455 / 720
            teracristal_x_offset = int(frame_width / 22),
            teracristal_y_offset = int(frame_height / 30)
        )
        return moves_coordinates

    @staticmethod
    def calculate_moves_mask(frame_width: int, frame_height: int) -> MaskModel:
        cover = cv2.imread("covers/cover_moves.jpg")
        x_start = int(frame_width / 1.741497) # 1280 / 735
        x_end = x_start + cover.shape[1]
        y_start = int(frame_height / 2.400000) # 720 / 300
        y_end = y_start + cover.shape[0]
        return MaskModel(
            x_start=x_start,
            x_end=x_end,
            y_start=y_start,
            y_end=y_end,
            cover=cover
        )