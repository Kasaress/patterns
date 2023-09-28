from functools import wraps
from exceptions import DoubleCreateSingletonException


def singleton(cls):
    """
        Разрешает создавать только один экземпляр класса.
        При попытке создать больше одного экземпляра,
        тихо подсовывает первый и единственный.
    """
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.__instance__:
            wrapper.__instance__ = cls(*args, **kwargs)
        return wrapper.__instance__
    wrapper.__instance__ = None
    return wrapper


def singleton_angry(cls):
    """
        Разрешает создавать только один экземпляр класса.
        Громко падает при попытке создать больше одного экземпляра!
    """
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.__instance__:
            wrapper.__instance__ = cls(*args, **kwargs)
        else:
            raise DoubleCreateSingletonException(
                f'Один экземпляр {cls.__name__} уже существует.'
            )
        return wrapper.__instance__
    wrapper.__instance__ = None
    return wrapper
