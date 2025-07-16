stich = ["Я к вам пишу – чего же боле?",
    "Что я могу еще сказать?",
    "Теперь, я знаю, в вашей воле",
    "Меня презреньем наказать.",
    "Но вы, к моей несчастной доле",
    "Хоть каплю жалости храня.",
    "Вы не оставите меня."]
class StringText:
    def __init__(self, lst_words):
        self._lst_words = list(lst_words)
    def __len__(self):
        return len(self._lst_words)
    def __gt__(self, other):
        return len(self) > len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __repr__(self):
        return ' '.join(self._lst_words)
lst_text = []
for line in stich:
    words = []
    for word in line.split():
        cleaned_word = word.strip('–?!,.')
        if cleaned_word:
            words.append(cleaned_word)
    lst_text.append(StringText(words))

lst_text_sorted = sorted(lst_text, key=lambda x: -len(x))
lst_text_sorted = [str(text) for text in lst_text_sorted]