class Dimensions:
    MIN_DIMENSIONS = 10
    MAX_DIMENSIONS = 1000
    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = None
        self.a = a
        self.b = b
        self.c = c
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, value):
        if self.MIN_DIMENSIONS <= value <= self.MAX_DIMENSIONS:
            self.__a = value
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, value):
        if self.MIN_DIMENSIONS <= value <= self.MAX_DIMENSIONS:
            self.__b = value
    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, value):
        if self.MIN_DIMENSIONS <= value <= self.MAX_DIMENSIONS:
            self.__c = value

    def __setattr__(self, key, value):
        if key == 'MIN_DIMENSIONS' or key == 'MAX_DIMENSIONS':
            raise AttributeError("Менять атрибуты запрещено.")
        object.__setattr__(self, key, value)
d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c
print(a, b, c)
d.MAX_DIMENSIONS = 10