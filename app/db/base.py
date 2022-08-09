import sqlite3

class DBConnection:
    def __init__(self) -> None:
        self.connection = self.check_if_connected()

    def check_if_connected(self):
        try:
            return sqlite3.connect("database.db")
        except Exception:
            return

    def get_connection(self):
        return self.check_if_connected()

connection = DBConnection()
