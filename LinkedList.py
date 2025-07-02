class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    def add_obj(self, obj):
        if self.head == None:
            self.head == obj
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
    def remove_obj(self):
        if self.tail is None:
            return
        prev = self.tail.get_prev()
        if prev:
            prev.set_next(None)
        self.tail = prev
        if self.tail is None:
            self.head = None
    def get_data(self):
        s = []
        h = self.head
        while h:
            s.append(h.get_data())
            h = h.get_next()
        return s

class ObjList:
    def __init__(self, data, next = None, prev = None):
        self.__next =  next
        self.__prev = prev
        self.__data = data
    def set_next(self, next):
        self.__next = next
    def set_prev(self, prev):
        self.__prev = prev
    def set_data(self, data):
        self.__data = data
    def get_next(self):
        return self.__next
    def get_prev(self):
        return self.__prev
    def get_data(self):
        return self.__data
