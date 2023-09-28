from abc import ABC, abstractmethod


class QuackBehavior(ABC):
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
        # print('*угрюмо молчит')
        pass
