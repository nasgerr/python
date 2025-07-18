class Triangle:
    def init(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, value):
        if self._verify(value) and self._triangulate():
            self._a = value
    @property
    def b(self):
        return self._b
    @b.setter
    def b(self, value):
        if self._verify(value) and self._triangulate():
            self._b = value
    @property
    def c(self):
        return self._c
    @c.setter
    def c(self, value):
        if self._verify(value) and self._triangulate():
            self._c = value

    def _verify(self, value):
        if value > 0 and isinstance(value, (int, float)):
            return True
        else:
            raise ValueError('Triangle value must be positive integer')
    def _triangulate(self):
        if self._a < self._b + self._c and self._b < self._c + self._a and self._c < self._a + self._b:
            return True
        else:
            raise ValueError('Triangle value must be greater than or equal to zero')

    def __len__(self):
        return int(self._a + self._b + self._c)
    def tr(self):
        p = (self.__len__())/2
        return (p * (p - self._a) * (p - self._b) * (p - self._c))**0.5
