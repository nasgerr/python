class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}
        self.pk_counter = 0
    def write(self, record):
        if record in self.dict_db:
            self.dict_db[record].append(record)
        else:
            self.dict_db[record] = [record]
    def read(self, pk):
        for records in self.dict_db.values():
            for record in records:
                if record.pk == pk:
                    return record
        return None


class Record:
    pk = 0
    def __init__(self, fio, descr, old):
        self.pk = Record.pk
        Record.pk += 1
        self.fio = fio.lower()
        self.descr = descr
        self.old = old
    def __eq__(self, other):
        if isinstance(other, Record):
            return self.pk == other.pk and self.fio == other.fio
        return NotImplemented
    def __hash__(self):
        return hash((self.fio, self.old))