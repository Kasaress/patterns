from abc import ABC, abstractmethod, abstractproperty
from typing import Any

from exceptions import UnknounPizzaType
from ingredients import (ChicagoPizzaIngredientFactory,
                         NYPizzaIngredientFactory, PizzaIngredientFactory)


# Пиццы
class Pizza(ABC):
    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        self.ingredient_factory = ingredient_factory

    @abstractmethod
    def get_description(self):
        pass

    def prepare(self):
        print(f'Подготовка пиццы {self.get_description}')

    def bake(self):
        print(f'Выпечка пиццы {self.get_description}')

    def cut(self):
        print(f'Нарезание пиццы {self.get_description}')

    def box(self):
        print(f'Упаковка пиццы {self.get_description}')


class CheesePizza(Pizza):
    @property
    def get_description(self):
        return '"Сырная пицца"'

    def prepare(self):
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        cheese = self.ingredient_factory.create_cheese()
        print(
            f'Добавление ингредиентов: {dough}, {sauce}, {cheese}'
        )


class PepperoniPizza(Pizza):
    @property
    def get_description(self):
        return '"Пицца пепперони"'

    def prepare(self):
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        pepperoni = self.ingredient_factory.create_pepperoni()
        print(
            f'Добавление ингредиентов: {dough}, {sauce}, {pepperoni}'
        )


class ClamPizza(Pizza):
    @property
    def get_description(self):
        return '"Пицца с мидиями"'

    def prepare(self):
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        clams = self.ingredient_factory.create_clams()
        print(
            f'Добавление ингредиентов: {dough}, {sauce}, {clams}'
        )


class VeggiePizza(Pizza):
    @property
    def get_description(self):
        return '"Вегетарианская пицца"'

    def prepare(self):
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        veggies = ', '.join(
            str(veg) for veg in self.ingredient_factory.create_veggies()
        )
        print(
            f'Добавление ингредиентов: {dough}, {sauce}, {veggies}'
        )


# Пиццерии
class PizzaStore(ABC):
    @abstractproperty
    def ingredient_factory(self):
        pass

    def create_pizza(self, pizza_type):
        if pizza_type == 'cheese':
            pizza = CheesePizza(self.ingredient_factory)
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza(self.ingredient_factory)
        elif pizza_type == 'clam':
            pizza = ClamPizza(self.ingredient_factory)
        elif pizza_type == 'veggie':
            pizza = VeggiePizza(self.ingredient_factory)
        else:
            raise UnknounPizzaType('Unknown type of pizza')
        return pizza

    def order_pizza(self, pizza_type) -> Any:
        try:
            self.pizza = self.create_pizza(pizza_type)
            self.pizza.prepare()
            self.pizza.bake()
            self.pizza.cut()
            self.pizza.box()
            return self.pizza
        except UnknounPizzaType as error:
            print(error)


class NYPizzaStore(PizzaStore):
    @property
    def ingredient_factory(self):
        return NYPizzaIngredientFactory()


class ChicagoPizzaStore(PizzaStore):
    @property
    def ingredient_factory(self):
        return ChicagoPizzaIngredientFactory()
