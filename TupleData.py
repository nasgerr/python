class CellException(Exception):
    pass
class Cell:
    pass
class CellIntegerException(CellException):
    pass
class CellFloatException(CellException):
    pass
class CellStringException(CellException):
    pass

class Cell:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, '_' + k, v)
        self._v = None
    @property
    def value(self):
        return self._v
    @value.setter
    def value(self, v):
        self._v = self.is_valid(v)
    def is_valid(self, v):
        raise NotImplemented

class CellInteger(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)
    def is_valid(self, v):
        if not self._min_value <= v <= self._max_value:
            raise CellIntegerException("значение выходит за допустимый диапазон")
        return v
class CellFloat(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def is_valid(self, v):
        if not self._min_value <= v <= self._max_value:
            raise CellFloatException("значение выходит за допустимый диапазон")
        return v
class CellString(Cell):
    def __init__(self, min_length, max_length):
        super().__init__(min_length=min_length, max_value=max_length)

    def is_valid(self, v):
        if not self._min_length <= len(v) <= self._max_length:
            raise CellStringException("длина строки выходит за допустимый диапазон")
        return v
class TupleData:
    def __init__(self, *args):
        [self.__is_cell(x) for x in args]
        self.cells = tuple(args)

    @staticmethod
    def __is_cell(x):
        if not isinstance(x, Cell):
            raise TypeError

    def __getitem__(self, item):
        return self.cells[item].value
    def __setitem__(self, key, value):
        self.cells[key].value = value
    def __len__(self):
        return len(self.cells)
    def __iter__(self):
        for x in self.cells:
            yield x.value

ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
