from pydantic import BaseModel


class TeamPreviewCoordinatesModel(BaseModel):
    teampreviews_x: int
    teampreview1_y: int
    teampreview2_y: int
    teampreview3_y: int
    teampreview4_y: int
    teampreview5_y: int
    teampreview6_y: int
    teampreviews_x_offset: int
    teampreviews_y_offset: int
    confirm_x: int
    confirm_y: int
    confirm_x_offset: int
    confirm_y_offset: int
