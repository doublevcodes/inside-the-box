from collections import namedtuple

from .colour import Colour


class CubeFace:
    """Cube face"""

    CubeFaceArray = namedtuple("CubeFaceArray",
                               "top_left top_centre top_right"
                               "middle_left middle_centre middle_right"
                               "bottom_left bottom_centre bottom_right")

    def __init__(self) -> None:
        self._face = CubeFace.CubeFaceArray(
            *[Colour.UNDEFINED for _ in range(9)]
        )

    def __getattr__(self, item: str):
        return self._face.__getattribute__(item)

    def __setattr__(self, key: str, value: Colour):
        return self._face.__setattr__(key, value)
