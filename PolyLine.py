class PolyLine:
    def __init__(self, start_coord, *args):
        self.__coords = [start_coord, *args]
    def add_coord(self, x, y):
        self.__coords.append((x, y))
    def remove_coord(self, indx):
        if 0 <= indx < len(self.__coords):
            del self.__coords[indx]
    def get_coords(self):
        return list(self.__coords)
