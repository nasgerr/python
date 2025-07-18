import sys
class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
    def __eq__(self, other):
        if not isinstance(other, ShopItem):
            return False
        return self.name.lower() == other.name.lower() and self.weight == other.weight and self.price == other.price
    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))
lst_in = list(map(str.strip, sys.stdin.readlines()))
shop_items = {}
for line in lst_in:
    parts = line.split(":")
    name = parts[0].strip()
    weight_price = parts[1].strip().split()
    weight = float(weight_price[0]) if '.' in weight_price[0] else int(weight_price[0])
    price = float(weight_price[1]) if '.' in weight_price[1] else int(weight_price[1])
item = ShopItem(name, weight, price)
if item in shop_items:
    shop_items[item][1] += 1
else:
    shop_items[item] = [item, 1]