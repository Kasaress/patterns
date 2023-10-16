from abc import ABC

from exceptions import ComponentAttributeError


class MenuComponent(ABC):
    def add(self, menu_component):
        raise ComponentAttributeError('Метод не реализован')

    def remove(self, menu_component):
        raise ComponentAttributeError('Метод не реализован')

    def get_child(self, index: int):
        raise ComponentAttributeError('Метод не реализован')

    def get_name(self):
        raise ComponentAttributeError('Метод не реализован')

    def get_description(self):
        raise ComponentAttributeError('Метод не реализован')

    def get_price(self):
        raise ComponentAttributeError('Метод не реализован')

    def is_vegetarian(self):
        raise ComponentAttributeError('Метод не реализован')

    def print(self):
        raise ComponentAttributeError('Метод не реализован')


class MenuItem(MenuComponent):
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

    def print(self) -> None:
        veg = 'вегетарианское' if self.is_vegetarian() else 'не вегетарианское'
        print(
            f'{self.name} - {self.price} р: {self.description.lower()}, {veg}'
        )


class Menu(MenuComponent):
    def __init__(
        self,
        name: str,
        description: str,
    ):
        self.name = name
        self.description = description
        self._collection: list[MenuComponent] = []
        self._cursor = 0

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def add(self, menu_component: MenuComponent):
        self._collection.append(menu_component)

    def remove(self, menu_component: MenuComponent):
        self._collection.remove(menu_component)

    def get_child(self, index: int):
        return self._collection[index]

    def print(self) -> None:
        print('-----------------')
        print(
            f'Меню: {self.get_name()}, {self.get_description()}',
        )
        for menu in self._collection:
            menu.print()


class Waitress:
    def __init__(self, all_menu: MenuComponent) -> None:
        self.all_menu = all_menu

    def print_menu(self) -> None:
        self.all_menu.print()
