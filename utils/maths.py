# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

from mathutils import (
    Vector,
    Matrix,
    Quaternion,
)
from math import (
    cos, sin, pi, inf, ceil, radians, degrees
)

# ------------------------------------------------------------------------------- #
# CLASSES
# ------------------------------------------------------------------------------- #

class Transform:
    def __init__(self, location=Vector((0, 0, 0)), rotation=Quaternion(), scale=Vector((1, 1, 1))):
        self.__location = location.copy()
        self.__rotation = rotation.copy()
        self.__scale = scale.copy()

    def __repr__(self):
        return f"<Transform loc={self.__location}, rot={self.__rotation}, scale={self.__scale}>"

    @property
    def location(self):
        return self.__location.copy()

    @location.setter
    def location(self, value):
        self.__location = Vector(value)

    @property
    def rotation(self):
        return self.__rotation.copy()

    @rotation.setter
    def rotation(self, value):
        self.__rotation = Quaternion(value)

    @property
    def scale(self):
        return self.__scale.copy()

    @scale.setter
    def scale(self, value):
        self.__scale = Vector(value)

    @property
    def normal(self):
        return self.__rotation @ Vector((0, 0, 1))

    @normal.setter
    def normal(self, value):
        target = Vector(value).normalized()
        if target.length != 0:
            rot_diff = self.normal.rotation_difference(target)
            self.__rotation = self.__rotation @ rot_diff

    @property
    def matrix(self):
        return Matrix.LocRotScale(self.__location, self.__rotation, self.__scale)

    @matrix.setter
    def matrix(self, matrix):
        location, rotation, scale = matrix.decompose()
        self.__location = location
        self.__rotation = rotation
        self.__scale = scale


class Rect2D:
    ''' X and Y are Center '''
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


    def point_is_within_boundary(self, px=0, py=0):
        half_w = int(self.w / 2)
        half_h = int(self.h / 2)
        lx = self.x - half_w
        rx = self.x + half_w
        by = self.y - half_h
        ty = self.y + half_h
        if px >= lx and px <= rx:
            if py >= by and py <= ty:
                return True
        return False


    def boundary_coord_vectors(self):
        half_w = int(self.w / 2)
        half_h = int(self.h / 2)
        lx = self.x - half_w
        rx = self.x + half_w
        by = self.y - half_h
        ty = self.y + half_h
        bl = Vector((lx, by))
        tl = Vector((lx, ty))
        br = Vector((rx, by))
        tr = Vector((rx, ty))
        return bl, tl, br, tr

# ------------------------------------------------------------------------------- #
# VECTORS
# ------------------------------------------------------------------------------- #

def aligned_rectangle(p1, p2, plane_matrix):
    x_axis = plane_matrix.to_3x3()[0]
    y_axis = plane_matrix.to_3x3()[1]
    delta = p2 - p1
    width  = delta.dot(x_axis)
    height = delta.dot(y_axis)
    rect = [
        p1,
        p1 + x_axis * width,
        p1 + x_axis * width + y_axis * height,
        p1 + y_axis * height
    ]
    return rect
