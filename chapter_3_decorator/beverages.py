from abc import ABC


class Beverage(ABC):
    """Базовый класс для всех видов напитков."""
    def __init__(self) -> None:
        self._description: str = 'Unknown beverage'
        self._cost: int = 0

    def cost(self) -> int:
        return self._cost

    def get_description(self) -> str:
        return self._description

    @property
    def info(self) -> None:
        print(
            f'Напиток: {self.get_description()}. '
            f'Стоимость: {self.cost()}'
        )


class CondimentDecorator(Beverage):
    """Базовый класс для всех видов добавок."""
    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage
        self._description: str = 'Unknown topping'
        self._cost: int = 0

    def cost(self) -> int:
        return self.beverage.cost() + self._cost

    def get_description(self) -> str:
        return f'{self.beverage.get_description()}, {self._description}'


# Основное меню
class Espresso(Beverage):
    def __init__(self) -> None:
        self._description: str = 'Эспрессо'
        self._cost: int = 200


class Decaf(Beverage):
    def __init__(self) -> None:
        self._description: str = 'Декаф'
        self._cost: int = 250


class DarkRoast(Beverage):
    def __init__(self) -> None:
        self._description: str = 'Темная обжарка'
        self._cost: int = 170


class HouseBlend(Beverage):
    def __init__(self) -> None:
        self._description: str = 'Домашняя смесь'
        self._cost: int = 100


# Добавки
class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage
        self._description: str = 'Шоколад'
        self._cost: int = 50


class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage
        self._description: str = 'Молоко'
        self._cost: int = 40


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage
        self._description: str = 'Соя'
        self._cost: int = 80


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage
        self._description: str = 'Взбитые сливки'
        self._cost: int = 120
