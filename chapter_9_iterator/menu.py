from array import array
from collections import deque


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


class PancakeHouseMenu:
    def __init__(self) -> None:
        self.menu_items: list[MenuItem | None] = []

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

    def get_menu_items(self) -> list[MenuItem]:
        return self.menu_items


class DinnerMenu:
    def __init__(self) -> None:
        self.max_size = 2
        self.menu_items: deque[MenuItem] = deque(maxlen=self.max_size)

    def add_item(
        self, name: str, description: str, vegetarian: bool, price: float
    ) -> None:
        if len(self.menu_items) >= self.max_size:
            print('Ошибка! Нельзя добавить новое блюдо в меню.')
            return
        new_item = MenuItem(name, description, vegetarian, price)
        self.menu_items.append(new_item)

    def get_menu_items(self) -> list[MenuItem]:
        return list(self.menu_items)
