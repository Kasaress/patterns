from commands import Command, NoCommand


class RemoutControl:
    def __init__(self) -> None:
        self._on_commands: dict[int, Command] = {
                i: NoCommand() for i in range(1, 7)
            }
        self._off_commands: dict[int, Command] = {
                i: NoCommand() for i in range(1, 7)
            }

    def __str__(self) -> str:
        return (
            'Пульт управления'
            'Команды включения: '
            f'{[command.__class__.__name__ for command in self._on_commands]}'
            'Комманды выключения: '
            f'{[command.__class__.__name__ for command in self._off_commands]}'
        )

    def set_command(
            self, slot: int, command_on: Command, command_off: Command
            ):
        self._on_commands[slot] = command_on
        self._off_commands[slot] = command_off

    def on_button_was_pressed(self, slot: int):
        self._on_commands[slot].excecute()

    def off_button_was_pressed(self, slot: int):
        self._off_commands[slot].excecute()
