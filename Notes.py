class Note:
    __valid_names = {'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'}
    __valid_tons = {-1, 0, 1}

    def __init__(self, name, ton):
        if name not in self.__valid_names:
            raise ValueError('недопустимое значение аргумента')
        if ton not in self.__valid_tons:
            raise ValueError('недопустимое значение аргумента')
        self._name = name
        self._ton = ton


class Notes:
    __instance = None
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._do = Note('до', 0)
            cls.__instance._re = Note('ре', 0)
            cls.__instance._mi = Note('ми', 0)
            cls.__instance._fa = Note('фа', 0)
            cls.__instance._solt = Note('соль', 0)
            cls.__instance._la = Note('ля', 0)
            cls.__instance._si = Note('си', 0)
        return cls.__instance

    def __getitem__(self, index):
        if not isinstance(index, int) or index < 0 or index > 6:
            raise IndexError('недопустимый индекс')

        notes = [self._do, self._re, self._mi, self._fa,
                 self._solt, self._la, self._si]
        return notes[index]


notes = Notes()