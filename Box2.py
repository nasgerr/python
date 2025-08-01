class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []
    @property
    def things(self):
        return self._things

    @things.setter
    def things(self, value):
        self._things = value

    @property
    def total_weight(self):
        return sum(x[1] for x in self._things)

    def add_thing(self, obj):
        name, weight = obj
        if self.total_weight + weight > self._max_weight:
            raise ValueError

        self._things.append(obj)

class BoxDefender:
    def __init__(self, box):
        self._box = box
        self._things = box.things[:]

    def __enter__(self):
        return self._box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._box.things = self._things
        return False