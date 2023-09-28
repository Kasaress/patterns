from abc import ABC, abstractproperty
from typing import Any

from constants import PIZZAS
from exceptions import UnknounPizzaTypeException
from ingredients import ChicagoPizzaIngredientFactory, NYPizzaIngredientFactory


# Пиццерии
class PizzaStore(ABC):
    def __init__(self):
        print(f'Открыта новая пиццерия: {self.__class__.__name__}')

    @abstractproperty
    def ingredient_factory(self):
        pass

    def get_style(self):
        return self.ingredient_factory.get_style()

    def create_pizza(self, pizza_type):
        if not PIZZAS.get(pizza_type):
            raise UnknounPizzaTypeException(
                f'Мы пока не готовим пиццу "{pizza_type}". '
                'Выберите из меню: '
                f'{", ".join(pizza["name"] for pizza in PIZZAS.values())}'
            )
        pizza = PIZZAS.get(pizza_type).get('type')(self.ingredient_factory)
        pizza.name = (
            f'"{PIZZAS.get(pizza_type).get("name")} '
            f'пицца в стиле {self.get_style()}"'
        )
        return pizza

    def order_pizza(self, pizza_type) -> Any:
        try:
            self.pizza = self.create_pizza(pizza_type)
        except UnknounPizzaTypeException as error:
            print(error)
        else:
            print(f'Поступил заказ: {self.pizza.name}')
            self.pizza.prepare()
            self.pizza.bake()
            self.pizza.cut()
            self.pizza.box()
            return self.pizza


class NYPizzaStore(PizzaStore):
    @property
    def ingredient_factory(self):
        return NYPizzaIngredientFactory()


class ChicagoPizzaStore(PizzaStore):
    @property
    def ingredient_factory(self):
        return ChicagoPizzaIngredientFactory()
