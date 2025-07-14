class WordString:
    def __init__(self, string=''):
        self._string = string
    def __len__(self):
        return len(self.string.split()) if self.string else 0
    def __call__(self, indx, *args, **kwargs):
        return self.string.split()[indx]
    @property
    def string(self):
        return self._string
    @string.setter
    def string(self, value):
        self._string = value

words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")

