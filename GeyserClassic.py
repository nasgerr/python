import time
class GeyserClassic:
    MAX_DATE_FILTER = 100
    def __init__(self):
        self.filter_class = ('Mechanical', 'Aragon', 'Calcium')
        self.filters = {(1, self.filter_class[0]): None, (2, self.filter_class[1]): None, (3, self.filter_class[2]): None}
    def add_filter(self, slot_num, filter):
        key = (slot_num, filter.__class__.__name__)
        if key in self.filters and not self.filters[key]:
            self.filters[key] = filter
    def remove_filter(self, slot_num):
        if type(slot_num) == int and 1 <= slot_num <= 3:
            key = (slot_num, self.filter_class[slot_num - 1])
            if key in self.filters:
                self.filters[key] = None
    def get_filters(self):
        return tuple(self.filters.values())
    def water_on(self):
        end = time.time()
        for f in self.filters.values():
            if f is None:
                return False
            start = f.data
            if end - start > self.MAX_DATE_FILTER:
                return False
        return True



class Mechanical:
    def __init__(self, data):
        self.data = data

    def __setattr__(self, key, value):
        if key == 'data' and key in self.__dict__:
            return
        object.__setattr__(self, key, value)
class Aragon:
    def __init__(self, data):
        self.data = data

    def __setattr__(self, key, value):
        if key == 'data' and key in self.__dict__:
            return
        object.__setattr__(self, key, value)
class Calcium:
    def __init__(self, data):
        self.data = data
    def __setattr__(self, key, value):
        if key == 'data' and key in self.__dict__:
            return
        object.__setattr__(self, key, value)