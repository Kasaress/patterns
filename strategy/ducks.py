from abc import ABC, abstractmethod
from fly import FlyWithWings, FlyNoWay, FlyBehavior
from quack import Quack, Squeak, MuteQuack, QuackBehavior


class Duck(ABC):
    """
        Абстрактный базовый класс утки.
        В наследниках необходимо установить атрибуты класса.
    """
    _fly_behavior: FlyBehavior
    _quack_behavior: QuackBehavior

    @abstractmethod
    def display(self) -> None:
        """Выводит название утки."""
        pass

    @property
    def fly_behavior(self) -> FlyBehavior:
        """Возращает экземпляр класса летного поведения."""
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self, fly_behavior: FlyBehavior) -> None:
        """Изменяет класс летного поведения."""
        self._fly_behavior = fly_behavior

    @property
    def quack_behavior(self) -> QuackBehavior:
        """Возращает экземпляр класса крякающего поведения."""
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior: QuackBehavior) -> None:
        """Изменяет класс крякающего поведения."""
        self._quack_behavior = quack_behavior

    def perform_fly(self) -> None:
        """
            Не знает, что произойдет при вызове метода fly,
            но знает, что он есть.
        """
        self.fly_behavior.fly()

    def perform_quack(self) -> None:
        """
            Не знает, что произойдет при вызове метода quack,
            но знает, что он есть.
        """
        self.quack_behavior.quack()


class MallardDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self) -> None:
        print("Дикая утка")


class RedHeadDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = MuteQuack()

    def display(self):
        print('Красноголовая утка')


class RubberDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self):
        print('Резиновая утка')


class ModelDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print('Утка-приманка')
