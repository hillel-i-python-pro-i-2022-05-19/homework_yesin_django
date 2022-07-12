from typing import Iterator

from .utils import User, generator_user


def create_fake(amount: int) -> Iterator[User]:
    for _ in range(amount):
        yield generator_user()
