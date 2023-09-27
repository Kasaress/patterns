from abc import ABC, abstractmethod


# Ингредиенты
class ThinCrustDough:
    def __str__(self) -> str:
        return 'Тонкое хрустящее тесто'


class ThickDough:
    def __str__(self) -> str:
        return 'Толстое пышное тесто'


class MarinaraSauce:
    def __str__(self) -> str:
        return 'Соус маринара'


class TomatoSauce:
    def __str__(self) -> str:
        return 'Соус томатный'


class ReggianoCheese:
    def __str__(self) -> str:
        return 'Пармезан'


class GoudaCheese:
    def __str__(self) -> str:
        return 'Сыр гауда'


class Garlic:
    def __str__(self) -> str:
        return 'Чеснок'


class Onion:
    def __str__(self) -> str:
        return 'Лук'


class Mushroom:
    def __str__(self) -> str:
        return 'Грибы'


class RedPepper:
    def __str__(self) -> str:
        return 'Красный перец'


class SlicedPepperoni:
    def __str__(self) -> str:
        return 'Нарезанная пепперони'


class FreshClams:
    def __str__(self) -> str:
        return 'Свежие мидии'


class FrozenClams:
    def __str__(self) -> str:
        return 'Замороженныеы мидии'


# Фабрики ингредиентов
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def get_style(self):
        """Возвращает стиль пиццы"""

    @abstractmethod
    def create_dough(self):
        """Тесто"""

    @abstractmethod
    def create_sauce(self):
        """Соус"""

    @abstractmethod
    def create_cheese(self):
        """Сыр"""

    @abstractmethod
    def create_veggies(self):
        """Овощи"""

    @abstractmethod
    def create_pepperoni(self):
        """Пепперони"""

    @abstractmethod
    def create_clams(self):
        """Мидии"""


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def get_style(self):
        """Возвращает стиль пиццы"""
        return 'Нью-Йорк'

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        """Соус"""
        return MarinaraSauce()

    def create_cheese(self):
        """Сыр"""
        return ReggianoCheese()

    def create_veggies(self):
        """Овощи"""
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self):
        """Пепперони"""
        return SlicedPepperoni()

    def create_clams(self):
        """Мидии"""
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def get_style(self):
        """Возвращает стиль пиццы"""
        return 'Чикаго'

    def create_dough(self):
        return ThickDough()

    def create_sauce(self):
        """Соус"""
        return TomatoSauce()

    def create_cheese(self):
        """Сыр"""
        return GoudaCheese()

    def create_veggies(self):
        """Овощи"""
        return [Garlic(), Onion(), Mushroom()]

    def create_pepperoni(self):
        """Пепперони"""
        return SlicedPepperoni()

    def create_clams(self):
        """Мидии"""
        return FrozenClams()
