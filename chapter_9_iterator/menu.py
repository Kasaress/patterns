from collections import OrderedDict
from typing import Protocol, Any


class MenuItem:
    def __init__(
        self,
        name: str,
        description: str,
        vegetarian: bool,
        price: float
    ) -> None:
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def is_vegetarian(self) -> bool:
        return self.vegetarian

    def __repr__(self) -> str:
        return f'{self.name} - {self.price} руб: {self.description.lower()}'


class Iterator(Protocol):
    _collection: Any
    _cursor: int

    def next(self) -> MenuItem:
        pass

    def has_next(self) -> bool:
        pass


class PancakeHouseIterator:
    def __init__(self, collection: list[MenuItem]):
        self._collection = collection
        self._cursor = 0

    def next(self) -> MenuItem:
        current_item = self._collection[self._cursor]
        self._cursor += 1
        return current_item

    def has_next(self) -> bool:
        return self._cursor + 1 <= len(self._collection)


class DinnerMenuIterator:
    def __init__(self, collection: OrderedDict[str, MenuItem]):
        self._collection = list(collection.values())
        self._cursor = 0

    def next(self) -> MenuItem:
        current_item = self._collection[self._cursor]
        self._cursor += 1
        return current_item

    def has_next(self) -> bool:
        return self._cursor + 1 <= len(self._collection)


class PancakeHouseMenu:
    def __init__(self) -> None:
        self.menu_items: list[MenuItem] = []

    def add_item(
        self,
        name: str,
        description: str,
        vegetarian: bool,
        price: float
    ) -> None:
        new_item = MenuItem(
            name,
            description,
            vegetarian,
            price
        )
        self.menu_items.append(new_item)

    def creat_iterator(self) -> PancakeHouseIterator:
        return PancakeHouseIterator(self.menu_items)


class DinnerMenu:
    def __init__(self) -> None:
        self.menu_items: OrderedDict[str, MenuItem] = OrderedDict()
        self.max_size = 6
        self.current_index = 0

    def add_item(
        self, name: str, description: str, vegetarian: bool, price: float
    ) -> None:
        if len(self.menu_items) < self.max_size:
            new_item = MenuItem(name, description, vegetarian, price)
            self.menu_items[str(self.current_index)] = new_item  # намеренноstr
            self.current_index += 1
        else:
            print("Меню уже достигло максимального размера")

    def creat_iterator(self) -> DinnerMenuIterator:
        return DinnerMenuIterator(self.menu_items)


class Waitress:
    def __init__(self, menus) -> None:
        self.menus: list = menus

    def _print_menu(self, iterator: Iterator) -> None:
        while iterator.has_next():
            print(iterator.next())

    def print_menu(self) -> None:
        for menu in self.menus:
            self._print_menu(menu.creat_iterator())
