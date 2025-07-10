class FloatValue:
    @classmethod
    def convert(cls, value):
        if type(value) != float:
            raise TypeError("The value is not a float")
    def __set_name__(self, owner, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        self.convert(value)
        setattr(instance, self.name, value)
class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]
class Cell:
    value = FloatValue()
    def __init__(self, value = 0.0):
        self.value = value

table = TableSheet(5, 3)
n = 1.0
for i in range(5):
    for j in range(3):
        table.cells[i][j].value = n
        n += 1.0