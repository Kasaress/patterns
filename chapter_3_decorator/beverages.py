from abc import ABC


class Beverage(ABC):
    """Базовый класс для всех видов напитков."""
    _description: str = 'Unknown beverage'
    _cost: int = 0

    @property
    def cost(self) -> int:
        return self._cost

    @property
    def description(self) -> str:
        return self._description

    @property
    def info(self) -> None:
        print(
            f'Напиток: {self.description}. '
            f'Стоимость: {self.cost}'
        )


class CondimentDecorator(Beverage):
    """Базовый класс для всех видов добавок."""
    _description: str = 'Unknown topping'
    _cost: int = 0

    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage

    @property
    def cost(self) -> int:
        return self.beverage.cost + self._cost

    @property
    def description(self) -> str:
        return f'{self.beverage.description}, {self._description}'


# Основное меню
class Espresso(Beverage):
    _description: str = 'Эспрессо'
    _cost: int = 200


class Decaf(Beverage):
    _description: str = 'Декаф'
    _cost: int = 250


class DarkRoast(Beverage):
    _description: str = 'Темная обжарка'
    _cost: int = 170


class HouseBlend(Beverage):
    _description: str = 'Домашняя смесь'
    _cost: int = 100


# Добавки
class Mocha(CondimentDecorator):
    _description: str = 'Шоколад'
    _cost: int = 50


class Milk(CondimentDecorator):
    _description: str = 'Молоко'
    _cost: int = 40


class Soy(CondimentDecorator):
    _description: str = 'Соя'
    _cost: int = 80


class Whip(CondimentDecorator):
    _description: str = 'Взбитые сливки'
    _cost: int = 120
