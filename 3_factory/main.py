from stores_pizzas import ChicagoPizzaStore, NYPizzaStore


def print_delimiter():
    print('-' * 20)


if __name__ == '__main__':
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()
    print_delimiter()
    ny_store.order_pizza('cheese')
    print_delimiter()
    chicago_store.order_pizza('cheese')
    print_delimiter()
    ny_store.order_pizza('pepperoni')
    print_delimiter()
    chicago_store.order_pizza('pepperoni')
    print_delimiter()
    ny_store.order_pizza('clam')
    print_delimiter()
    chicago_store.order_pizza('clam')
    print_delimiter()
    ny_store.order_pizza('veggie')
    print_delimiter()
    chicago_store.order_pizza('veggie')
    print_delimiter()
    ny_store.order_pizza('new')
    print_delimiter()
    chicago_store.order_pizza('new')
    print_delimiter()