from pydantic import BaseModel
from typing import Optional

class CompanyCreate(BaseModel):
    name: str
    inn: Optional[str] = None
    country: Optional[str] = "KG"

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    inn: Optional[str] = None
    country: Optional[str] = None

class CompanyOut(BaseModel):
    id: int
    name: str
    inn: Optional[str] = None
    country: Optional[str] = None

    class Config:
        from_attributes = True
