from ducks import Duck, MallardDuck, TurkeyAdaper, WildTurkey


def test_duck(duck: Duck) -> None:
    duck.quack()
    duck.fly()


def start_adapter():
    duck = MallardDuck()
    turkey = WildTurkey()
    turkey_adapter = TurkeyAdaper(turkey)
    print('Индюшка')
    turkey.gobble()
    turkey.fly()
    print('Утка')
    duck.quack()
    duck.fly()
    print('Адаптер')
    test_duck(turkey_adapter)


if __name__ == "__main__":
    start_adapter()
