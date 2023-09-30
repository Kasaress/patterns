from remout_control import RemoutControl
from devices import Light
from commands import LightOnCommand, LightOffCommand


def start_command():
    bedroom_light = Light('Спальня')
    bedroom_light_on = LightOnCommand(bedroom_light)
    bedroom_light_off = LightOffCommand(bedroom_light)
    control = RemoutControl()
    control.set_command(1, bedroom_light_on, bedroom_light_off)
    control.on_button_was_pressed(1)
    control.off_button_was_pressed(1)


if __name__ == "__main__":
    start_command()
