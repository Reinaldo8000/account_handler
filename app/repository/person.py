from models import Person
from . import BaseRepository
from db import connection


class PersonRepository(BaseRepository):
    def basic_table_config(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Person (id TEXT, name TEXT, last_name TEXT, email TEXT, balance REAL)"
        )

    def insert(self, person: Person):
        insert_stmt = "INSERT INTO Person (id, name, last_name, email, balance) VALUES (?,?,?,?,?);"
        data_tuple = (str(person.id), person.name, person.last_name, person.email, person.balance)
        self.cursor.execute(insert_stmt, data_tuple)
        self.commit()

    def get_by_id(self, id: str):
        select_stmt = ("SELECT * FROM Person WHERE ID = ?")
        self.cursor.execute(select_stmt, (id,))
        return self.cursor.fetchone()


person_repository = PersonRepository(connection)
