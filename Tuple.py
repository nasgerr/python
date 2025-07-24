class Tuple(tuple):
    def __add__(self, other):
        try:
            return Tuple(super().__add__(tuple(other)))
        except TypeError:
            return Tuple(super().__add__((other,)))