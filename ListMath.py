class ListMath:
    def __init__(self, lst=None):
        self.lst_math = lst if lst and type(lst) is list else []
        self.lst_math = list(filter(lambda x: type(x) in (int, float), self.lst_math))
    def __add__(self, other):
        self.__verify_value(other)
        return ListMath([x + other for x in self.lst_math])
    def __radd__(self, other):
        return self + other
    def __sub__(self, other):
        self.__verify_value(other)
        return ListMath([x - other for x in self.lst_math])
    def __rsub__(self, other):
        return ListMath([other - x for x in self.lst_math])
    def __mul__(self, other):
        self.__verify_value(other)
        return ListMath([x * other for x in self.lst_math])
    def __rmul__(self, other):
        return self * other
    def __truediv__(self, other):
        self.__verify_value(other)
        return ListMath([x / other for x in self.lst_math])
    def __rtruediv__(self, other):
        return ListMath([other / x for x in self.lst_math])
    def __iadd__(self, other):
        self.__verify_value(other)
        self.lst_math = [x + other for x in self.lst_math]
        return self
    def __isub__(self, other):
        self.__verify_value(other)
        self.lst_math = [x - other for x in self.lst_math]
        return self
    def __imul__(self, other):
        self.__verify_value(other)
        self.lst_math = [x * other for x in self.lst_math]
        return self
    def __itruediv__(self, other):
        self.__verify_value(other)
        self.lst_math = [x / other for x in self.lst_math]
        return self
    @staticmethod
    def __verify_value(value):
        if type(value) not in (int, float):
            raise ArithmeticError


