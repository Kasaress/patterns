from abc import ABC, abstractmethod, abstractproperty
from fly import FlyWithWings, FlyNoWay, FlyBehavior
from quack import Quack, Squeak, MuteQuack, QuackBehavior


class Duck(ABC):
    def __init__(self) -> None:
        super().__init__()
        print(f'Вот какая я уточка: {self.display()}')

    @abstractproperty
    def fly_behavior(self) -> FlyBehavior:
        pass

    @abstractproperty
    def quack_behavior(self) -> QuackBehavior:
        pass

    @abstractmethod
    def display(self) -> str:
        pass

    def perform_fly(self) -> None:
        return self.fly_behavior.fly()

    def perform_quack(self) -> None:
        return self.quack_behavior.quack()


class MallardDuck(Duck):
    @property
    def fly_behavior(self) -> FlyWithWings:
        return FlyWithWings()

    @property
    def quack_behavior(self) -> Quack:
        return Quack()

    def display(self):
        return 'Дикая утка'


class RedHeadDuck(Duck):
    @property
    def fly_behavior(self) -> FlyWithWings:
        return FlyWithWings()

    @property
    def quack_behavior(self) -> MuteQuack:
        return MuteQuack()

    def display(self):
        return 'Красноголовая утка'


class RubberDuck(Duck):
    @property
    def fly_behavior(self) -> FlyNoWay:
        return FlyNoWay()

    @property
    def quack_behavior(self) -> Squeak:
        return Squeak()

    def display(self):
        return 'Резиновая утка'
