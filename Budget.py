class Budget:
    def __init__(self):
        self.budget = []
    def add_item(self, it):
        self.budget.append(it)
    def remove_item(self, indx):
        if 0 <= indx < len(self.budget):
            self.budget.pop(indx)
    def get_items(self):
        return list(self.budget)
class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money
    def __add__(self, other):
        if type(other) is Item:
            return self.money + other.money
    def __radd__(self, other):
        if other == 0:
            return self.money
        return self.__add__(other)


