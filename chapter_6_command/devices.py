from abc import ABC, abstractmethod


class BaseDevice(ABC):
    # @abstractmethod
    # def get_name(self):
    #     pass

    @abstractmethod
    def on(self) -> None:
        pass

    @abstractmethod
    def off(self) -> None:
        pass


class Light(BaseDevice):
    def __init__(self, location) -> None:
        self._name: str = f'Свет, {location}'

    def on(self) -> None:
        print(f'{self._name} включен')

    def off(self) -> None:
        print(f'{self._name} выключен')
