from sqlalchemy import Column, ForeignKey, Integer, String

from models.database import Base


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name_city = Column(String,  nullable=False)
    days_delivery = Column(Integer,  nullable=False)

    def __str__(self):
        return self.name_city


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    name_client = Column(String, unique=True, nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'))
    email = Column(String, unique=True, nullable=False)
