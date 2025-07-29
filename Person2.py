class Person:
    __slots__ = ('_fio', '_job', '_old')
    def __init__(self, fio, old, job):
        self._fio = fio
        self._job = job
        self._old = old

persons = [Person('Суворов', 52, 'полководец'),
           Person('Рахманинов', 50, 'пианист и композитор'),
           Person('Балакирев', 34, 'программист и преподаватель'),
           Person('Пушкин', 32, 'поэт и писатель')
           ]


