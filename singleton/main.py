from support import print_delimiter
from boiler import ChocolateBoiler


if __name__ == '__main__':
    # Пытаемся создать 2 бойлера
    for _ in range(2):
        boiler = ChocolateBoiler()
        print(
            f"Объект ChocolateBoiler c id {id(boiler)} создан."
        )
        boiler.fill()
        boiler.boil()
        boiler.drain()
        print_delimiter()
