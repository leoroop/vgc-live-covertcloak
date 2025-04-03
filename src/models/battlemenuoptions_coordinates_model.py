from pydantic import BaseModel


class BattleMenuOptionsCoordinatesModel(BaseModel):
    options_x: int
    option1_y: int
    option2_y: int
    option3_y: int
    options_x_offset: int
    options_y_offset: int