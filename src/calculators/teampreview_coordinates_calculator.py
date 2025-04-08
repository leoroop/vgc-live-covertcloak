from src.models import TeamPreviewCoordinatesModel


class TeamPreviewCoordinatesCalculator:

    @staticmethod
    def calculate_teampreview_coordinates(frame_width: int, frame_height: int) -> TeamPreviewCoordinatesModel:
        moves_coordinates = TeamPreviewCoordinatesModel(
            teampreviews_x=int(frame_width * 0.121094), # 155 / 1280
            teampreview1_y=int(frame_height * 0.180556), # 130 / 720
            teampreview2_y=int(frame_height * 0.291667), # 210 / 720
            teampreview3_y=int(frame_height * 0.395833), # 285 / 720
            teampreview4_y=int(frame_height * 0.500000), # 360 / 720
            teampreview5_y=int(frame_height * 0.605556), # 436 / 720
            teampreview6_y=int(frame_height * 0.712500), # 513 / 720
            teampreviews_x_offset = int(frame_width / 6),
            teampreviews_y_offset = int(frame_height / 56), #TODO: trova un nome per queste costanti
            confirm_x=int(frame_width * 0.085937), # 110 / 1280
            confirm_y=int(frame_height * 0.794444), # 572 / 720
            confirm_x_offset=int(frame_width / 3),
            confirm_y_offset=int(frame_height / 16)
        )
        return moves_coordinates