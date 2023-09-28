from decorators import singleton, singleton_angry


# Можно выбрать один из двух декораторов
# Один лицемерный, второй кусаица
@singleton
# @singleton_angry
class ChocolateBoiler:
    def __init__(self) -> None:
        self.__empty = True
        self.__boiled = False

    @property
    def empty(self) -> bool:
        return self.__empty

    @property
    def boiled(self) -> bool:
        return self.__boiled

    def fill(self) -> None:
        """Заполнение бойлера."""
        if self.empty:
            self.__empty = False
            self.__boiled = False
            print('Заполнили бойлер чем-то холодным.')

    def boil(self) -> None:
        """Нагревание бойлера."""
        if not self.empty and not self.boiled:
            self.__boiled = True
            print('Нагрели содержимое бойлера.')

    def drain(self) -> None:
        """Опустошение бойлера."""
        if not self.empty and self.boiled:
            self.__empty = True
            print('Слили все из бойлера.')
