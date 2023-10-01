from abc import ABC, abstractmethod

from devices import (Fan, Light, Stereo, bedroom_light, kitchen_fan,
                     kitchen_light, stereo)


class Command(ABC):
    def __repr__(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def excecute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class NoCommand(Command):
    def excecute(self):
        print('Команда не установлена.')

    def undo(self):
        print('Команда не установлена, нечего отменять.')


class LightOnCommand(Command):
    def __init__(self) -> None:
        self.device: Light

    def excecute(self):
        self.device.on()

    def undo(self):
        self.device.off()


class LightOffCommand(Command):
    def __init__(self) -> None:
        self.device: Light

    def excecute(self):
        self.device.off()

    def undo(self):
        self.device.on()


class KitchenLightOnCommand(LightOnCommand):
    def __init__(self) -> None:
        self.device: Light = kitchen_light


class KitchenLightOffCommand(LightOffCommand):
    def __init__(self) -> None:
        self.device: Light = kitchen_light


class BedroomLightOnCommand(LightOnCommand):
    def __init__(self) -> None:
        self.device: Light = bedroom_light


class BedroomLightOffCommand(LightOffCommand):
    def __init__(self) -> None:
        self.device: Light = bedroom_light


class StereoCDOnCommand(Command):
    def __init__(self) -> None:
        self.device: Stereo = stereo

    def excecute(self):
        self.device.on()
        self.device.set_cd()
        self.device.set_volume(11)

    def undo(self):
        self.device.off()


class StereoCDOffCommand(Command):
    def __init__(self) -> None:
        self.device: Stereo = stereo

    def excecute(self):
        self.device.off()

    def undo(self):
        self.device.on()
        self.device.set_cd()
        self.device.set_volume(11)


class StereoRadioOnCommand(Command):
    def __init__(self) -> None:
        self.device: Stereo = stereo

    def excecute(self):
        self.device.on()
        self.device.set_radio()
        self.device.set_volume(9)

    def undo(self):
        self.device.off()


class StereoRadioOffCommand(Command):
    def __init__(self) -> None:
        self.device: Stereo = stereo

    def excecute(self):
        self.device.off()

    def undo(self):
        self.device.on()
        self.device.set_radio()
        self.device.set_volume(9)


class KitchenFanOnCommand(Command):
    def __init__(self) -> None:
        self.device: Fan = kitchen_fan

    def excecute(self):
        self.device.low()
        self.device.start()

    def undo(self):
        self.device.stop()


class KitchenFanOffCommand(Command):
    def __init__(self) -> None:
        self.device: Fan = kitchen_fan

    def excecute(self):
        self.device.stop()

    def undo(self):
        self.device.low()
        self.device.start()


class KitchenFanHighOnCommand(Command):
    def __init__(self) -> None:
        self.device: Fan = kitchen_fan
        self._prev_speed: int = 0

    def excecute(self):
        self.device.high()
        self.device.start()
        self._prev_speed = self.device.get_speed()

    def undo(self):
        # self.device.stop()
        print(f'предыдущая скорость {self._prev_speed}')
        self.device.set_speed(self._prev_speed)


class KitchenFanHighOffCommand(Command):
    def __init__(self) -> None:
        self.device: Fan = kitchen_fan
        self._prev_speed: int = 0

    def excecute(self):
        # self.device.stop()
        self.device.medium()
        self._prev_speed = self.device.get_speed()

    def undo(self):
        # self.device.start()
        # self.device.set_speed(40)
        self.device.high()
        self._prev_speed = self.device.get_speed()


class MacroCommand(Command):
    def __init__(self) -> None:
        self.commands: list[Command]

    def excecute(self):
        for command in self.commands:
            command.excecute()

    def undo(self):
        for command in self.commands:
            command.undo()


class PartyOnMacroCommand(MacroCommand):
    def __init__(self) -> None:
        self.commands = [StereoRadioOnCommand(), KitchenFanOnCommand()]


class PartyOffMacroCommand(MacroCommand):
    def __init__(self) -> None:
        self.commands = [StereoRadioOffCommand(), KitchenFanOffCommand()]
