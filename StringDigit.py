class StringDigit(str):
    def __init__(self, string):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")
        super().__init__()

    def __add__(self, other):
        if isinstance(other, str):
            if not other.isdigit():
                raise ValueError("в строке должны быть только цифры")
            return StringDigit(super().__add__(other))
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)