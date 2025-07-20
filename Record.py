class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__total_attrs = len(kwargs)
        self.__attrs = tuple(self.__dict__.keys())
    def __check_index(self, indx):
        if type(indx) != int or not (-self.__total_attrs <= indx <= self.__total_attrs):
            raise IndexError("Index out of range")

    def __getitem__(self, item):
        self.__check_index(item)
        return getattr(self, self.__attrs[item])

    def __setitem__(self, key, value):
        self.__check_index(key)
        setattr(self, self.__attrs[key], value)
