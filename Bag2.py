class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self._bag = []

    @property
    def total_weight(self):
        return sum(thing.weight for thing in self._bag)

    def add_thing(self, thing):
        if not isinstance(thing, Thing):
            raise ValueError('Not a thing')
        if self.total_weight + thing.weight > self.max_weight:
            raise ValueError('Too many things')
        self._bag.append(thing)
    def __check(self, item):
        if not (0 <= item < len(self._bag)) or not isinstance(item, int):
            raise IndexError()
    def __getitem__(self, item):
        self.__check(item)
        return self._bag[item]
    def __setitem__(self, key, value):
        self.__check(key)
        if not isinstance(value, Thing):
            raise ValueError('Not a thing')
        new_total = self.total_weight - self._bag[key].weight + value.weight
        if new_total > self.max_weight:
            raise ValueError('Too many things')
        self._bag[key] = value
    def __delitem__(self, key):
        self.__check(key)
        del self._bag[key]
class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight