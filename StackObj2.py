class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)
class Stack:
    def __init__(self):
        self.top = None
        self.__last = None
    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.__last.next = obj
        self.__last = obj
    def push_front(self, obj):
        if self.top is None:
            self.__last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj
    def __iter__(self):
        h = self.top
        while h:
            yield h
            h = h.next
    def __len__(self):
        return sum(1 for _ in self)

    def _get_obj(self, indx):
        if type(indx) != int or not (0 <= indx < len(self)):
            raise IndexError("Index out of range")
        for i, obj in enumerate(self):
            if i == indx:
                return obj
    def __getitem__(self, indx):
        return self._get_obj(indx).data
    def __setitem__(self, indx, obj):
        self._get_obj(indx).data = obj

