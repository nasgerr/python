class Validator:
    def _is_valid(self, data):
        return True

    def __call__(self, data):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return True

class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, int) and self.min_value <= data <= self.max_value

class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, float) and self.min_value <= data <= self.max_value


integer_validator = IntegerValidator(-19, 10)
float_validator = FloatValidator(-1, 1)

res1 = integer_validator(10)
res2 = float_validator(10)