from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from models.database import Base


class Buy(Base):
    __tablename__ = 'buy'

    id = Column(Integer, primary_key=True)
    buy_description = Column(Text)
    client_id = Column(Integer, ForeignKey('client.id'))

    def __str__(self):
        return self.buy_description


class Step(Base):
    __tablename__ = 'step'

    id = Column(Integer, primary_key=True)
    name_step = Column(String)


class BuyStep(Base):
    __tablename__ = 'buy_step'

    id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey('buy.id'))
    step_id = Column(Integer, ForeignKey('step.id'))
    date_step_beg = Column(DateTime, default=datetime.now)
    date_step_end = Column(DateTime)

    def set_step_end(self):
        """Установить дату окончания этапа обработки заказа."""
        self.date_step_end = datetime.utcnow()


class BuyBook(Base):
    __tablename__ = 'buy_book'

    id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey('buy.id'))
    book_id = Column(Integer, ForeignKey('book.id'))
    amount = Column(Integer)
