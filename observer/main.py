from weather_station import WeatherData, CurrentConditionsDisplay, WatchDisplay


def start_observer():
    weather_data = WeatherData()
    display1 = CurrentConditionsDisplay(weather_data)
    display2 = WatchDisplay(weather_data)
    weather_data.set_measurement(80, 65, 30.4)
    weather_data.set_measurement(84, 35, 34.4)


if __name__ == '__main__':
    start_observer()
