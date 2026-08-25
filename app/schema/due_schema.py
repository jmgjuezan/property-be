from datetime import date
from pydantic import BaseModel, Field
from .breakdown_schema import BreakdownSchema


class DueSchema(BaseModel):
    name: str | None = Field(description="Tenant Name", default=None)
    property: str
    totalAmount: float = Field(gt=0)
    dueDate: date
    dueFor: str
    coverageFromDate: date | None = Field(default=None)
    coverageToDate: date | None = Field(default=None)
    paid: str | None = Field(default=None)
    electricity: float | None = Field(default=None)
    electricityFromDate: date | None = Field(default=None)
    electricityToDate: date | None = Field(default=None)
    water: float | None = Field(default=None)
    waterFromDate: date | None = Field(default=None)
    waterToDate: date | None = Field(default=None)
    breakdown: list[BreakdownSchema] | None = Field(default=None)
    