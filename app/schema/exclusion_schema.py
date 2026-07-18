from typing import Optional
from pydantic import BaseModel


class ExclusionSchema(BaseModel):
    name: Optional[str] = None
    