class Body:
    def __init__(self, name, ro, volume):
        self._name = name
        self._ro = ro
        self._volume = volume
    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self._massa() == other
        elif isinstance(other, Body):
            return self._massa() == other._massa()
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self._massa() > other
        elif isinstance(other, Body):
            return self._massa() > other._massa()
        return NotImplemented
    def _massa(self):
        return self._ro * self._volume
