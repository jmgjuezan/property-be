from datetime import date
from pydantic import BaseModel, Field


class Payment(BaseModel):
    paymentDate: date
    amount: float = Field(ge=1)
    paymentFor: str
    tenant: str
    property: str
    