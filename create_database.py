import random

from faker import Faker

from models.books import Author, Book, Genre
from models.buys import Buy, BuyBook, BuyStep, Step
from models.clients import City, Client
from models.database import Session, create_db

faker = Faker()


def create_database(load_fake_data: bool = True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session)


def _load_fake_data(session: Session) -> None:

    genres = [Genre(name_genre=faker.word()) for _ in range(10)]
    session.add_all(genres)
    session.commit()

    authors = [Author(name_author=faker.name()) for _ in range(10)]
    session.add_all(authors)
    session.commit()

    cities = [
        City(name_city=faker.city(), days_delivery=random.randint(1, 7))
        for _ in range(5)
    ]
    session.add_all(cities)
    session.commit()

    clients = [
        Client(
            name_client=faker.name(),
            city_id=random.choice(cities).id,
            email=faker.email(),
        )
        for _ in range(15)
    ]
    session.add_all(clients)
    session.commit()

    books = [
        Book(
            title=faker.sentence(nb_words=4),
            author_id=random.choice(authors).id,
            genre_id=random.choice(genres).id,
            price=random.randint(100, 1000),
            amount=random.randint(1, 20),
        )
        for _ in range(20)
    ]
    session.add_all(books)
    session.commit()

    buys = [
        Buy(
            buy_description=faker.sentence(),
            client_id=random.choice(clients).id,
        )
        for _ in range(10)
    ]
    session.add_all(buys)
    session.commit()

    steps = [Step(name_step=faker.word()) for _ in range(5)]
    session.add_all(steps)
    session.commit()

    buy_steps = []
    for buy in buys:
        for step in steps:
            buy_step = BuyStep(buy_id=buy.id, step_id=step.id)
            buy_step.set_step_end()
            buy_steps.append(buy_step)
    session.add_all(buy_steps)
    session.commit()

    buy_books = [
        BuyBook(
            buy_id=random.choice(buys).id,
            book_id=random.choice(books).id,
            amount=random.randint(1, 5),
        )
        for _ in range(15)
    ]
    session.add_all(buy_books)
    session.commit()
