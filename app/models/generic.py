from uuid import uuid1
from pydantic import BaseModel

class GenericModel(BaseModel):
    __abstract__ = True

    id = uuid1()