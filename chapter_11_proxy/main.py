from code import Person, OwnerProxy, NoOwnerProxy


def try_to_change(obj, attr, args):
    try:
        getattr(obj, attr)(*args)
    except (AttributeError, NotImplementedError) as error:
        print(error)


def start_proxy():
    yana = Person('Yana', 'female', 'python')
    yana_owner_proxy = OwnerProxy(yana)
    print(yana_owner_proxy)
    yana_owner_proxy.set_name('Буяна')
    print(yana_owner_proxy)
    try_to_change(yana_owner_proxy, 'set_geek_rating', (5,))
    vanya = Person('Vanya', 'male', 'books')
    vanya_no_owner_proxy = NoOwnerProxy(vanya)
    print(vanya_no_owner_proxy)
    try_to_change(vanya_no_owner_proxy, 'set_geek_rating', (5,))
    print(vanya_no_owner_proxy)


if __name__ == "__main__":
    start_proxy()
