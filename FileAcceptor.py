class FileAcceptor:
    def __init__(self, *args):
        self._ext = tuple(dict.fromkeys(args))

    def __call__(self, filename):
        ext = filename.split('.')[-1]
        return ext in self._ext

    def __add__(self, other):
        combined = self._ext + other._ext
        unique = tuple(dict.fromkeys(combined))
        return FileAcceptor(*unique)
