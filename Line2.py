import math
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        length = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        return int(length)

    def __bool__(self):
        return len(self) >= 1

