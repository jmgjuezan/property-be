from datetime import date
from pydantic import BaseModel, Field


class TenantSchema(BaseModel):
    firstName: str = Field(min_length=2, max_length=100, description="Given Name")
    middleName: str | None= Field(min_length=2, max_length=100, default=None)
    lastName: str = Field(min_length=2, max_length=100, description="Family Name")
    property: str
    moveInDate: date = Field(description="Rent Due Date")
    paymentDate: date | None = Field(default=None, description="Preferred Rent Due Date")
    rentAmount: int = Field(gt=0)
