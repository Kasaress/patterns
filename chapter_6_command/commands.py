from abc import ABC, abstractmethod

from devices import BaseDevice, Fan, Stereo


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


class SimpleOnCommand(Command):
    def __init__(self, device: BaseDevice) -> None:
        self.device: BaseDevice = device

    def excecute(self):
        self.device.on()

    def undo(self):
        self.device.off()


class SimpleOffCommand(Command):
    def __init__(self, device: BaseDevice) -> None:
        self.device: BaseDevice = device

    def excecute(self):
        self.device.off()

    def undo(self):
        self.device.on()


class StereoCDOnCommand(Command):
    def __init__(self, device: Stereo) -> None:
        self.device: Stereo = device

    def excecute(self):
        self.device.on()
        self.device.set_cd()
        self.device.set_volume(11)

    def undo(self):
        self.device.off()


class StereoCDOffCommand(Command):
    def __init__(self, device: Stereo) -> None:
        self.device: Stereo = device

    def excecute(self):
        self.device.off()

    def undo(self):
        self.device.on()
        self.device.set_cd()
        self.device.set_volume(11)


class StereoRadioOnCommand(Command):
    def __init__(self, device: Stereo) -> None:
        self.device: Stereo = device

    def excecute(self):
        self.device.on()
        self.device.set_radio()
        self.device.set_volume(9)

    def undo(self):
        self.device.off()


class StereoRadioOffCommand(Command):
    def __init__(self, device: Stereo) -> None:
        self.device: Stereo = device

    def excecute(self):
        self.device.off()

    def undo(self):
        self.device.on()
        self.device.set_radio()
        self.device.set_volume(9)


class KitchenFanOnCommand(Command):
    def __init__(self, device: Fan) -> None:
        self.device: Fan = device

    def excecute(self):
        self.device.start()
        self.device.set_speed(40)

    def undo(self):
        self.device.stop()


class KitchenFanOffCommand(Command):
    def __init__(self, device: Fan) -> None:
        self.device: Fan = device

    def excecute(self):
        self.device.stop()

    def undo(self):
        self.device.start()
        self.device.set_speed(40)
