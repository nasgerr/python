class Recipe:
    def __init__(self, *args):
        self.__ing = list(args)
    def add_ingredient(self, ing):
        self.__ing.append(ing)
    def remove_ingredient(self, ing):
        if ing in self.__ing:
            self.__ing.remove(ing)
    def get_ingredients(self):
        return tuple(self.__ing)
    def __len__(self):
        return len(self.__ing)
class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure
    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"