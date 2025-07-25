class ItemAttrs:
    def __getitem__(self, index):
        return list(self.__dict__.values())[index]

    def __setitem__(self, index, value):
        key = list(self.__dict__.keys())[index]
        setattr(self, key, value)


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y