from sqlalchemy.orm import Session
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.common.database import Base

class Company(Base):
    __tablename__ = "companies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    inn: Mapped[str | None] = mapped_column(String(50), nullable=True)
    country: Mapped[str | None] = mapped_column(String(10), nullable=True)

class CompaniesRepo:
    def __init__(self, db: Session):
        self.db = db

    def list(self, skip=0, limit=100):
        return self.db.query(Company).offset(skip).limit(limit).all()

    def get(self, company_id: int):
        return self.db.get(Company, company_id)

    def create(self, data: dict):
        obj = Company(**data)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update(self, obj, data: dict):
        for k, v in data.items():
            if v is not None:
                setattr(obj, k, v)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, obj):
        self.db.delete(obj)
        self.db.commit()
