from constants import SLOTS_COUNT, commands
from remout_control import RemoutControl


def create_control_and_set_commands() -> RemoutControl:
    """Создает пульт и привязывает команды к кнопкам."""
    control = RemoutControl()
    for slot, data in commands.items():
        control.set_command(
            slot, data.get('on'), data.get('off')  # type: ignore
        )
    print(control)
    return control


def start_command():
    """Имитирует нажатие на все кнопки пульта."""
    control = create_control_and_set_commands()
    for i in range(1, SLOTS_COUNT):
        control.on_button_was_pressed(i)
        control.off_button_was_pressed(i)
        control.undo_button_was_pressed()


if __name__ == "__main__":
    start_command()
