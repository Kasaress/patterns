from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def excecute(self):
        pass


class NoCommand(Command):
    def excecute(self):
        print('я ничего не делаю')


class LightOnCommand(Command):
    def __init__(self, light) -> None:
        self.light = light

    def excecute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light) -> None:
        self.light = light

    def excecute(self):
        self.light.off()
