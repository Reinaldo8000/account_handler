from models import Person, BalanceMovement, BalanceMovementType
from repository import PersonRepository, BalanceMovementRepository
from db import connection


if __name__ == "__main__":
    p1 = Person(name="Jorge", last_name="Faro", email="jorge.faro@hotmail.com")
    print(p1.dict())
    sd = PersonRepository(connection)
    bal1 = BalanceMovement(value= 100, type= BalanceMovementType.DEBIT, description="Aiin", person_id=str(p1.id))
    bal2 = BalanceMovement(value= 150, type= BalanceMovementType.DEBIT, description="Aiin", person_id=str(p1.id))
    bal3 = BalanceMovement(value= 170, type= BalanceMovementType.CREDIT, description="Aiin", person_id=str(p1.id))
    bd = BalanceMovementRepository(connection)
    sd.insert(p1)
    bd.insert(bal1)
    bd.insert(bal2)
    bd.insert(bal3)
    print(sd.get_by_id(str(p1.id)))
    print(bd.get_by_id(str(bal1.id)))
    print(bd.get_by_person_id(str(p1.id)))

