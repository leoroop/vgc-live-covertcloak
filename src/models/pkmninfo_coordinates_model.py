from pydantic import BaseModel


class PkmnInfoCoordinatesModel(BaseModel):
    pkmninfo1_x: int
    pkmninfo1_y: int
    pkmninfo1_x_offset: int
    pkmninfo1_y_offset: int
    pkmninfo2_x: int
    pkmninfo2_y: int
    pkmninfo2_x_offset: int
    pkmninfo2_y_offset: int
    pkmninfo3_x: int
    pkmninfo3_y: int
    pkmninfo3_x_offset: int
    pkmninfo3_y_offset: int
    pkmninfo4_x: int
    pkmninfo4_y: int
    pkmninfo4_x_offset: int
    pkmninfo4_y_offset: int


