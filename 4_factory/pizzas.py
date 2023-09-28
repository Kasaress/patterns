from abc import ABC

from ingredients import PizzaIngredientFactory


# Пиццы
class Pizza(ABC):
    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        self.ingredient_factory = ingredient_factory
        self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

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
