from ducks import MallardDuck, RedHeadDuck, RubberDuck
from fly import FlyRocketPowered
from quack import MuteQuack
from support import print_delimiter


def start_stategy():
    ducks_types = (
        MallardDuck, RedHeadDuck, RubberDuck
    )
    for duck_type in ducks_types:
        duck = duck_type()  # type: ignore
        duck.display()
        duck.perform_fly()
        duck.perform_quack()
        # Меняем поведение утки
        duck.fly_behavior = FlyRocketPowered()
        duck.quack_behavior = MuteQuack()
        duck.perform_fly()
        duck.perform_quack()
        print_delimiter()


if __name__ == "__main__":
    start_stategy()
