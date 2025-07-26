class Furniture:
    def __init__(self, name, weight):
        self.__verify_name(name)
        self.__verify_weight(weight)
        self.__name = name
        self.__weight = weight
    def __verify_name(self, value):
        if type(value) is not str:
            raise TypeError('name must be a string')
    def __verify_weight(self, value):
        if not (value > 0):
            raise ValueError('weight must be positive')
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__verify_name(value)
        self.__name = value
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, value):
        self.__verify_weight(value)
        self.__weight = value


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return (self._name, self._weight, self._tp, self._doors)


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return (self._name, self._weight, self._height)


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return (self._name, self._weight, self._height, self._square)