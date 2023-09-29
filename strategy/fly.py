# для разнообразия кряканье наследуем от протокола,
# а летучесть от ABC
from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print('Лечу на крыльях')


class FlyNoWay(FlyBehavior):
    def fly(self):
        print('*Не умеет летать*')


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print('Лечу на ракете')
