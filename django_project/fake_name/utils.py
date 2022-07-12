from faker import Faker
from typing import NamedTuple, Iterator
from random import choice

fake = Faker()


class User(NamedTuple):
    user: str
    email: str


def generator_user() -> User:
    domain_main: list = ['gmail.com', 'yahoo.com', 'ukr.net', 'outlook.com']
    amount_in_email = range(1000)
    name = fake.first_name()
    email = f'{name}{choice(amount_in_email)}@{choice(domain_main)}'
    return User(user=name, email=email)


def create_fake(amount: int) -> Iterator[User]:
    for _ in range(amount):
        yield generator_user()


def list_fake(amount) -> str:
    return ''.join(
        f'<h1>{each_user.user} - {each_user.email}<h1>' for each_user in create_fake(amount=amount))
