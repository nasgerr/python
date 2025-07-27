from abc import ABC, abstractmethod
class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return f"Базовый класс Model"

class ModelForm(Model):
    _ID = 0
    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = ModelForm._ID
        ModelForm._ID += 1
    def get_pk(self):
        return self._id

