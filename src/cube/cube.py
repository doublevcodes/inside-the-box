from .face import CubeFace


class Cube(dict):
    """Cube"""

    def __init__(self):
        super().__init__({face_name: CubeFace for face_name in ("f", "b", "r", "l", "u", "d")})
