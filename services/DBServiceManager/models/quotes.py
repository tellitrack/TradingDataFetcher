from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Quotes(Base):
    __tablename__ = 'quotes'

    id_entry = Column("id_entry", Integer, primary_key=True)
    symbol = Column("symbol", String)
    timeframe = Column("timeframe", String)
    price = Column("price", Float)
    timestamp = Column("timestamp", Float)

    def __init__(self, id_entry, symbol, timeframe, price, timestamp):
        self.id_entry = id_entry
        self.symbol = symbol
        self.timeframe = timeframe
        self.price = price
        self.timestamp = timestamp

    def __repr__(self):
        return f"{self.id_entry} - {self.symbol} ({self.timeframe}) = {self.price} {self.timestamp}"
