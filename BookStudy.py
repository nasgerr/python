import sys
class BookStudy:
    def __init__(self, name, author, year):
        self.name = name.lower()
        self.author = author.lower()
        self.year = int(year)
    def __eq__(self, other):
        return self.name == other.name and self.author == other.author
    def __hash__(self):
        return hash((self.name, self.author))
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_bs = []
for line in lst_in:
    if line:
        name, author, year = line.split(';')
        lst_bs.append(BookStudy(name, author, year))
unique_books = len(set(lst_bs))