class Model:
    def __init__(self):
        self._data = None

    def query(self, **kwargs):
        self._data = kwargs

    def __str__(self):
        if self._data is None:
            return "Model"
        items = [f"{k} = {v}" for k, v in self._data.items()]
        return "Model: " + ", ".join(items)
model = Model()
model.query(id = 1, fio = 'SVU', old = 33)
print(model)