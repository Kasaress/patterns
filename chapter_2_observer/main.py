from active_observers import (ConditionsDisplayActive, WatchDisplayActive,
                              WeatherDataActive)
from passive_observers import (CurrentConditionsDisplay, WatchDisplay,
                               WeatherData)


def start_passive_observer():
    weather_data = WeatherData()
    display = CurrentConditionsDisplay(weather_data)
    WatchDisplay(weather_data)
    weather_data.set_measurement(80, 65, 30.4)
    weather_data.remove_observer(display)
    weather_data.set_measurement(50, 15, 34.4)
    weather_data.register_observer(display)
    weather_data.set_measurement(503, 5, 4.4)
    print('--------------------')


def start_active_observer():
    weather_data_active = WeatherDataActive()
    display = ConditionsDisplayActive(weather_data_active)
    WatchDisplayActive(weather_data_active)
    weather_data_active.set_measurement(80, 65, 30.4)
    weather_data_active.remove_observer(display)
    weather_data_active.set_measurement(50, 15, 34.4)
    weather_data_active.register_observer(display)
    weather_data_active.set_measurement(503, 5, 4.4)
    print('--------------------')


def start_observer():
    start_passive_observer()
    start_active_observer()


if __name__ == '__main__':
    start_observer()
