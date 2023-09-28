from ducks import MallardDuck, RedHeadDuck, RubberDuck
from support import print_delimiter


if __name__ == "__main__":
    # duck = RubberDuck()
    # duck.perform_fly()
    # duck.perform_quack()
    ducks_types = (
        MallardDuck, RedHeadDuck, RubberDuck
    )
    for duck_type in ducks_types:
        duck = duck_type()
        duck.perform_fly()
        duck.perform_quack()
        print_delimiter()
