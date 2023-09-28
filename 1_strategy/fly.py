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
        # print('Я не умею летать')
        pass
