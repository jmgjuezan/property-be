from pydantic import BaseModel, Field


class Breakdown(BaseModel):
    amount: float = Field(gt=0)
    electricity: float = Field(ge=0)
    name: str = Field(description="Tenant Name")
    paid: str | None = Field(default=None)
    water: float = Field(ge=0)
