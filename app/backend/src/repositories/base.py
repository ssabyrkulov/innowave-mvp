from sqlalchemy.orm import Session
from typing import Any, Type

class BaseRepo:
    def __init__(self, db: Session, model: Type[Any]):
        self.db = db
        self.model = model

    def get(self, skip=0, limit=100):
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def get_by_id(self, _id: int):
        return self.db.get(self.model, _id)

    def create(self, obj_in: dict):
        obj = self.model(**obj_in)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update(self, db_obj, obj_in: dict):
        for k, v in obj_in.items():
            if v is not None:
                setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj):
        self.db.delete(db_obj)
        self.db.commit()
