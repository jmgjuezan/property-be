from datetime import date
from pydantic import BaseModel


class ExclusionSchema(BaseModel):
    exclusionDate: date | None
    property: str
    