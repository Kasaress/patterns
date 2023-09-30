from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def register_observer(self) -> None:
        pass

    @abstractmethod
    def remove_observer(self) -> None:
        pass

    @abstractmethod
    def notify_observer(self) -> None:
        pass


class ObserverActive(ABC):

    @abstractmethod
    def update(self) -> None:
        pass

    def __repr__(self) -> None:
        return self.__class__.__name__


class DisplayElement(ABC):

    @abstractmethod
    def display(self) -> None:
        pass


class WeatherDataActive(Subject):
    def __init__(self):
        self._observers: set[ObserverActive] = set()
        self._temperature: float | None = None
        self._humidity: float | None = None
        self._pressure: float | None = None

    def register_observer(self, observer: ObserverActive) -> None:
        self._observers.add(observer)
        print(f'Зарегистирован наблюдатель: {observer}')

    def remove_observer(self, observer: ObserverActive) -> None:
        self._observers.discard(observer)
        print(f'Удален наблюдатель: {observer}')

    def notify_observer(self) -> None:
        for observer in self._observers:
            observer.update()
        print(
            'Уведомлены наблюдатели: '
            f'{", ".join(str(observer) for observer in self._observers)}'
        )

    def measurement_chaged(self) -> None:
        self.notify_observer()

    def set_measurement(
                self, temp: float, humidity: float, pressure: float
            ) -> None:
        self._temperature = temp
        self._humidity = humidity
        self._pressure = pressure
        self.measurement_chaged()

    def get_temperature(self) -> float:
        return self._temperature

    def get_humidity(self) -> float:
        return self._humidity

    def get_pressure(self) -> float:
        return self._pressure


class ConditionsDisplayActive(ObserverActive, DisplayElement):
    def __init__(self, weather_data):
        self._temperature: float | None = None
        self._humidity: float | None = None
        self._weather_data: WeatherDataActive = weather_data
        self._weather_data.register_observer(self)

    def display(self) -> None:
        print(
            f'Текущие показатели: температура {self._temperature}, '
            f'влажность {self._humidity}'
        )

    def update(self) -> None:
        self._temperature = self._weather_data.get_temperature()
        self._humidity = self._weather_data.get_humidity()
        self.display()


class WatchDisplayActive(ObserverActive, DisplayElement):
    def __init__(self, weather_data):
        self._temperature: float | None = None
        self._humidity: float | None = None
        self._pressure: float | None = None
        self._weather_data: WeatherDataActive = weather_data
        self._weather_data.register_observer(self)

    def display(self) -> None:
        print(
            f'Текущие показатели: температура {self._temperature}, '
            f'влажность {self._humidity}',
            f'давление {self._pressure}',
        )

    def update(self) -> None:
        self._temperature = self._weather_data.get_temperature()
        self._humidity = self._weather_data.get_humidity()
        self._pressure = self._weather_data.get_pressure()
        self.display()
