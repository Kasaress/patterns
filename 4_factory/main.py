from constants import PIZZAS
from stores import ChicagoPizzaStore, NYPizzaStore


def print_delimiter():
    print('-' * 20)


if __name__ == '__main__':
    ny_store = NYPizzaStore()  # Создание пиццерии в Нью-Йоркском стиле
    chicago_store = ChicagoPizzaStore()  # Создание пиццерии в Чикагском стиле
    print_delimiter()
    pizzas = list(PIZZAS.keys())
    pizzas.append('new')  # Проверка обработки несуществующей пиццы
    for store in (ny_store, chicago_store):  # Создание всех возможных пицц
        for pizza_type in pizzas:
            store.order_pizza(pizza_type)
            print_delimiter()
