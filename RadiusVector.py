class RadiusVector:
    def init(self, *args):
        if len(args) == 1 and type(args[0]) == int:
            self.__coords = [0] * args[0]
        else:
            self.__coords = list(args)
    def set_coords(self, *args):
        n = min(len(args), len(self.__coords))
        self.__coords[:n] = args[:n]
    def get_coords(self):
        return tuple(self.__coords)
    def __len__(self):
        return len(self.__coords)
    def __abs__(self):
        return (sum(x**2 for x in self.__coords))**0.5
