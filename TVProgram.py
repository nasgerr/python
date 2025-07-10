class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = []
    def add_telecast(self, tl):
        self.items.append(tl)
    def remove_telecast(self, indx):
        self.items.pop(indx)
class Telecast:
    def __init__(self, id, name, duration):
        self.__id = id
        self.__name = name
        self.__duration = duration
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, value):
        self.__duration = value
pr = TVProgram("Первые канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")