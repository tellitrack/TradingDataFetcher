from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, DateTime

Base = declarative_base()


class Signals(Base):
    __tablename__ = 'signals'

    id = Column("id", String)
    timestamp = Column("timestamp", DateTime)
    way = Column("way", String)
    price = Column("price", Float)
    max_price_update = Column("max_price_update", Float)
    min_price_update = Column("min_price_update", Float)
    order_type = Column("order_type", String)
    signal_type = Column("signal_type", String)
    trend_way_update = Column("trend_way_update", String)
    stoplosslimitprice_update = Column("stoplosslimitprice_update", Float)

    def __init__(self,
                 id,
                 timestamp,
                 way,
                 price,
                 max_price_update,
                 min_price_update,
                 order_type,
                 signal_type,
                 trend_way_update,
                 stoplosslimitprice_update
                 ):
        self.id = id
        self.timestamp = timestamp
        self.way = way
        self.price = price
        self.max_price_update = max_price_update
        self.min_price_update = min_price_update
        self.order_type = order_type
        self.signal_type = signal_type
        self.trend_way_update = trend_way_update
        self.stoplosslimitprice_update = stoplosslimitprice_update

    def __repr__(self):
        pass
