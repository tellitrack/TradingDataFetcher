
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime

Base = declarative_base()


class Quote(Base):
    __tablename__ = 'quotes'

    id = Column("id", Integer, primary_key=True)
    symbol = Column("symbol", String)
    timeframe = Column("timeframe", String)
    price = Column("price", Float)
    timestamp = Column("timestamp", DateTime)

    def __init__(self, id, symbol, timeframe, price, timestamp):
        self.id = id
        self.symbol = symbol
        self.timeframe = timeframe
        self.price = price
        self.timestamp = timestamp

    def __repr__(self):
        return f"{self.id} - {self.symbol} ({self.timeframe}) = {self.price} {self.timestamp}"
