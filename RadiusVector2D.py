class RadiusVector2D:
    def __init__(self, x = 0, y = 0):
        MIN_COORD = -100
        MAX_COORD = 1024
        if (type(x) in (int, float) and MIN_COORD <= x <= MAX_COORD) and (type(x) in (int, float) and MIN_COORD <= x <= MAX_COORD):
            self.__x = x
            self.__y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if self.__check_coord(value):
            self.__x = value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if self.__check_coord(value):
            self.__y = value
    @classmethod
    def __check_coord(cls, value):
        return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD
    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y