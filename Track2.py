class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.points = []
    def add_point(self, x, y, speed):
        self.points.append(((x, y), speed))

    def __getitem__(self, item):
        if not isinstance(item, int) or item < 0 or len(self.points) <= item:
            raise IndexError
        return self.points[item][0], self.points[item][1]
    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0 or len(self.points) <= key:
            raise IndexError
        point = self.points[key][0]
        self.points[key] = (point, value)


