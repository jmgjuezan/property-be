from pydantic import BaseModel, Field


class BreakdownSchema(BaseModel):
    amount: float = Field(gt=0)
    name: str = Field(description="Tenant Name")
    water: float = Field(gt=0)
    electricity: float = Field(gt=0)
    paid: str | None = Field(default=None)
