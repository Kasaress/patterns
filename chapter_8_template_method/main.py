from beverages import Coffee, Tea


def start_template():
    tea = Tea()
    tea.prepare_recipe()
    print('--------')
    coffee = Coffee()
    coffee.prepare_recipe()


if __name__ == "__main__":
    start_template()
