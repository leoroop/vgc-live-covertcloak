from src.models import BattleMenuOptionsCoordinatesModel


class BattleMenuOptionsCoordinatesCalculator:

    @staticmethod
    def calculate_battlemenuoptions_coordinates(frame_width: int, frame_height: int) -> BattleMenuOptionsCoordinatesModel:
        battlemenuoptions_coordinates = BattleMenuOptionsCoordinatesModel(
            options_x=int(frame_width * 0.960937), # 1230 / 1280
            option1_y=int(frame_height * 0.729167), # 525 / 720
            option2_y=int(frame_height * 0.811111), # 584 / 720
            option3_y=int(frame_height * 0.893055), # 643 / 720
            options_x_offset = int(frame_width / 64),
            options_y_offset = int(frame_height / 16) #TODO: trova un nome per queste costanti
        )
        return battlemenuoptions_coordinates