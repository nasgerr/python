class StackObj:
    def __init__(self, data, next = None):
        self.__data = data 
        self.__next = next

    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data
class Stack:
    def __init__(self, top = None, last = None):
        self.top = top
        self.last = last
    def push(self, obj):
        if self.last:
            self.last.next = obj
        self.last = obj
        if self.top is None:
            self.top = obj
    def pop(self):
        h = self.top
        if h is None:
            return
        while h.next != self.last:
            h = h.next
        if h:
            h.next = None
        last = self.last
        self.last = h
        if self.last is None:
            self.top = None
        return last
    def get_data(self):
        s = []
        h = self.top
        while h:
            s.append(h.data)
            h = h.next
        return s

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()