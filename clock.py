class Clock:
    def __init__(self, tm):
        self.__time = 0
        if self.__check_time(tm):
            self.__time = tm
    @classmethod
    def __check_time(cls, tm):
        return type(tm) is int and 0 <= tm < 100000

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm
    def get_time(self):
        return self.__time
clock = Clock(4530)

