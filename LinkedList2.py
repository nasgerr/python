class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        obj.prev = self.tail
        if self.tail:
            self.tail.next = obj
        self.tail = obj
        if self.head is None:
            self.head = obj
    def __get_obj_by_index(self, indx):
        h = self.head
        n = 0
        while h and n < indx:
            h = h.next
            n += 1
        return h
    def remove_obj(self, indx):
        obj = self.__get_obj_by_index(indx)
        if obj is None:
            return
        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p
        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p

    def __len__(self, linked_lst):
        n = 0
        h = self.head
        while h:
            n += 1
            h = h.next
        return n
    def __call__(self, indx, *args, **kwargs):
        obj = self.__get_obj_by_index(indx)
        return obj.data if obj else None
class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = self.__next = None
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if type(value) == str:
            self.__data = value
    @property
    def prev(self):
        return self.__prev
    @prev.setter
    def prev(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__prev = obj
    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__next = obj
