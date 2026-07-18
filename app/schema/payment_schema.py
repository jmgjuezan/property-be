from typing import Optional
from pydantic import BaseModel


class PaymentSchema(BaseModel):
    name: Optional[str] = None
    