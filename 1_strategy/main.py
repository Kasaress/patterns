from ducks import MallardDuck, RedHeadDuck, RubberDuck
from support import print_delimiter


if __name__ == "__main__":
    ducks_types = (
        MallardDuck, RedHeadDuck, RubberDuck
    )
    for duck_type in ducks_types:  # type: ignore
        duck = duck_type()  # type: ignore
        duck.perform_fly()  # type: ignore
        duck.perform_quack()  # type: ignore
        print_delimiter()
