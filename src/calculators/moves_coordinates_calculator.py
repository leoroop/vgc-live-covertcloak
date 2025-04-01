from src.models import MovesCoordinatesModel


class MovesCoordinatesCalculator:

    @staticmethod
    def calculate_moves_positions(frame_width: int, frame_height: int) -> MovesCoordinatesModel:
        moves_coordinates = MovesCoordinatesModel(
            moves_x=int(frame_width * 0.734375), # 940 / 1280
            move1_y=int(frame_height * 0.618056), # 445 / 720
            move2_y=int(frame_height * 0.722222), # 520 / 720
            move3_y=int(frame_height * 0.826389), # 595 / 720
            move4_y=int(frame_height * 0.930556), # 670 / 720
            moves_x_offset = int(frame_width / 64),
            moves_y_offset = int(frame_height / 36) #TODO: trova un nome per queste costanti
        )
        return moves_coordinates