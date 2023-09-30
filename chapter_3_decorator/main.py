from constants import BASE_MENU, TOPPING_MENU


def start_decorator():
    for base in BASE_MENU:
        for top1 in TOPPING_MENU:
            for top2 in TOPPING_MENU:
                top2(top1(base())).info


if __name__ == "__main__":
    start_decorator()
