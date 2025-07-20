class RadiusVector:
    def __init__(self, *args):
        self.coords = list(args)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.coords[key]
        elif isinstance(key, slice):
            return tuple(self.coords[key])
        else:
            raise TypeError()

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.coords[key] = value
        elif isinstance(key, slice):
            if isinstance(value, (list, tuple)):
                if len(self.coords[key]) != len(value):
                    raise ValueError()
                self.coords[key] = value
            else:
                for i in range(*key.indices(len(self.coords))):
                    self.coords[i] = value
        else:
            raise TypeError()



