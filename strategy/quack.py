# для разнообразия кряканье наследуем от протокола,
# а летучесть от ABC
from abc import abstractmethod
from typing import Protocol


class QuackBehavior(Protocol):
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print('Кря-кря')


class Squeak(QuackBehavior):
    def quack(self):
        print('Пи-пи-пи')


class MuteQuack(QuackBehavior):
    def quack(self):
        print('*угрюмо молчит*')
