from datetime import date
from pydantic import BaseModel, Field


class Property(BaseModel):
    name: str = Field(min_length=5, max_length=100)
    address: str | None = Field(min_length=25, max_length=250, default=None)
    currentTenant: int | None = Field(ge=0, default=None)
    maxTenant: int | None = Field(gt=0, default=None)
    acquiredDate: date | None = Field(default=None)
    standBy: bool | None = Field(default=None)
