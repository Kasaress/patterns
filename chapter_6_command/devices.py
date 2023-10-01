class BaseDevice:
    """Базовый класс для типовых устройств."""
    def __init__(self) -> None:
        self._name: str = 'Неизвестное устройство'

    def on(self) -> None:
        print(f'Устройство "{self._name}" включено')

    def off(self) -> None:
        print(f'Устройство "{self._name}" выключено')


class Light(BaseDevice):
    """Класс для освещения в любой локации."""
    def __init__(self, location) -> None:
        self._name: str = f'Свет, {location}'


# Нетипичные девайсы, например, из внешнего кода.
# Как будто мы только знаем их интерфейс,
# но не можем его изменять
class Stereo:
    def __init__(self) -> None:
        self._name: str = 'Стереосистема'
        self.volume: int = 0

    def on(self) -> None:
        print(f'Устройство "{self._name}" включено')

    def off(self) -> None:
        print(f'Устройство "{self._name}" выключено')

    def set_cd(self) -> None:
        print(f'Устройство "{self._name}" готово работать с CD-дисками')

    def set_radio(self) -> None:
        print(f'Устройство "{self._name}" готово работать в режиме радио')

    def set_volume(self, volume: int) -> None:
        self.volume = volume
        print(f'Громкость устройства "{self._name}": {self.volume}')


class Fan:
    HIGH: int = 3
    MEDIUM: int = 2
    LOW: int = 1
    OFF: int = 0

    def __init__(self, location) -> None:
        self._name: str = f'Вентилятор "{location}"'
        self.speed: int = self.__class__.LOW

    def start(self) -> None:
        print(
            f'Устройство "{self._name}" включено\n'
            f'Скорость: {self.speed}.'
        )

    def high(self) -> None:
        self.speed = self.__class__.HIGH
        print(f'Скорость устройства "{self._name}": {self.speed}')

    def medium(self) -> None:
        self.speed = self.__class__.MEDIUM
        print(f'Скорость устройства "{self._name}": {self.speed}')

    def low(self) -> None:
        self.speed = self.__class__.LOW
        print(f'Скорость устройства "{self._name}": {self.speed}')

    def off(self) -> None:
        self.speed = self.__class__.OFF
        print(f'Скорость устройства "{self._name}": {self.speed}')

    def stop(self) -> None:
        self.off()
        print(
            f'Устройство "{self._name}" выключено\n'
            f'Скорость: {self.speed}.'
        )

    def set_speed(self, speed: int) -> None:
        self.speed = speed
        print(f'Скорость устройства "{self._name}": {self.speed}')

    def get_speed(self) -> int:
        return self.speed


# Конкретные устройства
bedroom_light = Light('Спальня')
kitchen_light = Light('Кухня')
stereo = Stereo()
kitchen_fan = Fan('Кухня')
