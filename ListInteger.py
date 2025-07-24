class ListInteger(list):
    def __init__(self, lst):
        for x in lst:
            self.__check_type(x)
        super().__init__(lst)
    @staticmethod
    def __check_type(x):
        if type(x) != int:
            raise TypeError()

    def __setitem__(self, index, value):
        self.__check_type(value)
        super().__setitem__(index, value)

    def append(self, value):
        self.__check_type(value)
        super().append(value)

