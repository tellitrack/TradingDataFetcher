from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url = URL.create(
    drivername="postgresql",
    username="tellitrack",
    host="/tmp/postgresql/socket",
    database="db_trading"
)


class DBService:
    def __init__(self, db_url):
        self.db_url = db_url
        self.engine = create_engine(self.db_url)

    def connect(self):
        return self.engine.connect()

    def get_engine(self):
        return self.engine

    def get_url(self):
        return self.db_url

    def get_db_name(self):
        return self.db_url.database

    def get_db_type(self):
        return self.db_url.drivername

    def get_db_host(self):
        return self.db_url.host

    def get_db_port(self):
        return self.db_url.port

    def get_db_user(self):
        return self.db_url.username

    def get_db_password(self):
        return self.db_url.password

    def get_db_url(self):
        return self.db_url.get_dialect().driver + "://" + self.db_url.username + ":" + self.db_url.password + "@" + self.db_url.host + ":" + str(
            self.db_url.port) + "/" + self.db_url.database

    def get_db_url_without_password(self):
        return self.db_url.get_dialect().driver + "://" + self.db_url.username + "@" + self.db_url.host + ":" + str(
            self.db_url.port) + "/" + self.db_url.database

    def get_db_url_without_user_password(self):
        return self.db_url.get_dialect().driver + "://" + self.db_url.host + ":" + str(
            self.db_url.port) + "/" + self.db_url.database

    def get_db_url_without_user_password_port(self):
        return self.db_url.get_dialect().driver + "://" + self.db_url.host + "/" + self.db_url.database


if __name__ == "__main__":
    db_service = DBService(url)
    print(db_service.get_db_url())
    print(db_service.get_db_url_without_password())
    print(db_service.get_db_url_without_user_password())
    print(db_service.get_db_url_without_user_password_port())
