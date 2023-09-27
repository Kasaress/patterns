from abc import ABC, abstractproperty
from typing import Any

from exceptions import UnknounPizzaTypeException
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
        print(f'Подготовка {self.name}')

    def bake(self):
        print(f'Выпечка {self.name}')

    def cut(self):
        print(f'Нарезание  {self.name}')

    def box(self):
        print(f'Упаковка {self.name}')


class CheesePizza(Pizza):
    def prepare(self):
        print(f'Подготовка {self.name}')
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        cheese = self.ingredient_factory.create_cheese()
        print(
            f'Добавление ингредиентов: {dough}, {sauce}, {cheese}'
        )


class PepperoniPizza(Pizza):
    def prepare(self):
        print(f'Подготовка {self.name}')
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        pepperoni = self.ingredient_factory.create_pepperoni()
        print(
            f'Добавление ингредиентов: {dough}, {sauce}, {pepperoni}'
        )


class ClamPizza(Pizza):
    def prepare(self):
        print(f'Подготовка {self.name}')
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        clams = self.ingredient_factory.create_clams()
        print(
            f'Добавление ингредиентов: {dough}, {sauce}, {clams}'
        )


class VeggiePizza(Pizza):
    def prepare(self):
        print(f'Подготовка {self.name}')
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        veggies = ', '.join(
            str(veg) for veg in self.ingredient_factory.create_veggies()
        )
        print(
            f'Добавление ингредиентов: {dough}, {sauce}, {veggies}'
        )


PIZZAS = {
    'cheese': {
        'type': CheesePizza,
        'name': 'Сырная',
    },
    'pepperoni': {
        'type': PepperoniPizza,
        'name': 'Пепперони',
    },
    'clam': {
        'type': ClamPizza,
        'name': 'С мидиями',
    },
    'veggie': {
        'type': VeggiePizza,
        'name': 'Вегетарианская',
    },
}


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
                f'Можете выбрать из меню: {", ".join(pizza["name"] for pizza in PIZZAS.values())}'
            )
        pizza = PIZZAS.get(pizza_type).get('type')((self.ingredient_factory))
        pizza.set_name(
            f'"{PIZZAS.get(pizza_type).get("name")} пицца в стиле {self.get_style()}"'
        )
        return pizza

    def order_pizza(self, pizza_type) -> Any:
        try:
            self.pizza = self.create_pizza(pizza_type)
            print(f'Поступил заказ: {self.pizza.name}')
            self.pizza.prepare()
            self.pizza.bake()
            self.pizza.cut()
            self.pizza.box()
            return self.pizza
        except UnknounPizzaTypeException as error:
            print(error)


class NYPizzaStore(PizzaStore):
    @property
    def ingredient_factory(self):
        return NYPizzaIngredientFactory()


class ChicagoPizzaStore(PizzaStore):
    @property
    def ingredient_factory(self):
        return ChicagoPizzaIngredientFactory()
