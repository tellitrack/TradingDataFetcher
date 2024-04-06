from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, CHAR, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker

postgresql = {"user": "tellitrack",
              "password": "camille",
              "host": "localhost",
              "port": 5432,
              "db": "db_trading"}


def get_engine(user, password, host, port, db):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine


def get_engine_from_settings(config: dict):
    keys = ["user", "password", "host", "port", "db"]
    if not all(key in keys for key in postgresql.keys()):
        raise Exception("Bad credentials config")
    else:
        return get_engine(**config)


def get_session():
    engine = get_engine_from_settings(postgresql)
    session = sessionmaker(bind=engine)()
    return session


session1 = get_session()
print(session1)
