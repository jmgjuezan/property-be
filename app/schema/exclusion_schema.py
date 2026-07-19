from datetime import date
from pydantic import BaseModel, Field


class ExclusionSchema(BaseModel):
    exclusionDate: date | None = Field(default=None, description="Single Day")
    exclusionDateFrom: date | None = Field(default=None, description="Starting Range")
    exclusionDateTo: date | None = Field(default=None, description="Ending Range")
    name: str = Field(description="Tenant Name")
    property: str
    