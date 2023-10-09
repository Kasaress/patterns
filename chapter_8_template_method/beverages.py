from abc import ABC, abstractmethod
from typing import final


class CaffeineBeverage(ABC):
    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self) -> None:
        print('Добавить кипяток.')

    def pour_in_cup(self) -> None:
        print('Налить в чашку.')

    @final
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()


class Tea(CaffeineBeverage):
    def brew(self):
        print('Заварить чай.')

    def add_condiments(self):
        print('Добавить лимон.')


class Coffee(CaffeineBeverage):
    def brew(self):
        print('Заварить кофе.')

    def add_condiments(self):
        print('Добавить молоко.')
