from commands import (BedroomLightOffCommand, BedroomLightOnCommand,
                      KitchenFanHighOffCommand, KitchenFanHighOnCommand,
                      KitchenFanOffCommand, KitchenFanOnCommand,
                      KitchenLightOffCommand, KitchenLightOnCommand,
                      PartyOffMacroCommand, PartyOnMacroCommand,
                      StereoCDOffCommand, StereoCDOnCommand,
                      StereoRadioOffCommand, StereoRadioOnCommand)

SLOTS_COUNT: int = 7  # количество наборов команд для устройств

commands = {
    0: {
        'on': KitchenLightOnCommand(),
        'off': KitchenLightOffCommand()
    },
    1: {
        'on': BedroomLightOnCommand(),
        'off': BedroomLightOffCommand()
    },
    2: {
        'on': StereoCDOnCommand(),
        'off': StereoCDOffCommand()
    },
    3: {
        'on': StereoRadioOnCommand(),
        'off': StereoRadioOffCommand()
    },
    4: {
        'on': KitchenFanOnCommand(),
        'off': KitchenFanOffCommand()
    },
    5: {
        'on': KitchenFanHighOnCommand(),
        'off': KitchenFanHighOffCommand()
    },
    6: {
        'on': PartyOnMacroCommand(),
        'off': PartyOffMacroCommand()
    }
}
