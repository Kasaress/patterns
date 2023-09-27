from abc import ABC, abstractproperty
from typing import Any

from exceptions import UnknounPizzaType
from ingredients import (ChicagoPizzaIngredientFactory,
                         NYPizzaIngredientFactory, PizzaIngredientFactory)


# Пиццы
class Pizza(ABC):
    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        self.ingredient_factory = ingredient_factory
        self.name = None

    def set_name(self, name):
        self.name = name

    def prepare(self):
        print(f'Подготовка пиццы {self.name}')

    def bake(self):
        print(f'Выпечка пиццы {self.name}')

    def cut(self):
        print(f'Нарезание пиццы {self.name}')

    def box(self):
        print(f'Упаковка пиццы {self.name}')


class CheesePizza(Pizza):
    def prepare(self):
        print(f'Подготовка пиццы {self.name}')
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        cheese = self.ingredient_factory.create_cheese()
        print(
            f'Добавление ингредиентов: {dough}, {sauce}, {cheese}'
        )


class PepperoniPizza(Pizza):
    def prepare(self):
        print(f'Подготовка пиццы {self.name}')
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        pepperoni = self.ingredient_factory.create_pepperoni()
        print(
            f'Добавление ингредиентов: {dough}, {sauce}, {pepperoni}'
        )


class ClamPizza(Pizza):
    def prepare(self):
        print(f'Подготовка пиццы {self.name}')
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        clams = self.ingredient_factory.create_clams()
        print(
            f'Добавление ингредиентов: {dough}, {sauce}, {clams}'
        )


class VeggiePizza(Pizza):
    def prepare(self):
        print(f'Подготовка пиццы {self.name}')
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

    def get_style(self):
        return self.ingredient_factory.get_style()

    def create_pizza(self, pizza_type):
        if pizza_type == 'cheese':
            pizza = CheesePizza(self.ingredient_factory)
            pizza.set_name(
                f'Сырная пицца в стиле {self.get_style()}'
            )
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza(self.ingredient_factory)
            pizza.set_name(
                f'Пицца пепперони в стиле {self.get_style()}'
            )
        elif pizza_type == 'clam':
            pizza = ClamPizza(self.ingredient_factory)
            pizza.set_name(
                f'Пицца с мидиями в стиле {self.get_style()}'
            )
        elif pizza_type == 'veggie':
            pizza = VeggiePizza(self.ingredient_factory)
            pizza.set_name(
                f'Вегетарианская в стиле {self.get_style()}'
            )
        else:
            raise UnknounPizzaType(
                'Ошибка обработки заказа: неизвестный тип пиццы'
            )
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
