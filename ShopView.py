class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __str__(self):
        return '\n'.join(f'{k}: {v}' for k, v in self.__dict__.items())

    def __repr__(self):
        return str(self)


class ShopUserView:
    def __str__(self):
        return '\n'.join(f'{k}: {v}' for k, v in self.__dict__.items() if k != '_id')

    def __repr__(self):
        return str(self)


class Book(ShopItem):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year
