from sqlalchemy import Column, ForeignKey, Integer, String

from models.database import Base


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name_genre = Column(String, nullable=False)

    def __str__(self):
        return self.name_genre


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name_author = Column(String, nullable=False)

    def __str__(self):
        return self.name_author


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    price = Column(Integer)
    amount = Column(Integer)

    def __str__(self):
        return self.title
