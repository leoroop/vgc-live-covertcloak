from pydantic import BaseModel


class TargetsCoordinatesModel(BaseModel):
    target_left: int
    target_right: int
    target_top: int
    target_bottom: int
    target_x_offset: int
    target_y_offset: int