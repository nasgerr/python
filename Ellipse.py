class Ellipse:
    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
    def __bool__(self):
        return hasattr(self, 'x1') and hasattr(self, 'y1') and hasattr(self, 'x2') and hasattr(self, 'y2')
    def get_coords(self):
        if not self:
            raise AttributeError()
        return (self.x1, self.y1, self.x2, self.y2)
lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
for geom in lst_geom:
    if geom:
        print(geom.get_coords())
