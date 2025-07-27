from abc import ABC, abstractmethod
class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        """Добавление объекта в конец стека"""
        pass
    @abstractmethod
    def pop_back(self):
        """Удаление последнего объекта из стека"""
        pass

class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None


class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self._tail = None

    def push_back(self, obj):
        if not isinstance(obj, StackObj):
            return

        if self._top is None:
            self._top = obj
            self._tail = obj
        else:
            self._tail._next = obj
            self._tail = obj

    def pop_back(self):
        if self._top is None:
            return None

        if self._top == self._tail:
            last = self._top
            self._top = None
            self._tail = None
            return last

        h = self._top
        while h._next != self._tail:
            h = h._next

        last = self._tail
        h._next = None
        self._tail = h
        return last

