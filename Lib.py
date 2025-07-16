class Lib:
    def __init__(self):
        self.book_list = []
    def __add__(self, other):
        self.book_list.append(other)
        return self
    def __iadd__(self, other):
        return self.__add__(other)
    def __len__(self):
        return len(self.book_list)
    def __sub__(self, other):
        if type(other) is int:
            if other in self.book_list:
                self.book_list.pop(other)
        elif type(other) is Book:
            if 0 <= other < len(self.book_list):
                self.book_list.remove(other)
        return self
    def __isub__(self, other):
        return self.__sub__(other)
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year