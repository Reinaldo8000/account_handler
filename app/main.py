from models import Person
from repository import PersonRepository
from db import connection


if __name__ == "__main__":
    p1 = Person(name="Jorge", last_name="Faro", email="jorge.faro@hotmail.com")
    print(p1.dict())
    sd = PersonRepository(connection)
    sd.insert(p1)
    print(sd.get_by_id(str(p1.id)))

