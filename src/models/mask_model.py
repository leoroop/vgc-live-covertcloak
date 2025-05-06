from typing import Any

from cv2 import Mat
from numpy import ndarray, dtype
from pydantic import BaseModel, ConfigDict


class MaskModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    x_start: int
    x_end: int
    y_start: int
    y_end: int
    cover: Mat | ndarray[Any, dtype]