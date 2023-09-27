from abc import abstractmethod
from typing import Any


class UnknounPizzaType(Exception):
    pass


class Pizza:
    @abstractmethod
    def get_description(self):
        pass

    def prepare(self):
        print(f'Подготовка пиццы {self.get_description}')

    def bake(self):
        print(f'Выпечка пиццы {self.get_description}')

    def cut(self):
        print(f'Нарезание пиццы {self.get_description}')

    def box(self):
        print(f'Упаковка пиццы {self.get_description}')


class NYStyleCheesePizza(Pizza):
    @property
    def get_description(self):
        return '"Нью-Йоркская сырная пицца"'

    def cut(self):
        print(f'Нарезание пиццы квадратиками {self.get_description}')


class NYStylePepperoniPizza(Pizza):
    @property
    def get_description(self):
        return '"Нью-Йоркская пицца пепперони"'


class NYStylePClamPizza(Pizza):
    @property
    def get_description(self):
        return '"Нью-Йоркская пицца с мидиями"'


class NYStylePVeggiePizza(Pizza):
    @property
    def get_description(self):
        return '"Нью-Йоркская вегетарианская пицца"'


class ChicagoStyleCheesePizza(Pizza):
    @property
    def get_description(self):
        return '"Чикагская сырная пицца"'

    def cut(self):
        print(f'Нарезание пиццы кружочками {self.get_description}')


class ChicagoStylePepperoniPizza(Pizza):
    @property
    def get_description(self):
        return '"Чикагская пицца пепперони"'


class ChicagoStylePClamPizza(Pizza):
    @property
    def get_description(self):
        return '"Чикагская пицца с мидиями"'


class ChicagoStylePVeggiePizza(Pizza):
    @property
    def get_description(self):
        return '"Чикагская вегетарианская пицца"'


class PizzaStore:
    def __init__(self) -> None:
        self.pizza = None

    @abstractmethod
    def create_pizza(self, pizza_type):
        pass

    def order_pizza(self, pizza_type) -> Any:
        try:
            self.pizza = self.create_pizza(pizza_type)
            self.pizza.prepare()
            self.pizza.bake()
            self.pizza.cut()
            self.pizza.box()
            return self.pizza
        except UnknounPizzaType as error:
            print(error)


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == 'cheese':
            pizza = NYStyleCheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = NYStylePepperoniPizza()
        elif pizza_type == 'clam':
            pizza = NYStylePClamPizza()
        elif pizza_type == 'veggie':
            pizza = NYStylePVeggiePizza()
        else:
            raise UnknounPizzaType('Unknown type of pizza')
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == 'cheese':
            pizza = ChicagoStyleCheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = ChicagoStylePepperoniPizza()
        elif pizza_type == 'clam':
            pizza = ChicagoStylePClamPizza()
        elif pizza_type == 'veggie':
            pizza = ChicagoStylePVeggiePizza()
        else:
            raise UnknounPizzaType('Unknown type of pizza')
        return pizza


if __name__ == '__main__':
    ny_store = NYPizzaStore()
    ny_store.order_pizza('cheese')
    ny_store = ChicagoPizzaStore()
    ny_store.order_pizza('cheese')
