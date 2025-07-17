class Morph:
    def __init__(self, *args):
        self._words = list(map(lambda x: x.strip(" .,!;?:").lower(), args))
    def add_word(self, word):
        w = word.lower()
        if w not in self._words:
            self._words.append(w)
    def get_words(self):
        return tuple(self._words)
    def __eq__(self, other):
        if type(other) != str:
            raise ValueError()
        return other.lower() in self._words


