class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        if len(lst) > max_length:
            raise ValueError()
        return super().__new__(cls, lst)

    def __str__(self):
        return ' '.join(map(str, self))

    def __repr__(self):
        return ' '.join(map(str, self))


digits = list(map(float, input().split()))

try:
    tl = TupleLimit(digits, max_length=5)
    print(tl)
except ValueError as e:
    print(e)