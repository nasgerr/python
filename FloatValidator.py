class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != float or not (self.min_value <= value <= self.max_value):
            raise ValueError()

class IntegerValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != int or not (self.min_value <= value <= self.max_value):
            raise ValueError()

def is_valid(lst, validators):
    res = []
    for x in lst:
        for v in validators:
            try:
                v(x)
                res.append(x)
                break
            except ValueError:
                pass
    return res
