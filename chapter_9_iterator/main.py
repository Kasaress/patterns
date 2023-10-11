from menu import PancakeHouseMenu, DinnerMenu, Waitress
from items import breakfast, dinner


def start_iterator():
    pancake_menu = PancakeHouseMenu()
    for item in breakfast:
        pancake_menu.add_item(*item)
    dinner_menu = DinnerMenu()
    for item in dinner:
        dinner_menu.add_item(*item)
    waitress = Waitress([pancake_menu, dinner_menu])
    waitress.print_menu()


if __name__ == "__main__":
    start_iterator()
