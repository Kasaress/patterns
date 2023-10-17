from abc import ABC


class AbstractPerson(ABC):
    def __init__(
        self,
        name: str,
        gender: str,
        interests: str
    ):
        self.name = name
        self.gender = gender
        self.interests = interests
        self._rating: float = 0
        self._rate_count: int = 0

    def get_name(self) -> str:
        return self.name

    def get_gender(self) -> str:
        return self.gender

    def get_interests(self) -> str:
        return self.interests

    def get_geek_rating(self) -> float:
        return 0 if self._rate_count == 0 else self._rating/self._rate_count

    def set_name(self, name: str) -> None:
        self.name = name

    def set_gender(self, gender: str) -> None:
        self.gender = gender

    def set_interests(self, interests: str) -> None:
        self.interests = interests

    def set_geek_rating(self, rating: float) -> None:
        self._rating += rating
        self._rate_count += 1

    def __repr__(self) -> str:
        return (
            f'{self.name}, {self.gender}, {self.interests}, '
            f'рейтинг: {self._rating}'
        )


class Person(AbstractPerson):
    pass


class Proxy(AbstractPerson):
    def __init__(self, person: Person):
        self.person = person

    def get_name(self) -> str:
        return self.person.name

    def get_gender(self) -> str:
        return self.person.gender

    def get_interests(self) -> str:
        return self.person.interests

    def get_geek_rating(self) -> float:
        if self.person._rate_count == 0:
            return 0
        return self.person._rating / self.person._rate_count

    def set_name(self, name: str) -> None:
        self.person.set_name(name)

    def set_gender(self, gender: str) -> None:
        self.person.set_gender(gender)

    def set_interests(self, interests: str) -> None:
        self.person.set_interests(interests)

    def set_geek_rating(self, rating: float) -> None:
        self.person.set_geek_rating(rating)

    def __repr__(self) -> str:
        return (
            f'{self.person.name}, {self.person.gender}, '
            f'{self.person.interests}, '
            f'рейтинг: {self.person._rating}'
        )


class OwnerProxy(Proxy):
    def set_geek_rating(self, rating: float) -> None:
        raise NotImplementedError('Нельзя менять свой рейтинг')


class NoOwnerProxy(Proxy):
    def set_name(self, name: str) -> None:
        raise NotImplementedError('Нельзя менять чужое имя')

    def set_gender(self, gender: str) -> None:
        raise NotImplementedError('Нельзя менять чужой пол')

    def set_interests(self, interests: str) -> None:
        raise NotImplementedError('Нельзя менять чужие интересы')
