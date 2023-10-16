from machine import GumballMachine


def start_state():
    machine = GumballMachine(5)
    print(machine)
    machine.insert_quarter()
    machine.turn_crank()

    print(machine)
    machine.insert_quarter()
    machine.eject_quarter()
    machine.turn_crank()

    print(machine)
    machine.insert_quarter()
    machine.turn_crank()
    machine.insert_quarter()
    machine.turn_crank()
    machine.eject_quarter()

    print(machine)
    machine.insert_quarter()
    machine.insert_quarter()
    machine.turn_crank()
    machine.insert_quarter()
    machine.turn_crank()
    machine.insert_quarter()
    machine.turn_crank()
    machine.refill(5)

    print(machine)
    machine.insert_quarter()
    machine.turn_crank()

    print(machine)


if __name__ == "__main__":
    start_state()
