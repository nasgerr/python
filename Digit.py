class Digit:
    def _check_digit(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError()
    def __init__(self, value):
        self._check_digit(value)
        self.value = value

class Integer(Digit):
    def __init__(self, value):
        self._check_digit(value)
        super().__init__(value)
    def _check_digit(self, value):
        if not isinstance(value, int):
            raise TypeError()

class Float(Digit):
    def __init__(self, value):
        self._check_digit(value)
        super().__init__(value)

    def _check_digit(self, value):
        if not isinstance(value, float):
            raise TypeError()

class Positive(Digit):
    def __init__(self, value):
        self._check_digit(value)
        super().__init__(value)

    def _check_digit(self, value):
        if value < 0:
            raise TypeError()

class Negative(Digit):
    def __init__(self, value):
        self._check_digit(value)
        super().__init__(value)

    def _check_digit(self, value):
        if value >= 0:
            raise TypeError()

class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super().__init__(value)

class FloatPositive(Float, Positive):
    def __init__(self, value):
        super().__init__(value)

digits = [PrimeNumber(3), PrimeNumber(5), PrimeNumber(7), FloatPositive(8.76), FloatPositive(9.57), FloatPositive(10.42), FloatPositive(11.12), FloatPositive(12.67)]
lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))