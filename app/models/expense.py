from models.generic import GenericModel


class BalanceExchange(GenericModel):
    value: float
    type: str
