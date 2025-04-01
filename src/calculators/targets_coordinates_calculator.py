from src.models import TargetsCoordinatesModel


class TargetsCoordinatesCalculator:
    @staticmethod
    def calculate_targets_positions(frame_width: int, frame_height: int) -> TargetsCoordinatesModel:
        targets = TargetsCoordinatesModel(
            target_left = int(frame_width * 0.339843), # 435 / 1280
            target_right = int(frame_width * 0.507812), # 650 / 1280
            target_top = int(frame_height * 0.131944), # 95 / 720
            target_bottom = int(frame_height * 0.520833), # 375 / 720
            target_x_offset = int(frame_width / 6.4),
            target_y_offset = int(frame_height / 3.2) #TODO: trova un nome per queste costanti
        )
        return targets