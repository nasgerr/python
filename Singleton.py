class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name

class Game(Singleton):
    def __init__(self, name):
        super().__init__(name)
