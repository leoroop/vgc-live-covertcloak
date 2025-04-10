from src.models import PkmnInfoCoordinatesModel


class PkmnInfoCoordinatesCalculator:

    @staticmethod
    def calculate_pkmninfo_coordinates(frame_width: int, frame_height: int) -> PkmnInfoCoordinatesModel:
        moves_coordinates = PkmnInfoCoordinatesModel(
            pkmninfo1_x=int(frame_width * 0.238281), # 305 / 1280
            pkmninfo1_y=int(frame_height * 0.097222), # 70 / 720
            pkmninfo1_x_offset=int(frame_width / 6),
            pkmninfo1_y_offset=int(frame_height / 24),

            pkmninfo2_x=int(frame_width * 0.593750), # 760 / 1280
            pkmninfo2_y=int(frame_height * 0.097222), # 70 / 720
            pkmninfo2_x_offset=int(frame_width / 3),
            pkmninfo2_y_offset=int(frame_height / 24),

            pkmninfo3_x=int(frame_width * 0.121094), # 155 / 1280
            pkmninfo3_y=int(frame_height * 0.180556), # 130 / 720
            pkmninfo3_x_offset=int(frame_width / 3),
            pkmninfo3_y_offset=int(frame_height / 28),

            pkmninfo4_x=int(frame_width * 0.21875), # 280 / 1280
            pkmninfo4_y=int(frame_height * 0.784722), # 565 / 720
            pkmninfo4_x_offset=int(frame_width / 6),
            pkmninfo4_y_offset=int(frame_height / 20)
        )
        return moves_coordinates