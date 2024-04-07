from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker

from services.DBServiceManager.models.quotes import Quote

postgresql = {"user": "tellitrack",
              "password": "camille",
              "host": "localhost",
              "port": 5432,
              "db": "db_trading"}


def get_engine(user: str, password: str, host: str, port: int, db: str):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=True)
    return engine


def get_engine_from_settings(config: dict):
    keys = ["user", "password", "host", "port", "db"]
    if not all(key in keys for key in postgresql.keys()):
        raise Exception("Bad credentials config")
    else:
        return get_engine(**config)


def get_session():
    engine = get_engine_from_settings(postgresql)
    db_session = sessionmaker(bind=engine)()
    return db_session


session = get_session()

# new_quote = Quote(id=1, symbol="UCO", timeframe="minute", price=24.5, timestamp=232.323)
# session.add(new_quote)
# session.commit()
# session.close()

# engine = get_engine(**postgresql)
# meta = MetaData()
#
# students = Table(
#     'quotes', meta,
#     Column('id', Integer, primary_key=True),
#     Column('symbol', String),
#     Column('timeframe', String),
#     Column('price', Float),
#     Column('timestamp', Float),
# )
# meta.create_all(engine)

# session = get_session()
user = session.query(Quote).filter(Quote.id == 1).one()
print('type:', type(user))
print('name:', user.price)
session.close()
