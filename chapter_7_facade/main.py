from facade import HomeTheaterFacade


def start_facade() -> None:
    facade = HomeTheaterFacade()
    facade.watch_movie('Мстители')
    facade.end_movie()


if __name__ == "__main__":
    start_facade()
