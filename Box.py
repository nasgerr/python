class Box:
    def __init__(self):
        self._box = []
    def add_thing(self, obj):
        if isinstance(obj, Thing):
            self._box.append(obj)
    def get_things(self):
        return list(self._box)
    def __eq__(self, other):
        if not isinstance(other, Box):
            return False
        things1 = self._box[:]
        things2 = other._box[:]
        if len(things1) != len(things2):
            return False
        for thing in things1:
            if thing in things2:
                things2.remove(thing)
            else:
                return False
        return True
class Thing:
    def __init__(self, name, mass):
        self.name = name.lower()
        self.mass = mass
    def __eq__(self, other):
        return self.name == other.name and self.mass == other.mass

