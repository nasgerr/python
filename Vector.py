class Vector:
    def __init__(self, *args):
        self.coords = args
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.coords == other.coords
        return False
    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ValueError('Vector coords must have same length')
            new_coords = []
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] + other.coords[i])
            return Vector(*new_coords)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            new_coords = []
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] - other.coords[i])
            return Vector(*new_coords)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            new_coords = []
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] * other.coords[i])
            return Vector(*new_coords)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            new_coords = []
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] + other)
            self.coords = tuple(new_coords)
            return self
        elif isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            new_coords = []
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] + other.coords[i])
            self.coords = tuple(new_coords)
            return self
        else:
            return NotImplemented

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            new_coords = []
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] - other)
            self.coords = tuple(new_coords)
            return self
        elif isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            new_coords = []
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] - other.coords[i])
            self.coords = tuple(new_coords)
            return self
        else:
            return NotImplemented