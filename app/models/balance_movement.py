from typing import Optional
from models.generic import GenericModel
from models.data_types.balance_movement_type import BalanceMovementType as BMT


class BalanceMovement(GenericModel):
    value: float
    type: BMT = BMT.DEBIT
    description: str
    person_id: str
