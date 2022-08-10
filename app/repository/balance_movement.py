from . import BaseRepository
from models import BalanceMovement
from db import connection


class BalanceMovementRepository(BaseRepository):
    def basic_table_config(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Balance_Movement
             (id TEXT, value REAL, type TEXT, description TEXT, person_id TEXT)"""
        )

    def insert(self, balance: BalanceMovement):
        insert_stmt = "INSERT INTO Balance_Movement (id, value, type, description, person_id) VALUES (?,?,?,?,?);"
        data_tuple = (
            str(balance.id),
            balance.value,
            balance.type.value,
            balance.description,
            balance.person_id,
        )
        self.cursor.execute(insert_stmt, data_tuple)
        self.commit()

    def get_by_id(self, id: str):
        select_stmt = "SELECT * FROM Balance_Movement WHERE ID = ?"
        self.cursor.execute(select_stmt, (id,))
        return self.cursor.fetchone()

    def get_by_person_id(self, id: str):
        select_stmt = "SELECT * FROM Balance_Movement WHERE person_id = ?"
        self.cursor.execute(select_stmt, (id,))
        return self.cursor.fetchall()

    def get_all(self):
        select_stmt = "SELECT * FROM Balance_Movement"
        self.cursor.execute(select_stmt)
        return self.cursor.fetchall()


balance_movement_repository = BalanceMovementRepository(connection)
