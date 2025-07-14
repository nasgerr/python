class Complex:
    def __init__(self, real, img):
        self._real = self._img = None
        self.img = img
        self.real = real
    @property
    def real(self):
        return self._real
    @property
    def img(self):
        return self._img
    @real.setter
    def real(self, value):
        if type(value) in (int, float):
            self._real = value
        else:
            raise ValueError("Неверный тип данных.")
    @img.setter
    def img(self, value):
        if type(value) in (int, float):
            self._img = value
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return (self.real*self.real + self.img*self.img)**(1/2)

cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(cmp.real, cmp.img, c_abs)