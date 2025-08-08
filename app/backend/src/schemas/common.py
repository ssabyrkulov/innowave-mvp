from pydantic import BaseModel
from typing import Optional

class IDModel(BaseModel):
    id: int

class NameDescModel(BaseModel):
    name: str
    description: Optional[str] = None
