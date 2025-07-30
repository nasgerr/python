class Triangle:
    def __init__(self, a, b, c):
        if type(a) not in (int, float) or type(b) not in (int, float) or type(c) not in (int, float):
            raise TypeError
        if a <= 0 or b <= 0 or c <= 0:
            raise TypeError

        if a > b + c or b > a + c or c > a + b:
            raise ValueError

        self._a = a
        self._b = b
        self._c = c


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5),
                (7, 4, 6)]

lst_tr = []
for data in input_data:
    try:
        tr = Triangle(*data)
    except (TypeError, ValueError):
        pass
    else:
        lst_tr.append(tr)
