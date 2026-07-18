from typing import Optional
from pydantic import BaseModel


class DueSchema(BaseModel):
    name: Optional[str] = None
    