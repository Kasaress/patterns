from abc import ABC, abstractmethod


class Duck(ABC):
    """Прекрасные утки."""
    @abstractmethod
    def quack(self) -> None:
        pass

    @abstractmethod
    def fly(self) -> None:
        pass


class MallardDuck(Duck):
    def quack(self) -> None:
        print('кря')

    def fly(self) -> None:
        print('я лечу')


class Turkey(ABC):
    """Мерзкие индюки."""
    @abstractmethod
    def gobble(self) -> None:
        pass

    @abstractmethod
    def fly(self) -> None:
        pass


class WildTurkey(Turkey):
    def gobble(self) -> None:
        print('бр бр бр')

    def fly(self) -> None:
        print('я лечу недалеко')


class TurkeyAdaper(Duck):
    def __init__(self, turkey: Turkey) -> None:
        self.turkey = turkey

    def quack(self) -> None:
        self.turkey.gobble()

    def fly(self) -> None:
        for _ in range(5):
            self.turkey.fly()
