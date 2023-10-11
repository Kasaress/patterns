from menu import PancakeHouseMenu, DinnerMenu
from items import breakfast, dinner


def start_iterator():
    pancake_menu = PancakeHouseMenu()
    for item in breakfast:
        pancake_menu.add_item(*item)
    print(pancake_menu.get_menu_items())
    dinner_menu = DinnerMenu()
    for item in dinner:
        dinner_menu.add_item(*item)
    print(dinner_menu.get_menu_items())


if __name__ == "__main__":
    start_iterator()
