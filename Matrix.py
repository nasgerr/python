class Matrix:
    def __init__(self, *args):
        if len(args) == 3:
            rows, cols, fill_value = args
            if not isinstance(rows, int) or not isinstance(cols, int) or not isinstance(fill_value, (int, float)):
                raise TypeError()
            self._rows = rows
            self._cols = cols
            self._data = [[fill_value for _ in range(cols)] for _ in range(rows)]
        elif len(args) == 1 and isinstance(args[0], list):
            list2d = args[0]
            if not all(isinstance(row, list) for row in list2d) or not all(len(row) == len(list2d[0]) for row in list2d):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            if not all(isinstance(x, (int, float)) for row in list2d for x in row):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self._rows = len(list2d)
            self._cols = len(list2d[0]) if self._rows > 0 else 0
            self._data = [row.copy() for row in list2d]
        else:
            raise TypeError('неверные аргументы для инициализации матрицы')

    def __getitem__(self, indices):
        row, col = indices
        if not (isinstance(row, int) and isinstance(col, int)) or row < 0 or col < 0 or row >= self._rows or col >= self._cols:
            raise IndexError('недопустимые значения индексов')
        return self._data[row][col]

    def __setitem__(self, indices, value):
        row, col = indices
        if not (isinstance(row, int) and isinstance(col, int)) or row < 0 or col < 0 or row >= self._rows or col >= self._cols:
            raise IndexError('недопустимые значения индексов')
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        self._data[row][col] = value

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self._rows != other._rows or self._cols != other._cols:
                raise ValueError('операции возможны только с матрицами равных размеров')
            result = Matrix(self._rows, self._cols, 0)
            for i in range(self._rows):
                for j in range(self._cols):
                    result[i, j] = self[i, j] + other[i, j]
            return result
        elif isinstance(other, (int, float)):
            result = Matrix(self._rows, self._cols, 0)
            for i in range(self._rows):
                for j in range(self._cols):
                    result[i, j] = self[i, j] + other
            return result
        else:
            raise TypeError('можно складывать только матрицы или число')

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self._rows != other._rows or self._cols != other._cols:
                raise ValueError('операции возможны только с матрицами равных размеров')
            result = Matrix(self._rows, self._cols, 0)
            for i in range(self._rows):
                for j in range(self._cols):
                    result[i, j] = self[i, j] - other[i, j]
            return result
        elif isinstance(other, (int, float)):
            result = Matrix(self._rows, self._cols, 0)
            for i in range(self._rows):
                for j in range(self._cols):
                    result[i, j] = self[i, j] - other
            return result
        else:
            raise TypeError('можно вычитать только матрицы или число')

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self._data == other._data

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self._data])