import random
from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, machine: 'GumballMachine') -> None:
        self.machine = machine

    def __repr__(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def insert_quarter(self) -> None:
        """Вставить монету."""

    @abstractmethod
    def eject_quarter(self) -> None:
        """Вернуть монету."""

    @abstractmethod
    def dispense(self) -> None:
        """Выдать покупку."""

    @abstractmethod
    def turn_crank(self) -> None:
        """Дергнуть рычаг."""

    @abstractmethod
    def refill(self) -> None:
        """Заполнить автомат шариками."""


class NoQuarterState(State):
    def insert_quarter(self) -> None:
        """Вставить монету."""
        print('Вы вставили монету.')
        self.machine.set_state(self.machine.get_has_quarter_state())

    def eject_quarter(self) -> None:
        """Вернуть монету."""
        print('Мы не можем вернуть монету - вы ее не вставили.')

    def dispense(self) -> None:
        """Выдать покупку."""
        print('Сначала заплати!')

    def turn_crank(self) -> None:
        """Дергнуть рычаг."""
        print('Дергаете рычаг, а монету не вставили!')

    def refill(self) -> None:
        """Заполнить автомат шариками."""


class HasQuarterState(State):
    def insert_quarter(self) -> None:
        """Вставить монету."""
        print('Нельзя вставить еще одну монету.')

    def eject_quarter(self) -> None:
        """Вернуть монету."""
        print('Монета возвращена.')
        self.machine.set_state(self.machine.get_no_quarter_state())

    def dispense(self) -> None:
        """Выдать покупку."""
        print('Шарик не будет выдан')

    def turn_crank(self) -> None:
        """Дергнуть рычаг."""
        print('Вы дернули рычаг.')
        r = random.randint(1, 10)
        if r == 10 and self.machine.get_count() > 1:
            self.machine.set_state(self.machine.get_winner_state())
        else:
            self.machine.set_state(self.machine.get_sold_state())

    def refill(self) -> None:
        """Заполнить автомат шариками."""


class SoldState(State):
    def insert_quarter(self) -> None:
        """Вставить монету."""
        print('Подождите, покупка в процессе')

    def eject_quarter(self) -> None:
        """Вернуть монету."""
        print('Не можем вернуть монету, покупка в процессе')

    def dispense(self) -> None:
        """Выдать покупку."""
        self.machine.release_ball()
        if self.machine.get_count() > 0:
            self.machine.set_state(self.machine.get_no_quarter_state())
        else:
            print('Больше шариков нет, все продали!')
            self.machine.set_state(self.machine.get_sold_out_state())

    def turn_crank(self) -> None:
        """Дергнуть рычаг."""
        print('Не дергайте больше, покупка в процессе')

    def refill(self) -> None:
        """Заполнить автомат шариками."""


class SoldOutState(State):
    def insert_quarter(self) -> None:
        """Вставить монету."""
        print('Автомат пуст.')

    def eject_quarter(self) -> None:
        """Вернуть монету."""
        print('Автомат пуст.')

    def dispense(self) -> None:
        """Выдать покупку."""
        print('Автомат пуст.')

    def turn_crank(self) -> None:
        """Дергнуть рычаг."""
        print('Автомат пуст.')

    def refill(self) -> None:
        """Заполнить автомат шариками."""
        print('Автомат будет заполнен шариками.')
        self.machine.set_state(self.machine.get_no_quarter_state())


class WinnerState(State):
    def insert_quarter(self) -> None:
        """Вставить монету."""
        print('Подождите, покупка в процессе')

    def eject_quarter(self) -> None:
        """Вернуть монету."""
        print('Не можем вернуть монету, покупка в процессе')

    def dispense(self) -> None:
        """Выдать покупку."""
        self.machine.release_ball()
        if self.machine.get_count() == 0:
            print('Больше шариков нет, все продали!')
            self.machine.set_state(self.machine.get_sold_out_state())
        else:
            print('Вы выиграли! Выдаем второй шарик :)')
            self.machine.release_ball()
            if self.machine.get_count() > 0:
                self.machine.set_state(self.machine.get_no_quarter_state())
            else:
                print('Больше шариков нет, все продали!')
                self.machine.set_state(self.machine.get_sold_out_state())

    def turn_crank(self) -> None:
        """Дергнуть рычаг."""
        print('Не дергайте больше, покупка в процессе')

    def refill(self) -> None:
        """Заполнить автомат шариками."""


class GumballMachine:
    def __init__(self, count: int = 0) -> None:
        self.sold_out = SoldOutState(self)
        self.no_quarter = NoQuarterState(self)
        self.has_quarter = HasQuarterState(self)
        self.sold = SoldState(self)
        self.winner = WinnerState(self)
        self.count = count
        self.state = self.no_quarter if self.count > 0 else self.sold_out

    def insert_quarter(self) -> None:
        self.state.insert_quarter()

    def eject_quarter(self) -> None:
        self.state.eject_quarter()

    def dispense(self) -> None:
        self.state.dispense()

    def turn_crank(self) -> None:
        self.state.turn_crank()
        self.state.dispense()

    def set_state(self, state: State) -> None:
        self.state = state

    def release_ball(self) -> None:
        if self.count != 0:
            self.count -= 1
        print(f'Шарик катится к вам, остаток: {self.count}')

    def get_count(self) -> int:
        return self.count

    def get_sold_out_state(self) -> State:
        return self.sold_out

    def get_no_quarter_state(self) -> State:
        return self.no_quarter

    def get_has_quarter_state(self) -> State:
        return self.has_quarter

    def get_sold_state(self) -> State:
        return self.sold

    def get_winner_state(self) -> State:
        return self.winner

    def refill(self, count: int) -> None:
        self.count += count
        print(f'В автомат добавлено {count} шариков. Всего: {self.count}')
        self.state.refill()

    def __repr__(self) -> str:
        return f'Состояние: {self.state}, жвачек: {self.count}'
