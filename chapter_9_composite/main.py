from items import breakfast, desserts, dinner
from menu import Menu, MenuItem, Waitress


def start_iterator():
    pancake_menu = Menu('Pancake_Menu', 'Завтраки')
    dinner_menu = Menu('Dinner_menu', 'Обеды')
    dessert_menu = Menu('Dessert_menu', 'Десерты')
    all_menus = Menu('All_menus', 'Полное меню')
    all_menus.add(pancake_menu)
    all_menus.add(dinner_menu)
    for item in breakfast:
        pancake_menu.add(MenuItem(*item))
    for item in dinner:
        dinner_menu.add(MenuItem(*item))
    for item in desserts:
        dessert_menu.add(MenuItem(*item))
    dinner_menu.add(dessert_menu)
    waitress = Waitress(all_menus)
    waitress.print_menu()


if __name__ == "__main__":
    start_iterator()
