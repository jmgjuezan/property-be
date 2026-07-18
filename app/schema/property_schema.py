from typing import Optional
from pydantic import BaseModel


class PropertySchema(BaseModel):
    name: Optional[str] = None
    