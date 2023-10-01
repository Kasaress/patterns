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
    def __init__(self, location) -> None:
        self._name: str = f'Вентилятор "{location}"'
        self.speed: int = 0

    def start(self) -> None:
        print(f'Устройство "{self._name}" включено')

    def stop(self) -> None:
        print(f'Устройство "{self._name}" выключено')

    def set_speed(self, speed: int) -> None:
        self.speed = speed
        print(f'Скорость устройства "{self._name}": {self.speed}')
