from active_observers import (ConditionsDisplayActive,
                                       WatchDisplayActive, WeatherDataActive)
from passive_observers import (CurrentConditionsDisplay, WatchDisplay,
                                        WeatherData)


def start_passive_observer():
    weather_data = WeatherData()
    display1 = CurrentConditionsDisplay(weather_data)
    display2 = WatchDisplay(weather_data)
    weather_data.set_measurement(80, 65, 30.4)
    weather_data.remove_observer(display2)
    weather_data.set_measurement(50, 15, 34.4)
    weather_data.register_observer(display2)
    weather_data.set_measurement(503, 5, 4.4)
    print('--------------------')
    weather_data_active = WeatherDataActive()
    display3 = ConditionsDisplayActive(weather_data_active)
    display4 = WatchDisplayActive(weather_data_active)
    weather_data_active.set_measurement(80, 65, 30.4)
    weather_data_active.remove_observer(display3)
    weather_data_active.set_measurement(50, 15, 34.4)
    weather_data_active.register_observer(display3)
    weather_data_active.set_measurement(503, 5, 4.4)
    print('--------------------')


if __name__ == '__main__':
    start_passive_observer()
