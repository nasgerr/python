class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

class DictShop(dict):
    def __init__(self, things=None):
        things = {} if things is None else things

        if not isinstance(things, dict):
            raise TypeError("things must be a dict")
        if things and not all(isinstance(key, Thing) for key in things):
            raise TypeError()
        super().__init__(things)

    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError("key must be a Thing")
        super().__setitem__(key, value)
