from abc import abstractmethod
from db.base import DBConnection


class BaseRepository:
    def __init__(self, connection_config: DBConnection) -> None:
        self.config_connection = connection_config
        self.create_connection()
        self.basic_table_config()

    def create_connection(self):
        self.connection = self.config_connection.get_connection()
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()
        self.connection.close()
        self.create_connection()

    @abstractmethod
    def basic_table_config(self):
        return

    @abstractmethod
    def insert(self):
        return
