from commands import (KitchenFanOffCommand, KitchenFanOnCommand,
                      SimpleOffCommand, SimpleOnCommand, StereoCDOffCommand,
                      StereoCDOnCommand, StereoRadioOffCommand,
                      StereoRadioOnCommand)
from devices import Fan, Light, Stereo

SLOTS_COUNT: int = 7  # количество наборов команд для устройств

bedroom_light = Light('Спальня')
kitchen_light = Light('Кухня')
stereo = Stereo()
kitchen_fan = Fan('Кухня')

commands = {
    0: {
        'device':  kitchen_light,
        'on': SimpleOnCommand(kitchen_light),
        'off': SimpleOffCommand(kitchen_light)
    },
    1: {
        'device':  bedroom_light,
        'on': SimpleOnCommand(bedroom_light),
        'off': SimpleOffCommand(bedroom_light)
    },
    2: {
        'device':  stereo,
        'on': StereoCDOnCommand(stereo),
        'off': StereoCDOffCommand(stereo)
    },
    3: {
        'device':  stereo,
        'on': StereoRadioOnCommand(stereo),
        'off': StereoRadioOffCommand(stereo)
    },
    4: {
        'device':  kitchen_fan,
        'on': KitchenFanOnCommand(kitchen_fan),
        'off': KitchenFanOffCommand(kitchen_fan)
    }
}
