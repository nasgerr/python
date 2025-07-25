class SoftList(list):
    def __getitem__(self, index):
        if -len(self) <= index < len(self):
            return super().__getitem__(index)
        return False