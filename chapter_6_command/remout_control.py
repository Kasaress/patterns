from commands import Command, NoCommand
from constants import SLOTS_COUNT


class RemoutControl:
    """Пульт управления устройствами."""
    def __init__(self) -> None:
        self._on_commands: dict[int, Command] = {
                i: NoCommand() for i in range(SLOTS_COUNT)
            }
        self._off_commands: dict[int, Command] = {
                i: NoCommand() for i in range(SLOTS_COUNT)
            }
        self.undo_command: Command = NoCommand()

    def __repr__(self) -> str:
        return (
            'Пульт управления.\n'
            'Команды включения: '
            f'{[command for command in self._on_commands.values()]}.\n'
            'Команды выключения: '
            f'{[command for command in self._off_commands.values()]}.\n'
        )

    def set_command(
            self, slot: int, command_on: Command, command_off: Command
            ):
        """Привязывает пару команд для устройства к кнопкам на пульте."""
        self._on_commands[slot] = command_on
        self._off_commands[slot] = command_off

    def on_button_was_pressed(self, slot: int):
        """Запускает выполнение команды включения."""
        command = self._on_commands[slot]
        command.excecute()
        self.undo_command = command

    def off_button_was_pressed(self, slot: int):
        """Запускает выполнение команды выключения."""
        command = self._off_commands[slot]
        command.excecute()
        self.undo_command = command

    def undo_button_was_pressed(self):
        """Запускает выполнение команды выключения."""
        print('Галя, у нас отмена!')
        self.undo_command.undo()
