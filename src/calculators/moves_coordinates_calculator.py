from src.models import MovesCoordinatesModel


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
    def get_marker_area(moves_coordinates: MovesCoordinatesModel) -> int:
        base = moves_coordinates.moves_x_offset
        height = moves_coordinates.moves_y_offset
        return base * height