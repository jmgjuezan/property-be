from datetime import date
from pydantic import BaseModel


class PaymentSchema(BaseModel):
    paymentDate: date
    amount: int
    paymentFor: str
    tenant: str
    property: str
    