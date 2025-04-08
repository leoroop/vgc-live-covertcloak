from pydantic import BaseModel


class ChangesCoordinatesModel(BaseModel):
    changes_x: int
    change1_y: int
    change2_y: int
    change3_y: int
    change4_y: int
    changes_x_offset: int
    changes_y_offset: int