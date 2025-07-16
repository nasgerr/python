class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
    @property
    def data(self):
        return self.__data
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, obj):
        self.__next = obj
class Stack:
    def __init__(self):
        self.top = None
        self.__last = None
    def push_back(self, obj):
        if self.last:
            self.last.next = obj
        self.last = obj
        if self.top is None:
            self.top = obj

    def pop_back(self):
        h = self.top
        if h is None:
            return
        while h.next != self.__last:
            h = h.next
        if h:
            h.next = None
        last = self.last
        self.__last = h
        if self.last is None:
            self.top = None
        return last
    def __add__(self, other):
        self.push_back(other)
        return self
    def __iadd__(self, other):
        return self.__add__(other)
    def __mul__(self, other):
        for x in other:
            self.push_back(StackObj(x))
    def __imul__(self, other):
        return self.__mul__(other)