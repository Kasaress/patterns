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


class Observer(ABC):

    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        pass

    def __repr__(self) -> None:
        return self.__class__.__name__


class DisplayElement(ABC):

    @abstractmethod
    def display(self) -> None:
        pass


class WeatherData(Subject):
    def __init__(self):
        self._observers: set[Observer] = set()
        self._temperature: float | None = None
        self._humidity: float | None = None
        self._pressure: float | None = None

    def register_observer(self, observer: Observer) -> None:
        self._observers.add(observer)
        print(f'Зарегистирован наблюдатель: {observer}')

    def remove_observer(self, observer: Observer) -> None:
        self._observers.discard(observer)
        print(f'Удален наблюдатель: {observer}')

    def notify_observer(self) -> None:
        for observer in self._observers:
            observer.update(
                self._temperature,
                self._humidity,
                self._pressure
            )
        print(
            'Уведомлены наблюдатели: '
            f'{", ".join(str(observer) for observer in self._observers)}'
        )

    def measurement_chaged(self) -> None:
        self.notify_observer()

    def set_measurement(self, temp: float, humidity: float, pressure: float):
        self._temperature = temp
        self._humidity = humidity
        self._pressure = pressure
        self.measurement_chaged()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self._temperature: float | None = None
        self._humidity: float | None = None
        self._weather_data: WeatherData = weather_data
        self._weather_data.register_observer(self)

    def display(self) -> None:
        print(
            f'Текущие показатели: температура {self._temperature}, '
            f'влажность {self._humidity}'
        )

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self._temperature = temp
        self._humidity = humidity
        self.display()


class WatchDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self._temperature: float | None = None
        self._humidity: float | None = None
        self._pressure: float | None = None
        self._weather_data: WeatherData = weather_data
        self._weather_data.register_observer(self)

    def display(self) -> None:
        print(
            f'Текущие показатели: температура {self._temperature}, '
            f'влажность {self._humidity}',
            f'давление {self._pressure}',
        )

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self._temperature = temp
        self._humidity = humidity
        self._pressure = pressure
        self.display()
