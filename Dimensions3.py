class Dimensions:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __eq__(self, other):
        if not isinstance(other, Dimensions):
            return NotImplemented
        return (self.a == other.a) and (self.b == other.b) and (self.c == other.c)



input_str = input().strip()
if not input_str:
    lst_dims = []
else:
    parts = input_str.split(';')
    lst_dims = []
    for part in parts:
        try:
            a, b, c = part.strip().split()
            lst_dims.append(Dimensions(a, b, c))
        except ValueError as e:
            pass

lst_dims_sorted = sorted(lst_dims, key=lambda x: hash(x))