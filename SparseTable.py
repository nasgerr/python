class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.table = {}

    def __check(self, row, col):
        return isinstance(row, int) and isinstance(col, int) and row >= 0 and col >= 0
    def update_index(self):
        self.rows = max(key[0] for key in self.table) + 1
        self.cols = max(key[1] for key in self.table) + 1
    def add_data(self, row, col, data):
        self.__check(row, col)
        self.table[(row, col)] = data
        self.update_index()

    def remove_data(self, row, col):
        try:
            del self.table[(row, col)]
            self.update_index()
        except KeyError:
            raise IndexError()
    def __getitem__(self, item):
        try:
            return self.table[(item[0], item[1])].value
        except KeyError:
            raise ValueError()
    def __setitem__(self, key, value):
        item = (key[0], key[1])
        if item not in self.table:
            self.table[item] = Cell(value)
            self.update_index()
        else:
            self.table[item] = Cell(value)
class Cell:
    def __init__(self, value):
        self.value = value

