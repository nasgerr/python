class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self._rows = rows
        self._cols = cols
        self._type_data = type_data
        self.__cells = tuple(tuple(Cell() for _ in range(cols)) for _ in range(rows))
    def __check_index(self, index):
        r, c = index
        if not (0 <= r < self._rows) or not (0 <= c < self._cols):
            raise IndexError("Index out of range")

    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item
        return self.__cells[r][c].data

    def __setitem__(self, key, value):
        self.__check_index(key)
        if type(value) != self._type_data:
            raise TypeError()
        r, c = key
        self.__cells[r][c].data = value

    def __iter__(self):
        for row in self.__cells:
            yield (x.data for x in row)


class Cell:
    def __init__(self, data):
        self.__data = data
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        self.__data = value
