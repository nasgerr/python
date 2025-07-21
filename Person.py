class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
    def __check_index(self, item):
        if not isinstance(item, int) or item < 0 or item > 4:
            raise IndexError('Index out of range')
    def __getitem__(self, item):
        self.__check_index(item)
        return getattr(self, self._get_attr_name(item))
    def _get_attr_name(self, item):
        attr = ['fio', 'job', 'old', 'salary', 'year_job']
        return attr[item]
    def __setitem__(self, key, value):
        self.__check_index(key)
        setattr(self, self._get_attr_name(key), value)
    def __iter__(self):
        self._iter_index = 0
        return self
    def __next__(self):
        if self._iter_index < 5:
            res = self[self._iter_index]
            self._iter_index += 1
            return res
        else:
            raise StopIteration
