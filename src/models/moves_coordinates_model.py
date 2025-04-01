from pydantic import BaseModel


class MovesCoordinatesModel(BaseModel):
    moves_x: int
    move1_y: int
    move2_y: int
    move3_y: int
    move4_y: int
    moves_x_offset: int
    moves_y_offset: int