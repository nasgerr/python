import sys
class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = int(old)
        self.score = int(score)
    def __bool__(self):
        return self.score > 0
lst_in = list(map(str.strip, sys.stdin.readlines()))
players = []
for line in lst_in:
    name, old, score = line.split(';')
    players.append(Player(name.strip(), old.strip(), score.strip()))
players_filtered = list(filter(bool, players))

