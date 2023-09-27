from stores_pizzas import ChicagoPizzaStore, NYPizzaStore

if __name__ == '__main__':
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()
    ny_store.order_pizza('cheese')
    chicago_store.order_pizza('cheese')
    ny_store.order_pizza('pepperoni')
    chicago_store.order_pizza('pepperoni')
    ny_store.order_pizza('clam')
    chicago_store.order_pizza('clam')
    ny_store.order_pizza('veggie')
    chicago_store.order_pizza('veggie')
